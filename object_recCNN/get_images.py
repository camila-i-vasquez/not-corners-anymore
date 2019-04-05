import numpy as np
import glob
import pandas as pd
import cv2 as cv
import matplotlib.pyplot as plt
import tensorflow as tf


train_images=[]
train_images = [cv.imread(file) for file in glob.glob('/Users/camila/Documents/GitHub/not-corners-anymore/NYU_DIRECTORY/training/**/*colors.png', recursive=True)]
train_target = [cv.imread(file) for file in glob.glob('/Users/camila/Documents/GitHub/not-corners-anymore/NYU_DIRECTORY/training/**/*ground_truth.png', recursive=True)]

###########

test_images = [cv.imread(file) for file in glob.glob('/Users/camila/Documents/GitHub/not-corners-anymore/NYU_DIRECTORY/training/**/*colors.png', recursive=True)]
test_target = [cv.imread(file) for file in glob.glob('/Users/camila/Documents/GitHub/not-corners-anymore/NYU_DIRECTORY/training/**/*ground_truth.png', recursive=True)]



print(test_images[0].shape)
test_images[25].shape
