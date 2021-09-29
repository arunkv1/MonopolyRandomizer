board = open("/Users/arunkrishnavajjala/Documents/Monopoly/Monopolyall.csv")
#%%

import random

squares = []

for i in board:
    squares.append(i)
    

count = 0
while count < 100:
    random.shuffle(squares)
    count += 1

   
    
#%%
for i in squares:
    print(i)
#print(squares)
#%%
file1 = open("out.txt","w")
for i in squares:
   file1.write(i)
   


