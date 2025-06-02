import random
import string
import re

f_chars = "1lIoO0"
s_chars = "_@$!:.,;&'(-=+)"
r_chars = string.ascii_letters + string.digits + string.punctuation
i = random.randint(12, 20)
def generate_password(length=i):
    while True:
        password = ''.join(random.choices(r_chars, k=length))
        if (re.search(r"[a-z]", password) and
            re.search(r"[A-Z]", password) and
            re.search(r"[0-9]", password) and
            re.search(f"[{re.escape(s_chars)}]", password) and
            not any(c in f_chars for c in password)):
            return password

secure_password = generate_password()
print(secure_password)
