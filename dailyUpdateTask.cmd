@ECHO OFF

:: This CMD script auto update data to github repository daily.

python "D:\Development\Python\Wikipedia Article of the day\main.py"

cd "D:\Development\Python\Wikipedia Article of the day\"

git add .

git commit -m "Commited by Automated Bot"

git push

PAUSE