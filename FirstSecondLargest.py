list=[]
while True:
  a=int(input())
  list.append(a)
  if a == -1:
    break
  list.sort()
print("First Largest:" ,list[-2])
print("Second Largest:" ,list[-3])