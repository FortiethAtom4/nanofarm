import cv2 as cv
import pyautogui
import time
import numpy as np


def get_card_locale(img_rgb,template):
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

    w, h = template.shape[::-1]

    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.8

    loc = np.where( res >= threshold)
    return zip(*loc[::-1])

# color of spellbook values:
# lower bound: 55, 23, 27
# upper bound: 132, 73, 66
def main():
    print("Now Running...")
    while True:
        enchant_selected = False
        time.sleep(3)

        
        # template images for spell, enchant, and enchanted spell
        enchant_template = cv.imread("images/enchant_template.png", cv.IMREAD_GRAYSCALE)
        spell_template = cv.imread("images/spell_template.png",cv.IMREAD_GRAYSCALE)
        enchanted_spell_template = cv.imread("images/enchanted_spell.png",cv.IMREAD_GRAYSCALE)

        # find location of enchant on screen
        ss1 = pyautogui.screenshot("images/current_game.png")
        img_rgb = cv.imread("images/current_game.png")
        enchant_loc = get_card_locale(img_rgb,enchant_template)    

        # click on the first enchant
        list_enchant_loc = list(enchant_loc)
        if not len(list_enchant_loc) == 0:
            pyautogui.moveTo(list_enchant_loc[0][0],list_enchant_loc[0][1],0.25)
            pyautogui.click()
            pyautogui.moveTo(100,100,0.25)
            enchant_selected = True

        # find spell on screen
        spell_loc = get_card_locale(img_rgb,spell_template)

        # click on the spell to enchant it
        list_spell_loc = list(spell_loc)
        if not len(list_spell_loc) == 0 and enchant_selected:
            pyautogui.moveTo(list_spell_loc[0][0],list_spell_loc[0][1],0.25)
            pyautogui.click()
            pyautogui.moveTo(100,100,0.25)

        # find the enchanted spell
        ss1 = pyautogui.screenshot("images/current_game.png")
        img_rgb = cv.imread("images/current_game.png")
        enchanted_spell_loc = get_card_locale(img_rgb,enchanted_spell_template)
    
        # cast it
        list_enchanted_spell_loc = list(enchanted_spell_loc)
        if not len(list_enchanted_spell_loc) == 0:
            pyautogui.moveTo(list_enchanted_spell_loc[0][0],list_enchanted_spell_loc[0][1],0.25)
            pyautogui.click()
        else:
            pyautogui.keyDown("a")
            time.sleep(0.25)
            pyautogui.keyUp("a")
            time.sleep(0.25)
        
        pyautogui.moveTo(100,100,0.25)
            
        
        

if __name__ == "__main__":
    main()