@ECHO OFF

:: This CMD script auto update and commit data to github repository daily.

python "D:\Development\PYTHON\Final Projects\Wikipedia Article of the day\main.py"

cd "D:\Development\PYTHON\Final Projects\Wikipedia Article of the day\"

git add .

git commit -m "Commited by Automated Bot"

git push
