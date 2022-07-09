import json
import keyring


NAMESPACE = "applock"
ENTRY = "Apps"


def remove_app(app: str):
    """
        Apps that are to be locked, storing in keyring.
        app[str]: App.
    """
    apps = get_apps()
    if apps is None:
        apps = {"App": [app]}
    else:
        apps = json.loads(apps)
    apps["App"] = apps["App"].remove(app)
    keyring.set_password(NAMESPACE, ENTRY, apps)


def get_apps():
    """
        Get list of apps from that stored in keyring.
    """
    return keyring.get_password(NAMESPACE, ENTRY)
