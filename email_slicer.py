# collect email from user
# split the email using the @ symbol, save the first part as the user name
# split domain using ".",

def main():
    print(" Welcome to the email slicer")
    print("")

    email_input = input("Input your email addresss : ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username :", username)
    print("Domain :", domain)
    print("Extension :", extension)


main()
