def renketu(x,i,j):
  a=x[j][i]
  if a==10:
    return 1
  x[j][i]=10
  if i!=5:
    if a==x[j][i+1] :
      renketu(x,i+1,j)
  if i!=0:
    if a==x[j][i-1] :
      renketu(x,i-1,j)
  if j!=12:
    if a==x[j+1][i]:
      renketu(x,i,j+1)
  if j!=0:
    if a==x[j-1][i]:
      renketu(x,i,j-1)
  return 1
def rensa(x):
  for j in range(12):
    for i in range(5):
      count2=0
      y=copy.deepcopy(x)
      renketu(x,i,j)
      for l in range(12):
        for k in range(5):
          if x[l][k]==10:
            count2+=1
      if cont2>=4:
        for l in range(12):
          for k in range(5):
            if x[l][k]==10:
              x[l][k]=0
      else:
        for l in range(12):
          for k in range(5):
            if x[l][k]==10:
              x[l][k]=y[l][k]


