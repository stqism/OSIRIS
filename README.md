OSIRIS
======

OSIRIS is a web app server written in Python. It was written with the idea that web apps should be fast, should scale, and don't actually need an Apache Cassandra driver unless the developer actually wants one.

OSIRIS is event based; powered by libev, sockets, and multiprocessing.

It supports a couple killer features, such as
* Live preview
* Multiple hostname support
* Reverse proxy resolving
* Template support
* Access to full headers and sent data
* Ability to send custom headers
* Serve data directly or serve files in a single LoC

Running OSIRIS
==========
* Install libev 
* run ``sudo pip install pyev``
* run ``sudo bash install.sh /usr``

Setting up the config file
==========================
First, make your config file

Create a file called ``osiris.conf``, data entered will be in ini format

```
[OSIRIS]
port = 8000
host = 127.0.0.1
workers = 1
debug = 1
proxy = 0
```

Only port, host, and workers are required. 1 is yes, 0 is no.

Debug makes output verbose and shows warnings, it also enables live editing. Please do not use this in production, it's rather inefficient.

Proxy makes it resolve a ``X-Real-IP`` header as the passed IP

Dealing with hostnames
======
```
[testsite.com]
mod = testsite
```

Mod is the name of the module loaded, the section name is the hostname to resolve it for. Mod files are python files located in the ``app`` folder. If the hostname requested by the client does not exist a section called fallback (You have to add this) will be used.


Writing modules
======
An example module showing off features is in ``app/testapp.py``
