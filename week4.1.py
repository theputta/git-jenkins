#Write a script which prompts the user five times for a hostname (hint: Use a while loop!) and appends the, input to a list. Cast that list to a set, and print out the set to inform the user of the unique hostnames they provided.


host_list = {"null"}
var = 0

while var <= 4:
    host_input = input ("Please enter the hostname: ")
    var = var + 1 
    host_list.append(host_input)

host_list.discard("null")
print ("the unique hosts you have entered till now are: \n ", host_list)
    