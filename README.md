# Ad Hoc Utility

Since iOS and Android promo codes are a hassle to figure out (in terms of delivering the codes to people),
this script will help automate sending those codes.

- Add the emails and promo codes in Google Sheet
- Configure env for this script
    - Mailjet credentials `.config/env`
    - Google credentials `.config/service_account.json`
    - Google spreadsheet id

```
SPREADSHEET_ID=
MJ_APIKEY_PUBLIC=
MJ_APIKEY_SECRET=
FROM_EMAIL=
FROM_NAME=
FROM_SUBJECT=
```

- Hit `python send.py` and you're good to go.