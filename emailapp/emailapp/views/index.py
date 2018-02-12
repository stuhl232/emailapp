from flask import Blueprint, render_template
import glob

bp = Blueprint(__name__, __name__, template_folder='templates')

def fetch_emails():
    final_emails = []
    emails = glob.glob('emailapp/emails/*.email')

    for email in emails:
        with open(email) as _file:
            final_emails.append(_file.read())
        
        _file.close()

    return final_emails    

@bp.route("/")
def show():
    return render_template('index.html', emails=fetch_emails())
