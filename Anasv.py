import requests
import time

# Define your Instagram credentials
username = "anasalsibani"
password = "Ins101325"

# Define the function for reporting spam accounts
def report_spam(account_urls):
    session = requests.Session()
    
    # Log in to Instagram
    login_url = "https://www.instagram.com/accounts/login/ajax/"
    login_data = {"username": username, "password": password}
    session.headers.update({"user-agent": "Mozilla/5.0"})
    session.post(login_url, data=login_data)
    
    # Wait for the login process to complete
    time.sleep(5)
    
    # Report spam for each account
    for url in account_urls:
        report_url = url + "?__a=1"
        response = session.get(report_url)
        
        if response.status_code == 200:
            user_id = response.json()["graphql"]["shortcode_media"]["owner"]["id"]
            report_api_url = f"https://www.instagram.com/users/{user_id}/report/"
            report_data = {"source_name": "", "reason_id": 1, "frx_context": ""}
            report_response = session.post(report_api_url, data=report_data)
            
            if report_response.status_code == 200:
                print(f"Successfully reported {url} as spam.")
        
        time.sleep(60)

# Define the list of spam accounts to report
spam_accounts = [
    "https://www.instagram.com/spam_account1/",
    "https://www.instagram.com/spam_account2/",
    "https://www.instagram.com/spam_account3/",
]

# Report spam for each account
report_spam(spam_accounts)
