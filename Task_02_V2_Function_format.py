def initialize (n):
    return {i: 'close' for i in range(1, n + 1)}

def run (Room_Door_State,n):
    for x in range (1 , n+1):
        for j in range (x , n+1):
            if (j%x ==0):
                if (Room_Door_State[j] == 'open'):
                    Room_Door_State[j] = 'close'
                else:
                    Room_Door_State[j] = 'open'
    return (Room_Door_State)
    
def count (Room_Door_State,n):
    open_count = 0
    close_count = 0
    for k in range (1,n+1):
        if (Room_Door_State[k] == 'open'):
            open_count = open_count + 1
        else:
            close_count = close_count + 1
    return (open_count, close_count)
def cal (n):
    Room_Door_State = initialize(n) 
    Room_Door_State = run(Room_Door_State,n)
    open_count, close_count = count (Room_Door_State,n)
    print ('Number of doors open=', open_count)        
    print ('Number of doors closed=', close_count) 
    
    
#main 
n = int(input("Please enter number of hotel rooms"))
cal (n)
