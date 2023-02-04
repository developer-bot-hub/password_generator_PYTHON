def password_generator(num):
    chars = "AbCdEfGhIjK"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 3
    password = f"{chars[c1]}{chars[c2]}{num*27}{chars[c3]}{num*34}"
    return password
PASSWORD = password_generator(3)
message = f"suggested password: {PASSWORD}"
print(message)