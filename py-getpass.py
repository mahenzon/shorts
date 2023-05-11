"""
Get user password
"""

from getpass import getpass

password = getpass(
    prompt="Enter your password: ",
)

print("Pass:", password)
