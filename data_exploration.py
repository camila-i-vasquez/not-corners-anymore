import h5py
import pandas as pd
nyu_hdf = h5py.File('nyu_depth_data_labeled.mat', 'r')


#print(list(file.keys()))
# note that the kets are:['#refs#', '#subsystem#', 'accelData', 'depths', 'images', 'labels', 'names', 'namesToIds', 'rawDepths', 'scenes']
#accel = file['accelData']
#print(type(accel))
#dset = file['nyu_depth_data_labeled.mat']
#file.keys()

#with h5py.File('nyu_depth_data_labeled.mat', 'r') as f:
   # f.write("nyu_hdf")