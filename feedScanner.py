# Adam Pluguez
#10/30/2018
# Program to scan W:\NewDownloads\Feed
# Shows and locations stored in CurrentShows.txt
#Outline:
#0.Load show names into array.
#1.Scan W:\NewDownloads\Feed for matching show names partial strings?
#2.Move each matching file to its storege location in CurrentShows.txt
#3.Remove any remaining files or folders in W:\NewDownloads\Feed.

#Working but errors around the 100 /mysteries of musem????
import shutil, os, send2trash, datetime, time
from pathlib import Path

#Set working directory
os.chdir('T:\\TV\\Feed\\')

#Read CurrentShows.txt into lines
showlocations = open("I:\\CurrentShows.txt", "r")
lines = showlocations.read().split(',')
showlocations.close()

notice = ' is being moved to '
home = 'T:\\Tv\Feed'

#Add MusicDownloads Scan/Move
#Add MoviesFeed scan/Move
#Add KidsMovies scan/Move
#Add AnimeMovies
#Add Kids Cartoons

#Tv RSS Feed Scan
for folderName, subfolders, filenames in os.walk(home):
        #Mark as executed so code only executes once during designated hour, runs at 3am

        for filename in filenames:
            if filename.endswith('.mkv') or filename.endswith('.avi') or filename.endswith('.mp4'):
                # Special Cases/Name Conflicts
                if filename.lower().startswith("marvels") or filename.lower().startswith("marvel's"):
                    if "spider-man" in filename.lower():
                            print(filename + notice + lines[165])
                            print("Copying file please wait patiently....")
                            my_file = Path(lines[165]+filename)
                            if my_file.is_file():
                                os.unlink(lines[165]+filename)
                            shutil.move(folderName + '\\' + filename, lines[165])
                            continue
                    elif "agents" in filename.lower():
                            print(filename + notice + lines[125])
                            print("Copying file please wait patiently....")
                            my_file = Path(lines[120] + filename)
                            if my_file.is_file():
                                os.unlink(lines[120] + filename)
                            shutil.move(folderName + '\\' + filename, lines[125])
                            continue

                    elif "runaways" in filename.lower():
                            print(filename + notice + lines[160])
                            print("Copying file please wait patiently....")
                            my_file = Path(lines[160] + filename)
                            if my_file.is_file():
                                os.unlink(lines[160] + filename)
                            shutil.move(folderName + '\\' + filename, lines[160])
                            continue

                elif filename.lower().startswith("star"):
                    if "trek" in filename.lower():
                        print(filename + notice + lines[225])
                        print("Copying file please wait patiently....")
                        my_file = Path(lines[230] + filename)
                        if my_file.is_file():
                            os.unlink(lines[230] + filename)
                        shutil.move(folderName + '\\' + filename, lines[230])
                        continue
                    elif "wars" in filename.lower():
                        print(filename + notice + lines[235])
                        print("Copying file please wait patiently....")
                        my_file = Path(lines[235] + filename)
                        if my_file.is_file():
                            os.unlink(lines[235] + filename)
                        shutil.move(folderName + '\\' + filename, lines[230])
                        continue
                elif filename.lower().startswith("the"):
                    if "big" in filename.lower():
                        print(filename + notice + lines[249])
                        print("Copying file please wait patiently....")
                        my_file = Path(lines[254] + filename)
                        if my_file.is_file():
                            os.unlink(lines[254] + filename)
                        shutil.move(folderName + '\\' + filename, lines[254])
                        continue
                    elif "conners" in filename.lower():
                        print(filename + notice + lines[259])
                        print("Copying file please wait patiently....")
                        my_file = Path(lines[259] + filename)
                        if my_file.is_file():
                            os.unlink(lines[259] + filename)
                        shutil.move(folderName + '\\' + filename, lines[259])
                        break
                    elif "flash" in filename.lower():
                        print(filename + notice + lines[269])
                        print("Copying file please wait patiently....")
                        shutil.move(folderName + '\\' + filename, lines[269])
                        continue
                    elif "simpsons" in filename.lower():
                        print(filename + notice + lines[277])
                        print("Copying file please wait patiently....")
                        my_file = Path(lines[277] + filename)
                        if my_file.is_file():
                            os.unlink(lines[277] + filename)
                        shutil.move(folderName + '\\' + filename, lines[277])
                        continue
                    elif "venture" in filename.lower():
                        print(filename + notice + lines[277])
                        print("Copying file please wait patiently....")
                        my_file = Path(lines[279] + filename)
                        if my_file.is_file():
                            os.unlink(lines[279] + filename)
                        shutil.move(folderName + '\\' + filename, lines[279])
                        continue
                    elif "walking" in filename.lower():
                        print(filename + notice + lines[282])
                        print("Copying file please wait patiently....")
                        my_file = Path(lines[284] + filename)
                        if my_file.is_file():
                            os.unlink(lines[284] + filename)
                        shutil.move(folderName + '\\' + filename, lines[284])
                        continue

                    elif "100" in filename.lower():
                       print(filename + notice + lines[244])
                       print("Copying file please wait patiently....")
                       my_file = Path(lines[250] + filename)
                       if my_file.is_file():
                           os.unlink(lines[250] + filename)
                       shutil.move(folderName + '\\' + filename, lines[250])
                       continue
                elif filename.lower().startswith("modern"):
                    print(filename + notice + lines[170])
                    print("Copying file please wait patiently....")
                    my_file = Path(lines[170] + filename)
                    if my_file.is_file():
                        os.unlink(lines[170] + filename)
                    shutil.move(folderName + '\\' + filename, lines[170])
                    continue
                elif filename.lower().startswith("fresh"):
                    print(filename + notice + lines[85])
                    print("Copying file please wait patiently....")
                    my_file = Path(lines[85] + filename)
                    if my_file.is_file():
                        os.unlink(lines[85] + filename)
                    shutil.move(folderName + '\\' + filename, lines[85])
                    continue
                elif filename.lower().startswith("american"):
                    if "horror" in filename.lower():
                        print(filename + notice + lines[14])
                        print("Copying file please wait patiently....")
                        my_file = Path(lines[14] + filename)
                        if my_file.is_file():
                            os.unlink(lines[14] + filename)
                        shutil.move(folderName + '\\' + filename, lines[14])
                        continue
                    elif "dad" in filename.lower():
                        print(filename + notice + lines[9])
                        print("Copying file please wait patiently....")
                        my_file = Path(lines[9] + filename)
                        if my_file.is_file():
                            os.unlink(lines[9] + filename)
                        shutil.move(folderName + '\\' + filename, lines[9])
                        continue

                #General Cases
                else:
                    for i in range(1, 295):
                        if lines[i].lower() in filename.lower():
                            print(filename + notice + lines[i + 3])
                            print("Copying file please wait patiently....")
                            my_file = Path(lines[i + 3] + filename)
                            if my_file.is_file():
                                os.unlink(lines[i + 3] + filename)
                            shutil.move(folderName+'\\'+ filename,lines[i+3])
                            continue
                print("All video files have in %s been moved!" % folderName)

#This section checks for any unmoved video files in folders
#Counts folders in home location
flag = []
count = 0
for folderName, subfolders, filenames in os.walk(home):
    count = count + 1
count = count

#Create list of folders to be deleted
for i in range(count):
    flag.append(0)

#Flag folders with video files or part files
index = 0
for folderName, subfolders, filenames in os.walk(home):
    for filename in filenames:
        if  filename.endswith('.mkv') or  filename.endswith('.avi') or  filename.endswith('.mp4') or filename.endswith('.part'):
           flag[index] = 1
    if index < count:
        index = index + 1


#Delete all folders in working directory with no video or part files
index = 0
for folderName, subfolders, filenames in os.walk(home):
    if "John" in folderName:
        print("Deleting %s ..." % folderName)
        shutil.rmtree(folderName)
    elif folderName != home and flag[index] == 0:
        print("Deleting %s ..." % folderName)
        shutil.rmtree(folderName)
    if index < count-1:
        index = index + 1

print("Feed Folder Check Complete!")