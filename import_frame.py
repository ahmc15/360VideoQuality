import os
import numpy as np
import skvideo.io

def get_1_frame(video_iterator: skvideo.io.FFmpegReader, num_frame: int):
  '''
  Gets the frame of a especified index
  video_iterator is the skvideo.io.FFmpegReader object that is looped until it reaches frame of number num_frame
  Returns frame in the [height,width, color channel format]
  '''

  i=0
  while i !=num_frame:
    frame1=video_iterator.__next__()
    i+=1
  return frame

def frame_division_patches(vid_frame,patch_h,patch_w):
  '''
  divides the frame into patches for later prossessing
  '''
  
  h,w,channel = frame.shape
  num_patch_vertical = int(h/patch_h)
  num_patch_horizontal = int(w/patch_w)
  dict_of_patches={}

  for j in range(num_patch_vertical):
    for i in range(num_patch_horizontal):
      dict_of_patches[str(i)+","+str(j)]=vid_frame[i*patch_w:(i+1)*patch_w, j*patch_h:(j+1)*patch_h,:]
      cv2_imshow(vid_frame[i:i+patch_w,j:j+patch_h,:])
  return dict_of_patches