#!/bin/bash
# getting the methods allowed
curl -sI "$1" | grep "Allow" | cut -d ' ' -f
