import botnoi as bn
import pickle
from botnoi import cv
import numpy as np

### load model
modFile = 'mymod.mod'
mod = pickle.load(open(modFile,'rb'))
def predicting(imgurl):
  a = cv.image(imgurl)
  feat = a.getresnet50()
  # feat = a.getmobilenet()
  res = mod.predict([feat])[0]
  return res