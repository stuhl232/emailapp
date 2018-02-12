import requests

url = "https://messagingapis.paylite.net/api/email/send"

payload = '''{
    "ApiKey": "7ad86c93d9b344b0bc4db49ded1311709c244048991740039de7d36638618530",
    "FromEmail": {
        "Email": "stuphikappa@gmail.com",
        "Name": "Stu"
        },
        "ToEmail": [
            {
                "Email": "stuart.h.longley@gmail.com",
                "Name": "To Name"
            }
        ],
        "Subject": "Subject goes here",
        "HtmlContent": "Html body goes here" 
    }'''
headers = {'Content-Type': 'application/json'}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
