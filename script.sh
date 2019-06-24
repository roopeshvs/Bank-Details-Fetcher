#!/bin/bash
TOKEN=$(curl -s -X POST -H 'Accept: application/json' -H 'Content-Type: application/json' --data '{"username":"roopesh","password":"roopesh"}' https://secure-woodland-74914.herokuapp.com/api/token/ | jq -r '.access')

curl http://secure-woodland-74914.herokuapp.com/banks/?limit=10&offset=20 && echo "1 - Bank List"
curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" http://secure-woodland-74914.herokuapp.com/branchlist/?limit=15&offset=100 && echo "2 - Branches List"
curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" http://secure-woodland-74914.herokuapp.com/branches/MUMBAI/ALLAHABAD%20BANK?limit=5&offset=10 && echo "3 - Endpoint with City name and Bank name - Example 1" 
curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" http://secure-woodland-74914.herokuapp.com/branches/COIMBATORE/ALLAHABAD%20BANK && echo "4 - Endpoint with City name and Bank name - Example 2" 
curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" http://secure-woodland-74914.herokuapp.com/ifsc/ABHY0065009 && echo "5 - Endpoint with IFSC code" 
$SHELL