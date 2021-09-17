import threading

import AminoLab

client = AminoLab.Client()
email = input("Email >> ")
password = input("Password >> ")
client.auth(email=email, password=password)

clients = client.my_communities()
for x, name in enumerate(clients.name, 1):
 print(f"{x}.{name}")
ndc= clients.ndcId[int(input("Select the community >> "))-1]
chats = client.get_from_link(input("link chat:")).objectId
print(chats)
def join():
 return client.join_thread(ndc, chats)
def lv():
 return client.leave_thread(ndc, chats) 
while True:
 threading.Thread(target=join).start()
 threading.Thread(target=lv).start()