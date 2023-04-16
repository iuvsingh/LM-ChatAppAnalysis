#!/bin/bash


if [ -e /home/usingh2/Desktop/imports/Signal/database.sqlite ]; then
    sqlite3 database.sqlite <<EOF  #signal
    .headers on
    .mode csv
    .output signalMessagesDB.csv
    SELECT * FROM message
EOF
fi

if [ -e msgstore.db ]; then #whatsapp
    sqlite3 "msgstore.db" ".headers on" ".mode csv" ".output whatsAppMessagesDB.csv" "SELECT * FROM message"
fi

if [ -f cache4.db ]; then # telegram 
    sqlite3 "cache4.db" ".headers on" ".mode csv" ".output TelegramDB.csv" "SELECT * FROM messages_v2"
fi

if [ -f courgette.db ]; then # nandbox
    sqlite3 "courgette.db" ".headers on" ".mode csv" ".output NandboxDB.csv" "SELECT * FROM MESSAGE"
fi

if [ -e SkypeTeams.db ]; then # teams
    sqlite3 "SkypeTeams.db" ".headers on" ".mode csv" ".output TeamsDB.csv" "SELECT * FROM message"
fi


if [ -f kikDatabase.db ]; then # kik
    sqlite3 "kikDatabase.db" ".headers on" ".mode csv" ".output KiKDB.csv" "SELECT * FROM messagesTable"
fi

if [ -f wire.db ]; then # wire
    sqlite3 "wire.db" ".headers on" ".mode csv" ".output WireDB.csv" "SELECT * FROM Messages"
fi

if [ -f skype.db ]; then # wire
    sqlite3 "skype.db" ".headers on" ".mode csv" ".output skypeDB.csv" "SELECT * FROM messagesv12"
fi
