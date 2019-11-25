import os
thisD=os.getcwd()
file=os.path.join(thisD,"t1H1")
file=os.path.join(file,"txt1.txt")
with open (file,"r") as f:
      print (f.readlines())
print ("hahha") 
