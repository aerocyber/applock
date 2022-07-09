from passlib.context import CryptContext
import keyring
ctx = CryptContext(schemes=["bcrypt", "argon2", "scrypt"],
                   default="bcrypt",
                   bcrypt__rounds=18)

NAMESPACE = "applock"
ENTRY = "Password"


def change_pass(old_pswd: str, new_pswd: str):
    """
        Secure password by hashing and storing in keyring.
        pswd[str]: Old password.
    """
    if old_pswd == new_pswd:
        return "Old password and new passwords are the same!"
    elif not verify_pass(old_pswd):
        return "Password mismatched!"
    hashed_pswd = ctx.hash(new_pswd)
    try:
        keyring.delete_password(NAMESPACE, ENTRY)
    except Exception:
        pass
    keyring.set_password(NAMESPACE, ENTRY, hashed_pswd)


def verify_pass(pswd: str):
    """
        Verify the password matches from that stored in keyring.
        pswd[str]: Password to be verified.
    """
    h_pass = keyring.get_password(NAMESPACE, ENTRY)
    return ctx.verify(pswd, h_pass)
