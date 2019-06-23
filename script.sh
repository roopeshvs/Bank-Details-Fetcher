#!/bin/bash
TOKEN=$(curl -s -X POST -H 'Accept: application/json' -H 'Content-Type: application/json' --data '{"username":"roopesh","password":"roopesh"}' https://secure-woodland-74914.herokuapp.com/api/token/ | jq -r '.access')

curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" http://secure-woodland-74914.herokuapp.com/ifsc/ABHY0065007

$SHELL