from requests import get
from bs4 import BeautifulSoup
from time import sleep as unnecessaryPause

# Access URL and check if it is accessible
url = "https://www.ndtv.com/latest"
result = get(url)
status = False
for i in range(5):
    if result.status_code == 200:
        print("[+] URL accessible, parsing content")
        status = True
        unnecessaryPause(1)
        break
    else:
        print("[-] Unable to reach URL, attempting again")
        unnecessaryPause(1)

# Exit program if URL not reachable
if(not status):
    print("[-] Page unreachable, check the URL or server status and try again.")
    quit()

# Get headings from latest news page and print
parsedContent = BeautifulSoup(result.content, 'lxml')
headings = parsedContent.find_all(class_="newsHdng")
for heading in headings:
    print("--------------------------------------------------")
    print(heading.text)
    unnecessaryPause(0.2)

# Option to write down headings for use in other programs
if input("\nSave headings to a file?(y/n): ") == 'y':
    print("[+] Writing headings to _headings.txt")
    unnecessaryPause(0.5)
    with open("_headings.txt", "w") as f:
        for heading in headings:
            writeHeading = heading.text+"\n"
            f.write(writeHeading)
    print("[+] Done")
print("[+] Skipping...")
unnecessaryPause(0.2)
