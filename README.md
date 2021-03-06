# iLovePDF

Python module that wraps the [iLovePDF REST API](https://developer.ilovepdf.com/docs/api-reference).

## Installation

~~~console
$ git clone git@github.com:sdelquin/ilovepdf.git
$ cd ilovepdf
$ pipenv install
~~~

> Set your settings in the `.env` file.

## Usage

### Using ilovepdf as a library

Example of compressing a file:
```python
from ilovepdf import ILovePdf

i = ILovePdf(config.PUBLIC_KEY, config.SECRET_KEY)
i.new_task('compress')
i.add_file('input.pdf')
i.execute()
i.download('compressed_doc.pdf')
```

### Using ilovepdf as a standalone script

Example of compressing a file:

~~~console
$ python ipdf.py compress --verbose -o compressed_doc.pdf input.pdf
~~~

## Disclaimer

Implemented tasks:
* `merge`
* `split`
* `compress`
* `pdfjpg`
* `imagepdf`

## Developer Keys

In order to work properly with the module, you will have to get the developer keys from https://developer.ilovepdf.com/. You will have to sign up and then go to `Console -> My project`. There you will find two keys:
- Project key (JTI Claim) aka **Public key**.
- **Secret key**.

> Add these keys to `.env` file.

## Tests

```console
$> pytest
```
