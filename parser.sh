#!/bin/bash

if [ "$#" != "2" ]; then
	echo "Breach-Parse v2: A Breached Domain Parsing Tool by Heath Adams"
	echo " "
	echo "Usage: breach-parse <domain to search> <file to output>"
	echo "Example: breach-parse @gmail.com gmail.txt"
	echo " "
	echo 'For multiple domains: breach-parse "<domain to search>|<domain to search>" <file to output>'
	echo 'Exmple: breach-parse "@gmail.com|@yahoo.com" multiple.txt' 
