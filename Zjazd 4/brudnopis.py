last_login = {}
last_logout = {}
with open("logs.txt") as f:
    for line in f:
        login, action, time = line.split(";")
        time = int(time)
        if action == "LOGIN":
            last_login[login] = time
        elif action == "LOGOUT":
            last_logout[login] = time

    d3 = {key: last_logout[key] - last_login.get(key, 0) for key in last_logout}

