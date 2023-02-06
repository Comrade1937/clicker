import pyautogui  
import time 



def save(rect):
    #  WARNING MAGIC NUMBERS , locations of buttons to click for 1366x768 
    menu_loc = [1347,655]  # menu button location
    sgame_loc = [715,333]  # save game button location
    save_loc  = [722,550]  # save button location
    cmenu_loc = [715,570]  # close menu button location 
    go_loc = [320,125]     # need to upause game , pause is auto with menu start 


    debug_delay = 0.11  #  used 2 sec to adjust, from documentation : 
    # If the duration is less than pyautogui.MINIMUM_DURATION the movement will be instant.
    #  By default, pyautogui.MINIMUM_DURATION is 0.1.) - sideffects do not recommend !
    pyautogui.moveTo(menu_loc[0]+rect[0], menu_loc[1]+rect[1], debug_delay)
    pyautogui.click()
    pyautogui.moveTo(sgame_loc[0]+rect[0],sgame_loc[1]+rect[1],debug_delay)
    pyautogui.click()
    pyautogui.moveTo(save_loc[0]+rect[0],save_loc[1]+rect[1],debug_delay)
    pyautogui.click()
    # NEEd good time delay ! estimate from Eeblan 3-4s worst case scenario , so safety margin x2 
    time.sleep(8)
    # or again screen recognition untill clock has wanished from screen too complicated for nothing
    pyautogui.moveTo(cmenu_loc[0]+rect[0],cmenu_loc[1]+rect[1],debug_delay)
    pyautogui.click()
    pyautogui.moveTo(go_loc[0]+rect[0],go_loc[1]+rect[1],debug_delay)
    pyautogui.click()
    pyautogui.moveTo(menu_loc[0]+rect[0], menu_loc[1]+rect[1], debug_delay)