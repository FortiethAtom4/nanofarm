from genericpath import isfile
from xmlrpc.client import boolean
import cv2 as cv
import pyautogui
import time
import numpy as np
import argparse


def get_card_locale(img_rgb,template):
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

    w, h = template.shape[::-1]

    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.85

    loc = np.where( res >= threshold)
    return zip(*loc[::-1])

# color of spellbook values:
# lower bound: 55, 23, 27
# upper bound: 132, 73, 66
def main():
    parser = argparse.ArgumentParser(description='A wiz farming script written in Python.')
    parser.add_argument("-n","--no_enchant", help="Disables script enchant usage.", action="store_true")
    parser.add_argument("-s","--shimmy", help="Enable automatic keyboard \
                        presses between battles. This will increase farming speed but will make it unsafe to switch tabs while it is running.", \
                            action="store_true")
    parser.add_argument("-t","--timer", type=int, default=-1, help="Set a value to automatically stop the script after a set amount of time.")
    args = parser.parse_args()
    
    farm_timer_start = time.time()
    # Template images for spell, enchant, and enchanted spell
    spell_template = enchant_template = enchanted_spell_template = ""
    print("Reading in spell images...")
    # This can't be the most efficient way to do this
    if isfile("images/spell_template.png"):
        spell_template = cv.imread("images/spell_template.png",cv.IMREAD_GRAYSCALE)
        print("-> Spell template found.")
    else:
        print("-X WARNING: Spell template image not found.")
    
    if isfile("images/enchant_template.png"):
        enchant_template = cv.imread("images/enchant_template.png", cv.IMREAD_GRAYSCALE)
        print("-> Enchant template found.")
    else:
        print("-X WARNING: Enchant template image not found.")
    
    if isfile("images/enchanted_spell.png"):
        enchanted_spell_template = cv.imread("images/enchanted_spell.png",cv.IMREAD_GRAYSCALE)
        print("-> Enchanted spell template found.")
    else:
        print("-X WARNING: Enchanted spell template image not found.")

    args_string = "Running nanofarm with arguments: \n"
    for arg in vars(args):
        args_string += f"{arg}: {vars(args)[arg]}\n"
    print(args_string)
    print("-> Now Running...\nPress Ctrl+C at any time to stop")


    # Loop
    while True:
        enchant_selected = False
        time.sleep(3)
        
        # find location of enchant on screen
        # TODO: cleanup
        ss1 = pyautogui.screenshot("images/current_game.png")
        img_rgb = cv.imread("images/current_game.png")
          

        # click on the first enchant
        if not args.no_enchant:
            enchant_loc = get_card_locale(img_rgb,enchant_template)
            list_enchant_loc = list(enchant_loc)
            if not len(list_enchant_loc) == 0:
                pyautogui.moveTo(list_enchant_loc[0][0]+10,list_enchant_loc[0][1]+10,0.25)
                pyautogui.click()
                pyautogui.moveTo(100,100,0.25)
                enchant_selected = True

        # find spell on screen
        spell_loc = get_card_locale(img_rgb,spell_template)

        # click on the spell to enchant it
        list_spell_loc = list(spell_loc)
        if not len(list_spell_loc) == 0 and (enchant_selected or args.no_enchant):
            pyautogui.moveTo(list_spell_loc[0][0]+10,list_spell_loc[0][1]+10,0.25)
            pyautogui.click()
            pyautogui.moveTo(100,100,0.25)
            
        # find the enchanted spell
        if not args.no_enchant:
            ss1 = pyautogui.screenshot("images/current_game.png")
            img_rgb = cv.imread("images/current_game.png")
            enchanted_spell_loc = get_card_locale(img_rgb,enchanted_spell_template)
            # cast it
            list_enchanted_spell_loc = list(enchanted_spell_loc)
            if not len(list_enchanted_spell_loc) == 0:
                pyautogui.moveTo(list_enchanted_spell_loc[0][0]+10,list_enchanted_spell_loc[0][1]+10,0.25)
                pyautogui.click()

        if args.shimmy:
            pyautogui.keyDown("a")
            time.sleep(0.25)
            pyautogui.keyUp("a")
            time.sleep(0.25)
           

        pyautogui.moveTo(100,100,0.5)
        farm_timer_end = time.time() - farm_timer_start
        print(f"Current farm duration: {round(farm_timer_end,2)}s")
        if args.timer > 0 and farm_timer_end >= args.timer:
            print("-> Farm time limit reached. Terminating script...")
            break
        
            
            
        
        

if __name__ == "__main__":
    main()