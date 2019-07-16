import json

class Activate():

    @staticmethod
    def activateEmail(email, activateKey):
        newUsers = []
        with open('users.txt', 'r') as the_file:
            users = json.loads(the_file.read())
            for user in users:
                if user['email'] == email:
                    if user['emailActivateKey'] == activateKey:
                        user['emailActivated'] = True
                newUsers.append(user)
        with open('users.txt', 'w') as file:
            print(newUsers)
            file.write(json.dumps(newUsers))
