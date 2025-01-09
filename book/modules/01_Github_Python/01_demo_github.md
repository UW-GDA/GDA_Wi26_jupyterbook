# Github Demo

UW Geospatial Data Analysis  
CEE467/CEWA567  
David Shean, Eric Gagliano, Quinn Brencher

## Preparation and discussion
- Make sure you know where to find everything so you can stay on top of your assignments! 
- Log into the class Jupyterhub and start your server (link pinned to the `#general` channel on slack!)
    - If you're not able to log on, please let us know ASAP
- Make sure to accept the Github classroom starter assignment (link pinned to `#general` on slack)


## Jupyterhub overview
- Basic interface overview 
    - start a shell
    - start a notebook
    - storage and persistence
    - our jupyterhub will be shut down on June 13th, 2025
- Where is this running??

## Shell overview
- Discussion of prompt (jovyan)
- Disucssion of file system navigation (all the way to /)
- Commands and arguments
- Tab completion
- `ls -l` - modificaiton timestamps

## Set up git on Jupyterhub
- Get a [personal access token](https://gda-wi25-jupyterbook.readthedocs.io/en/latest/resources/github.html#first-time-login) from Github
- Run the following commands, replacing with your own info
  - `git config --global user.name "Eric Gagliano"`, 
  - `git config --global user.email "egagli@uw.edu"`
- Run the following command. Next time you enter your credentials (use the Github token as your password!), they will be saved.
  - `git config --global credential.helper store`

## Basic git / Github workflow
1. Discussion: git vs. github, local vs remote 
2. Use `git clone` to download Github starter assignment to the Jupyterhub
3. Try a `git status`
4. Put your name on the assignment on the remote repository
5. Try a `git status`
6. Try `git pull`
7. Now add the date to the assignment on the local repository
8. `git status`
9. Use `git add filename`, `git commit -m "your commit message here"`, and `git push` to push your work up! 
10. Try `git log`

## Lab 01 assignment (due NEXT Friday)
1. Create `labs` folder
1. Distribute week 01 lab assignment link through slack channel 
1. Clone assignment locally into the labs folder - be careful of where you clone!!
1. Add a folder `ramblings`
1. Add a file in that folder called `my_thoughts_on_git.txt` 
1. Add some of your thoughts
1. Practice the add, commit, push workflow!

We will go over and work on the lab together this Friday. Please come prepared by doing this weeks reading assignment--the feedback form is due this Friday before class.

## Other topics to discuss
* You will make mistakes, it's OK, can always start over with git
* origin, branches, forks, more git log functionality
* du and df
* Best practices with git
    * https://stackoverflow.com/questions/572549/difference-between-git-add-a-and-git-add
    * https://uwgda-jupyterbook.readthedocs.io/en/latest/resources/github.html#why-are-a-bunch-of-random-files-added-to-my-repo

