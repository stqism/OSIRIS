cp osirisd $1/bin/
cp osiris.sh /etc/init.d/osiris
cp osiris.conf $1/etc/osiris/
cp -r testapp* $1/etc/osiris/app/
mkdir -pf $1/etc/osiris/app
chmod +x $1/bin/osirisd
chmod +x /etc/init.d/osiris

echo Please add the user osiris before running, settings for launching the daemon are in /etc/init.d/osiris
echo You may need to change CONFIG=/usr/etc/osiris to $1/etc/osiris
