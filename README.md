# iLovePDF

Python module that wraps the [iLovePDF REST API](https://developer.ilovepdf.com/docs/api-reference).

## Installation

```console
$> mkvirtualenv ilovepdf
$> workon ilovepdf
$> git clone git@github.com:sdelquin/ilovepdf.git
$> cd ilovepdf
$> pip install -r requirements
$> cp config.tmpl.py config.py
# modify config.py with your keys
```

## Usage

### Using ilovepdf as a library

Example of compressing a file:
```python
from ilovepdf import ILovePdf

i = ILovePdf(config.PUBLIC_KEY, config.SECRET_KEY)
i.new_task("compress")
i.add_file("input.pdf")
i.execute()
i.download("compressed_doc.pdf")
```

### Using ilovepdf as a standalone script

Example of compressing a file:

```console
$> python ipdf.py compress --verbose -o compressed_doc.pdf input.pdf
```

## Disclaimer

Implemented tasks:
* `compress`
* `merge`
* `split`
* `pdfjpg`

## Developer Keys

In order to work properly with the module, you will have to get the developer keys from https://developer.ilovepdf.com/. You will have to sign up and then go to `Console -> My project`. There you will find two keys:
- Project key (JTI Claim) aka **Public key**.
- **Secret key**.

Both keys should be written in `config.py`.

## Python versions

The lib is compatible from *Python 2.7* to *Python 3.6*.

## Tests

```console
$> pytest
```
