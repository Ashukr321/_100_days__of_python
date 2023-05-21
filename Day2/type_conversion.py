#  type conversion in the python 
#  type()=> this function gives the type of the data in the python 


#  lets convert some data object from one to another 

# exaple :) 
number = 6; 
print(str(number));
print(float(number));
print(complex(number));
str(number);

#  example 2 : 
# lets convet the float number 3.14 to a string and integer 
number = 3.14;
print(str(number));
print(int(number));
print(type(number));
print(type(number));

print(type(str(number))); # string 
print(type(int(number))) # int 

# convert boolean to an integer and float and string 

bool1 = True;
bool2 = False;

print(int(bool1)); # 1
print(int(bool2)); # 0

# type conversion 
print((float(bool1)));
print((float(bool2)));
 

print(bool(1)); 
print(bool(0));


# lets find out the data type of the data 
print(type(True));
print(type(False));
print(9/3);
print(9//4);
print(type(9/3));
print(type(9//4));

# exponential 
x = 2**3;
print(x);
#  let calculate how many minutes in 20h 

one_hour = 60; 
hour = 24 ; 
minutes = hour * one_hour;
print(minutes);

print(); # this add a new line 
# calculate how many hour in 348 minutes
minutes = 348; 
one_our = 60; 
hour = minutes / one_our;
print(hour);

print();
# store the vlaue 89  in to the variables 
number   = 89 ; 
print(number);
print(type(number));