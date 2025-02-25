import time

def log_success(username, password):
    with open('successful_logins.txt', 'a') as f:
        f.write(f"\nSuccessful login at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Username: {username}\nPassword: {password}\n")
        f.write("="*50 + "\n")

def print_success(username, password):
    success_message = f"✅ PASSWORD FOUND!\nUsername: {username}\nPassword: {password}"
    print("\n" + "="*50)
    print(success_message)
    print("="*50 + "\n")