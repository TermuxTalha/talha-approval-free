print(logo)
		print("")
		print("\033[1;37m     Youtube Channel  No Subscribe No Approved")
		print("")
		print("\033[1;32m [1] First Subscribe My Youtube Channel")
		print("\033[1;33m [2] Exit")
		print("")
		Baloch = input("\n\033[1;31m  Chose ==> \033[1;32m")
		if Baloch in ["", " "]:
			exit()
		elif Baloch in ["2", "02"]:
			print("    Thanks♥️")
			exit()
		elif Baloch in ["1", "01"]:
			os.system("xdg-open https://youtube.com/c/TalhaTechnologychannel")
			print("")
			time.sleep(2.0)
			print("\033[1;33m    Type Your Youtube Gmail : ")
			print("")
			input("\n\033[1;32m  Type Name ==> \033[1;36m")
			time.sleep(2.1)
			print("")
			print("\033[1;32m Successful Bro")
			time.sleep(2.0)
			os.system("clear")
