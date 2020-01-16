host_list = ["example-hostname"]
command_list = ["example-command"]

print (" press 1 for add \n press 2 for delete \n press 3 for view \n press 4 for exit")

while True:
    user_input = input("Enter number: ")
    
    try:
        user_input = int (user_input)
        
        if user_input > 0 and user_input < 5:
            break
        else:
            print("Number out of range.")
    except ValueError:
        print ("Bad user.  Numbers only")

print ("the input value you have given is: ", user_input)

if user_input == 4:
    print ("we are now exiting the condition")
    exit()

elif user_input == 1:
    temp_val = 0 
    while temp_val <= 2:
        print ("Please enter the host which you want to add ")
        hostnames = input ("Please add the hostname: ")
        commands = input ("Please add the command: ")
        host_list.append (hostnames)
        command_list.append (commands)
        temp_val = temp_val + 1
    print (" your hosts are:", host_list[0:temp_val] ,"\n", "your commands are:" ,command_list[0:temp_val])
    host_list = set (host_list)
    commad_list = set (command_list)
    print ("your unique hostnames will be: ", host_list ,"\n" "your unique commds will be: " ,command_list )

elif user_input == 2:
     print ("Please enter the host which you want to remove from: " , host_list)
     hostnames = input ()
     host_list.remove (hostnames)
     print ("Please enter the command you want to remove from:", command_list)
     commands = input ()
     command_list.remove (commands)
     print (host_list , command_list)

else:
    print (" your hosts are: ",host_list,"\n","your commands are: " , command_list)

   
print ("we came to the end of the condition and program")  
    


