# urllib for python3
```python
# GET一个URL
import urllib.request
with urllib.request.urlopen('http://www.python.org/') as f:
    print(f.read(300))
 
#PUT一个请求
import urllib.request
DATA=b'some data'
req = urllib.request.Request(url='http://localhost:8080', data=DATA,method='PUT')
with urllib.request.urlopen(req) as f:
    pass
print(f.status)
print(f.reason)
 
#基本的HTTP认证
import urllib.request
auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm='PDQ Application',
                          uri='https://mahler:8092/site-updates.py',
                          user='klem',
                          passwd='kadidd!ehopper')
opener = urllib.request.build_opener(auth_handler)
urllib.request.install_opener(opener)
urllib.request.urlopen('http://www.example.com/login.html')
 
#使用proxy
proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
 
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
opener.open('http://www.example.com/login.html')
 
# 添加头部
import urllib.request
req = urllib.request.Request('http://www.example.com/')
req.add_header('Referer', 'http://www.python.org/')
r = urllib.request.urlopen(req)
 
# 更改User-agent
import urllib.request
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
opener.open('http://www.example.com/')
 
# 使用GET时设置URL的参数
import urllib.request
import urllib.parse
params = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
url = "http://www.musi-cal.com/cgi-bin/query?%s" % params
with urllib.request.urlopen(url) as f:
    print(f.read().decode('utf-8'))
 
# 使用POST时设置参数
import urllib.request
import urllib.parse
data = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
data = data.encode('ascii')
with urllib.request.urlopen("http://requestb.in/xrbl82xr", data) as f:
    print(f.read().decode('utf-8'))
 
# 指定proxy
import urllib.request
proxies = {'http': 'http://proxy.example.com:8080/'}
opener = urllib.request.FancyURLopener(proxies)
with opener.open("http://www.python.org") as f:
    f.read().decode('utf-8')

# 不使用proxy, 覆盖环境变量的proxy
import urllib.request
opener = urllib.request.FancyURLopener({})
with opener.open("http://www.python.org/") as f:
    f.read().decode('utf-8')
# 原文链接：https://blog.csdn.net/permike/article/details/52437492
```

# urllib3
* https://urllib3.readthedocs.io/en/latest/

## Making requests

First things first, import the urllib3 module:

```
>>> import urllib3
```

