#!/bin/bash


if [ -e /home/usingh2/Desktop/imports/Signal/database.sqlite ]; then
    sqlite3 database.sqlite <<EOF  #signal
    .headers on
    .mode csv
    .output signalMessagesDB.csv
    SELECT * FROM message
EOF
fi

if [ -e /home/usingh2/Desktop/imports/com.whatsapp/databases/msgstore.db ]; then
    sqlite3 "msgstore.db" ".headers on" ".mode csv" ".output whatsAppMessagesDB.csv" "SELECT * FROM message"
fi

if [ -e /home/usingh2/Desktop/imports/com.whatsapp/databases/msgstore.db ]; then
    sqlite3 "msgstore.db" ".headers on" ".mode csv" ".output whatsAppMessagesDB.csv" "SELECT * FROM message"
fi