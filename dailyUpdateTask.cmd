@ECHO OFF

:: This CMD script auto update data to github repository daily.

python "D:\Development\Python\Wikipedia Article of the day\main.py"

git add .

git commit -m "Commited by Automated Bot"

git push