# Python program to explain os.DirEntry.inode() method 

# importing os module 
import os 


# Directory to be scanned 
path = os.getcwd() 

# Using os.scandir() method 
# scan the specified directory 
# and yield os.DirEntry object 
# for each file and sub-directory 

print("Directory entry name and their inode number") 
with os.scandir(path) as itr: 
	for entry in itr : 
		# Exclude the entry name 
		# starting with '.' 
		if not entry.name.startswith('.') : 
			# print entry name 
			# and entry's inode() number 
			print(entry.name, " :", entry.inode()) 
