#!/bin/bash

# use this when flask is already running

url=$1

printf "\n ~~ creating flask db ~~ \n"
flask init-db
printf "\n ~~ curling login POST (should be error, no users yet) ~~ \n"
curl -X POST -d "username=JonSmith&password=pw123" "${url}/login"
printf "\n ~~ curling register POST (should be successful) ~~ \n"
curl -X POST -d "username=JonSmith&password=pw123" "${url}/register"
printf "\n ~~ curling login POST (should now be successful) ~~ \n"
curl -X POST -d "username=JonSmith&password=pw123" "${url}/login"
