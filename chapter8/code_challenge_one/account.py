from user import user_profile as empty_profile

def create_account():
    """Stores user details in the global user_profile dictionary."""
    global empty_profile
    empty_profile.update({
        "username": input("What would you like your username to be: ").strip(),
        "password": input("What would you like your password to be: ").strip(),
        "firstname": input("What is your first name: ").strip(),
        "lastname": input("What is your last name: ").strip(),
        "location": input("Where do you stay: ").strip()
    })