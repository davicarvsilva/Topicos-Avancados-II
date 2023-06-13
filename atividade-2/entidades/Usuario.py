class Usuario:
    def __init__(self, login, password):
        self.login = login
        self.password = hash(password)