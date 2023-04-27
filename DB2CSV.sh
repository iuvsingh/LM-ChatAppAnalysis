#!/bin/bash

#Bash script to convert sql database files into csv format so the GUI can interpret and display

# The if statement checks to see if the database filename exists in current database
#if yes, it executes the sqlite command
#.headers on: it will include column headers
#.mode csv: the output will be in csv format
#.output ****.csv: hardcoding the output filename
#SELECT * FROM ******: this is selecting all of the columns from a particular table within the database

if [ -e database.sqlite ]; then #signal
     sqlite3 "database.sqlite" ".headers on" ".mode csv" ".output signalMessagesDB.csv" "SELECT * FROM message"
fi

if [ -e msgstore.db ]; then #whatsapp
    sqlite3 "msgstore.db" ".headers on" ".mode csv" ".output whatsAppMessagesDB.csv" "SELECT * FROM message"
fi

if [ -e cache4.db ]; then # telegram 
    sqlite3 "cache4.db" ".headers on" ".mode csv" ".output TelegramDB.csv" "SELECT * FROM messages_v2"
fi

if [ -e courgette.db ]; then # nandbox
    sqlite3 "courgette.db" ".headers on" ".mode csv" ".output NandboxDB.csv" "SELECT * FROM MESSAGE"
fi

if [ -e SkypeTeams.db ]; then # microsoft teams
    sqlite3 "SkypeTeams.db" ".headers on" ".mode csv" ".output TeamsDB.csv" "SELECT * FROM message"
fi


if [ -e kikDatabase.db ]; then # kik
    sqlite3 "kikDatabase.db" ".headers on" ".mode csv" ".output KiKDB.csv" "SELECT * FROM messagesTable"
fi

if [ -e wire.db ]; then # wire
    sqlite3 "wire.db" ".headers on" ".mode csv" ".output WireDB.csv" "SELECT * FROM Messages"
fi

if [ -e skype.db ]; then # skype
    sqlite3 "skype.db" ".headers on" ".mode csv" ".output skypeDB.csv" "SELECT * FROM messagesv12"
fi