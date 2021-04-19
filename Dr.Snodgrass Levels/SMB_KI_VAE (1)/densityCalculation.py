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

densities = []
for file in sortedFileList1:
    DensityFactor = 0
    with open(basePath1 + file,"rt") as infile:
        currentLevel = np.matrix([list(line.strip("\n")) for line in infile.readlines()])
        for k in range(0, currentLevel.shape[0]):
            for m in range(0, currentLevel.shape[1]):
                if currentLevel[k, m] != '-':
                    DensityFactor += 1
        density = DensityFactor/(currentLevel.shape[0] * currentLevel.shape[1])
    densities.append(density)
for file in sortedFileList2:
    DensityFactor = 0
    with open(basePath2 + file,"rt") as infile:
        currentLevel = np.matrix([list(line.strip("\n")) for line in infile.readlines()])
        for k in range(0, currentLevel.shape[0]):
            for m in range(0, currentLevel.shape[1]):
                if currentLevel[k, m] != '-':
                    DensityFactor += 1
        density = DensityFactor/(currentLevel.shape[0] * currentLevel.shape[1])
    densities.append(density)
print("The mean of the densities for is: " + str(std.mean(densities)) )
print("\nThe SD of the densities for is: " + str(std.stdev(densities)))