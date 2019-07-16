import json
from .Check import CheckUser

class Change():

    @staticmethod
    def changePassword(email, password, newPassword):
        userFound = False
        userFound = CheckUser.loginCheck(email, password)
        if userFound:
            with open('users.txt', 'r') as the_file:
                newUsers = []

                users = json.loads(the_file.read())
                for user in users:
                    if email == user['email']:
                        if password == user['password']:
                            user['password'] = newPassword
                    newUsers.append(user)
            with open('users.txt', 'w') as file:
                file.write(json.dumps(newUsers))

    @staticmethod
    def changeEmail():
        pass
