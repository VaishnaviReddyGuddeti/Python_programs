# Write to an Existing File

# Open the file "demofile2.txt" and append content to the file:
f = open("demofile2.txt", "a")
f.write("Hi This is my new car")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
# print(f.read())

# Open the file "demofile3.txt" and overwrite the content:
f = open("demofile3.txt", "w")
f.write("Hey is this Maserati Quattroporte")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
