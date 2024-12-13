import re

def parse_email(email):
    pattern = r'([^@]+)@(.+)'
    match = re.match(pattern, email)
    
    if match:
        username = match.group(1)
        domain = match.group(2)
        return username, domain
    else:
        return None, None

email = input("Введите ваш email: ")

username, domain = parse_email(email)

if username and domain:
    print(f"username: {username}\ndomain: {domain}")
else:
    print("Неверный формат email.")
