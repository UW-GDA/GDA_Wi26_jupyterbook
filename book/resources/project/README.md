# Final Project

UW Geospatial Data Analysis  
CEE467/CEWA567  
David Shean, Eric Gagliano, Quinn Brencher  

## Overview
The final project is an essential component of this course. It provides an opportunity for you to independently scope and explore a topic of interest, and hopefully apply some of the concepts and approaches that we've covered during the course, solidifying your understanding of the material. The hope is that you can share what you learned with your classmates, and then proudly post your final project repository on your Github page to share with the world (and future employers).

## Expectations, Deliverables, and Milestones
### Weeks 1-3: Defining a project
If you already have an idea for a project, great! If not, also great!

There is intentionally a lot of flexibility here. This can be an individual or group project, though I encourage you to consider a group project, as you can do more collectively, and it will provide real-world experience with collaborative development on Github. 

You have multiple options:
1. Propose a research question or a new tool/package, develop a plan (hopefully applying the concepts we’ve covered in class) and do the development, analysis, and interpretation
    * If you’re already engaged in independent research, try to define a project that will help you move that work forward
    * Explore a side project unrelated to your current research - you never know, it could become a viable research project in the future
    * If independent research is new to you, I encourage you to talk to me, and talk to other professors and grad students in your discipline to define a suitable final project
2. Join forces with others in the class who have already done #1.
3. Something that doesn’t fit into the above categories - pitch it!

### Week 3: Project Idea Pitches (Friday, January 24th, 2025)
* Develop a short, 1-minute pitch/summary of project idea(s)
* Come to class ready to share your idea(s) in small groups and provide feedback to others
* If you see potential opportunities to work with other students, follow up with them on Slack!

### Week 4: Submit Short Summary (Friday, January 31st, 2025)
* Submit a short summary of your project. Please include a short "title" summarizing the idea, and then a short description (a few sentences or a paragraph). Submit on Canvas, and share on the Slack #project channel:
   * If you feel like you're ready (you probably are!), please post directly to the #project channel on Slack
      * Others can provide feedback, or potentially join forces!
      * Remember that this is non-binding and your project will inevitably change as you continue refining and start the work
   * If you are still unsure and not ready to share with the class, send a direct message to the instructor and TA on Slack
      * We will attempt to provide feedback and answer lingering questions
      * When ready, please post to #project channel

### Week 5: Review Summaries, Continue Refining, Additional Group Formation (Friday, February 7th, 2025)
* Review the lists of project summaries on the #project channel
   * Offer feedback, ask questions, suggestions for datasets
* If you see potential opportunities to work with others, or discuss shared needs, follow up with them on Slack.
   * For group projects, start discussing next steps with your team, defining roles, dividing tasks
* Start preparing more detailed project outline (see below)

### Week 6: Repo and Project Outline (Friday, February 14th, 2025)
#### Create a Github repository
Create a new private repo for your project *within the GDA organization* (can transfer to personal accounts later if desired). Go to https://github.com/UW-GDA and click the big green "New" button.

Try to think of a descriptive repo name, bonus points if it is clever - try to avoid repo names like “finalproject”, which doesn’t help your classmates distinguish between projects. 

When you initialize, select to include a README.md and include a .gitignore file for Python.

If you are doing a group project, please check out the group project best practices tab.

Don’t stress too much about the specifics of the repo - these are not permanent, and you can always change repo names, or start over entirely (just copy and add existing files as a first commit). One of the goals here is to gain more experience using git (potentially for collaborative work), and you’re inevitably going to make some mistakes along the way. Best to do it here, where stakes are pretty low.


#### Prepare your README
The README.md file in your new repo will serve as the landing page for your project. You can continue to update as your project evolves, but for now, please prepare a basic project outline. I recommend that you review the markdown cheat sheet and use some basic headings, bulleted/numbered lists, and other formatting to organize your outline.

Please include the following (can combine and reorganize as necessary):
- Project Title
- Name(s) of individual or team members
   - See requirement above for at least one contribution/commit from each team member on the project README.md. Adding names is a good way to practice collaboratively editing a file on Github.
- Short 1-2 sentence summary
- Some introductory background information
- Problem statement, question(s) and/or objective(s)
- Datasets you will use (with links, if available)
- Tools/packages you’ll use (with links)
- Planned methodology/approach
- Expected outcomes
- Any other relevant information, images/tables, references, etc.
- References

That may sound like a lot, but some of these items should only be 1-2 sentences, others can be short lists. Consider this the start of your final report.

