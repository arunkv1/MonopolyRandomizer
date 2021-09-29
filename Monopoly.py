import random
#%%
class Set:
    name = ""
    count = 0
    special = ""
    ID = 0
    order = ""
    def __init__(self, name, count, special, ID, order):
        self.name = name
        self.count = count
        self.special = special
        self.ID = ID
        self.order = order
    def __str__(self):
        return "Name: " + self.name + "\nCount: " + str(self.count) + "\nSpecial: " + self.special + "\nID: " + str(self.ID) + "\nOrder: " + self.order
        
#%%
board = open("/Users/arunkrishnavajjala/Documents/Monopoly/MonopolyBoard.csv")

flow = []

count = 0
for i in board:
    if count > 0:
        splt = i.split(",")
        add = Set(splt[0], int(splt[1]), splt[2], int(splt[3]), splt[4])
        flow.append(add)
    count += 1

print(flow)
#%%
def swapPositions(list, pos1, pos2): 
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

#%%
# rotation
rand = random.randint(1,len(flow))
flow = flow[rand:] + flow[:rand] 

print(flow[0])
#%%
for i in flow:
    print(i)
    
#%%
    

for j in range(0,1000):
    num1 = random.randint(0, len(flow))%len(flow)
    num2 = random.randint(0, len(flow))%len(flow)
    if flow[num1].ID == flow[num2].ID:
        flow = swapPositions(flow, num1, num2)
#%%
for i in flow:
    print(i)











