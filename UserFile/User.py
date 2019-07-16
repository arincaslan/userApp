import json
import hashlib
import smtplib
import ssl

import traceback

class User():
    def __init__(self, id, name, surname, email, password):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

        self.list = []
        self.emailActivated = False
        self.emailActivateKey = hashlib.sha256(self.name.encode()).hexdigest()

    def addUser(self):
        users = ''

            #self.list.append({'id' : self.id, 'name' : self.name, 'surname' : self.surname, 'email' : self.email, 'password' : self.password})
        with open('users.txt', 'r') as the_file:
            users = json.loads(the_file.read())
            users.append({'id' : self.id, 'name' : self.name, 'surname' : self.surname, 'email' : self.email, 'password' : self.password, 'emailActivated' : self.emailActivated, 'emailActivateKey' : self.emailActivateKey})

        with open('users.txt', 'w') as file:
            file.write(json.dumps(users))
            self.sendActivationMail()
                #the_file.write("{'id' : %s, 'name' : %s, 'surname' : %s, 'email' : %s, 'password' : %s}" % (self.id, self.name, self.surname, self.email, self.password))

    def sendActivationMail(self):
        gmail_user = 'a.arincaslan@gmail.com'
        gmail_password = 'PASSWROD_WILL_COME_HERE'

        sent_from = 'arincaslan@gmail.com'
        to = ['berkelmas96@gmail.com']
        subject = 'Email Onay Maili'
        body = self.emailActivateKey

        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)
        context = ssl.create_default_context()

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(gmail_user, gmail_password)
                server.sendmail(sent_from, to, email_text)
                server.close()

                print('Email Gönderildi...')

        except Exception:
            traceback.print_exc()


    @property
    def get_email(self):
        return self.email

    @property
    def get_password(self):
        return self.password

    @property
    def get_activation_key(self):
        return self.emailActivateKey
