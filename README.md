# nanofarm
A wiz farming script written in Python. /
Created by Zirconium (@FortiethAtom4 on GitHub)
# INSTALLATION
1. Clone this repo to a local directory. `git clone https://github.com/FortiethAtom4/nanofarm.git` 
2. Navigate to the directory you cloned it to.
3. A local environment for this script is recommended, but not necessary.
 - Creating a local environment can be done by typing `python -m venv venv`, which will create the folder 'venv' in your directory.
 - To enter the local environment, invoke either of the two Activate scripts in the /Scripts directory within the venv folder.
 - To exit the env, type `deactivate`.
4. Whether you are in a local environment or not, install the required libraries by typing `pip install -r requirements.txt`.

# PREPARATION
This script works by using local images of the enchant and spell it will cast in order to find and click on them. Images for the enchant 'Epic' and the spell 'Humongofrog' are included by default. However, if you intend to farm with a different spell/enchant, you will need to replace these images in order for the script to work. Here are the steps you can take to do this:
1. Get the required images. The default images are screenshots directly from the game. However, the images from the Wizard101 Wiki should also work, provided they are resized. 
    - Note: Be sure to use the extension `.png`. 
    - You will need a picture of the spell, a picture of the enchant, and a picture of the spell after being enchanted.
2. If necessary, resize the images. On a 1920x1080 screen, the spell cards are approximately 80x125 pixels in size. If your resolution is different, you may have to use a slightly different spell size. If your images are too small or too large, the script may not be able to detect the spell on the screen.
    - If your preferred resolution makes resizing the spell images difficult, simply go into a battle with the cards and take screenshots of them. Those screenshots should work fine.
3. Replace the images in the /images/ folder. Make sure you name the replacement images EXACTLY the same as the ones currently in the folder (e.g. `enchant_template.png`,`spell_template.png`, `enchanted_spell.png`). 

# IN-GAME PREP
You will need to make a deck to use while the script is running. For best results, make a deck with 3 copies of the spell and 3 copies of the enchant. That way, in case of an unexpected event (a crit block, low roll, etc.) the script will simply continue to enchant and cast as soon as you have the pips to use another spell. 
Note: This script does NOT work with single-target spells. Be sure to use an AOE spell. Low-pip AOE spells are recommended, e.g. Frog, Meteor, Blizzard. 

# USAGE

Command: `python nanofarm.py` 

The code will attempt to enchant/cast every 5 seconds. Simply start the script as you run into a battle and nanofarm will do the rest. 

The script will run infinitely until halted, but is safe to keep on if, e.g. you want to check your inventory or switch tabs temporarily between fights. The script will only force mouse movements/clicking if it detects the spell cards in the images folder. 

This script does NOT take into account all the other factors of fights in wiz (HP, mana, backpack inventory space, etc.). Although the script will work forever in a vacuum, in reality you will eventually be whittled down by the mobs or run out of mana. This is unavoidable and a fact of life when farming in wiz. You can leave the script running for a while, but be ready to *eventually* walk your wizard away from the farming area temporarily to heal, regain mana and/or clear your inventory. 

# ENJOY
