import numpy as np
import os, os.path
import random
import sys
import statistics as std

def check(a, b, upper_left):
    ul_row = upper_left[0]
    ul_col = upper_left[1]
    b_rows, b_cols = b.shape
    a_slice = a[ul_row : ul_row + b_rows, :][:, ul_col : ul_col + b_cols]
    # parent_Slice = parent[ul_row : ul_row + b_rows, :][:, ul_col : ul_col + b_cols]
    if a_slice.shape != b.shape:
        return False
    return (a_slice == b).all() # here also need to return the parent matric slice

def find_slice(big_array, small_array, noOfSamples):
    for sample in range(0, noOfSamples):
        upper_left = np.argwhere(big_array[sample] == small_array[0,0])
        for ul in upper_left:
            if check(big_array[sample], small_array, ul): # need to keep checking for all values and store them instead of just returning
                return True
    return False

def checkBySubsampling(fullLevels, currentLevel, windowSize):
    plagiarism = 0
    for i in range(0, currentLevel.shape[0]-(windowSize-1)):
        for j in range(0, currentLevel.shape[1]-(windowSize-1)):
            plagiarised = find_slice(full, currentLevel[i:i+windowSize,j:j+windowSize], 21)
            if plagiarised:
                plagiarism += 1
    return plagiarism

marioFileEndings = ["1-1", "1-2", "1-3", "2-1", "3-1", "3-3", "4-1", "4-2", "5-1", "5-3", "6-1", "6-2", "6-3", "7-1", "8-1"]
# loading all training full resolutions
full = []
for trainingCount in range(1, 7):
    with open("../Input Raw & Processed/Full Levels Processed/KI/kidicarus_" + str(trainingCount) + ".txt","rt") as infile:
        full.append(np.matrix([list(line.strip('\n')) for line in infile.readlines()]))
for trainingCount in marioFileEndings:
    with open("../Input Raw & Processed/Full Levels Processed/SMB/mario-" + trainingCount + ".txt","rt") as infile:
        full.append(np.matrix([list(line.strip('\n')) for line in infile.readlines()]))

# coCreativities = ['Random', "MinUnique", "MaxUnique", "MaxSMB", "MaxReward", "MaxKI", "MaxEnemies", "Last", "First", "FiftyFifty"]
# coCreativities = ["MinUnique", "MaxUnique", "MaxSMB", "MaxReward", "MaxKI", "MaxEnemies", "Last", "First", "FiftyFifty"]
# mergedIdentifier = "mergedLevel"
coCreativities = ["MaxSMB"]
kiFolders = ["level1", "level2", "level3", "level4", "level5", "level6"]
kiFiles = ["mergedlevel1", "mergedlevel2", "mergedlevel3", "mergedlevel4", "mergedlevel5", "mergedlevel6"]
marioFolders = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
marioFiles = ["mergedLevel1", "mergedLevel2", "mergedLevel3", "mergedLevel4", "mergedLevel5", "mergedLevel6", "mergedLevel7", "mergedLevel8", "mergedLevel9", "mergedLevel10", "mergedLevel11", "mergedLevel12", "mergedLevel13", "mergedLevel14", "mergedLevel15"  ]

windowSize = 5
for coCreativity in coCreativities:
    plagiarismCount = 0
    totalCombination = 0
    totalPlagiarism = []
    for kiFolder, kiFile in zip(kiFolders, kiFiles):
        with open("../generatedSections/" + coCreativity + "/KI Generated/" + kiFolder + "/" + kiFile + ".txt","rt") as kiInfile:
            currentKILevel = np.matrix([list(line.strip("\n")) for line in kiInfile.readlines()])
            plagiarismCount = checkBySubsampling(full, currentKILevel, windowSize)
            plagiarismForThisLevel = plagiarismCount / ((currentKILevel.shape[1]-windowSize)*(currentKILevel.shape[0]-windowSize))
        totalPlagiarism.append(plagiarismForThisLevel)
    for smbFolder, smbFile in zip(marioFolders, marioFiles):
        with open("../generatedSections/" + coCreativity + "/SMB Generated/" + smbFolder + "/" + smbFile + ".txt","rt") as smbInfile:
            currentSMBLevel = np.matrix([list(line.strip("\n")) for line in smbInfile.readlines()])
            plagiarismCount = checkBySubsampling(full, currentSMBLevel, windowSize)
            plagiarismForThisLevel = plagiarismCount / ((currentSMBLevel.shape[1]-windowSize)*(currentSMBLevel.shape[0]-windowSize))
        totalPlagiarism.append(plagiarismForThisLevel)
    print("Total plagiarism count for co-creativity type " + coCreativity + " is: " + str(std.mean(totalPlagiarism)))    
    print("Effective plagiarism count for co-creativity type " + coCreativity + " is: " + str(std.stdev(totalPlagiarism)))    
    
    
    
    
    
    

