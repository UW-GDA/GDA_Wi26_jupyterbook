# Demo

UW Geospatial Data Analysis  
CEE467/CEWA567  
David Shean, Eric Gagliano, Quinn Brencher

## Preparation and discussion
- Make sure all students are on Jupyterhub (add UW netid from Hub Control Panel if necessary)
- Make sure everyone has started their Jupyterhub server
- Basic interface overview - start a shell, start a notebook
- Ask about OS? Anybody using Linux? All of you!
- Discuss virtual machine and cloud computing
   - underlying infrastructure, computer somewhere in Google data center in CA or OR
- Close tab in Jupyterlab - demonstrate persistence
- Storage will persist throughout quarter, server will shut down after ~1 hour of inactivity

## Shell overview
- Discussion of prompt (jovyan)
- Disucssion of file system navigation (all the way to /)
- Commands and arguments
- Tab completion
- `ls -l` - modificaiton timestamps

## Set up git on Jupyterhub
- https://gda-wi25-jupyterbook.readthedocs.io/en/latest/resources/github.html#first-time-login
- Set up token

## Basic git/Github workflow
1. Create `labs` folder
1. Distribute Week 01 Github classroom assignment link through Slack channel 
1. Clone assignment locally:  
   ```
   git clone https://github.com/UW-GDA/01-shell-github-dshean.git
   cd gda_test  
   ls -l
   ```
1. git vs. github, local vs remote 
1. Discuss repo contents - markdown files, csv
1. Pick a text editor
1. Edit `README.md` and add your name
1. Commit the change
```
git status
git add README.md
git status
git commit -m "Added my name to README.md"
git status
```

### Discussion of local vs origin
* Open web browser to view origin repo on Github
* `git push`
* Refresh page, verify README.md was updated

### Edit README.md on Github, commit directly
* Add today's date below your name

### Pull changes to local repo
* `git pull`
* `git log`

## Add a new file to the repo

### Create a new text file
* `nano git_reflections.txt`
* Add some text "Git is ..."
* Follow above add, commit, push
   * For now, always specify each file to commit
   * For now, modify single file, add and commit
   * Try without `-m` and demonstrate nano (how to get out)


### Commit the change
```
git status
git add myawesomescript.py
git status
git commit -m "Added myawesomescript.py"
```


### Review log, main is ahead of origin
```
git log
git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
```

### Push to origin
```
git push
git status
```

### Review log, both origin and main are same
```
git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
```

# Other topics to discuss
* You will make mistakes, it's OK, can always start over with git
* Post to #01_github_python channel for help
* Best practices with git
    * https://stackoverflow.com/questions/572549/difference-between-git-add-a-and-git-add
    * https://uwgda-jupyterbook.readthedocs.io/en/latest/resources/github.html#why-are-a-bunch-of-random-files-added-to-my-repo
* Tab completion
* Command `history` (use up arrow)
* du and df

# Introduce assignment
* Walk through first few questions of assignment together
