from passlib.context import CryptContext


class Crypto:
    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def encrypt(self, secret: str) -> str:
        return self.pwd_context.hash(secret)

    def verify(self, plain: str, hashed: str) -> bool:
        return self.pwd_context.verify(plain, hashed)
