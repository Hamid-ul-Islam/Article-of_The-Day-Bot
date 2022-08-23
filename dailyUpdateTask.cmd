@ECHO OFF

:: This CMD script auto update and commit data to github repository daily.

python "D:\Development\PYTHON\Final Projects\Article of the Day Wikipedia\Article-of_The-Day-Bot\main.py"

cd "D:\Development\PYTHON\Final Projects\Article of the Day Wikipedia\Article-of_The-Day-Bot\"

git add .

git commit -m "Commited by Automated Bot"

git push