You’ll need a [`PoolManager`](https://urllib3.readthedocs.io/en/latest/reference/index.html#urllib3.poolmanager.PoolManager) instance to make requests. This object handles all of the details of connection pooling and thread safety so that you don’t have to:

```
>>> http = urllib3.PoolManager()
```

To make a request use `request()`:

```
>>> r = http.request('GET', 'http://httpbin.org/robots.txt')
>>> r.data
b'User-agent: *\nDisallow: /deny\n'
```

`request()` returns a [`HTTPResponse`](https://urllib3.readthedocs.io/en/latest/reference/index.html#urllib3.response.HTTPResponse) object, the [Response content](https://urllib3.readthedocs.io/en/latest/user-guide.html#response-content) section explains how to handle various responses.

You can use `request()` to make requests using any HTTP verb:

```
>>> r = http.request(
...     'POST',
...     'http://httpbin.org/post',
...     fields={'hello': 'world'})
```

The [Request data](https://urllib3.readthedocs.io/en/latest/user-guide.html#request-data) section covers sending other kinds of requests data, including JSON, files, and binary data.



## Response content

The [`HTTPResponse`](https://urllib3.readthedocs.io/en/latest/reference/index.html#urllib3.response.HTTPResponse) object provides `status`, [`data`](https://urllib3.readthedocs.io/en/latest/reference/index.html#urllib3.response.HTTPResponse.data), and `header` attributes:

```
>>> r = http.request('GET', 'http://httpbin.org/ip')
>>> r.status
200
>>> r.data
b'{\n  "origin": "104.232.115.37"\n}\n'
>>> r.headers
HTTPHeaderDict({'Content-Length': '33', ...})
```

### JSON content

JSON content can be loaded by decoding and deserializing the [`data`](https://urllib3.readthedocs.io/en/latest/reference/index.html#urllib3.response.HTTPResponse.data) attribute of the request:

```
>>> import json
>>> r = http.request('GET', 'http://httpbin.org/ip')
>>> json.loads(r.data.decode('utf-8'))
{'origin': '127.0.0.1'}
```

### Binary content

The [`data`](https://urllib3.readthedocs.io/en/latest/reference/index.html#urllib3.response.HTTPResponse.data) attribute of the response is always set to a byte string representing the response content:

```
>>> r = http.request('GET', 'http://httpbin.org/bytes/8')
>>> r.data
b'\xaa\xa5H?\x95\xe9\x9b\x11'
```

Note

For larger responses, it’s sometimes better to [stream](https://urllib3.readthedocs.io/en/latest/advanced-usage.html#stream) the response.

### Using io Wrappers with Response content

Sometimes you want to use [`io.TextIOWrapper`](https://docs.python.org/3.7/library/io.html#io.TextIOWrapper) or similar objects like a CSV reader directly with [`HTTPResponse`](https://urllib3.readthedocs.io/en/latest/reference/index.html#urllib3.response.HTTPResponse) data. Making these two interfaces play nice together requires using the `auto_close` attribute by setting it to `False`. By default HTTP responses are closed after reading all bytes, this disables that behavior:

```
>>> import io
>>> r = http.request('GET', 'https://example.com', preload_content=False)
>>> r.auto_close = False
>>> for line in io.TextIOWrapper(r):
>>>     print(line)
```



## Request data

### Headers

You can specify headers as a dictionary in the `headers` argument in `request()`:

```
>>> r = http.request(
...     'GET',
...     'http://httpbin.org/headers',
...     headers={
...         'X-Something': 'value'
...     })
>>> json.loads(r.data.decode('utf-8'))['headers']
{'X-Something': 'value', ...}
```

### Query parameters

For `GET`, `HEAD`, and `DELETE` requests, you can simply pass the arguments as a dictionary in the `fields` argument to `request()`:

```
>>> r = http.request(
...     'GET',
...     'http://httpbin.org/get',
...     fields={'arg': 'value'})
>>> json.loads(r.data.decode('utf-8'))['args']
{'arg': 'value'}
```

For `POST` and `PUT` requests, you need to manually encode query parameters in the URL:

```
>>> from urllib.parse import urlencode
>>> encoded_args = urlencode({'arg': 'value'})
>>> url = 'http://httpbin.org/post?' + encoded_args
>>> r = http.request('POST', url)
>>> json.loads(r.data.decode('utf-8'))['args']
{'arg': 'value'}
```



### Form data

For `PUT` and `POST` requests, urllib3 will automatically form-encode the dictionary in the `fields` argument provided to `request()`:

```
>>> r = http.request(
...     'POST',
...     'http://httpbin.org/post',
...     fields={'field': 'value'})
>>> json.loads(r.data.decode('utf-8'))['form']
{'field': 'value'}
```

### JSON

You can send a JSON request by specifying the encoded data as the `body` argument and setting the `Content-Type` header when calling `request()`:

```
>>> import json
>>> data = {'attribute': 'value'}
>>> encoded_data = json.dumps(data).encode('utf-8')
>>> r = http.request(
...     'POST',
...     'http://httpbin.org/post',
...     body=encoded_data,
...     headers={'Content-Type': 'application/json'})
>>> json.loads(r.data.decode('utf-8'))['json']
{'attribute': 'value'}
```

### Files & binary data

For uploading files using `multipart/form-data` encoding you can use the same approach as [Form data](https://urllib3.readthedocs.io/en/latest/user-guide.html#form-data) and specify the file field as a tuple of `(file_name, file_data)`:

```
>>> with open('example.txt') as fp:
...     file_data = fp.read()
>>> r = http.request(
...     'POST',
...     'http://httpbin.org/post',
...     fields={
...         'filefield': ('example.txt', file_data),
...     })
>>> json.loads(r.data.decode('utf-8'))['files']
{'filefield': '...'}
```

While specifying the filename is not strictly required, it’s recommended in order to match browser behavior. You can also pass a third item in the tuple to specify the file’s MIME type explicitly:

```
>>> r = http.request(
...     'POST',
...     'http://httpbin.org/post',
...     fields={
...         'filefield': ('example.txt', file_data, 'text/plain'),
...     })
```

For sending raw binary data simply specify the `body` argument. It’s also recommended to set the `Content-Type` header:

```
>>> with open('example.jpg', 'rb') as fp:
...     binary_data = fp.read()
>>> r = http.request(
...     'POST',
...     'http://httpbin.org/post',
...     body=binary_data,
...     headers={'Content-Type': 'image/jpeg'})
>>> json.loads(r.data.decode('utf-8'))['data']
b'...'
```



## Certificate verification

> Note
>
> *New in version 1.25*
>
> HTTPS connections are now verified by default (`cert_reqs = 'CERT_REQUIRED'`).

While you can disable certification verification, it is highly recommend to leave it on.

Unless otherwise specified urllib3 will try to load the default system certificate stores. The most reliable cross-platform method is to use the [certifi](https://certifi.io/) package which provides Mozilla’s root certificate bundle:

```
pip install certifi
```

You can also install certifi along with urllib3 by using the `secure` extra:

```
pip install urllib3[secure]
```

Warning

If you’re using Python 2 you may need additional packages. See the [section below](https://urllib3.readthedocs.io/en/latest/user-guide.html#ssl-py2) for more details.

Once you have certificates, you can create a [`PoolManager`](https://urllib3.readthedocs.io/en/latest/reference/index.html#urllib3.poolmanager.PoolManager) that verifies certificates when making requests:

```
>>> import certifi
>>> import urllib3
>>> http = urllib3.PoolManager(
...     cert_reqs='CERT_REQUIRED',
...     ca_certs=certifi.where())
```

The [`PoolManager`](https://urllib3.readthedocs.io/en/latest/reference/index.html#urllib3.poolmanager.PoolManager) will automatically handle certificate verification and will raise [`SSLError`](https://urllib3.readthedocs.io/en/latest/reference/index.html#urllib3.exceptions.SSLError) if verification fails:

```
>>> http.request('GET', 'https://google.com')
(No exception)
>>> http.request('GET', 'https://expired.badssl.com')
urllib3.exceptions.SSLError ...
```

Note

You can use OS-provided certificates if desired. Just specify the full path to the certificate bundle as the `ca_certs` argument instead of `certifi.where()`. For example, most Linux systems store the certificates at `/etc/ssl/certs/ca-certificates.crt`. Other operating systems can be [difficult](https://stackoverflow.com/questions/10095676/openssl-reasonable-default-for-trusted-ca-certificates).



### Certificate verification in Python 2

Older versions of Python 2 are built with an [`ssl`](https://docs.python.org/3.7/library/ssl.html#module-ssl) module that lacks [SNI support](https://urllib3.readthedocs.io/en/latest/advanced-usage.html#sni-warning) and can lag behind security updates. For these reasons it’s recommended to use [pyOpenSSL](https://pyopenssl.readthedocs.io/en/latest/).

If you install urllib3 with the `secure` extra, all required packages for certificate verification on Python 2 will be installed:

```
pip install urllib3[secure]
```

If you want to install the packages manually, you will need `pyOpenSSL`, `cryptography`, `idna`, and `certifi`.

Note

If you are not using macOS or Windows, note that [cryptography](https://cryptography.io/en/latest/) requires additional system packages to compile. See [building cryptography on Linux](https://cryptography.io/en/latest/installation/#building-cryptography-on-linux) for the list of packages required.

Once installed, you can tell urllib3 to use pyOpenSSL by using `urllib3.contrib.pyopenssl`:

```
>>> import urllib3.contrib.pyopenssl
>>> urllib3.contrib.pyopenssl.inject_into_urllib3()
```

Finally, you can create a [`PoolManager`](https://urllib3.readthedocs.io/en/latest/reference/index.html#urllib3.poolmanager.PoolManager) that verifies certificates when performing requests:

```
>>> import certifi
>>> import urllib3
>>> http = urllib3.PoolManager(
...     cert_reqs='CERT_REQUIRED',
...     ca_certs=certifi.where())
```

If you do not wish to use pyOpenSSL, you can simply omit the call to `urllib3.contrib.pyopenssl.inject_into_urllib3()`. urllib3 will fall back to the standard-library [`ssl`](https://docs.python.org/3.7/library/ssl.html#module-ssl) module. You may experience [several warnings](https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings) when doing this.

Warning

If you do not use pyOpenSSL, Python must be compiled with ssl support for certificate verification to work. It is uncommon, but it is possible to compile Python without SSL support. See this [Stackoverflow thread](https://stackoverflow.com/questions/5128845/importerror-no-module-named-ssl) for more details.

If you are on Google App Engine, you must explicitly enable SSL support in your `app.yaml`:

```
libraries:
- name: ssl
  version: latest
```

## Using timeouts

Timeouts allow you to control how long (in seconds) requests are allowed to run before being aborted. In simple cases, you can specify a timeout as a `float` to `request()`:

```
>>> http.request(
...     'GET', 'http://httpbin.org/delay/3', timeout=4.0)
<urllib3.response.HTTPResponse>
>>> http.request(
...     'GET', 'http://httpbin.org/delay/3', timeout=2.5)
MaxRetryError caused by ReadTimeoutError
```

For more granular control you can use a [`Timeout`](https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html#urllib3.util.timeout.Timeout) instance which lets you specify separate connect and read timeouts:

```
>>> http.request(
...     'GET',
...     'http://httpbin.org/delay/3',
...     timeout=urllib3.Timeout(connect=1.0))
<urllib3.response.HTTPResponse>
>>> http.request(
...     'GET',
...     'http://httpbin.org/delay/3',
...     timeout=urllib3.Timeout(connect=1.0, read=2.0))
MaxRetryError caused by ReadTimeoutError
```

If you want all requests to be subject to the same timeout, you can specify the timeout at the [`PoolManager`](https://urllib3.readthedocs.io/en/latest/reference/index.html#urllib3.poolmanager.PoolManager) level:

```
>>> http = urllib3.PoolManager(timeout=3.0)
>>> http = urllib3.PoolManager(
...     timeout=urllib3.Timeout(connect=1.0, read=2.0))
```

You still override this pool-level timeout by specifying `timeout` to `request()`.

## Retrying requests

urllib3 can automatically retry idempotent requests. This same mechanism also handles redirects. You can control the retries using the `retries` parameter to `request()`. By default, urllib3 will retry requests 3 times and follow up to 3 redirects.

To change the number of retries just specify an integer:

```
>>> http.requests('GET', 'http://httpbin.org/ip', retries=10)
```

To disable all retry and redirect logic specify `retries=False`:

```
>>> http.request(
...     'GET', 'http://nxdomain.example.com', retries=False)
NewConnectionError
>>> r = http.request(
...     'GET', 'http://httpbin.org/redirect/1', retries=False)
>>> r.status
302
```

To disable redirects but keep the retrying logic, specify `redirect=False`:

```
>>> r = http.request(
...     'GET', 'http://httpbin.org/redirect/1', redirect=False)
>>> r.status
302
```

For more granular control you can use a [`Retry`](https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html#urllib3.util.retry.Retry) instance. This class allows you far greater control of how requests are retried.

For example, to do a total of 3 retries, but limit to only 2 redirects:

```
>>> http.request(
...     'GET',
...     'http://httpbin.org/redirect/3',
...     retries=urllib3.Retry(3, redirect=2))
MaxRetryError
```

You can also disable exceptions for too many redirects and just return the `302` response:

```
>>> r = http.request(
...     'GET',
...     'http://httpbin.org/redirect/3',
...     retries=urllib3.Retry(
...         redirect=2, raise_on_redirect=False))
>>> r.status
302
```

If you want all requests to be subject to the same retry policy, you can specify the retry at the [`PoolManager`](https://urllib3.readthedocs.io/en/latest/reference/index.html#urllib3.poolmanager.PoolManager) level:

```
>>> http = urllib3.PoolManager(retries=False)
>>> http = urllib3.PoolManager(
...     retries=urllib3.Retry(5, redirect=2))
```

You still override this pool-level retry policy by specifying `retries` to `request()`.

## Errors & Exceptions

urllib3 wraps lower-level exceptions, for example:

```
>>> try:
...     http.request('GET', 'nx.example.com', retries=False)
>>> except urllib3.exceptions.NewConnectionError:
...     print('Connection failed.')
```

See [`exceptions`](https://urllib3.readthedocs.io/en/latest/reference/index.html#module-urllib3.exceptions) for the full list of all exceptions.

## Logging

If you are using the standard library [`logging`](https://docs.python.org/3.7/library/logging.html#module-logging) module urllib3 will emit several logs. In some cases this can be undesirable. You can use the standard logger interface to change the log level for urllib3’s logger:

```
>>> logging.getLogger("urllib3").setLevel(logging.WARNING)
```

# 抓取所有链接
```python
# 利用 requests_html
from requests_html import HTMLSession
session = HTMLSession()
url = 'https://www.baidu.com'
r = session.get(url)
print(r.html.links)
print('*'*100)

# 利用 BeautifulSoup
import requests
from bs4 import BeautifulSoup
url = 'http://www.baidu.com'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
for a in soup.find_all('a'):
    print(a['href'])
print('*'*100)

# 利用 re (不推荐用正则,太麻烦)

# 利用 lxml.etree
from lxml import etree
tree = etree.HTML(r.text)
for link in tree.xpath('//@href'):
    print(link)
print('*'*100)

# 利用 selenium
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get(url)
for link in browser.find_elements_by_tag_name('a'):
    print(link.get_attribute('href'))
# 原文链接：https://blog.csdn.net/Waspvae/article/details/80738559
```