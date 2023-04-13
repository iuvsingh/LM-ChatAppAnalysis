#!/bin/bash

#sqlite3 database.sqlite <<EOF  #signal
#.headers on
#.mode csv
#.output signalMessagesDB.csv
#SELECT * FROM message
#EOF


sqlite3 msgstore.db <<EOF # whatsapp
.headers on
.mode csv
.output whatsAppMessagesDB.csv
SELECT * FROM message
EOF
