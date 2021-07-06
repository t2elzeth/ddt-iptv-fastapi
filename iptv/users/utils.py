from secrets import token_urlsafe


def generate_authtoken():
    return token_urlsafe(64)
