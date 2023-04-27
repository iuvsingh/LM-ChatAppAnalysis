import subprocess
import os
import shlex
import time
import colorama
from colorama import Fore, Style

#to get the current working directory
python_directory_path = os.getcwd()

#Name of the current user
cmd=subprocess.run("whoami",stdout=subprocess.PIPE)
user_name=cmd.stdout.decode("utf-8").strip()

#Change the following as necessary
desktop_path="/home/{user}/Desktop".format(user=user_name)

#NOTE: Change LM if necessary
path_to_NDK_cmake="{desktop_p}/LM/android-ndk-r25c/build/cmake/android.toolchain.cmake".format(desktop_p=desktop_path)

#executable name
ndk_executable="copydbF"

#Android temp file path
data_lcl_tmp_path="/data/local/tmp/"

#android sd card path
sd_card_path="/sdcard"

#Backup path on android for signal
bckup_path = "/storage/emulated/0/Signal/Backups"

#creating the menu options 
def menu_options():
	print_ast()
	print("WELCOME\n")
	print("Select an option below")
	print("1 - Export the database files (NOTE: ALL FIlES WILL BE IMPORTED ON DESKTOP)")
	print("2 - Export the attachment (NOTE: ALL FIlES WILL BE IMPORTED ON DESKTOP)")
	print("3 - View new apps")
	print("4 - Quit")
	print("5 - Clear screen")
	print_ast()

#printing 50 asterisks in the menu_options function
def print_ast():
	print()
	print(Fore.CYAN  + Style.BRIGHT + 50 * "*"+ Style.RESET_ALL)
	print()

#checks to see if there is a signal backup in the backup folder on the device
def check_signal(path_to_dbs):
	# TODO: Change the hardcoded stuff 
	cmd = "adb pull {bckup} {desk}/imports/{user_pk}".format(bckup=bckup_path,user_pk=path_to_dbs,desk=desktop_path)
	subprocess.run(cmd.split(),stdout=subprocess.PIPE)
	#prints successfully imported once the process is done
	print(Fore.GREEN + "Successfully Imported"+ Style.RESET_ALL)

#dictates what happens after user chooses one of the menu options
def menu_check():

	while True:

		#creates an imports directory
		subprocess.run("mkdir {desk}/imports".format(desk=desktop_path).split(),stderr=subprocess.PIPE)

		#the menu options will present itself once this function gets called
		menu_options()

		user_val = str(input("Please enter your option: "))

		#if the user chooses option one, they will type in the chat application package name that they want to export
		if user_val=="1":
			user_path=str(input("Please provide the package name to import: "))
			#checks to make sure the package name is not the signal app's package name
			if user_path!="org.thoughtcrime.securesms":

				#passes the package name to the executable and runs the executable using adb with elevated privileges 
				cmd="adb shell su -c \"{tmp_path}./{exe} {user_opt} {user_pack}\" /dev/null 2>&1".format(tmp_path=data_lcl_tmp_path,exe=ndk_executable,user_opt=user_val,user_pack=user_path)
				subprocess.run(cmd.split(),stdout=subprocess.PIPE)
				print()
				# TODO: Change the hardcoded stuff 

				#pulls the package from the sdcard to the local machine imports folder
				cmd = "adb pull /sdcard/dbs_attchmnt/{user_pk} {desk}/imports/{user_pk}".format(user_pk=user_path,desk=desktop_path)
				subprocess.run(cmd.split(),stdout=subprocess.PIPE)

				print(Fore.GREEN + "Successfully Imported"+ Style.RESET_ALL)
			else:
				check_signal(user_path)
		#elif statement if user chooses to grab an attachment
		elif user_val=="2":
			user_path=str(input("Please provide the path to attachment: "))
			#passes the attachment filepath to the executable and runs the executable using adb with elevated privileges 
			cmd="adb shell su -c \"{tmp_path}./{exe} {user_opt} {user_attach}\" /dev/null 2>&1".format(tmp_path=data_lcl_tmp_path,exe=ndk_executable,user_opt=user_val,user_attach=user_path)
			subprocess.run(cmd.split(),stdout=subprocess.PIPE)
			print ()

			# TODO: Change the hardcoded stuff 
			# cmd = "adb pull /sdcard/dbs_attchmnt/{user_pk} {desk}/imports/".format(user_pk=user_path,desk=desktop_path)

			#pulls to attachment to the imports folder
			cmd = "adb pull {user_pk} {desk}/imports/".format(user_pk=user_path,desk=desktop_path)
			subprocess.run(cmd.split(),stdout=subprocess.PIPE)

			print(Fore.GREEN + "Successfully Imported"+ Style.RESET_ALL)

		#if user chooses to clear the list of new applications
		elif user_val=="3":
			while True:
				user_val2=str(input("Would you like to clear the list of new apps? (y/n): ")).lower()
				if user_val2=='y' or user_val2=='yes' or user_val2=='n' or user_val2=='no':
					break
				else: #says invalid option if the user types an option that is not y, yes, n, no 
					print(Fore.RED + "INVALID OPTION" + Style.RESET_ALL)
					print()
			#runs adb command and gets the ndk executable to clear the new list of apps
			cmd="adb shell su -c \"{tmp_path}./{exe} {user_opt} {user_opt2}\" /dev/null 2>&1".format(tmp_path=data_lcl_tmp_path,exe=ndk_executable,user_opt=user_val,user_opt2=user_val2)
			subprocess.run(cmd.split(),stdout=subprocess.PIPE)

			#runs command to pull the diff,txt file to the desktop to view which applications have been used
			cmd="adb pull /sdcard/exe_files/diff.txt {desk}".format(desk=desktop_path)
			subprocess.run(cmd.split(),stdout=subprocess.PIPE)

			print()
			# Open the file in read mode
			with open("{desk}/diff.txt".format(desk=desktop_path), "r") as file:
				# Read the contents of the file and print them
				contents = file.read()
				print(Fore.GREEN + contents+ Style.RESET_ALL)

		#if user wants to stop using the menu
		elif user_val=="4":
			print_ast()
			print("Goodbye!")
			print_ast()
			break

		#option 5 will clear everything
		elif user_val=="5" or user_val=="clear" or user_val=="cls":
			subprocess.run("clear")

		#if user inputs anything that is not 1-5
		else:
			print_ast()
			print(Fore.RED + "INVALID OPTION" + Style.RESET_ALL)
			print_ast()

