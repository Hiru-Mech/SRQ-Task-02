# SRQ-Task-02
Task 02: Algorithms, Problem Solving and Critical Thinking 
 There are ‘n’ number of hotel room in a hotel building. Each room has only one (01)
door. Initially all doors are closed, and each room has one person inside. 
 Starting from room number 01, each person follows a routine one after the other. The
routine is as follows, 
o Person in room number 1 opens the room door, come out and open every door
until the nth door. 
o Person in room number 2 come out and close every door only if the room number
is divisible by 2 starting from his own room (room number 2) and repeat the
process until the nth door. (Closes door number 2, 4, 6, 8, and so on until the nth
door) 
o Person in room number 3 come out and switch the state of every door (if the door
is open, closes the door. if the door is closed, opens the door) only if the room
number is divisible by 3 starting from his own room (room number 3) and repeat
the process until the nth door. (switch the states of door number 3, 6, 9, 12, 15,
and so on) 
o Person in room number 4 come out and switch the state of every door (if the door
is open, closes the door. if the door is closed, opens the door) only if the room
number is divisible by 4 starting from his own room (room number 4) and repeat
the process until the nth door. (Switch the states of door number 4, 8, 12, 16, 20,
and so on). 

 This routine is performed by everyone from 1st person to nth person in the hotel building.
Once the nth person is done, 
o How many closed room doors are there in the hotel building? 
o How many open room doors are there in the hotel building? 
 Using any preferred programming language write an efficient algorithm to solve this
problem. 
 The solution must be in a function format of the programming language of your
choosing. The function should take on argument as an input and result the number of
closed doors and open doors (you have the freedom to just print the result as a text or
return as a two integers)
