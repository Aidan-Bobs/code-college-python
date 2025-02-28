from user import user_profile as profile

def my_login(pf):
    """Handles user login authentication."""
    logged_in = False

    while not logged_in:
        print("Please Login:")
        un = input("What is your Username: ").strip()
        pw = input("What is your Password: ").strip()

        if un == profile.get("username") and pw == profile.get("password"):
            logged_in = True
            print(f"Here is your profile:\n{profile}")
        else:
            print("False entry.")