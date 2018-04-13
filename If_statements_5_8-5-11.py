# different messages to users in a list using a if statement and for loop
usernames = ['admin', 'john', 'ammie', 'bubba']

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello " + username.title() + 
                  " would you like to see status report?")
        else: 
            print("Hello " + username.title() + 
                  "thank you for logging in again!")

else:
    print("We need to find some users!")

current_users = ['admin', 'john', 'ammie', 'bubba', 'lobster']

new_users = ['bob', 'teddy', 'admin', 'Ammie', 'enderman' ]

lowercase_new_users = []

if new_users:      
    for new_user in new_users:
        if new_user.lower() in current_users:
            print(new_user + " is not avalible for use.")
        else:
            print(new_user + " is avalible for use.")

