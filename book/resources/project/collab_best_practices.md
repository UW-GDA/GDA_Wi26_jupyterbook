# Group project best practices
### Group project initialization
If you’ve decided to do a group project, pick a project lead to initiate and manage the repo, add others as collaborators (individuals or using a new Github Team within the UW-GDA organization), and make sure all can access and commit to the repo. 

Some of the resources from our recent ICESat-2 Hackweek event may be useful here (swapping `UW-GDA` for `ICESAT-2HackWeek` in the urls): https://icesat-2hackweek.github.io/learning-resources/projects/project_initialization/.  If you encounter issues, send me a direct message on Slack (including everyone on the group project), so I can help you navigate. 

I would like to see **at least one commit from each group member** at this phase of the project, even if it is as simple as everyone using the Github interface to edit the README.md file and add their name. There are many approaches to collaborative group/team development using git/Github and no "right" way. 

### Group project collaboration
Collaboration can be a bit more complicated with Jupyter notebooks (vs. standalone Python scripts/libraries), since running cells in the notebook will change execution count and output, even if the code and content appear identical. Best practice is to avoid situations where two people are independently working on the same notebook. When trying to push/pull changes to/from same origin branch, there will inevitably be merge conflicts that can be messy to untangle (though ReviewNB is useful for reviewing notebook diff).

General recommendation - split up the project into multiple smaller notebooks, and have each person work on different components. Avoid the long mega-notebook (like most of our labs), and instead structure your repo with a series of notebooks. For example, you could have one notebook that ingests files, reduces/manipulates the data (e.g., reprojection), then writes new files out to disk in "analysis-ready" format. Then a second notebook reads in those data and does some analysis, creates some plots, etc. If you can pass things back and forth between group members like this, you'll avoid conflicts.

Alternatively, each team member can create separate notebooks with different filenames that both live in the shared repo. When another team member does some work and commits their notebook to the shared repo, you can can pull changes, open their notebook, select relevant cells, copy and paste into your notebook. One simple option with this model is for each group member to create and maintain a subdirectory within the repo where they will stage and modify their own notebooks for their component of the project. 

If you feel comfortable with git/github, you can also use a more standard git branching workflow: https://icesat-2hackweek.github.io/learning-resources/projects/example_workflow/. Reach out to the instructor and TA for additional recommendations.