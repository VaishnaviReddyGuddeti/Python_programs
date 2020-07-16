# Used to simplify exception handling
# python code to demonstrate example of
# with keyword

# Open a file and write the text using
# "with statement"

# file name
file_name = "file1.txt"

# opening a file and creating with-block
with open(file_name, "w") as myfile:
    myfile.write("Welcome @ includehelp!")

# ensure that file is closed or not
if myfile.closed:
    print("file is closed")
