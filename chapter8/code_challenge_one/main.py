# MAIN CHALLENGE (all that is needed to solve the problem):
# Separate the following program into atleast 2 separate modules

# TIPS:
# A third module is possible in order to neaten your code even further.
# The more Python practices you utilize, the more points you get.
# You can neaten up one of the functions to make your code even more easy to manage.

# THE ZEN OF PYTHON:

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!


from account import create_account as ca
from auth import my_login as login
from user import user_profile as prfl

def main():
   
    ca()
    login(prfl)


main()