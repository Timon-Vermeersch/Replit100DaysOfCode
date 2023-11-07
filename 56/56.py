import os,time,traceback,csv
##DictReader leest als row["artist"] reader leest als row[3]
directory_path = "C:/Users/timon/Documents/shitcoding/Replit/56"
filename = "100MostStreamedSongs.csv"
def checkAndAdd():
    print()
    files = os.listdir()
    if row["Artist(s)"] not in files:
        print("save not in files")
        os.mkdir(row["Artist(s)"])
        song_file_path = os.path.join(row["Artist(s)"], row["Song"])
        with open(song_file_path, "w", encoding="utf-8") as song_file:
                   song_file.write(row["Song"])
    

print(os.getcwd())

try:
    os.chdir(directory_path)
    with open(filename, "r", newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"{row['Artist(s)']} - {row['Song']}")
            checkAndAdd()
             

except FileNotFoundError:
    print("File not found")


















