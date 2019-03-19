import h5py
import pandas as pd
import numpy as np

from h5py import File

file_name = 'nyu_depth_data_labeled.mat'
def dataProcessing(filename):
   f = h5py.File(filename, 'r')
   my_dict = {}
   my_dict['accelData'] = ['roll', 'yaw',  'pitch', 'tilt']
   my_dict['depths']=['height', 'width', 'N']
   my_dict['images'] =['height', 'width', 'RGB', 'N']
   my_dict['labels']=['height', 'width', 'N']
   my_dict['names']=['names']
   my_dict['rawDepths']=['height','width', 'N']
   dframe_names =['accelData', 'depths','images', 'labels', 'names', 'namesToIds','rawDepths', 'scenes']
   accelData=f['accelData'][()]
   depths = f['depths'][()]
   images = f['images'][()]
   labels = f['labels'][()]
   rawDepths = f['rawDepths'][()]
   names=[]
   for name in f.get("names"):
    names.append("".join(list(map(lambda x: chr(x), list(f[name[0]])))))
   np.save('accelData', accelData)
   np.save('depths', depths)
   np.save('images', images)
   np.save('labels', labels)
   np.save('names', names)
   np.save('rawDepths', rawDepths)

dataProcessing(file_name)


