import cv2 as cv 
import keyboard
#import timeit 
import get_screen
import click_save
import argparse

parser = argparse.ArgumentParser(
                    prog = 'loop.py',
                    description = 'Saves game with requested frequency on 2nd of month',
                    epilog = 'Workers of the world, unite!')

parser.add_argument('freq',type=str,choices=["yearly","hyearly","qrly","monthly"])  
args = parser.parse_args()

mon=["January", "February", "March", "April", "May","June",
     "July", "August", "September", "October", "November", "December"]
fnames = [ "img/"+x+"_only.jpg" for x in mon]
save_steps = {"yearly":0,"hyearly":6,"qrly":3,"monthly":1}
print(args.freq)
y = 0 
img_srch = cv.imread(fnames[y],cv.IMREAD_UNCHANGED) # date image
#cv.imshow("test",img_srch)
#cv.waitKey() 
prev_frame_Nhit = True # is it true that previous frame capture is not hit 
# needed to prevent multiple overwrite of file on single date due to asinhron screen 
# capture / frame rates ..  
while True:
     #tstart = timeit.default_timer()
     rect,img_base = get_screen.get_vic_screen() # image in which we search for date
     cmp = cv.matchTemplate(img_base,img_srch,cv.TM_CCOEFF_NORMED)
     min_val, max_val, min_loc, max_loc = cv.minMaxLoc(cmp)
    
     # WARNING MAGIC NUMBER .. do not touch .. checked whole matrix of options 
     # in order not to have false positive identification of dates ending on 12 & 22 ! 
     if max_val>0.98 and prev_frame_Nhit:           
          click_save.save(rect)  
          prev_frame_Nhit = False
          # refresh comparison img based on save freq.  
          y = y + save_steps[args.freq]
          img_srch = cv.imread(fnames[y%12],cv.IMREAD_UNCHANGED)
     else:
          prev_frame_Nhit = True 
     #
     #tstop = timeit.default_timer()
     #execution_time = tstop - tstart
     #print("caoture frame rate  ",int(1/execution_time)) 
     
     if keyboard.is_pressed("q"):
        print(" User requested exit! Have a nice day!")
        break