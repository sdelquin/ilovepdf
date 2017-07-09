# iLovePDF

Python module that wraps the [iLovePDF REST API](https://developer.ilovepdf.com/docs/api-reference).

## Disclaimer

At this moment, `compress` is the only task that is implemented and tested.

## Developer Keys

In order to work properly with the module, you will have to get the developer keys from https://developer.ilovepdf.com/. You will have to sign up and then go to `Console -> My project`. There you will find two keys:
- Project key (JTI Claim) aka **Public key**.
- **Secret key**.

Both keys should be written in `config.py`.

## Python versions

The lib is compatible from *Python 2.7* to *Python 3.6*.

## Tests

```console
> pip install -r requirements
> cp config.tmpl.py config.py
# modify config.py with your keys
> pytest
```
