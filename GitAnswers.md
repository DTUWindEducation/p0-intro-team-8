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

## 5. What is a branch and why would I use one?

## 6. How could you visualize a branch with 3 commits, and then another branch that breaks off after the second commit and has a single commit?


## 7. Give an example of a set of git commands that would result in a merge conflict.
One exapmle of merge conflict might look like this:
* 1. You have a file in the main branch.
* 2. Create a new branch and make changes to the same file.
* 3. Make different changes to the same file in the main branch.
* 4. When merging the branches, Git detects conflicting changes in the same file.

After this, th euse should manually resolve the conflicts and commit the changes.

## 8. Is Git suitable for latex documents?
Yes, you can use git for tracking the changes for .tex files.

## 9. Should I from now on version my word and powerpoint slides using git? Why/why not?
One could, but in general it is not recommended as git is not meant to hold file of large dimensions - which could be the case for word or powerpoint files.

## 10. What could happen when I push my latest commit to the remote repository without pulling first?
You might get a “non-fast-forward” error and need to pull and resolve conflicts before pushing.

## 11. What happens when I pull without commiting my local changes first?
Git will attempt to merge, and if there are conflicts, you’ll need to resolve them. It’s better to commit or stash changes first.

## 12. What is the difference between branching and forking?

* Branching: Command that creates a separate line of development within the same repository.
* Forking: Creates a copy of the repository under your account, useful for contributing to projects you don’t have write access to.
