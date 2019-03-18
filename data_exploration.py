import h5py
import pandas as pd
from scipy.io import loadmat
import numpy as np
nyu_hdf = h5py.File('nyu_depth_data_labeled.mat', 'r')
accelData = nyu_hdf['accelData'][()]
accelData = np.transpose(accelData)
depths = nyu_hdf['depths'][()]
# images = nyu_hdf['images'][()]
# names = nyu_hdf['names'][()]
# namesToIds=nyu_hdf['namesToIds'][()]
# rawDepths =nyu_hdf['rawDepths'][()]
# scenes =nyu_hdf['scenes'][()]
names = ['accelData', 'depths', 'images','names','namesToIds', 'rawDepths', 'scenes']
accelLabels = ['roll', 'yaw',  'pitch', 'tilt']
depthsLabels = ['height', 'width', 'N']
imageLabels =['height', 'width', 'RGB', 'N']
accelData = pd.DataFrame(np.array(accelData), columns=accelLabels)
#depths = pd.DataFrame(np.array(depths), columns = depthsLabels)







#print(list(file.keys()))
# note that the kets are:['#refs#', '#subsystem#', 'accelData', 'depths', 'images', 'labels', 'names', 'namesToIds', 'rawDepths', 'scenes']
#accel = file['accelData']
#print(type(accel))
#dset = file['nyu_depth_data_labeled.mat']
#file.keys()

#with h5py.File('nyu_depth_data_labeled.mat', 'r') as f:
   # f.write("nyu_hdf")