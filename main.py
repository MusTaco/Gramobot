
from tkinter.filedialog import askopenfilename
import json
from gramobot import login, post, comment, like

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
    # file_path = askopenfilename()
    # caption = input('Enter caption: ')
    # post.insta_post(file_path, caption)
    like_post = like.like_post('https://www.instagram.com/p/Cz6qMbgL4mZ/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA==')
    print(like_post)
    input()

