# Write to an Existing File

# Open the file "demofile2.txt" and append content to the file:
f = open("demofile2.txt", "a")
f.write("Hi This is my new car")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
