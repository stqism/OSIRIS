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
* run ``sudo bash install.sh``
* run ``sudo service osiris start``
 
OSIRIS is now fully installed, its config folder is at ``/etc/osiris``

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

If you use templeting please make a folder with the name of the app without .py. Such as, ``app/testapp``

Writing modules
======
An example module showing off features is in ``app/testapp.py``

Do Not Track
======
OSIRIS supports respecting the DHT header passed by browsers.
To use it, shove a ``<tracker></tracker>`` around your tracking Javascript, it won't be sent if the header is passed.

In addition, a `dnt` int is passed in the payload sent to the module.

Extra options
======
OSIRIS also supports another custom called ``<xopt></xopt>``, if it's enabled in the returned data it will be shown, otherwise it's stripped out on load. The best possible use of this is only showing a cookie banner for IPs from Europe, and can be done pretty easily. This can be seen in action at https://osiris.tox.im
