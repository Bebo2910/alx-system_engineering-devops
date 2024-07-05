#!/bin/bash
# getting the size of a request from the server
curl -s "$1" | wc -c
