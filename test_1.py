ls - list

cat filename - give the content in the terminal itself

-rf file name - deletes the file
touch filename - create a new file

mkdir foldername - to create a folder

git init - initialise

git add filename - to add specific files 
git add . - add all files


git log - to get all the commit history

git reset commitid will reset to the commit id

types of reset 

git --soft reset

git -- mixed reset ( default)  - unstages all changes ; you will find changes in the codes though
he key benefit of git reset --mixed is that it gives you the opportunity to reorganize, modify, or selectively stage changes before committing again. It doesn't throw away your changes but instead gives you flexibility to decide what to do with them.


git --hard reset - All the changes after the reset is lost


# Git Stash 

Saves the changes in your working directory (modified and/or untracked files) and staging area into a stash (a temporary storage area).

Used 

1. Working on one branch and suddenly you want to work on another branch . the git would not allow to move if you haven't committed changes. in this case you can just stash and comeback and refer'
2. You are experimenting - you were working on something. now keep it asside and you need a fresh slate to work open
3. Pulling and merging changes - if your changes are not committed and you want to pull then it will throw error. so you can stash and save the changes temporirly

Stash doesn't overwrite new changes. if there is a conflit it will ask to resolve'
''
'


git stash apply - to apply changes again while keeping the stash in list// more prefered as if you are resolving conflicts you can go back and reapply stash

git stash pop - apply changes but deletes from the list

git stash list - will show you all the changes stashed

git stash apply stash@{1} to pick specifically 

#check where it is pulling and pushing
git remote -v

git push origin main - origin is where you are pulling and main is where brnach you want to push


# Git Fork vs cloning

git fork means - creating a copy of a repo to your github - used to do it on github. adv it retains the link from the orginal repo (Called upstream) and you can pull new changes

adding git upstream as git remote add upstream url

git clone - means - copying a repo from github to your local machine - used to clone a repo on your local machine. adv it doesn't retain the link from the orginal repo and you have to pull new changes manually

# Git Branching'
git branch - to see all branches

git checkout -b branchname - to create a new branch

git checkout branchname - to switch to branch

- new branch is created out of main. make sure main is the latest version by doing git pull


#git pull request

if you have created a pull request in one branch and add more commits to it it will be added in the same commit 

#best practices

- a new branch for each feature
- if you add more features in the same branch then the commits would be added to the same pull request
-lets say you added feature 1 and feature 2 in the same branch and did a pull request. problems -
- difficult to review two different feature
- if feature 1 is good but feature 2 has problem, you cant selectively merge feature 1 and not do merge for feature 2. 
- more merge conflicts .for eg -if someone made changes seperately in feature 2 and already commited it to main. but now if you will commit your branch, you will have prob resolving because your branch has both feature 1 and feature 2


#Git conflicts

This is a common issue when someone else (or even you, from another machine) has pushed changes to the remote branch after you last pulled or cloned it.

Why This Happens
The remote branch has new commits that your local branch does not have.
Git requires you to first synchronize your local branch with the remote branch before pushing your changes.

#hard push - that my current push overwrites the branch in the github
git push -f

#creating conflit
#more conflicts with nothing in the word 