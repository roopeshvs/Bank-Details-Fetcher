#!/bin/bash
TOKEN=$(curl -s -X POST -H 'Accept: application/json' -H 'Content-Type: application/json' --data '{"username":"roopesh","password":"roopesh"}' https://secure-woodland-74914.herokuapp.com/api/token/ | ./jq-win64.exe -r '.access')

curl http://secure-woodland-74914.herokuapp.com/banks/ && echo "1 - Bank List" &&
curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" http://secure-woodland-74914.herokuapp.com/branchlist/ && echo "2 - Branches List"
curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" http://secure-woodland-74914.herokuapp.com/branches/MUMBAI/ALLAHABAD%20BANK && echo "3 - Endpoint with City name and Bank name - Example 1" &&
curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" http://secure-woodland-74914.herokuapp.com/branches/COIMBATORE/ALLAHABAD%20BANK && echo "4 - Endpoint with City name and Bank name - Example 2" &&
curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" http://secure-woodland-74914.herokuapp.com/ifsc/ABHY0065009 && echo "5 - Endpoint with IFSC code - Example 1" &&
curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" http://secure-woodland-74914.herokuapp.com/ifsc/ABHY0065011 && echo "6 - Endpoint with IFSC code - Example 2"
$SHELL