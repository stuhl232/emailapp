url = "https://messagingapis.paylite.net/api/email/send"

payload = "{\r\n\t\"ApiKey\": \"7ad86c93d9b344b0bc4db49ded1311709c244048991740039de7d36638618530\",
\r\n\t\"FromEmail\": {\r\n\t\t\"stuphikappa@gmail.com\": \"From Email\",
\r\n\t\t\"Name\": \"From Name\"\r\n\t},

\r\n\t\"ToEmail\": [\r\n\t{\r\n\t\t\"stuart.h.longley@gmail.com\": \"To Email Address\",
\r\n\t\t\"Name\": \"To Name\"\r\n\t}\r\n\t],
\r\n\t\"CcEmail\": [\r\n\t{\r\n\t\t\"Email\": \"Cc Email Address\",
\r\n\t\t\"Name\": \"Cc Name\"\r\n\t}\r\n\t],
\r\n\t\"BccEmail\": [\r\n\t{\r\n\t\t\"Email\": \"Bcc Email\",
\r\n\t\t\"Name\": \"Bcc Name\"\r\n\t}\r\n\t],

\r\n\t\"Subject\": \"Subject goes here\",
\r\n\t\"HtmlContent\": \"Html body goes here\" \r\n}"
headers = {'Content-Type': 'application/json'}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
