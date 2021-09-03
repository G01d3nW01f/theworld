#!/usr/bin/python3

import os
import subprocess
import sys
import datetime

logo = """
The World!!!!!!!!
.'`~~~~~~~~~~~`'.
(  .'11 12 1'.  )
|  :10 \|   2:  |
|  :9   @   3:  |
|  :8       4;  |
'. '..7 6 5..' .'
 ~-------------~ 
"""

def init():
	print(logo)

	#os.system("timedatectl")

def change_timezone():

	os.system("date")

	print("Change the TimeZone")
	print("[+]Input the TimeZone DataBase Name_")
	print("[*]Check this site: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones")
	prompt = "> "
	chose = input(prompt)
	cmd = f"sudo timedatectl set-timezone {chose}"
	
	cmd_result = subprocess.getoutput(cmd)
	if "Failed" in cmd_result:
		print(f"Failed: {chose} is Invalid Value")

	else:

		print("Changed the Time zone!!!!!!")
		os.system("date")


if __name__ == "__main__":

	init()
	change_timezone()
