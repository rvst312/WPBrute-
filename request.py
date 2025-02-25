import json
from concurrent.futures import ThreadPoolExecutor, as_completed

from config import FIXED_USERNAME, MAX_WORKERS
from password_handler import try_password
from logger import log_success, print_success
from password_generator import load_and_generate_passwords

def main():
    try:
        # Load passwords from JSON file
        with open('credentials.json', 'r') as file:
            password_data = json.load(file)
        
        passwords = load_and_generate_passwords(password_data)
        print(f"Generated {len(passwords)} password combinations to test\n")
        
        print(f"Testing {len(passwords)} passwords for user: {FIXED_USERNAME}\n")

        # Use ThreadPoolExecutor for parallel password testing
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            future_to_password = {executor.submit(try_password, pwd): pwd for pwd in passwords}
            
            for future in as_completed(future_to_password):
                success, password = future.result()
                if success:
                    print_success(FIXED_USERNAME, password)
                    log_success(FIXED_USERNAME, password)
                else:
                    print(f"❌ Failed password: {password}")

    except FileNotFoundError:
        print("❌ Error: credentials.json file not found")
    except json.JSONDecodeError:
        print("❌ Error: Invalid JSON format in credentials.json")
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()