# -*- coding: utf-8 -*-
"""
    Sogang University Datamining Laboratory
    FileName: colorExtractor200, 200x200 personal color analyzer
    Author: Sogo
    Start Date: 15/02/08
    Copyright (c) Sogang University Datamining Lab All right Reserved
"""
import cv2
import numpy as np

"""
    Yerago Version
    0-3 : spring
    4-7 : summer
    8-11: autumn
    12-15:winter
"""
skinMap = [[243, 221, 161], [216, 181, 122], [222, 163, 107], [177, 132, 50],
           [213, 186, 152], [192, 160, 135], [166, 111, 81], [136, 92, 36],
           [246, 218, 164], [234, 162, 122], [193, 137, 88], [126, 87, 53],
           [242, 219, 177], [205, 171, 116], [192, 113, 59], [115, 59, 28]
           ]

def color_extractor(file_path_200):
    '''
    :param file_path_200: 200 x 200 size of image file
    :return: analyzed personal color string <Spring, Summer, Autumn, Winter>
    '''
    targetImage = cv2.imread(file_path_200)
    skinCandidates = []
    # count weather color from cheeks
    for x in range(45):
        for y in range(40):
            skinColor = color_detector(targetImage[35+x][95+y])
            if skinColor is not -1:
                skinCandidates.append(skinColor)
            skinColor = color_detector(targetImage[130+x][95+y])
            if skinColor is not -1:
                skinCandidates.append(skinColor)
    # arrange suitable weather and return best personal skin color
    weather_score = [0, 0, 0, 0]
    for i in range(len(skinCandidates)):
        if skinCandidates[i] <= 3:
            # Spring
            weather_score[0] += 1
        elif skinCandidates[i] <= 7:
            # Summer
            weather_score[1] += 1
        elif skinCandidates[i] <= 11:
            # Autumn
            weather_score[2] += 1
        elif skinCandidates[i] <= 15:
            # Winter
            weather_score[3] += 1
        else:
            print('something is wrong please contact to manager')
    return weather_score

def color_detector(pixelBGR):
    score = 1000
    colorIdx = -1
    # if pixel is not in range BGR, return -1
    if pixelBGR[2] < 115 or pixelBGR[2] > 246:
        return -1
    if pixelBGR[1] < 59 or pixelBGR[1] > 221:
        return -1
    if pixelBGR[0] < 36 or pixelBGR[0] > 177:
        return -1
    # else find best skin color
    for i in range(len(skinMap)):
        Rscore = abs(skinMap[i][0] - pixelBGR[2])
        Gscore = abs(skinMap[i][1] - pixelBGR[1])
        Bscore = abs(skinMap[i][2] - pixelBGR[0])
        tempScore = Rscore + Gscore + Bscore
        # smaller is better suitable for skin
        if tempScore < score:
            score = tempScore
            colorIdx = i
    # return best skin index
    return colorIdx