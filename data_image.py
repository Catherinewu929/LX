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
    
            header = file.read(64)
        
            ch1 = []
            
            ArrayCH1 = []
        
            misc = file.read(20000)
            
            PlotSize = 4096000*2
            
            for i in range(PlotSize):
               # while value1 !=：
                value1 = int.from_bytes(file.read(2),"little", signed=False)
            
                if value1 == 0: #8192
                    
                    if cnt ==0:
                        indexValue= file.tell()-2  # 1 x 2 byte
                       
                    cnt=cnt+1
                    
                    if cnt ==1:
                        
                        FlagMsk=1
                        
                        
                else:
                  
                    if cnt != 0:
                        file.seek(indexValue)
                        
                        while cnt > 0:
                        
                            cnt=cnt-1
                    
                            int_value1= int.from_bytes(file.read(2),"little", signed=False)
                            ch1.append(int_value1)
                              
                    else:
                        ch1.append(value1)
               
            
                if FlagMsk:
                    while True:
                        value11 = int.from_bytes(file.read(2),"little", signed=False)
            
                        if value11 != 0:
                            
                            arCH1= ch1[len_x1:len(ch1)]
                            lenxx1=len(ch1)-len_x1
                            ArrayCH1.append(arCH1)
                            cntArray_y1=cntArray_y1+1
                            len_x1=len(ch1)
                            count_x1.append(lenxx1)
            
                            value11 = value11;
                            ch1.append(value11)
            
                            FlagMsk = 0
                            cnt=0
                            print(3)
                   
                            break
            
            ArrayCH1 = ArrayCH1[1:-1] 
            count_x1 = count_x1[1:-1] 
            
            
            print(max(count_x1))
            print(min(count_x1))
            
            
            A1 = zeros((len(ArrayCH1),max(count_x1)),dtype=int)
            
            ch21 = []
            
            Average1 = []
            ch31 = []
            
            
            xx=0
            x = 0;y = 0;
            i=0
            ii=0
            c1=0
            count_ch21 = []
            
            while i < len(ArrayCH1):
                x=i
                print(1)
                ch31.clear()
                ch21.clear()
                ch21=ArrayCH1[i]
                count_ch21.append(len(ch21))
            #   print(len(ch21))
                       
                for ii in range(int(len(ch21))):
                    number1 = ii
                    number2 = number1
                    number11 = ch21[number1:number2]
                    Average1 = np.sum(number11)
                    ch31.append(Average1)
                                            
                for num in ch31:
                    A1[x][y]= num
                    y += 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                    if y == len(ch31):
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
            
            im1.save('c:\\test\\result\\9.9-test1(压缩).tiff')
            
            
            
            # np.savetxt('c:\\LightX\\result\\9.8-test12（压缩）.txt', np.c_[A1],
            # fmt='%s',delimiter='\t') 
            # np.savetxt('c:\\LightX\\result\\9.8-test12行数（压缩）.txt', np.c_[count_ch21],
            # fmt='%s',delimiter='\t') 
            plt.matshow(A1, cmap='gray')
            plt.show() 
    #         return A1
    #
    # except Exception as e:
    #     print("数据处理失败：", e)
    #     return









