#!/bin/bash


if [ -e /home/kali/Desktop/Imports/Signal/database.sqlite ]; then
	sqlite3 database.sqlite <<EOF  #signal
	.headers on
	.mode csv
	.output signalMessagesDB.csv
	SELECT * FROM message
EOF
fi

if [ -f msgstore.db ]; then #whatsapp
	sqlite3 "msgstore.db" ".headers on" ".mode csv" ".output whatsAppMessagesDB.csv" "SELECT * FROM message"
fi

if [ -f wa.db ]; then #whatsapp
	sqlite3 "wa.db" ".headers on" ".mode csv" ".output whatsAppContactsDB.csv" "SELECT * FROM wa_contacts"
fi

if [ -e /home/kali/Desktop/Imports/org.telegram.messenger/files/cache4.db ]; then # telegram 
	sqlite3 "cache4.db" ".headers on" ".mode csv" ".output TelegramDB.csv" "SELECT * FROM message_v2"
fi

if [ -e home/kali/Desktop/Imports/databases/com.nandbox.nandbox/courgette.db ]; then # nandbox
	sqlite3 "courgette.db" ".headers on" ".mode csv" ".output NandboxDB.csv" "SELECT * FROM message"
fi

if [ -e /home/kali/Desktop/Imports/com.microsoft.teams/databases/SkypeTeams.db ]; then # teams
	sqlite3 "SkypeTeams.db" ".headers on" ".mode csv" ".output TeamsDB.csv" "SELECT * FROM message"
fi


if [ -e /home/kali/Desktop/Imports/kik.android/databases/51c54d5d-cfda-4355-8ac2-9470dcecd5b2.kikDatabase.db ]; then # kik
	sqlite3 "kikDatabase.db" ".headers on" ".mode csv" ".output KiKDB.csv" "SELECT * FROM MessageTable"
fi

if [ -e //home/kali/Desktop/Imports/com.wire/databases/af7b1f93-b00c-433f-93da-ac19cbebd308.db ]; then # wire
	sqlite3 "wire.db" ".headers on" ".mode csv" ".output WireDB.csv" "SELECT * FROM messages"
fi


