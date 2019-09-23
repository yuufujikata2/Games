import pickle

a=open('haichi.binaryfile','rb')
haichi=pickle.load(a)
a.close

for i in range(13):
  for j in range(6):
    print(haichi[i][j])
