import numpy as np
from data_exploration import loadingData
import tensorflow as tf
import pandas as pd
#accelData,depths,images,labels,names, rawDepths =loadingData()
names =np.load('names.npy')
names_df = pd.DataFrame(names, columns='name')
names_df.unique().count()