#!/bin/bash

curl -s "https://scamalytics.com/ip/$1" | grep '"ip":"'
curl -s "https://scamalytics.com/ip/$1" | grep '"score":"'
curl -s "https://scamalytics.com/ip/$1" | grep '"risk":"' 

