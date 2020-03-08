# -*- coding: utf-8 -*-

import cv2
import numpy as np
import os
import re

from os.path import isfile, join
 
def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
 
    #for sorting the file names properly
   
    def get_digits(text):
        # A helper function to return digits inside text
        return int(text) if text.isdigit() else text


    def natural_keys(text):
        # A helper function to generate keys for sorting frames AKA natural sorting
        return [get_digits(c) for c in re.split(r'(\d+)', text)]

    files.sort(key=natural_keys)

 
    for i in range(len(files)):
        filename=pathIn + files[i]
        #reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        print(filename)
        #inserting the frames into an image array
        frame_array.append(img)
 
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
 
    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()
 
def main():
    pathIn= './frames/'
    pathOut = 'video.avi'
    fps = 30.0
    convert_frames_to_video(pathIn, pathOut, fps)
 
if __name__=="__main__":
    main()