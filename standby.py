import os
import sys

print("StandBy!!!!!!")

if os.geteuid() != 0:
	print("You need execute this as root_privilege")
	sys.exit()

else:
	print("You are root user good")
	os.system("sudo cp theworld.py /usr/local/bin/theworld")
	print("Done!!!!!!")
