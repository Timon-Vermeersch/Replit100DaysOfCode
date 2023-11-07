f = open("filenames.list","r")
contents = f.readline()
contents = contents.split()
for key in contents:
    print(key)
f.close()

#--------------

f = open("filenames.list", "r")
while True:
    contents = f.readline().strip()
    if contents == "":
        break
    print(contents)
