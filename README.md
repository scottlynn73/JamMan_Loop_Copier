# JamMan_Loop_Copier by Scott Hamilton
Getting loops onto the JamMan Stereo is a pain in the backside. This script makes it easy.

This is a python script to add loops to the Digitech Jamman Stereo pedal (more specifically it's external SD card) in a convenient manner. The script only requires 
standard python 3 libraries so can be easily executed with 'python jamman_processor.py' in the terminal (provided python 3 is installed on the system).

# How to use the script
Prepare a folder of single loops you wish to add to your JamMan Stereo, these need to be in 44.1Hz, Stereo format.

Open the `jamman_processor.py` in a text editor or IDE

Set the `loop_folder` variable to the folder you just created e.g `/Users/myusername/Music/drum_loops`

Run the script with `python jamman_processor.py` in your terminal

# Results
The script will make folders inside `Processed_loops` (which is placed inside the `loop_folder` you defined) that have the correct structure to copy to the JamMan. 
Simply copy these to the SD card, placing all the `Phrase0`, `Phrase02` etc. folders inside the `JamManStereo` folder on the SD card. **The Phrase folders MUST go inside the JamManStereo folder or the pedal won't find them**.

The `Phrase$$` folders all have the necessary .xml files placed inside too- all loops are defined in these as being loops (i.e. not single play) and with instant
stopping mode. You can edit the example .xml files provided with this repo if you want to change these options, which are applied to all loops regardless of their
original properties (e.g. tempo etc). For my purposes I don't care if the loops have a defined BPM on the JamMan that matches the real tempo of the loop after
it is copied over as I don't use the on board rhythm functions on the unit. All loops are given the same tempo in other words.

The script also places a file called `loop_locations.txt` into your `Processed_loops` folder. This file shows the original filename of each wav, and the loop
number it has been assigned to in the JamMan. I find this useful to be able to find loops that had a meaningful name prior to renaming them for the JamMan!

Example entries in `loop_locations.txt` are shown below (on the left is the name of the wav from your library, and on the right you can see where it ended up on the JamMan.

...................................................................
Locations of the original file in the Jamman folders:

Bridge 03e_120.wav = Processed_loops/Patch01/PhraseA/phrase.wav

Pre Chorus 03c_120.wav = Processed_loops/Patch02/PhraseA/phrase.wav

Pre Chorus 02c_120.wav = Processed_loops/Patch03/PhraseA/phrase.wav


**Hope this helps you out! Happy looping!**
