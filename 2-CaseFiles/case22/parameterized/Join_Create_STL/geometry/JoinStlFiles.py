# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# Imports the necessary modules
import os as os
from os.path import isfile, join
import subprocess as sub


# Gets the current file path
start_path=os.getcwd()

# Checks if the user has a folder named "FilesToJoin"
check_folder=os.path.isdir('FilesToJoin')

#checks if the user has any file named mylist
check_myList=os.path.isfile('mylist')
# If mylist exists, deletes it
if check_myList == True:
    os.remove('mylist')

if check_folder == False:
    
    # In case the folder "FilesToJoin" is non existent it will ask the user to create it and copy the .stl files there.
    def warning():
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        tk.messagebox.showinfo("! warning !", "There is no folder called FilesToJoin. \n"
                            "Please create a folder called FilesToJoin and copy all .stl files to its location")
    warning()

else:
    
    #Creates a path to the folder "FilesToJoin"
    folder_path = start_path + "/FilesToJoin"
    
    # Lists every file in that folder
    files_in_folder0 = [f for f in os.listdir(folder_path) if isfile(join(folder_path, f))]
    
    #Changes the path to the folder
    os.chdir(folder_path)
    
    # If any of the files has the extension .STL changes it to .stl
    for i in range(len( files_in_folder0)):
        if files_in_folder0[i][-4:] == ".STL":
            os.rename(files_in_folder0[i], start_path+'/'+files_in_folder0[i][:-4] + ".stl")
            
           
    # Returns to the start path
    os.chdir(start_path)
    
    # creates a file named "mylist" with all the .stl file names
    text_file=open("mylist","w+")
    for i in files_in_folder0:
        text_file.write(i[:-4]+"\n")
    text_file.close()
    
    # Runs the script.
    
  #  result = sub.call(['./uniqueSTL.X'], shell=True)
    
