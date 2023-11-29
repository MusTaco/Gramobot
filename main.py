
from tkinter.filedialog import askopenfilename
import json
from gramobot import login, post, comment, like, dm, follow, unfollow

def get_credentials():

    with open('settings.json', 'r') as f:
        data = json.load(f)
        credentials = data.get('credentials', {})
    username = credentials.get('username', '')
    password = credentials.get('password', '')
    
    return username, password

credentials = get_credentials()

if __name__ == '__main__':
    login.login(credentials[0], credentials[1])
    follow_user = unfollow.unfollow_user('username..')
    print(follow_user)
    input()

