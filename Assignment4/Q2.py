import os
inp = input("Enter text to write to the file: ")
path = "Assignment4\\output.txt"
file = open(path,"a")
file.write(inp +'\n')
print("Data successfully written to output.txt.")
inp1 = input("Enter additional text to append: ")
file.write(inp1+'\n')
print("Data successfully appended.")
print("Final content of output.txt:")
file = open(path,"r")
for line in file.readlines():
    print(line.strip())        
file.close()