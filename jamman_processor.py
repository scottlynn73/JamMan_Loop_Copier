import os
import shutil

# Folder with loops to be transferred from
loop_folder = "/Users/scotthamilton/Music/drum_loops"

# Folder where loops are stored
processed_loops_folder = os.path.join(loop_folder, "Processed_loops")
processed_loops_folder = "Processed_loops"

# Make the output folder if it doesn't exist already
if not os.path.exists(processed_loops_folder):
    os.mkdir(processed_loops_folder)

# Loop through all the files and place a renamed copy inside each PHRASE folder
counter = 1

# Make a text file tha shows which loop has been placed where (to aid in finding files when they're on the Jamman)
f = open(os.path.join(processed_loops_folder, "loop_locations.txt"), 'w')
f.write("----------------------------------------------------\n")
f.write("Locations of the original file in the Jamman folders\n")
f.write("----------------------------------------------------\n\n")

# Loop through all the files and place them in PHRASE folders defined by the counter
for i in os.listdir(loop_folder):
    if ".wav" not in i:
        pass
    else:
        if counter < 10:
            counter_str = f'0{counter}'
        else:
            counter_str = str(counter)

        # make the path folder and phrase folder inside it
        patch_folder = os.path.join(processed_loops_folder, f'Patch{str(counter_str)}')
        phrase_folder = os.path.join(patch_folder, "PhraseA")

        if not os.path.exists(patch_folder):
            os.mkdir(patch_folder)
            os.mkdir(phrase_folder)

        # Copy the wav into the phrase folder
        src = os.path.join(loop_folder, i)
        dst = os.path.join(phrase_folder, 'phrase.wav')
        shutil.copy(src, dst)
        
        # Ad line to text file
        f.write(f'{i} = {dst}\n')
        f.write("\n")

        # copy the patch.xml file
        src = "patch.xml" 
        dst =  os.path.join(patch_folder, "patch.xml")
        shutil.copy(src, dst)

        # copy the phrase.xml file
        src = "phrase.xml" 
        dst =  os.path.join(phrase_folder, "phrase.xml")
        shutil.copy(src, dst)
                
        counter += 1

# close the text file
f.close()

print("Now copy the contents of the Processed_loops folder to a JammanStereo folder on the SD card.")

