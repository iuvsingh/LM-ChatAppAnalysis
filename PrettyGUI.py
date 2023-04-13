import os
import os.path
import subprocess		#UV: import
import time
import sys
import tkinter as tk
import tkinter.scrolledtext as st
import tkinter.messagebox
import tkinter.filedialog
from tkinter import ttk
from tkinter import StringVar, filedialog
from typing import Text
from ScrollableNotebook import *
import threading
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from PIL import Image, ImageTk
from pandastable import Table, TableModel
import sqlite3
import pandas as pd
import csv
import shutil



#defines the window
root = tk.Tk()
root.title('Access D3niers')
#set background color
root['background']='#003478'
root.geometry('1280x720')

######################################################
src = '/home/kali/Desktop/Imports/com.whatsapp/databases/msgstore.db'
dst = './msgstore.db'  # Destination directory is the current directory

# Change current directory to destination directory
#os.chdir('/path/to/destination/directory')

# Copy the file
shutil.copy(src, dst)

#############################################
#defines the notebook widget
tabControl = ScrollableNotebook(root, wheelscroll=True, tabmenu=True)


#screen layout
def tabLayout():
    #destroy the start button
    btn0.destroy()
    #makes uploadedFiles a list
    orderedUploads = list(uploadedFiles)
    #sort by alphabetical order
    orderedUploads.sort(key = lambda x: x.lower())

    #for each file in ordered uploads
    for name in orderedUploads:
        print(name)
        #if txt file
        if name.lower().endswith(('.txt', '.png', '.jpg', 'jpeg', '.db', '.csv')):#'.db',
            if name not in previousUploads:
                #add name to used list
                previousUploads.add(name)
                tab = ttk.Frame(tabControl)

                #text files
                if name.lower().endswith('.txt'):
                    #put a scrolled text box onto the tab and have it fill the area
                    content = st.ScrolledText(tab, wrap = tk.WORD)
                    content.pack(expand = True, fill = "both")
                    #open the file and read it
                    with open(name, 'r') as f:
                        #reads the data
                        data = f.read()
                        #inserts data into the content window
                        content.insert(tk.END, data)
                    tab_name = name

                elif name.lower().endswith('.db') or name.lower().endswith('.sqlite'):
                    os.system("./DB2CSV.sh")
                    continue
                #     tab_name = name
                #     read_from_db(name,tab, tab_name)
                    #tab_name = name
                elif name.lower().endswith('.csv'):
                    tab_name = name
                    csvDisplay(name, tab)
                else:
                    # open the picture to resize
                    img = Image.open(name)
                    # resize the image
                    imgrs = img.resize((img.width, img.height), Image.ANTIALIAS)
                    # set the picture
                    pic = ImageTk.PhotoImage(imgrs)
                    # set the label to display the picture
                    content = tkinter.Label(tab, image=pic)
                    # keep a reference to the tkinter object so that the picture shows: "Why do my Tkinter images not appear?"
                    content.image = pic
                    # place the image
                    content.pack(expand=True, fill="both")
                    tab_name = name

                # give tab the current file name
                tabControl.add(tab, text=tab_name)
                # organize the tabs
                tabControl.pack(expand=True, fill="both")


# set for uploadedFiles
uploadedFiles = set()
# set for previous uploads to compare to
previousUploads = set()

# def db_to_csv(filename,ext = "db", tableName = "list_item"):
#     """ inputFolder - Folder where sqlite files are located. 
#         ext - Extension of your sqlite file (eg. db, sqlite, sqlite3 etc.)
#         tableName - table name from which you want to select the data.
#     """
#     csvWriter = csv.writer(open('keep.csv', 'w', newline=''))
#     # for file1 in os.listdir(inputFolder):
#     #if file1.endswith('.'+ext):
#     conn = sqlite3.connect(filename)
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM "+tableName)
#     #df = pd.read_sql_query("SELECT *  FROM {}".format(tableName), conn)

#     df.to_csv(r'{}.csv'.format(name[:-3]), index = False)
#         #set filepath name
#     filepath = name[:-3] + ".csv"
#     return filepath

#         #cursor = conn.cursor()
#         #cursor.execute("SELECT * FROM "+tableName)
#         #rows = cursor.fetchall()
#         #for row in rows:
#             #csvWriter.writerow(row)
    

# def read_from_db(filename, tab, tabname, table_name = "list_item"):
#     table = Table(tab, showstatusbar=True, showtoolbar=True)

    # conn = sqlite3.connect(filename)
    # cursor=conn.cursor()
    # data = cursor.fetchall()
    # print(data)
    # cursor.execute("SELECT * FROM {}".format(table_name))
    # data = cursor.fetchall()
    # showData = ''
    # for data in table_name:
    #     showData += str(data) + "\n"

    # dataLabel = Label(tab, text=showData)
    # dataLabel.grid(row=0, column=0)
    # conn.commit()
    # conn.close()

#display the csv
def csvDisplay(filepath, tab):
    # os.system("./csv.sh")
    #sets the table
    table = Table(tab, showstatusbar=True, showtoolbar=True)

    #open the csv file
    table.importCSV(filepath)
    
    #show the csv file on the table
    table.show()


# scans the current directory for
def fileUpdate():
    # set path as current directory
    path = os.getcwd()
    # os.chdir('./ScriptFiles')

    # iterate through each file in the directory
    for entry in os.scandir(path):
        if entry.path.lower().endswith(('.txt', '.png', '.jpg', 'jpeg', '.db','.csv')) or entry.name == "signalBackup":#'.db', 
            # sleep timer for databases to load and convert
            time.sleep(.1)
            # adds the file to the set
            uploadedFiles.add(entry.name)

# what fileWatch calls to update the tabs


class Event(LoggingEventHandler):
    def dispatch(self, event):
        fileUpdate()
        tabLayout()


# automatically update the tabs
def fileWatch():
    # set the format for logging info
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    # set format for displaying path
    path = os.getcwd()
   # with open('watchdogOuput.txt', 'w') as f:
    #    sys.stdout = f# initialize logging event
    event_handler = Event()
    # initialize logging event handler to print actions
    event_log = LoggingEventHandler()


    # initialize Observer
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.schedule(event_log, path, recursive=True)

    # start the observer
    observer.start()
    try:
        while True:
            # set the thread sleep time
            time.sleep(.1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    #sys.stdout = sys.__stdout__
def file_pull():
	subprocess.run("gnome-terminal -x sh -c \"python3 pull_database.py; bash\"",shell=True)

B=tkinter.Button(root,text="Pull Database",command= file_pull)
B.place(x=25, y=3000)
B.pack()

# initial start button
btn0 = tk.Button(text='Start', width=10, fg='black', highlightbackground='#003478',command=lambda: [fileUpdate(), tabLayout()])
btn0.place(relx=0.5, rely=0.5, anchor='center')

# start another thread for fileWatch, set to daemon so that it stops when the window closes
fileWatchThread = threading.Thread(target=fileWatch, daemon=True)
fileWatchThread.start()

# spawns the window
root.mainloop()
