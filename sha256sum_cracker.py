from pwn import *
import sys

if len(sys.argv) != 2:
	print("Please enter a valid argument!")
	print(">> {} <sha256sum hash>".format(sys.argv[0]))
	exit()

entered_hash = sys.argv[1]
password_file = "rockyou.txt"
attempts = 0

with log.progress("Attempting to back: {}!\n".format(entered_hash)) as p:
	with open(password_file, "r", encoding='latin-1') as pass_list:
		for password in pass_list:
			password = password.strip("\n").encode('latin-1')
			password_hash = sha256sumhex(password)
			p.status("[{}] {} == {}".format(attempts, password.decode('latin-1'), password_hash))
			if password_hash == entered_hash:
				p.success(">> Password hash found:{}".format(password.decode('latin-1')))
				exit()
			attempts += 1
		p.failure("Sorry :( Password not found.")
    
#Credit: TCM Security
