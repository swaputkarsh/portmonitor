#!/bin/bash

# Function to send email notification
send_email() {
  python3 ./app.py "$1" "$2"
}

# Check if Apache service is running
apache_status=$(systemctl is-active apache2)

# Check if the port is open
port_status=$(nc -zv localhost "3000" 2>&1)

# If Apache service is not running or port is closed, send email notification
if [ "$apache_status" != "active" ] || [[ "$port_status" == *"refused"* ]]; then
  send_email "$apache_status" "$port_status"
fi
