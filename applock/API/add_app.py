import json
import keyring


NAMESPACE = "applock"
ENTRY = "Apps"


def add_app(app: str):
    """
        Apps that are to be locked, storing in keyring.
        app[str]: App.
    """
    apps = get_apps()
    if apps is None:
        apps = {"App": []}
    else:
        apps = json.loads(apps)
    apps["App"] = apps["App"].append(app)
    keyring.set_password(NAMESPACE, ENTRY, apps)


def get_apps():
    """
        Get list of apps from that stored in keyring.
    """
    return keyring.get_password(NAMESPACE, ENTRY)
