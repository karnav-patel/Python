# Python

# Windows App: 

-build methods:
 - before this: ```pip install pyinstaller``` to the  C:\Users\patel\AppData\Local\Programs\Python\Python38-32\Scripts
 1) ```pyinstaller.exe --onefile --icon=myicon.ico main.py``` (with ByDefault cmd/terminal)
 2) ```pyinstaller.exe --onefile -w main.py```
 - Note: you have to update your python pip and add env variable 
 - Something like: C:\Users\patel\AppData\Local\Programs\Python\Python38-32\Scripts Install all your import to this path 
 
# Very Important:
 - If you want to make exe with firestore this is very IMP 
 - https://stackoverflow.com/questions/55848884/google-cloud-firestore-distribution-doesnt-get-added-to-pyinstaller-build
 
