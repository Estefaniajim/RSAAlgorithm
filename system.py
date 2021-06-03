import manager

personalManager = manager.PersonalManager()


def menu():
    print("Welcome to my final project")
    print("This is a really  insecure cryptoCoin")
    print("First lets create an user")
    print("Enter your username: ")
    userName = input()
    user = manager.User(userName)
    print("Great!! now choose and option")
    print("1. Sent money to user")
    print("2. Sent my public key to another user")
    print("3. Leave")
    option = input()
    if option == 1:
        print("Enter the user of the person")
        person = input()
        print("Now enter the key they gave you")
        key = input()
        if personalManager.ValidateKey(person, key):
            print("Great!, you have a valid key for the user. But this is not real so we dont sent money, bye!")
            return
    if option == 2:
        print("Send it youself c:, here is your encrypted key")
        print(user.sentKey())
        return
    if option == 3:
        print("bye")
        return


personalManager.addUser(manager.User("Juan"))
personalManager.addUser(manager.User("Pepe"))

menu()