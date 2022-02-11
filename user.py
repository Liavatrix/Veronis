from sanic_jwt import exceptions


class User:

    def __init__(self, id, username, password):
        self._user_id = id
        self._username = username
        self._password = password

    @property
    def username(self):
        return self._username

    @property
    def user_id(self):
        return self._user_id

    @property
    def password(self):
        return self._password

    def __repr__(self):
        return "User(id='{}')".format(self._user_id)

    def to_dict(self):
        return {"user_id": self._user_id, "username": self._username}


USERNAME = "VERONIS"
PASSWORD = "1234"

USERS = [User(id=1, username=USERNAME, password=PASSWORD), ]
username_table = {u.username: u for u in USERS}


class Authenticate:
    @classmethod
    def authenticate(cls, username, password):
        if not username or not password:
            raise exceptions.AuthenticationFailed("Missing username or password.")

        user = username_table.get(username, None)
        if user is None:
            raise exceptions.AuthenticationFailed("Bad login")

        if password != user.password:
            raise exceptions.AuthenticationFailed("Bad login")

        return user
