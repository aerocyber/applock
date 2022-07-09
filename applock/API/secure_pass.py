from passlib.context import CryptContext
import keyring

ctx = CryptContext(schemes=["bcrypt", "argon2", "scrypt"],
                   default="bcrypt",
                   bcrypt__rounds=18)

NAMESPACE = "applock"
ENTRY = "Password"


def secure_pass(pswd: str):
    """
        Secure password by hashing and storing in keyring.
        pswd[str]: Password.
    """
    hashed_pswd = ctx.hash(pswd)
    keyring.set_password(NAMESPACE, ENTRY, hashed_pswd)


def verify_pass(pswd: str):
    """
        Verify the password matches from that stored in keyring.
        pswd[str]: Password to be verified.
    """
    h_pass = keyring.get_password(NAMESPACE, ENTRY)
    return ctx.verify(pswd, h_pass)