def build_push_assign():
	#command to kill the process of the ndk executable and send error outputs to /dev/null
	cmd="adb shell su -c \"killall -9 //data/local/tmp/./copydbF\" 2>/dev/null"
	subprocess.run(cmd.split(),stdout=subprocess.PIPE)
	#command to build the cmake using arm64 architecture
	cmd="cmake -DCMAKE_TOOLCHAIN_FILE={path_NDK} -DANDROID_ABI=arm64-v8a -DANDROID_NATIVE_API_LEVEL=16 {cur_dir}".format(path_NDK=path_to_NDK_cmake,cur_dir=python_directory_path)
	subprocess.run(cmd.split(),stdout=subprocess.PIPE)
	#runs to command to make/build to C code
	cmd = "make"
	subprocess.run(cmd, stdout=subprocess.PIPE)

	#command to ndk executable to the sdcard
	cmd="adb push {curnt_path}/{ndkexe} {sd_path}/".format(curnt_path=python_directory_path,sd_path=sd_card_path, ndkexe=ndk_executable)
	subprocess.run(cmd.split(),stdout=subprocess.PIPE)

	#command to copy the ndk executable from the sdcard to the destination path
	cmd="adb shell su -c \"cp -rvf {sd_path}/{ndkexe} {and_path}\"".format(and_path=data_lcl_tmp_path,sd_path=sd_card_path, ndkexe=ndk_executable)
	subprocess.run(cmd.split(),stdout=subprocess.PIPE)

	print("Please wait...")
	subprocess.run("sleep 2".split())

	#gives ndk executable full permissions 
	cmd="adb shell su -c \"chmod 777 {and_path}/{ndkexe}\"".format(and_path=data_lcl_tmp_path,ndkexe=ndk_executable)
	subprocess.run(cmd.split(),stdout=subprocess.PIPE)

#starting the whole process and opening adb server in terminal
def main():
	cmd = "adb start-server"
	subprocess.run(cmd.split(),stdout=subprocess.PIPE)
	#calling the build ndk executable function
	build_push_assign()
	#calling function requesting user input
	menu_check()


if __name__ == "__main__":
	main()