### Weeks 7-10: Do the project!
* Start early!
* Create subdirectories in your repo to store:
   * notebooks
   * data (if applicable) - make sure filesize (<20 MB) and total number of files (<20) is limitied.
   * doc (if applicable) for any additional documentation, static images you want to include in notebooks or markdown files, etc.
* Start adding and developing notebooks, code, markdown files, etc.
* If you need to use additional packages that are not available in default environment on the hub, see instructions [here](../conda.md)

#### Recommendations
* Start with limited test case(s) for initial development and exploration:
   * Extract a small region of a large raster
   * If you need the entire raster, start with a downsampled version, then when you're happy with methods, run for native resolution
   * Start with a single timestep or subset of timesteps for time series analysis
* Data storage
    * Ideally, develop reproducible workflows that dynamically fetch and process data stored on centralized public data centers (e.g., AWS S3, NSIDC, CUAHSI)
    * If necessary, you can store files on the Jupyterhub, or even better, host externally and fetch dynamically for analysis
    * Don’t add unnecessary files to your repo (careful with `git add .`)
    * We'll discuss some options during labs later in the quarter
* Commit early, commit often

### Final Exam Week: Presentations (Thursday, March 20th, 2025)
* Each individual/group will prepare and deliver a ~5-10 minute presentation/demo during a group session at the eScience Institute
   * Format is flexible: can be slides, scrolling through notebook(s), scrolling through markdown files
      * If using slides, please include a copy of your presentation in your final project repo (ideally a pdf, which will render on Github)
   * Check out the rubric tab!
* There will be short Q&A/discussion after each presentation
    * Let's try to type all questions/comments in the #project Slack channel, so presenters can follow up later
    * Hoping we can do one short question/response live during the transition to the next speaker
    * Meaningful engagement will reflect positively in your participation grade :)

### Final Exam Week: Repo Submission (Thursday, March 20th, 2025)
* Finalize your repository with notebooks, scripts and documentation
    * Can use README, notebooks, or separate markdown files to summarize methods, results, conclusions, lessons learned and future work
    * Clean up old or unused files (can remove or create an `old` subdirectory and move files there)
    * Update the README with information about the notebooks used during processing and provide a clear indication of which notebooks contain the final results
      * Help someone who is unfamiliar with your project quickly find the good stuff! 
   * Check out the rubric tab!

* Submit the Github url for your final project repo on Canvas


#### Some Perspective
Please remember that nobody is asking for or expecting perfection on your final projects. The reality is that you probably only had time to attempt 10-30% of the things you outlined during Week 6. And that’s OK. If some things worked out, fantastic! Tell us a little about them so we can share your success and learn from what you’ve done. If nothing worked out, that’s also OK! Share a bit of why you chose this project, what you attempted, some of the challenges you encountered, and plans/recommendations for future work. We've worked hard this quarter to foster a friendly and supportive community. Let’s support each other and celebrate our collective accomplishments!


### Optional: Share your amazing work!
You have two options - share with the world or only share with other students in the class. It's up to you, but if you are comfortable sharing and there are no issues involving proprietary data, I suggest sharing with the world (colleagues, advisors, friends, family, future employers!):
1. To share the repo with the class:
   * Go to "Settings" tab (with gear icon) below repo name
   * From left menu, select "Collaborators and Teams"
   * Click the big green "Add Teams" button
   * Type in `gda_w20XX_students` (replacing XX with current year). The student team should appear in results - click it.
   * Grant "read" access so others can see your repo, but not modify
2. To make the repo public and share with the world:
   * From the "Settings" tab, scroll all the way down to the `Danger Zone` and click "Change Visibility"
   * Select "Make Public" and type the repo name in the prompt
   * Proudly share the repo url with others!

## Sample project ideas
Several groups and individuals from previous years made their GDA projects public within the GDA Organization (you should too!). You are encouraged to review these samples for inspiration and some guidance.

Here are a small sample of the public projects:

[Land Use, Transit Flows, and Demographics in King County](https://github.com/UW-GDA/land-use-travel-patterns)

[Assessing Sea Ice Thickness Changes around Kivalina, AK Using ICESat-2 ATL10 Gridded Monthly Data](https://github.com/UW-GDA/kvlclimate)

[Tracking water quality over time in the Lower Mekong](https://github.com/UW-GDA/mekong-water-quality)

[Oakland-Gentrification-Ed-Analysis](https://github.com/UW-GDA/Oakland-Gentrification-Ed-Analysis/tree/main)

[Assessing temporal variability in glacial turbidity through Sentinel-2 rasterized data for Lake Chelan, WA](https://github.com/UW-GDA/Project_Chelanigans)



## Sample data
[Open Data for Projects](./project_data_sources.md)
