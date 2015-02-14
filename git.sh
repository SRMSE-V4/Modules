git init
echo "*.sh\n*.gitignore\n*~" > .gitignore
git remote add origin https://github.com/SRMSE-V4/Modules.git
git add -f *
git commit -m "$1"
git rm --cached .gitignore
git pull https://github.com/SRMSE-V4/Modules.git
git push -u origin master




