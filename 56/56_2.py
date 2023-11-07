import os,csv

file_path = r"C:\Users\timon\Documents\shitcoding\Replit\56\100MostStreamedSongs.csv"
directory_path = "C:/Users/timon/Documents/shitcoding/Replit/56"
with open(file_path,encoding="utf-8") as file:
    
    reader = csv.DictReader(file)
    for row in reader:
        os.chdir(directory_path)
        dir = os.listdir()
        artist = row["Artist(s)"]
        if artist not in dir:
            print("xd")
            

            song_file_path = os.path.join(row["Artist(s)"], row["Song"])
            os.mkdir(row["Artist(s)"])
            song_file_path = os.path.join(row["Artist(s)"], row["Song"])
            with open(song_file_path, "w", encoding="utf-8") as song_file:
                   song_file.write(row["Song"])
        else:
            directory_path_artist = f"C:/Users/timon/Documents/shitcoding/Replit/56/{artist}"
            os.chdir(directory_path_artist)
            print("if you see this its good going")
          
        
        song = row["Song"]
        