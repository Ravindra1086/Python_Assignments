import os
path = "Assignment4\\sample.txt"
if os.path.exists(path):
    file = open(path,"r")
    print("Reading file content:")
    i =1
    for line in file.readlines():
        print("Line {}: {}".format(i,line.strip()))
        i = i+1
    file.close()
else:
    print("Error: The file 'sample.txt' was not found.")