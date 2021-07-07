# Upload files to a seafile instance

## Fetching credentials first

For this scripts to work, a valid token is expected in hidden file
`.seafile-authtoken.json`.
You can fetch a token like this, replacing `MYSECRETPASSWORD` and `MYNAME`
appropriately:

```
curl -d "username=MYNAME@uni-bremen.de&password=MYSECRETPASSWORD" https://seafile.zfn.uni-bremen.de/api2/auth-token/ >.seafile-authtoken.json
```

With the token in place, uploads or any other calls to the
[seafile API](https://download.seafile.com/published/web-api/v2.1)
are possible.

## Usage

Check out 

- `bin/seafile-list-libraries.py` to list all your libraries, including their
  IDs
- `bin/seafile-update-current.py` to upload/update a fixed file to a library
  specified by the library's ID

## Dependencies

The scripts require the `requests` package.
Either install it with your system's package manager, or with `pip` in a
virtual environment or directly into your user packages:

```
python3.8 -m pip install --user requests
```

## Copyright
ISC (C) Robert Schmidt 2021
