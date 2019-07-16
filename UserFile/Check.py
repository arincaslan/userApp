import json

class CheckUser():
    @staticmethod
    def loginCheck(email, password):
        userFound = False
        with open('users.txt', 'r') as the_file:
            users = json.loads(the_file.read())
            for user in users:
                if email == user['email']:
                    if password == user['password']:
                        userFound = True
            if userFound:
                return userFound
            else:
                return userFound
