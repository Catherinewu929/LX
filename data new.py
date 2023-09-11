import os

from numpy import *
import numpy as np
from PIL import Image
#import cv2
import scipy.io as scio
#from cv2 import equalizeHist
import matplotlib.pyplot as plt
#from sklearn import preprocessing 
import ast
from _ast import Try


def data_file(filepath):
    # try:
        int_value1=0
        value1=0
        cnt=0
        FlagMsk=0
        cntArray_y1=0
        len_x1=0
        count_x1=[]
    
        with open(filepath,"rb")as file:     
        #file = open("c:\\LightX\\data\\XIP3.lx","rb")  
        
            file.seek(0, os.SEEK_END);
            fileSize = file.tell();
            file.seek(0);
            header = file.read(64)  #file header
            shit = file.read(0x4000)  #file header
            dataArray = []
            
            ArrayCH1 = []
        
            #misc = file.read(20000)
            
            PlotSize = fileSize - 64- 0x4000;
            
            PlotSize = PlotSize >> 1;   #convert plotsize to sample size
            
            count=0;
            
            #find the line start
            while True:
               # while value1 !=：
                if PlotSize > 1:
                    value1 = int.from_bytes(file.read(2),"little", signed=False);
                    PlotSize = PlotSize - 1;
                else:
                    print("File Invalid!");
                    os._exit();
                
                if(value1 == 0):
                    break;
            
            #new data array
            dataArray.append([])
            
            #find valid data
            while True:
               # while value1 !=：
                if PlotSize > 1:
                    value1 = int.from_bytes(file.read(2),"little", signed=False);
                    PlotSize = PlotSize - 1;
                else:
                    print("File Invalid!");
                    os._exit();
                
                if(value1 != 0):
                    dataArray[0].append(value1);
                    break;
            
            i=0;
            
            #handle valid data
            while True:
               # while value1 !=：
                if PlotSize > 1:
                    value1 = int.from_bytes(file.read(2),"little", signed=False)
                    PlotSize = PlotSize - 1
                else:
                    break

                if value1 == 0: #8192
                    # FlagMsk=1
                    dataArray.append([])
                    i = i + 1
                else:
                    dataArray[i].append(value1)
            
            xSize = 0;
            ySize = len(dataArray);
            
            #get the xSize max
            for j in range(ySize):
                size = len(dataArray[j])
                print(j)
                if(xSize < size):
                    xSize = size
                    print(xSize)
            # ySize = ySize[1:-1] 
            # xSize = xSize[1:-1] 
            
            
            A1 = zeros((ySize,xSize),dtype=int)
            
            ch21 = []
            
            Average1 = []
            ch31 = []
            
            
            xx=0
            x = 0;y = 0;
            i=0
            ii=0
            c1=0
            count_ch21 = []
            
            while i < ySize:
                x=i
                  
                ch31.clear()
                ch21.clear()
                ch21=dataArray[i]
                # count_ch21.append(len(ch21))
            #   print(len(ch21))
                       
                # for ii in range(int(len(ch21))):
                #     number1 = ii
                #     number2 = number1
                #     number11 = ch21[number1:number2]
                #     Average1 = np.sum(number11)
                #     ch31.append(Average1)
                                            
                for num in ch21:
                    A1[x][y]= num
                    y += 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                    if y == len(ch21):
                        y = 0
            
                i= i+1
                
            else:
                i=0
            
            # A2 = np.average(A1[:,:99], axis=1)
            # A3 = A1[:,99:]
            # A4 = np.insert(A3, 0, values=A2, axis=1)
            
            
            
            
            # print(A2)
            
               
            # A2 = np.repeat(A1, 15, axis=0)
            im1 = Image.fromarray(A1)
            
            
            im1 = im1.convert('I;16')
            
            im1.save('c:\\test\\result\\9.11-test17(线对卡).tiff')
            
            
            
            # np.savetxt('c:\\LightX\\result\\9.8-test7（压缩）.txt', np.c_[A1],
            # fmt='%s',delimiter='\t') 
            # np.savetxt('c:\\LightX\\result\\9.8-test7行数（压缩）.txt', np.c_[count_ch21],
            # fmt='%s',delimiter='\t') 
            plt.matshow(A1, cmap='gray')
            plt.show() 
    #         return A1
    #
    # except Exception as e:
    #     print("数据处理失败：", e)
    #     return
filepath = 'c:\\LightX\\data\\9.11-test17.lx'
data_file(filepath)    








