import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        

Site = input("Site name: ")
Author = input("Author: ")
Java = input("Do you want a folder for JavaScript (y or n)? ")
CSS = input("Do you want a folder for CSS (y or n)? ")

Site_str = f"./{Site}"
html = f"./{Site}/index.html"
Java_str = f"./{Site}/js/"
CSS_str = f"./{Site}/css/"
# Example
createFolder(Site_str)
createFolder(html)
if Java == 'y': createFolder(Java_str)
if CSS == 'y': createFolder(CSS_str)
