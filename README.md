# Successfully integrate CinetPay’s CHECKOUT API

## Documentation

The documentation for the Cinetpay API can be found [here][apidocs].

The Python library documentation can be found [here][libdocs].


### Supported Python Versions

This library supports the following Python implementations:

* Python 2.7
* Python 3.4
* Python 3.5
* Python 3.6
* Python 3.7
* Python 3.8
* Python 3.9

## Installation

Install from PyPi using [pip](https://pip.pypa.io/en/latest/), a
package manager for Python.

    pip install -i https://test.pypi.org/simple/ cinetpay-sdk==0.1.1

If pip install fails on Windows, check the path length of the directory. If it is greater 260 characters then enable [Long Paths](https://docs.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation) or choose other shorter location.

Don't have pip installed? Try installing it, by running this from the command
line:

    $ curl https://bootstrap.pypa.io/get-pip.py | python

Or, you can [download the source code
(ZIP)](https://github.com/amaniCinetpay/SDK_api_paiement_cinetpay.git "Cinetpay_SDK-python
source code") for `Cinetpay_SDK-python`, and then run:

    python setup.py install

You may need to run the above commands with `sudo`.


## Getting Started

Getting started with the Cinetpay API couldn't be easier. Create a
`Client` and you're ready to go.

### API Credentials

The `CHECKOUT API` needs your Cinetpay credentials. You can either pass these
directly to the constructor (see the code below) or via environment variables.

```python
from cinetpay_sdk.s_d_k import Cinetpay

apikey = "XXXXXXXXXXXXXXXXXX"
site_id = "XXXXXX"

client = Cinetpay(apikey,site_id)
```

Alternatively, a `Client` constructor without these parameters will
look for `APIKEY` and `ClIENT_AUTH_TOKEN` variables inside the
current environment.

We suggest storing your credentials as environment variables. Why? You'll never
have to worry about committing your credentials and accidentally posting them
somewhere public.

### initialize a Payment

```python
from cinetpay_sdk.s_d_k import Cinetpay

apikey = "XXXXXXXXXXXXXXXXXX"
site_id = "XXXXXX"

client = Cinetpay(apikey,site_id)

data = { 
    'amount' : 00000,
    'currency' : "XOF",            
    'transaction_id' : "XXXXXXXXXXXXXXXX",  
    'description' : "TRANSACTION DESCRIPTION",  
    'return_url' : "https://www.exemple.com/return",
    'notify_url' : "https://www.exemple.com/notify", 
    'customer_name' : "XXXXXXXXXXXX",                              
    'customer_surname' : "XXXXXXXXXXXXX",       
}  
print(client.PaymentInitialization(data) )
```

### Check Transaction with transaction id

```python
from cinetpay_sdk.s_d_k import Cinetpay

apikey = "XXXXXXXXXXXXXXXXXX"
site_id = "XXXXXX"

client = Cinetpay(apikey,site_id)
transaction_id = "XXXXXX"

print(client.TransactionVerfication_trx(transaction_id))
```

### Check Transaction with  token

```python
from cinetpay_sdk.s_d_k import Cinetpay

apikey = "XXXXXXXXXXXXXXXXXX"
site_id = "XXXXXX"

client = Cinetpay(apikey,site_id)
token ="XXXXXX"

print(client.TransactionVerfication_token(token))
```

If you've instead found a bug in the library or would like new features added, go ahead and open issues or pull requests against this repo!

[apidocs]: https://cinetpay.com/developer/api/paiement
[libdocs]: https://docs.python.org/3/
