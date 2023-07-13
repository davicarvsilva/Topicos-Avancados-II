import hashlib

class Usuario:
    def __init__(self, login, password):
        self.id = None
        self.login = login
        self.password = hashlib.sha256(password.encode()).hexdigest()

    def __eq__(self, other):
        if isinstance(other, Usuario):
            return (
                self.login == other.login and
                self.password == other.password
            )
        return False