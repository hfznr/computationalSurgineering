# Copyright (C) 2019 Eugene Pomazov, <stereopi.com>, virt2real team
#
# This file is part of StereoPi tutorial scripts.
#
# StereoPi tutorial is free software: you can redistribute it 
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of the 
# License, or (at your option) any later version.
#
# StereoPi tutorial is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with StereoPi tutorial.  
# If not, see <http://www.gnu.org/licenses/>.
#
# Most of this code is updated version of 3dberry.org project by virt2real
# 
# Thanks to Adrian and http://pyimagesearch.com, as there are lot of
# code in this tutorial was taken from his lessons.
# 


import cv2
import os
import json

try:
  camera_params = json.load(open("camera_params.txt", "r"))
except Exception as e:
  print(e)
  print("Please run 1_test.py first.")
  exit(-1)

# Global variables preset
total_photos = 15
scale = camera_params['scale']
photo_width = int(camera_params['width'] * scale)
photo_height = int(camera_params['height'] * scale)
img_height = photo_height
img_width = int(photo_width / 4)
photo_counter = 0
print(photo_width)

# Main pair cut cycle
if (os.path.isdir("./pairs")==False):
    os.makedirs("./pairs")
while photo_counter != total_photos:
    photo_counter +=1
    filename = './scenes/scene_'+str(photo_width)+'x'+str(photo_height)+\
               '_'+str(photo_counter) + '.jpg'
    if os.path.isfile(filename) == False:
        print ("No file named "+filename)
        continue
    pair_img = cv2.imread(filename,-1)
    
    cv2.imshow("ImagePair", pair_img)
    cv2.waitKey(0)
    img1 = pair_img [0:img_height,0:img_width] #Y+H and X+W
    img2 = pair_img [0:img_height,img_width:img_width*2]
    img3 = pair_img [0:img_height,img_width*2:img_width*3]
    img4 = pair_img [0:img_height,img_width*3:photo_width]
    img1Name = './pairs/left_'+str(photo_counter).zfill(2)+'.png'
    img4Name = './pairs/right_'+str(photo_counter).zfill(2)+'.png'
    img2Name = './pairs/mid1_'+str(photo_counter).zfill(2)+'.png'
    img3Name = './pairs/mid2_'+str(photo_counter).zfill(2)+'.png'
    cv2.imwrite(img1Name, img1)
    cv2.imwrite(img4Name, img4)
    cv2.imwrite(img3Name, img3)
    cv2.imwrite(img2Name, img2)
    print ('Pair No '+str(photo_counter)+' saved.')
    
print ('End cycle')
