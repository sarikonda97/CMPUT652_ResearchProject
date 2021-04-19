import numpy as np
import statistics as std
import os
from os import walk
import natsort

basePath1 = "./KI_VAE Levels/"
basePath2 = "./SMB-VAE Levels/"
fileList = os.listdir(basePath1)
fileList2 = os.listdir(basePath2)
sortedFileList1 = natsort.natsorted(fileList,reverse=False)
sortedFileList2 = natsort.natsorted(fileList2,reverse=False)

kiLinearityFactor = []
smbLinearityFactor = []
nonLinearities = []
for file in sortedFileList1:
    kiLinearityFactor = []
    with open(basePath1 + file,"rt") as infile:
        currentKILevel = np.matrix([list(line.strip("\n")) for line in infile.readlines()])
        for k in range(0, currentKILevel.shape[0]):
                for m in range(0, currentKILevel.shape[1]):
                    if currentKILevel[k, m] != '-':
                        kiLinearityFactor.append(m)
        nonLinearity = sum(kiLinearityFactor)/len(kiLinearityFactor)
        print ("The non-linearity of is: " + str(sum(kiLinearityFactor)/len(kiLinearityFactor)))
    nonLinearities.append(nonLinearity)
for file in sortedFileList2:
    smbLinearityFactor = []
    with open(basePath2 + file,"rt") as infile:
        currentSMBLevel = np.matrix([list(line.strip("\n")) for line in infile.readlines()])
        for k in range(0, currentSMBLevel.shape[0]):
                for m in range(0, currentSMBLevel.shape[1]):
                    if currentSMBLevel[k, m] != '-':
                        smbLinearityFactor.append(k )
        nonLinearity = sum(smbLinearityFactor)/len(smbLinearityFactor)
        print ("The non-linearity is: " + str(sum(smbLinearityFactor)/len(smbLinearityFactor)))
    nonLinearities.append(nonLinearity)

print("The mean of the non0linearities for is: " + str(std.mean(nonLinearities)) )
print("\nThe SD of the non0linearities for is: " + str(std.stdev(nonLinearities)))
