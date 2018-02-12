from flask import Blueprint, render_template, request, redirect
import random
import requests

bp = Blueprint(__name__, __name__, template_folder='templates')

def random_string(length=16):
    final_string = ""
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    
    for i in range(0, length):
        final_string += chars[random.randint(0, len(chars)-1)]
    return final_string
    
    if __name__ == '__main__':
        main()

@bp.route("/createemail", methods=["POST", "GET"])
def show():
    if request.method == "POST":
        if request.form.get("sendemail"):
            fromaddress = request.form.get("senderaddress")
            sender = request.form.get("sendername")
            toaddress = request.form.get("receiveraddress")
            to = request.form.get("toname")
            subject = request.form.get("emailsubject")
            text = request.form.get("emailtext")
            entire_email = fromaddress + '  * ' + sender + \
                ' * ' + toaddress + ' * ' + to + ' * ' + subject + ' * ' + text
            
            apikey = '"7ad86c93d9b344b0bc4db49ded1311709c244048991740039de7d36638618530"'
            url = "https://messagingapis.paylite.net/api/email/send"


            with open("emailapp/emails/{}.email".format(random_string()), "w+") as _file:
                _file.write(entire_email)
            
            _file.close()

            payload = '''{ ApiKey:''' + apikey + ''',
            FromEmail: {
            Email: ''' + f'"{fromaddress}"' + ''',
            Name: ''' + f'"{sender}"' + '''
            },
            ToEmail: [
                {
                    Email:''' + f'"{toaddress}"' + ''',
                    Name: ''' + f'"{to}"' + '''
                }
            ],
            Subject: ''' + f'"{subject}"' + ''',
            HtmlContent: ''' + f'"{text}"' + '''
            }'''

            headers = {'Content-Type': 'application/json'}

            response = requests.request("POST", url, data=payload, headers=headers)
            print(response.text)

            return redirect("/")
            
    return render_template('createemail.html')
