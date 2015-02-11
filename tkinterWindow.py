# -*- coding: utf-8 -*-
"""
    Sogang University Datamining Laboratory
    FileName: tkinterWindow, window view
    Author: Sogo
    Start Date: 15/02/08
    Copyright (c) Sogang University Datamining Lab All right Reserved
"""
import Tkinter as tk
from Tkinter import *
import tkFileDialog as filedialog
#import Image
from PIL import Image, ImageTk
from faceDetection import *

# Instance and call the run method to run
class MainWindow(tk.Frame):
    def __init__(self, master):
        # Initialize window using the parent's constructor
        tk.Frame.__init__(self,
                          master,
                          width=400,
                          height=100)
        # Set the title
        self.master.title('예라고 퍼스널 컬러 추출 - Prototype')
        # This allows the size specification to take effect
        self.pack_propagate(0)
        # We will use the flexible pack layout manager
        self.pack()
        # Text Labels
        self.result_label = None
        self.weather_matrix = None
        self.logo_label = tk.Label(text='Yerago Personal Color System \n Copyright (c) Yerago 2015 All rights reserved')
        # Filedialog
        self.open_button = tk.Button(self,
                                     text='이미지 파일 열기 (jpg, jpeg, png 형식만 가능)',
                                     command=self.open_file)
        # The go button
        self.analyze_button = tk.Button(self,
                                        text='분석하기',
                                        command=self.analyze)
        # Put the controls on the form
        self.open_button.pack(fill=tk.X, side=tk.TOP)
        self.analyze_button.pack(fill=tk.X, side=tk.TOP)
        self.logo_label.pack(side=tk.BOTTOM)
        # Open Image's filename
        self.file_name = None
        self.loaded_image = None

    def open_file(self):
        '''
        :return: Get an absolute image file string from FileOpen Dialog
        '''
        self.file_name = filedialog.askopenfilename(filetypes=(("Jpg images", "*.jpg"),
                                                              ("PNG files", "*.png"),
                                                                ("Jpeg images", "*.jpeg")))
        print(self.file_name, 'is loaded.')
        # load image and resize (PIL side), output: (resize)image
        if self.file_name:
            image = Image.open(self.file_name)
            basewidth = 380
            wpercent = (basewidth/float(image.size[0]))
            hsize = int((float(image.size[1])*float(wpercent)))
            image = image.resize((basewidth, hsize), Image.ANTIALIAS)

            # load image for Tkinter
            photo = ImageTk.PhotoImage(image)
            if self.loaded_image:
                # 한 번에 하나씩만 이미지가 올라오도록 (Garbage Collection)
                self.loaded_image.destroy()
            self.loaded_image = Label(image=photo)
            self.loaded_image.image = photo
            self.loaded_image.pack()

    def analyze(self):
        '''
        :return Print a greeting constructed from the selections
        made by the user
        '''
        try:
            self.file_name
        except:
            print("Exception Error Occurred! Please contact Manager (jaehyunahn@sogang.ac.kr).")
        else:
            if self.file_name is not None:
                if self.result_label is not None:
                    self.result_label.destroy()
                    self.weather_matrix.destroy()
                # Do analyze!
                print('%s will be analyzed.' % self.file_name)
                (weather, personal_color_array) = face_detect(self.file_name)
                # Print out result

                print('weather is %s' % weather)
                print('weather matrix ', personal_color_array)
                self.result_label = Label(text=weather)

                # print our weather matrix
                total = float(sum(personal_color_array))
                weather_destribution = '봄: %0.2f%% ' % ((float(personal_color_array[0])/total)*100)
                weather_destribution += '여름: %0.2f%% ' % ((float(personal_color_array[1])/total)*100)
                weather_destribution += '가을: %0.2f%% ' % ((float(personal_color_array[2])/total)*100)
                weather_destribution += '겨울: %0.2f%% ' % ((float(personal_color_array[3])/total)*100)
                # Pack and print out
                self.weather_matrix = Label(text=weather_destribution)
                self.result_label.pack(side=tk.BOTTOM)
                self.weather_matrix.pack(side=tk.BOTTOM)
            else:
                print("There's no exception occurred.")
    def run(self):
        '''
        :return: run the app
        '''
        self.mainloop()