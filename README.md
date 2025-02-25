# WordPress Brute Force Tester

A Python-based tool designed to test the security of WordPress websites by simulating brute force attacks on the `wp-admin` login page. This tool is intended for **ethical hacking**, **security testing**, and **educational purposes only**. Use it responsibly and only on systems you own or have explicit permission to test.

---

## Features

- **Customizable Wordlist Generation:** Generate password lists dynamically based on patterns.
- **Multi-threaded Requests:** Perform multiple login attempts simultaneously for faster testing.
- **Logging:** Detailed logging of attempts, including successful logins.
- **Configuration:** Easily configure target URL, usernames, and other parameters.
- **Success Tracking:** Stores successful login attempts in `successful_logins.txt`.

---

## File Structure
├── config.py # Configuration file for target URL, usernames, etc.
├── credentials.json # Stores credentials for testing (if needed).
├── logger.py # Handles logging of attempts and results.
├── password_generator.py # Generates password lists for brute force attempts.
├── password_handler.py # Manages password lists and iteration.
├── request.py # Handles HTTP requests to the WordPress login page.
└── successful_logins.txt # Stores successfully cracked credentials.
