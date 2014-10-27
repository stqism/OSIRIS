mkdir -p /etc/osiris/app
python -OO -m py_compile "osirisd.py"
mv osirisd.pyo /bin/osirisd
cp osiris.sh /etc/init.d/osiris
yes n | cp -i osiris.conf /etc/osiris/
yes n | cp -ir app/testapp* /etc/osiris/app/
chmod +x /usr/bin/osirisd
chmod +x /etc/init.d/osiris

echo Please add the user osiris before running, settings for launching the daemon are in /etc/init.d/osiris
echo You may need to change CONFIG=/usr/etc/osiris to $1/etc/osiris