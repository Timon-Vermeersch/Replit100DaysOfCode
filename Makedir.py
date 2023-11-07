#define number of files to be created
num_files = 100

# loop to create the files
for i in range(1, num_files, 1):
    #generate the filename
    filename = f"{i}.py"

    #create and write to file
    with open(filename, 'w'):
        pass
    print(f"the file {filename} has been created as an empty python file")
