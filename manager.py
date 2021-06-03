import RSAAlgorithm as RSA
class User:
  def __init__(self, userName):
    self.userName = userName
    self.keys = RSA.generateKeys()
    puK, n = self.keys["public"]
    prK = self.keys["private"]
    self.encrypted, self.original = RSA.encrypt(puK, n)
    print("User created")

  def sentKey(self):
      return self.encrypted

  def checkPuK(self):
      return self.puK

class PersonalManager:
    def __init__(self):
        self.users = {}

    def addUser(self, user):
        if user.userName not in self.users:
            self.users[user.userName] = user.keys
        else:
            print("Username already taken, please choose another one")
            return

    def sendUsers(self):
        for user in self.users:
            print(user)

    def ValidateKey(self, user, key):
        if self.users[user]:
            if RSA.decrypt(self.users[user].prK, key) == self.users[user].original:
                return True
            else:
                return False