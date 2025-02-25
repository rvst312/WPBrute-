def generate_combinations(base_words, combinations, suffixes):
    passwords = set()
    
    # Handle single string or list of base words
    if isinstance(base_words, str):
        base_words = [base_words]
    
    # Generate combinations for each base word
    for base in base_words:
        # Base word alone
        passwords.add(base)
        passwords.add(base.capitalize())
        
        # Base + combination
        for combo in combinations:
            passwords.add(f"{base}{combo}")
            passwords.add(f"{base.capitalize()}{combo}")
        
        # Base + suffix
        for suffix in suffixes:
            passwords.add(f"{base}{suffix}")
            passwords.add(f"{base.capitalize()}{suffix}")
        
        # Base + combination + suffix
        for combo in combinations:
            for suffix in suffixes:
                passwords.add(f"{base}{combo}{suffix}")
                passwords.add(f"{base.capitalize()}{combo}{suffix}")
    
    return list(passwords)

def load_and_generate_passwords(json_data):
    all_passwords = []
    for cred in json_data['credentials']:
        base_words = cred['base']
        combinations = cred['combinations']
        suffixes = cred['suffixes']
        
        passwords = generate_combinations(base_words, combinations, suffixes)
        all_passwords.extend(passwords)
    
    return list(set(all_passwords))  # Remove any duplicates