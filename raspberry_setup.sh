#!/bin/bash

# Set up Python virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Make the Python script executable
chmod +x cloudflare_ddns.py

echo "Setup complete! You can now run the script with: python cloudflare_ddns.py"
echo "To set up a cron job to run this automatically, use: crontab -e"
echo "Add this line to run every 5 minutes:"
echo "*/5 * * * * cd ~/cloudflare_ddns && source venv/bin/activate && python cloudflare_ddns.py >> ddns.log 2>&1" 