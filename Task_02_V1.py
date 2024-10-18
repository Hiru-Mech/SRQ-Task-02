n = int(input("Please enter n"))
Room_Door_State = {i: 'close' for i in range(1, n + 1)} #dictionary for room numbers and door state
print(Room_Door_State)
open_count = 0
close_count = 0
#print (x, Room_Door_State)
for x in range (1 , n+1):
    for j in range (x , n+1):
        if (j%x ==0):
            if (Room_Door_State[j] == 'open'):
                Room_Door_State[j] = 'close'
            else:
                Room_Door_State[j] = 'open'
    #print (x, Room_Door_State)
#print (Room_Door_State)

for k in range (1,n+1):
    if (Room_Door_State[k] == 'open'):
        open_count = open_count + 1
    else:
        close_count = close_count + 1
        
print ('Number of doors open=', open_count)        
print ('Number of doors closed=', close_count)            
        
