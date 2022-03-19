import requests

data = {'userId': '',
        'password': '',
        'serviceName': 'ProntoAuthentication',
        'Submit22': 'Login'
        }

URL = '''http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://captive.apple.com/hotspot-detect.html'''
requests.post(URL, data, timeout=5)

# Curl command taken from Burpsuite

# curl -i -s -k -X $'POST' \
#     -H $'Host: phc.prontonetworks.com' -H $'Content-Length: 80' -H $'Cache-Control: max-age=0' -H $'Sec-Ch-Ua: \"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"' -H $'Sec-Ch-Ua-Mobile: ?0' -H $'Sec-Ch-Ua-Platform: \"Windows\"' -H $'Upgrade-Insecure-Requests: 1' -H $'Origin: https://phc.prontonetworks.com' -H $'Content-Type: application/x-www-form-urlencoded' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' -H $'Sec-Fetch-Site: same-origin' -H $'Sec-Fetch-Mode: navigate' -H $'Sec-Fetch-User: ?1' -H $'Sec-Fetch-Dest: document' -H $'Referer: https://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://google.com/' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: en-US,en;q=0.9' -H $'Connection: close' \
#     --data-binary $'userId=19BCE2030&password=GUV67N&serviceName=ProntoAuthentication&Submit22=Login' \
#     $'https://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://captive.apple.com/hotspot-detect.html'
