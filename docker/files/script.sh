#!/bin/bash

sed -i 's|%OWNER%|'"$OWNER"'|g' /var/www/html/index.html

echo "Start Script --- OK"

nginx -g 'daemon off;'