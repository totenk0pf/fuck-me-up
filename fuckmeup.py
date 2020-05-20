import os, requests, json, random, string

url = "https://nhanskinlienminh-2018.weebly.com/ajax/apps/formSubmitAjax.php"
charlist = string.ascii_letters + string.digits + "!@#$%^&*()"
random.seed = os.urandom(1024)
data_path = os.path.abspath("MOCK_DATA.json")

with open(data_path, "r") as username_file:
    db = json.load(username_file)
    name_list = db["username"]

while True:
    username = random.choice(name_list)
    password = "".join(random.choice(charlist) for i in range(random.randrange(8,16)))
    requests.post(url, data = {
        "_u537729901536555550": username,
        "_u136221182933453064": password
    }, allow_redirects = False)
    print("Sent POST request with the following data - " + "Username: " + username + ", Password: " + password)