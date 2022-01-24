import time
from datetime import datetime

from anixart import AnixUserAccount, AnixAPI

anix_user = AnixUserAccount()
anix_user.id = 12345
anix_user.token = "token"
anix = AnixAPI(anix_user)

print("\n\nAnixart time bot.")

while True:
    s = "✨ " + datetime.now().strftime("%H:%M %d/%m/%Y")
    anix.profile.edit.status(s)
    print(f"Status edit: {s}")
    time.sleep(15)
