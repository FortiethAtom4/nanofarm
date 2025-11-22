from genericpath import isfile
import random
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

# function to click a card found with get_card_locale
# mouse is moved away after clicking due to funky wiz resize-on-hover logic
def click_first_card(img_rgb,template):
    list_locs = list(get_card_locale(img_rgb,template))
    if not len(list_locs) == 0:
        pyautogui.moveTo(list_locs[0][0]+15,list_locs[0][1]+15,0.25)
        pyautogui.click()
        pyautogui.moveTo(100 + random.randrange(0,25),100 + random.randrange(-25,25),0.25)
        time.sleep(0.25)

def get_spell_image(img_path: str):
    if isfile(img_path):
        print("-> Spell template found.")
        return cv.imread(img_path,cv.IMREAD_GRAYSCALE)
    print(f"-X WARNING: file {img_path} not found.")
    return ""

# color of spellbook values:
# lower bound: 55, 23, 27
# upper bound: 132, 73, 66
def main():
    parser = argparse.ArgumentParser(description='A wiz farming script written in Python.')
    parser.add_argument("-n","--no_enchant", help="Disables script enchant usage.", action="store_true")
    parser.add_argument("-s","--shimmy", help="Enable automatic keyboard presses between battles. This will increase farming speed but will make it unsafe to switch tabs while it is running.",
                         action="store_true")
    parser.add_argument("-t","--timer", type=int, default=-1, help="Set a value to automatically stop the script after a set amount of time.")
    args = parser.parse_args()
    
    # Used to time script usage
    farm_timer_start = time.time()
    # Template images for spell, enchant, and enchanted spell
    spell_template = enchant_template = enchanted_spell_template = ""
    print("Reading in spell images...")
    # This can't be the most efficient way to do this. Use a dict or something
    spell_template = get_spell_image("images/spell_template.png")
    enchant_template = get_spell_image("images/enchant_template.png")
    enchanted_spell_template = get_spell_image("images/enchanted_spell.png")

    args_string = "Running nanofarm with arguments: \n"
    for arg in vars(args):
        args_string += f"{arg}: {vars(args)[arg]}\n"
    print(args_string)
    print("-> Now Running...\nPress Ctrl+C at any time to stop")

    # Loop
    while True:
        time.sleep(3)
        
        # find location of enchant on screen
        pyautogui.screenshot("images/current_game.png")
        img_rgb = cv.imread("images/current_game.png")
        time.sleep(0.5)

        farm_timer_end = time.time() - farm_timer_start
        print(f"Current farm duration: {round(farm_timer_end,2)}s")
        if args.timer > 0 and farm_timer_end >= args.timer:
            print("-> Farm time limit reached. Terminating script...")
            break

        # make wizard shimmy a little to speed up runs, if enabled
        if args.shimmy:
            pyautogui.keyDown("a")
            time.sleep(0.25)
            pyautogui.keyUp("a")
            pyautogui.keyDown("d")
            time.sleep(0.25)
            pyautogui.keyUp("d")

        # do a test run on the screenshot. If no spell card found, sleep and try again
        if len(list(get_card_locale(img_rgb,spell_template))) == 0:
            print("Nothing to do")
            continue

        print("Casting spell")

        # click on the first enchant
        if not args.no_enchant:
            click_first_card(img_rgb,enchant_template)

        # click the spell (to cast, or to enchant if enchanting is enabled)
        click_first_card(img_rgb,spell_template)
            
        # find the enchanted spell
        if not args.no_enchant:
            pyautogui.screenshot("images/current_game.png")
            img_rgb = cv.imread("images/current_game.png")
            time.sleep(0.5)
            click_first_card(img_rgb,enchanted_spell_template)
           
        # move mouse back to corner to "reset"
        pyautogui.moveTo(100 + random.randrange(0,25),100 + random.randrange(-25,25),0.25)

if __name__ == "__main__":
    main()