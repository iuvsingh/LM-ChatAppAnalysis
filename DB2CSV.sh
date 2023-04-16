#!/bin/bash


if [ -e /home/kali/Desktop/Imports/Signal/database.sqlite ]; then
	sqlite3 database.sqlite <<EOF  #signal
	.headers on
	.mode csv
	.output signalMessagesDB.csv
	SELECT * FROM message
EOF
fi

if [ -e /home/kali/Desktop/Imports/com.whatsapp/databases/msgstore.db ]; then
	sqlite3 "msgstore.db" ".headers on" ".mode csv" ".output whatsAppMessagesDB.csv" "SELECT * FROM message"
fi

