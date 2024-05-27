import requests

def checkUsername(name):
    url = f"https://github.com/{name}"
    rtrn = requests.get(url)

    if rtrn.status_code == 200: # Check page status for username
        return f"{name} is Taken :("
    else:
        return f"{name} is Available!"

    