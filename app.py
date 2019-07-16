from UserFile.User import User
from UserFile.Check import CheckUser
from UserFile.Change import Change
from UserFile.Activate import Activate

#user1 = User(12, 'berk', 'elmas', 'berkelmas96@gmail.com', '123456')
#user2 = User(17, 'arınç', 'aslan', 'arincaslan@gmail.com', '1234dsda56')

#userCheck = User(12, 'berk', 'elmas', 'berkelmas96@gmail.com', '123456')
user2 = User(17, 'arınç', 'aslan', 'arincaslan@gmail.com', '1234dsda56')

#print(Change.changePassword(user2.get_email, user2.get_password, '123456'))
#user2.addUser()

Activate.activateEmail(user2.get_email, '6d3a3ace821424f6b59c92cf2240fe5fe126228f06cba5cbdab9329d0354dea3')
