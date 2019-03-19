import h5py
import pandas as pd
import numpy as np

def dataProcessing(filename):
   file = h5py.File(filename, 'r')
   my_dict = {}
   my_dict['accelData'] = ['roll', 'yaw',  'pitch', 'tilt']
   my_dict['depths']=['height', 'width', 'N']
   my_dict['images'] =['height', 'width', 'RGB', 'N']
   my_dict['labels']=['height', 'width', 'N']
   my_dict['names']=['names']
   my_dict['namesToIds']=['name', 'ID']
   my_dict['rawDepths']=['height','width', 'N']
   my_dict['scenes']=['image_scene']
   dframe_names =['accelData', 'depths','images', 'labels', 'names', 'namesToIds','rawDepths', 'scenes']
   accelData=file['accelData'][()]
   depths = file['depths'][()]
   images = file['images'][()]
   labels = file['labels'][()]
   names = file['names'][()]
   namesToIds = file['namesToIds'][()]
   rawDepths = file['rawDepths'][()]
   scenes =file['scenes'][()]
   return accelData,depths,images,names,namesToIds, rawDepths, scenes, my_dict
