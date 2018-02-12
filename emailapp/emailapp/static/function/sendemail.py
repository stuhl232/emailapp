import requests

apikey = '"7ad86c93d9b344b0bc4db49ded1311709c244048991740039de7d36638618530"'
url = "https://messagingapis.paylite.net/api/email/send"

payload = '''{ ApiKey:''' + apikey + ''',
    FromEmail: {
        Email: 'stuphikappa@gmail.com',
        Name: 'Stu'
        },
        ToEmail: [
            {
                Email: 'emily.grimball@gmail.com',
                Name: 'Emily G'
            }
        ],
        Subject: 'sand is for...',
        HtmlContent: 'Beaches! I am sending this email from the program I write today!'
    }'''
headers = {'Content-Type': 'application/json'}

print (payload)

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
