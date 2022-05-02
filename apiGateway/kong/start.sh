#!/sbin/tini /bin/sh
echo "Starting helper to get services url"
/helper.py $FUNCTION_NAMESPACE /kong.yml
echo "Starting Kong API Gateway DB-less"
/usr/local/bin/kong start -v -c /kong.conf
