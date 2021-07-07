#!/usr/bin/env python3.8
"""List all your repositories"""

import requests
import json

BASEURL = "https://seafile.zfn.uni-bremen.de"
URL = BASEURL + "/api2/repos/"

with open(".seafile-authtoken.json", "r") as fh:
    token = json.load(fh)["token"]

headers = {"Authorization": "Token " + token}

resp = requests.get(URL, headers=headers)

print(json.dumps(resp.json(), sort_keys=True, indent=4))
