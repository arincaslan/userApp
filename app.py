from UserFile.User import User
from UserFile.Check import CheckUser
from UserFile.Change import Change

#user1 = User(12, 'berk', 'elmas', 'berkelmas96@gmail.com', '123456')
#user2 = User(17, 'arınç', 'aslan', 'arincaslan@gmail.com', '1234dsda56')

#userCheck = User(12, 'berk', 'elmas', 'berkelmas96@gmail.com', '123456')
user2 = User(17, 'arınç', 'aslan', 'arincaslan@gmail.com', '1234dsda56')

print(Change.changePassword(user2.get_email, user2.get_password, '123456'))
