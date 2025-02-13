## 1.	What is the difference between git and GitLab? 
Git is a software handling version control locally, GitLab is a hosting site for online repos 

## 2.	What is the difference between GitLab, GitHub, and BitBucket?  
They are different companies offering the (basically) same service

## 3.	Why would I ever want to use git, but not GitLab?  
If you only want to save stuff locally, e. g. sensitive data that you don't want stored online. 

## 4.	What are the steps to update the GitLab server with some changes I made on my computer? 
Stage the changes to specify what changes are to be comitted (finished/polished files):
    `git add <file>` or `git add .` for staging all changes
Commit your snapshot of your staged changes that you want to push to your branch:
    `git commit -m "commit message"` (the -m means message)
    `git commit -am "commit message"` (add changes and commit (add + commit in one command))

Push your changes to the branch:
    `git push`

## 5.	What is a branch and why would I use one?  
## 6.	How could you visualize a branch with 3 commits, and then another branch that breaks off after the second commit and has a single commit?  
## 7.	Give an example of a set of git commands that would result in a merge conflict.  
## 8.	Is Git suitable for latex documents?  
## 9.	Should I from now on version my word and powerpoint slides using git? Why/why not?  
## 10.	What could happen when I push my latest commit to the remote repository without pulling first?  
## 11.	What happens when I pull without commiting my local changes first?  
## 12.	What is the difference between branching and forking?