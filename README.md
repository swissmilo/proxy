# Cloudflare DDNS Updater

A Python script that automatically updates Cloudflare DNS records with your current public IP address, effectively creating a Dynamic DNS service.

## Setup

1. Create a virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install requests python-dotenv
```

2. Create a `.env` file with your Cloudflare credentials:
```
CLOUDFLARE_API_TOKEN=your_api_token
CLOUDFLARE_ZONE_ID=your_zone_id
CLOUDFLARE_RECORD_ID=your_record_id
CLOUDFLARE_SUBDOMAIN=your.subdomain.com
```

## Usage

Run the script:
```bash
python cloudflare_ddns.py
```

The script will:
1. Get your current public IP address
2. Update the specified DNS record in Cloudflare
3. Print the result of the operation 