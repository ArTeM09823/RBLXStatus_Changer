import requests,random,time,os,json

os.system('cls')

#Load CFG
cfg = open('config.json')
data = json.load(cfg)
words = data['Words']
cookie = data['Cookie']
seconds = data['Seconds']


rand_text = words
os.system('cls')

session = requests.session()
session.cookies['.ROBLOSECURITY'] = cookie

os.system("cls")

def random_gen(len):
        return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890') for x in range(len))

def grabCSRF(): #GrabCSRF not mine
   r = session.post("https://auth.roblox.com/v2/user/passwords/change")
   csrf = r.headers['x-csrf-token']
   return csrf

#Checks Cookie
try:
    grabCSRF()
except KeyError:
    print("Cookie is invalid!")
    input()

os.system("cls")

csrf = grabCSRF()

while True:
    time.sleep(seconds)
    rand_status = random.choice(rand_text)
    sfo = {
        "description":rand_status
    }
    s = session.post(url = "https://accountinformation.roblox.com/v1/description",headers ={"X-CSRF-Token": csrf},data=sfo)
    if "403" in str(s.status_code):
        print("Cooldown Detected! Please wait 60 secs | Status Code: " + str(s.status_code))
        time.sleep(60)
    else:
        print("Status Changed to: " + rand_status + " | Status Code: " + str(s.status_code) + " | " + s.json()["description"] )

input()