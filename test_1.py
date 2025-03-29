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


