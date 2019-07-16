import json

class registerUser():

    def __init__(self, id, name, surname, email, password):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

        self.list = []

    def addUser(self):
        users = ''

            #self.list.append({'id' : self.id, 'name' : self.name, 'surname' : self.surname, 'email' : self.email, 'password' : self.password})
        with open('users.txt', 'r') as the_file:
            users = json.loads(the_file.read())
            users.append({'id' : self.id, 'name' : self.name, 'surname' : self.surname, 'email' : self.email, 'password' : self.password})

        with open('users.txt', 'w') as file:
            file.write(json.dumps(users))
                #the_file.write("{'id' : %s, 'name' : %s, 'surname' : %s, 'email' : %s, 'password' : %s}" % (self.id, self.name, self.surname, self.email, self.password))

user1 = registerUser(12, 'berk', 'elmas', 'berkelmas96@gmail.com', '123456')
user2 = registerUser(17, 'arınç', 'aslan', 'arincaslan@gmail.com', '1234dsda56')

print(user2.addUser())
