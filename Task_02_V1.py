
n = int(input("Please enter n"))
Room_Door_State = {i: 'open' for i in range(1, n + 1)} #dictionary for room numbers and door state
print(Room_Door_State)
open_count = 0
close_count = 0
for j in range (2 , n):
    if (j%2 ==0):
        Room_Door_State[j] = 'close'
    if (j%3 ==0):
        Room_Door_State[j] = 'close'
    if (j%4==0):
        if (Room_Door_State[j] == 'open'):
            Room_Door_State[j] = 'close'
        if (Room_Door_State[j] == 'close'):
            Room_Door_State[j] = 'open'
print (Room_Door_State)

for k in range (1,n):
    if (Room_Door_State[k] == 'open'):
        open_count = open_count + 1
    else:
        close_count = close_count + 1
        
print ('Number of doors open=', open_count)        
print ('Number of doors closed=', close_count)            
        
        