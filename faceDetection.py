# -*- coding: utf-8 -*-
"""
    Sogang University Datamining Laboratory
    FileName: faceDetection, find object's face using Haar-Classifier
    Author: Sogo
    Start Date: 15/02/08
    Copyright (c) Sogang University Datamining Lab All right Reserved
"""
from colorExtractor200 import *

faceCascade = cv2.CascadeClassifier('./haarClassifier/haarcascade_frontalface_alt.xml')

# Haar-cascade face detection algorithm
def haar_face_detection(image, neighbors):
    item = faceCascade.detectMultiScale(
        image,
        scaleFactor=1.1,
        minNeighbors=neighbors,
        minSize=(30, 30)
    )
    return item

class faceCandidate():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0

# loading classifiers
def face_detect(file_path):
    image = cv2.imread(file_path)
    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except:
        return ('파일을 읽지 못했습니다.', [1, 1, 1, 1])
    faces = haar_face_detection(gray, 5)
    # read image
    if len(faces) <= 0:
        print("We cannot found face in %s." % file_path)
        return ('얼굴을 인식하지 못했습니다. 다른 사진을 올려주세요.', [1, 1, 1, 1])
    else:
        # Found face which has highest <y> coordinate
        mainCandidate = faceCandidate()
        for (x, y, w, h) in faces:
            if mainCandidate.y < y:
                mainCandidate.x = x
                mainCandidate.y = y
                mainCandidate.w = w
                mainCandidate.h = h
            else:
                pass
        cropFace = image[y:y+h, x:x+w]
        cropSize = (200, 200)
        cropFace = cv2.resize(cropFace, cropSize)
        # overwrite temp file
        try:
            tmp_file_path = './tempResources/test_result.jpg'
            cv2.imwrite(tmp_file_path, cropFace)
        except:
            tmp_file_path = './test_result.jpg'
            cv2.imwrite(tmp_file_path, cropFace)
        else:
            weather_score = color_extractor(tmp_file_path)
            personal_color = weather_score.index(max(weather_score))
            print(weather_score)
            if personal_color is 0:
                return ("'봄'형 피부색 입니다.", weather_score)
            elif personal_color is 1:
                return ("'여름'형 피부색 입니다.", weather_score)
            elif personal_color is 2:
                return ("'가을'형 피부색 입니다.", weather_score)
            else:
                return ("'겨울'형 피부색 입니다.", weather_score)