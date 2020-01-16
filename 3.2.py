#declaring hostnames list 
hostnames = []
input_msg = ("Please enter the hostname")
count = 1 

#looping the condition for reducing the code 
while (count <= 3):
    hostnames.append(input(input_msg + str(count) + ":"))
    count = count + 1   
print (hostnames)

#popping the values fromt the list
a = hostnames.pop()
b = hostnames.pop()
c = hostnames.pop()
print ("the popped up values from the list are: ",a,b,c)