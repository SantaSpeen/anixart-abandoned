from anixart import AnixUserAccount, AnixAPI
from datetime import datetime
import time

anix_user = AnixUserAccount("rewrwerwfwef", "APIPassword")
anix = AnixAPI(anix_user)

print("\n\nAnixart time bot.")

while True:
	s = "✨ "+ datetime.now().strftime("%H:%M %d/%m/%Y")
	anix.profile.edit.status(s)
	print(f"Status edit: {s}")
	time.sleep(15)
