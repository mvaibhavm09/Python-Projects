# Code is written in python2
import zipfile

no_of_attempts = 1

with open('password.txt', 'r') as pass_list:
	for entry in pass_list.readlines():
		password = entry.strip()
		try:
			with zipfile.ZipFile('protected.zip','r') as zf:
				zf.extractall(pwd=password)
				data = zf.namelist()[0]
				data_size = zf.getinfo(data).file_size
				print('''******************************\n[+] Password found! ~ %s\n ~%s\n ~%s\n******************************'''
					% (password.decode('utf8'), data, data_size))
				break
		except:
			number = no_of_attempts
			print('[%s] [-] Password failed! - %s' % (number,password.decode('utf8')))
			no_of_attempts += 1
			pass


# Credit: W3W3W3
