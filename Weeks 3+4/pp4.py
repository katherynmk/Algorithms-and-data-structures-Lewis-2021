#Chapter 4 -Programming Project [P-4.23]: implement a recursive function with signature find(path, filename) 
#that reports all entries of the file system rooted at the given path having the given file name.

import os
#Sources and tutorials listed below(So i can remember for later as well)
#https://realpython.com/working-with-files-in-python/
#https://www.bogotobogo.com/python/python_traversing_directory_tree_recursively_os_walk.php 
#def print_fnmatches(pattern, dir, files):
    #for filename in files:
        #if fnmatch(filename, pattern):
            #print os.path.join(dir, filename)
#^^^source: https://rosettacode.org/wiki/Walk_a_directory/Recursively

#os.listdir(path)
#os.path.getsize(path)
#os.path.isdir(path)
#os.path.join(path, filename)


def find(path, filename):

#if path is path
    if os.path.isdir(path):
#for the object in the path
        for file in os.listdir(path):
            #print all of the objects in this path for all of it
            print(file)
            #checks path for filename
            if os.path.isdir(os.path.join(path, file)):
                #recursion callback 
                find(os.path.join(path, file), filename)


            elif file == filename:
                #final print 
                print(os.path.join(path, file))

           