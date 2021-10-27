# networking-in-py
Python scripts for interacting with different networks

## emailClient.py
Sends an email through SMTP server of specified email service. Currently supports only Gmail and Yahoo. Since it doesn't use any OAuth authorization method, set the sender email to allow insecure access and disable any 2FA for it. Maybe just create a new email for this purpose.
## portScanner.py
A simple port scanner that simply indicates whether the port is open or not. Use the -h command-line option to know about the usage of arguments.
## weatherApp.py
Uses OpenWeatherMap API to retrieve current weather for any city in JSON format. The script includes the credentials to an account made for creating this API key. Anyone can generate keys for themselves, just **don't tamper with the password** since the email is a temporary one.
## webScrapper.py
A simple script for practicing web scrapping in Python3. This script simply extracts headings of latest news from the NDTV website. *Requires `bs4` and `lxml` modules to work.*
