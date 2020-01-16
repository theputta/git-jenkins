total_size = 100
print ("Please enter The total size of the disk in use (in GBs)")

try:
    disk_use = input ()
    float_disk_use = float (disk_use)
    disk_left = 100 - float_disk_use
    
except ValueError:
    print ("you have entered string value whihc is: ",disk_use)
    print ("only INT/FLOAT is acceptable")
    print ("taking by default, 10GB")
    disk_use = 10
    float_disk_use = float (disk_use)
    disk_left = 100 - float_disk_use
    
if disk_left >= 90.00 :
    print ("Please clean your disk since you have just",disk_left,"GB left")
elif disk_left >= 70 :
    print ("Please use your soace carefully, since you have just",disk_left,"GB left")
else:
    print ("you have lot of space left over and to be precise its",disk_left,"GB")


