# with open('sample.txt', "w") as file:
#   file.write("Hello, World!\n")
#   file.write("This is a new text file created with Python.\n")
#   file.write("This is one more line.")

# print("File Written successfully.")

# myfile = open('sample.txt')
# print(myfile.read())

# # After reading the file the pointer reaches the end of the file
# # So if we use the read method again it will output nothing
# print(myfile.read())

# # To read the file again from the start we have to reset the pointer
# myfile.seek(0) # To reset the file pointer to start of the file

# # We can save the contents of the file to a variable 
# # and read from it whenever needed
# # content = myfile.read()
# # print(content)

# # lines_list = myfile.readlines() # returns a list of each lines an an item of list
# first_line = myfile.readline() # returns the first line
# print(first_line)

from pathlib import Path

file_path = Path('demo.txt')
file_path.write_text("This file was created using pathlib.")

# content = file_path.read_text()
# print(content)

print(file_path.read_text())
print(file_path.read_text())