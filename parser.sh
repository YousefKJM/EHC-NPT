#!/bin/bash

if [ "$#" != "2" ]; then
	echo "Breach-Parse v2: A Breached Domain Parsing Tool by Heath Adams"
	echo " "
	echo "Usage: breach-parse <domain to search> <file to output>"
	echo "Example: breach-parse @gmail.com gmail.txt"
	echo " "
	echo 'For multiple domains: breach-parse "<domain to search>|<domain to search>" <file to output>'
	echo 'Exmple: breach-parse "@gmail.com|@yahoo.com" multiple.txt' 
else 
	fullfile=$2
	fbname=$(basename "$fullfile" | cut -d. -f1)
	master=$fbname-master.txt
	users=$fbname-users.txt
	passwords=$fbname-passwords.txt
	
	touch $master
	total_Files=$(find /opt/breach-parse/BreachCompilation/data -type f | wc -l)
	file_Count=0

	function ProgressBar {
		
		let _progress=(${file_Count}*100/${total_Files}*100)/100
		let _done=(${_progress}*4)/10
		let _left=40-$_done
	 	
		_fill=$(printf "%${_done}s")
		_empty=$(printf "%${_left}s")
		
		printf "\rProgress : [${_fill// /\#}${_empty// //-}] ${_progress}%%"
	}
