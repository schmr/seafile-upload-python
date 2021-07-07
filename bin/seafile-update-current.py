#!/usr/bin/env python3.8
"""Upload and/or update a local file to a seafile repository"""

import requests
import json

# Update BASEURL and REPO to point to your instance and repository
BASEURL = "https://seafile.zfn.uni-bremen.de"
REPO = "ed0f8801-70f3-40b6-9554-ef1c8e89ce05"
URL = BASEURL + "/api2/repos/" + REPO + "/upload-link/"


with open(".seafile-authtoken.json", "r") as fh:
    token = json.load(fh)["token"]

headers = {"Authorization": "Token " + token}
uploadlink = requests.get(URL, headers=headers)

# This request uploads the file `top.pdf` to the subfolder `current/` in REPO
resp = requests.post(
    uploadlink.json(),
    data={
        "filename": "top.pdf",
        "parent_dir": "/",
        "relative_path": "current/",
        "replace": "1",
    },
    files={"file": open("top.pdf", "rb")},
    headers=headers,
)

# Raise if something went bad
resp.raise_for_status()
