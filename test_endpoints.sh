#!/bin/bash

if [[ $1 -eq "" ]]
then
    URL="https://autumnchiu.duckdns.org/"
else
    URL=$1
fi

ROUTES=("" "blog/" "health/" "mlh/" "mlh/Experience/" "mlh/Projects/" "mlh/Accomplishments/" "mlh/register/" "mlh/login/")
EXIT=0

CURL_CMD='curl -s -o /dev/null -w "%{http_code}"'

HEAD="-I"

POST='-X POST -d "username=JonSmith&password=pw123"'

check_route () {
    if [[ $RESPONSE -eq 200 || $RESPONSE -eq 418 ]]
    then
	echo "response $RESPONSE ok"
    else
	echo "response $RESPONSE not good"
	EXIT=1
    fi
}

for ROUTE in ${ROUTES[@]}; do
    REQUEST=$URL$ROUTE
    echo "curling $REQUEST"
    RESPONSE=$(eval $CURL_CMD $HEAD $REQUEST)
    check_route
done

echo "curling register POST"
RESPONSE=$(eval $CURL_CMD $POST "${URL}mlh/register")
check_route

echo "curling login POST"
RESPONSE=$(eval $CURL_CMD $POST "${URL}mlh/login")
check_route

exit $EXIT
