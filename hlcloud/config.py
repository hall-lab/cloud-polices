import getpass, google.auth
from google.cloud import storage

class HLCConfig(object):
    __instance = None
    def __new__(cls):
        if HLCConfig.__instance is None:
            HLCConfig.__instance = object.__new__(cls)
            tok = google.auth.default()
            HLCConfig.__instance.credentials, HLCConfig.__instance.project = google.auth.default()
            HLCConfig.__instance.user = getpass.getuser()
        return HLCConfig.__instance

    # -- __new__

# -- HLCConfig
