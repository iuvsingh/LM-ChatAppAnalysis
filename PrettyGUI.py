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



#defines the window
root = tk.Tk()
root.title('Access D3niers')
#set background color
root['background']='#003478'
root.geometry('1280x720')

#defines the notebook widget
tabControl = ScrollableNotebook(root, wheelscroll=True, tabmenu=True)

#to get the current working directory
python_directory_path = os.getcwd()

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
            if name not in previousUploads and name != 'LM.png' and name != 'GMU.png':
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
                    os.system("./csvV1.sh")
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
        if entry.path.lower().endswith(('.txt', '.png', '.jpg', 'jpeg', '.db','.csv')):#'.db', 
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

    # initialize logging event
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

def file_pull():
	#1 FOR MAC: For macOS run the following and comment out the line 216 (2 GNOME Terminal....) if using this code
	subprocess.run("gnome-terminal -x sh -c \"python3 pull_database.py; bash\"",shell=True)
    # subprocess.run(["python3", "pull_database.py"])
	
	# 2 GNOME-TERMINAL: for linux that gnome-terminal installed. Comment out the lin 213 if using this code	
	# Can hard code this: x-terminal-emulator
	# Read the list of terminal emulators from a file
	
	# path="{dir_py}/terminals.txt".format(dir_py=python_directory_path)
	# with open(path) as f:
	#     terminals = f.read().splitlines()

	# # Iterate over the list of terminal emulators and check for their presence using the `which` command
	# available_terminals = []
	# for term in terminals:
	# 	try:
	# 		subprocess.run(["which", term.lower()], check=True,stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
	# 		break
	# 	except subprocess.CalledProcessError:
	# 		pass
	
	# cmd = "{terminal} -e sh -c \"python3 pull_database.py; bash\"".format(terminal=term)
	# subprocess.run(cmd,shell=True,stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)

B=tkinter.Button(root,text="Pull Database",command= file_pull)
B.place(x=25, y=3000)
B.pack()

#Setting LM and GMU logos
imgLM = Image.open('LM.png')
imgGMU = Image.open('GMU.png')
 
# Resize the image using resize() method
resize_image = imgLM.resize((300, 40))
ri = imgGMU.resize((50, 50))
 
imgLM = ImageTk.PhotoImage(resize_image)
imgGMU = ImageTk.PhotoImage(ri)
 
# create label and add resize image
label1 = Label(image=imgLM,bg='#003478')
label1.place(relx=0.1, rely=0.0, anchor='nw')
label1.image = imgLM
#label1.pack()

label2 = Label(image=imgGMU,bg='#003478')
label2.place(relx=0.75, rely=0.0, anchor='ne')
label2.image = imgGMU
#label2.pack()



# initial start button
btn0 = tk.Button(text='Start', width=10, fg='black', highlightbackground='#003478',command=lambda: [fileUpdate(), tabLayout()])
btn0.place(relx=0.5, rely=0.5, anchor='center')

# start another thread for fileWatch, set to daemon so that it stops when the window closes
fileWatchThread = threading.Thread(target=fileWatch, daemon=True)
fileWatchThread.start()

# spawns the window
root.mainloop()
