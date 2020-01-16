#Write a script to expand on your user roles script. Provide a prompt to the user to query them for their name. Your roles should now be kept in a dictionary and you should be able to obtain the role from that dict. In the event that you do not have a role for the name you should tell them that the role is Unknown.

roles_list = {"aditya" : "OC" , "ron" : "Manager" , "tim" : "CEO" }

try:
    
    user_req = input ("please enter your name: ")
    user_req = user_req.lower()
    print ("Hi",user_req,"your role in the company is:", roles_list[user_req])

except KeyError:
    
    print ("Sorry",user_req,"your role in unknown in company")
