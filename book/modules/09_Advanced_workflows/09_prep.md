# 09: Advanced workflows - Geospatial software design, APIs, STAC, dask, shell scripting, and more!

UW Geospatial Data Analysis  
CEE467/CEWA567  
David Shean, Eric Gagliano, Quinn Brencher

## Overview
This week, we're going to put it all together. We'll cover the basics of developing Python packages that enable more advanced geospatial data analysis workflows. We'll also discuss how these workflows can dynamically pull in geospatial data using APIs and STAC.  We'll briefly touch on Dask, a parallel computing library that can help us process large datasets. 

Please take some time to review the following material, and come with questions on topics that are unclear, so we can discuss together.

## Geospatial software design

- [pandas docstring guide](https://pandas.pydata.org/docs/development/contributing_docstring.html)
- [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Python packages for data people, Parts 1-3](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

## Introduction to APIs

APIs (Application Programming Interfaces) are mechanisms that enable us to access data and services over the internet. 

### API Request

When accessing data programmatically, REST APIs provide a standardized way to interact with remote resources. Each REST API request consists of four high level components, which we've summarized from [How to Use the Python Requests Module With REST APIs](https://www.nylas.com/blog/use-python-requests-module-rest-apis/).

- Endpoint: specific URL that identifies the resource you wish to access. Just as a website URL points to a specific webpage, an API endpoint directs your request to a particular dataset or service.
- Method: The method defines the type of operation you want to perform on the resource. 
    - GET — Retrieve data without modifying it (e.g., fetch satellite imagery metadata)
    - POST — Create new resources (e.g., upload a new GeoJSON feature)
    - PUT — Replace an existing resource entirely (e.g., update all attributes of a feature)
    - PATCH — Partially modify an existing resource (e.g., update only the elevation value of a point)
    - DELETE — Remove a resource (e.g., delete a stored analysis result)
- Data payload: For methods that modify resources (POST, PUT, PATCH), you must include the data to be created or changed. This payload is typically formatted as JSON or XML and contains all necessary attributes.
- Headers
    - Authentication — API keys, tokens, or credentials that verify your identity
    - Content-Type — Specifies the format of data being sent (e.g., application/json)
    - Accept — Indicates what format you want the response in (e.g., application/geojson)
    - Cache-Control — Directives for how the response should be cached


### Anatomy of an API request

Let's look at the anatomy of an API request using the Open-Meteo example we'll implement below:

```
https://api.open-meteo.com/v1/forecast?latitude=47.6&longitude=-122.3&current_weather=true
```

What does each part of this API request mean??

1. **Base URL**: The root address of the API
   - `https://api.open-meteo.com`

2. **Path**: Specifies the resource or service being accessed
   - `/v1/forecast`

3. **Query Parameters**: Key-value pairs appended to the URL after a question mark
   - `latitude=47.6` (Seattle's latitude)
   - `longitude=-122.3` (Seattle's longitude)
   - `current_weather=true` (requesting current weather data)
   - Multiple parameters are separated by ampersands (`&`)

This doesn't include all potential parts of API requests, headers, request body, authentication (api keys, etc), and path parameters aren't shown in this example.

### API Response

After sending a request, you'll receive a response, usually in json format. Let's look at what's included in the Open-Meteo response:

1. **Status Codes**: Indicate the result of the request
   - 200: OK (Success) - What we got from Open-Meteo
   - 201: Created (for successful POST requests)
   - 400: Bad Request (if we provided invalid parameters)
   - 401: Unauthorized (if authentication failed)
   - 404: Not Found (if the endpoint doesn't exist)
   - 500: Internal Server Error (if the server had an error)

2. **Response Body**: The data returned by the API
   - Our Open-Meteo response is in JSON format
   - Contains:
     - `current_weather` object with temperature, wind speed, etc.
     - Metadata like latitude, longitude, elevation
     - Time information

3. **Response Structure Example** (simplified from Open-Meteo):
```json
{
  "latitude": 47.6,
  "longitude": -122.3,
  "generationtime_ms": 0.2510547637939453,
  "utc_offset_seconds": 0,
  "timezone": "GMT",
  "timezone_abbreviation": "GMT",
  "elevation": 74.0,
  "current_weather": {
    "temperature": 12.6,
    "windspeed": 8.1,
    "winddirection": 262.0,
    "weathercode": 3,
    "time": "2023-04-21T12:00"
  }
}
```

For geospatial applications, APIs provide:
- Programmatic and scalable access to datasets without downloading
- Standardized interfaces to diverse data sources
- Ability to perform server-side filtering and process

### See how an API request changes depending on what you're asking for
Check out the [open-meteo documentation](https://open-meteo.com/en/docs). Scroll down to right underneath the chart and take note of the API url and its parameters. Now scroll back up, change the selections, and scroll back down to see how the url has changed.


## STAC and the STAC API


From the [STAC specification website](https://stacspec.org/en)...


> At its core, the SpatioTemporal Asset Catalog (STAC) specification provides a common structure for describing and cataloging spatiotemporal assets. A spatiotemporal asset is any file that represents information about the earth captured in a certain space and time.
>
>The STAC Specification consists of 4 semi-independent specifications. Each can be used alone, but they work best in concert with one another.
>
>- **STAC Item** is the core atomic unit, representing a single spatiotemporal asset as a GeoJSON feature plus datetime and links.
>
>- **STAC Catalog** is a simple, flexible JSON file of links that provides a structure to organize and browse STAC Items. A series of best practices helps make recommendations for creating real world STAC Catalogs.
>
>- **STAC Collection** is an extension of the STAC Catalog with additional information such as the extents, license, keywords, providers, etc that describe STAC Items that fall within the Collection.
>
>- **STAC API** provides a [RESTful](https://restfulapi.net/) endpoint that enables search of STAC Items, specified in OpenAPI, following OGC's WFS 3.

STAC standardizes metadata about spatial extent, temporal information, data properties (bands, cloud cover, etc.), and links to actual data. We like STAC because it is a consistent way to search across different data providers, it has machine-readable metadata, the data is self-describing, and it is interoperalbe between different platforms.


### Making use of STAC catalogs: pystac_client and odc-stac 

In order to take advantage of the [vast amount of STAC static catalogs and STAC APIs](https://stacindex.org/catalogs?access=public), we'll use [pystac_client](https://pystac-client.readthedocs.io/en/stable/) and [odc-stac](https://odc-stac.readthedocs.io/en/latest/).

Microsoft's Planetary Computer is one of many platforms that host a variety of Earth observation datasets accompanied by a STAC catalog to access them. Check out [Reading Data from the STAC API
](https://planetarycomputer.microsoft.com/docs/quickstarts/reading-stac/) for more info. We'll be querying their [Sentinel-2 dataset](https://planetarycomputer.microsoft.com/dataset/sentinel-2-l2a#overview) in the API and STAC demo.

Check out some other STAC catalogs, such as [Element84's Earth Search](https://github.com/Element84/earth-search) and [NASA's cmr-stac](https://github.com/nasa/cmr-stac) ([Data Discovery notebook with CMR-STAC API](https://nasa-openscapes.github.io/2021-Cloud-Hackathon/tutorials/02_Data_Discovery_CMR-STAC_API.html)).

## Advanced shell & shell scripting

We already got the chance to use the shell in this class, but we've only scratched the surface! The shell can be powerful for some geospatial data analysis tasks...

- Automation of repetitive tasks - process multiple files with a single command
- Pipeline construction - chain together specialized geospatial tools (GDAL, OGR, etc.)
    - [GDAL command line guide from Geospatial Linux](https://geospatial-linux.readthedocs.io/en/latest/gdal.html#)
- System integration - easily combine Python with other geospatial software
- Batch processing - efficiently handle large datasets across multiple files
- Resource management - control CPU/memory allocation for intensive geospatial operations

Brush up on your shell skills by checking out Software Carpentry's [The Unix Shell tutorial](https://swcarpentry.github.io/shell-novice/aio.html).

### Shell examples

#### File Navigation and management
```bash
# List files by type
ls *.tif                  # List all GeoTIFF files
find . -name "*.shp"      # Find all shapefiles in current directory and subdirectories

# Handle large datasets
du -h landsat_scenes/     # Check disk usage of a directory
head -n 10 points.csv     # Preview first 10 lines of CSV data
wc -l points.csv          # Count records in CSV file
```

#### GDAL
```bash
# Raster operations
gdalinfo input.tif                # Get raster metadata
gdal_translate -of GTiff -co "COMPRESS=LZW" input.tif output.tif   # Convert with compression
gdalwarp -t_srs EPSG:4326 input.tif reprojected.tif   # Reproject raster
```


#### Data wrangling and processing
```bash
# Filter and extract data
grep "POINT" features.geojson     # Find all point features in GeoJSON
cut -d',' -f1,2 coordinates.csv   # Extract first two columns (e.g., lon/lat)
awk '{if ($3 > 100) print $0}' measurements.txt   # Filter by attribute value

# Batch rename
rename 's/landsat_/ls_/' *.tif    # Rename all landsat TIFFs
```

#### Shell and python together
```python
import subprocess

# Run a shell command and capture output
result = subprocess.run(['gdalinfo', 'input.tif'], 
                        capture_output=True, text=True)
print(result.stdout)

# Process multiple files
import glob
for tif_file in glob.glob('*.tif'):
    subprocess.run(['gdal_translate', '-of', 'GTiff', 
                   '-co', 'COMPRESS=LZW', tif_file, f'compressed_{tif_file}'])
```

### Shell scripting
Besides just running shell commands on the command line, you can create shell scripts to automate processes! Learn more about shell scripts from Software Carpentry's [Shell Scripts](https://swcarpentry.github.io/shell-novice/06-script.html#nelles-pipeline-creating-a-script) tutorial. You can create a `.sh` file where you put all your shell commands, then you can run the entire script from the command line. There are some great examples in [Data wrangling with Shell Scripts](https://medium.com/zasti/data-wrangling-with-shell-scripts-a7f74f87f9e9). Here is another potential use case...

### Clip satellite images on disk in bulk
```bash
#!/bin/bash
# Script to clip multiple satellite images to a study area

# Define variables
STUDY_AREA="study_area.shp"
OUTPUT_DIR="clipped_scenes"

# Create output directory if it doesn't exist
mkdir -p $OUTPUT_DIR

# Process each Landsat scene
for scene in landsat_scenes/*.tif; do
    # Get filename without path and extension
    filename=$(basename -- "$scene")
    name="${filename%.*}"
    
    echo "Processing $name..."
    
    # Clip raster to study area
    gdalwarp -cutline $STUDY_AREA -crop_to_cutline \
             -dstnodata 0 $scene "$OUTPUT_DIR/${name}_clipped.tif"
    
    # Calculate statistics for the clipped file
    gdalinfo -stats "$OUTPUT_DIR/${name}_clipped.tif" > "$OUTPUT_DIR/${name}_stats.txt"
done
```