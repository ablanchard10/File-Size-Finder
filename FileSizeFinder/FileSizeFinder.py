
import os
from Search import Search
from pathlib import Path
from Folder import Folder

input_path = input("Enter the path of folder you would like to investigate. Syntax should resemble - c://folder/folder/file : ")
os.chdir(input_path)

running = True
currdir = Path(os.getcwd())
parent = currdir.parent
parent_folder = Folder(parent)
sear = Search()
indents = 0

sear.dfs_method(currdir, parent_folder, indents, os.listdir(currdir))

"""
while running:
    f_list = os.listdir()
    for f in f_list:
        if 
"""


