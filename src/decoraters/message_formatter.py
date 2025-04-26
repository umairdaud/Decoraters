def decorate(func):
    def decor():

        print("**########**")

        message = func()
        print(message)

        print("##********##")

    return decor
