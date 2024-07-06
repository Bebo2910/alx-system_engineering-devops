#!/bin/bash
#getting the status code only
curl -s -o /dev/null -w "%{http_code}\n" "$1"
