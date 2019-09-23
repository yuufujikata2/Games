import numpy as np
import matplotlib.pyplot as plt
import matplotlib.figure as figure
import pylab
import matplotlib.patches as patches
import time
import copy
import puyo_func as puyo
import pickle
pylab.figure(figsize=(6,12))
ax=plt.gca()
plt.xlim(xmin=0)
plt.xlim(xmax=6)
plt.ylim(ymin=0)
plt.ylim(ymax=12)
haichi=[[0 for i in range(6)] for j in range(13)]
n13=raw_input('[13] ')
n12=raw_input('[12] ')
n11=raw_input('[11] ')
n10=raw_input('[10] ')
n9=raw_input('[9]  ')
n8=raw_input('[8]  ')
n7=raw_input('[7]  ')
n6=raw_input('[6]  ')
n5=raw_input('[5]  ')
n4=raw_input('[4]  ')
n3=raw_input('[3]  ')
n2=raw_input('[2]  ')
n1=raw_input('[1]  ')
num1=[int(x) for x in list(str(n1))]
num2=[int(x) for x in list(str(n2))]
num3=[int(x) for x in list(str(n3))]
num4=[int(x) for x in list(str(n4))]
num5=[int(x) for x in list(str(n5))]
num6=[int(x) for x in list(str(n6))]
num7=[int(x) for x in list(str(n7))]
num8=[int(x) for x in list(str(n8))]
num9=[int(x) for x in list(str(n9))]
num10=[int(x) for x in list(str(n10))]
num11=[int(x) for x in list(str(n11))]
num12=[int(x) for x in list(str(n12))]
num13=[int(x) for x in list(str(n13))]
haichi[0][0]=num1[0]
haichi[0][1]=num1[1]
haichi[0][2]=num1[2]
haichi[0][3]=num1[3]
haichi[0][4]=num1[4]
haichi[0][5]=num1[5]
haichi[1][0]=num2[0]
haichi[1][1]=num2[1]
haichi[1][2]=num2[2]
haichi[1][3]=num2[3]
haichi[1][4]=num2[4]
haichi[1][5]=num2[5]
haichi[2][0]=num3[0]
haichi[2][1]=num3[1]
haichi[2][2]=num3[2]
haichi[2][3]=num3[3]
haichi[2][4]=num3[4]
haichi[2][5]=num3[5]
haichi[3][0]=num4[0]
haichi[3][1]=num4[1]
haichi[3][2]=num4[2]
haichi[3][3]=num4[3]
haichi[3][4]=num4[4]
haichi[3][5]=num4[5]
haichi[4][0]=num5[0]
haichi[4][1]=num5[1]
haichi[4][2]=num5[2]
haichi[4][3]=num5[3]
haichi[4][4]=num5[4]
haichi[4][5]=num5[5]
haichi[5][0]=num6[0]
haichi[5][1]=num6[1]
haichi[5][2]=num6[2]
haichi[5][3]=num6[3]
haichi[5][4]=num6[4]
haichi[5][5]=num6[5]
haichi[6][0]=num7[0]
haichi[6][1]=num7[1]
haichi[6][2]=num7[2]
haichi[6][3]=num7[3]
haichi[6][4]=num7[4]
haichi[6][5]=num7[5]
haichi[7][0]=num8[0]
haichi[7][1]=num8[1]
haichi[7][2]=num8[2]
haichi[7][3]=num8[3]
haichi[7][4]=num8[4]
haichi[7][5]=num8[5]
haichi[8][0]=num9[0]
haichi[8][1]=num9[1]
haichi[8][2]=num9[2]
haichi[8][3]=num9[3]
haichi[8][4]=num9[4]
haichi[8][5]=num9[5]
haichi[9][0]=num10[0]
haichi[9][1]=num10[1]
haichi[9][2]=num10[2]
haichi[9][3]=num10[3]
haichi[9][4]=num10[4]
haichi[9][5]=num10[5]
haichi[10][0]=num11[0]
haichi[10][1]=num11[1]
haichi[10][2]=num11[2]
haichi[10][3]=num11[3]
haichi[10][4]=num11[4]
haichi[10][5]=num11[5]
haichi[11][0]=num12[0]
haichi[11][1]=num12[1]
haichi[11][2]=num12[2]
haichi[11][3]=num12[3]
haichi[11][4]=num12[4]
haichi[11][5]=num12[5]
haichi[12][0]=num13[0]
haichi[12][1]=num13[1]
haichi[12][2]=num13[2]
haichi[12][3]=num13[3]
haichi[12][4]=num13[4]
haichi[12][5]=num13[5]
puyo.hyouji(haichi)
plt.savefig('/home/harada/python2/result_puyo.png')
print('Do you want to save?')
ans=raw_input()
if ans=='y':
  f=open('haichifile.binaryfile','wb')
  pickle.dump(haichi,f)
  f.close
plt.close()
