import requests
import json
import socket

# 🔹 Load configuration from .env file
from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = os.getenv('CLOUDFLARE_API_TOKEN')
ZONE_ID = os.getenv('CLOUDFLARE_ZONE_ID') 
RECORD_ID = os.getenv('CLOUDFLARE_RECORD_ID')
SUBDOMAIN = os.getenv('CLOUDFLARE_SUBDOMAIN')

if not all([API_TOKEN, ZONE_ID, RECORD_ID, SUBDOMAIN]):
    raise ValueError("Missing required environment variables. Please check your .env file.")

# 🔍 Get the current public IP of the machine
def get_public_ip():
    try:
        return requests.get("https://api4.ipify.org?format=json").json()["ip"]
    except Exception as e:
        print(f"Error getting public IP: {e}")
        return None

# 🔹 Update the DNS Record in Cloudflare
def update_dns_record(ip_address):
    url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{RECORD_ID}"
    
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    data = {
        "type": "A",  # Change to "AAAA" if using IPv6
        "name": SUBDOMAIN,
        "content": ip_address,
        "ttl": 300,  # 5 minutes
        "proxied": False  # Set to True if you want Cloudflare Proxy
    }

    response = requests.put(url, headers=headers, data=json.dumps(data))
    result = response.json()
    
    if result.get("success"):
        print(f"DNS Updated: {SUBDOMAIN} -> {ip_address}")
    else:
        print(f"Error updating DNS: {result}")

# 🚀 Run the script
if __name__ == "__main__":
    ip = get_public_ip()
    if ip:
        update_dns_record(ip)
    else:
        print("Could not fetch public IP. Exiting.")
