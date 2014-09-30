cp osirisd $/bin/
cp osiris.sh /etc/init.d/osiris
cp osiris.conf $1/etc/osiris/
cp -r testapp* $1/etc/osiris/app/
mkdir -pf $1/etc/osiris/app
chmod +x $/bin/osirisd
chmod +x /etc/init.d/osiris

Please add the user osiris before running, settings for launching the daemon are in /etc/init.d/osiris
You may need to change CONFIG=/usr/etc/osiris to $1/etc/osiris