import subprocess
import os
import shlex
import time

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


def print_ast():
	print()
	print(50 * "*")
	print()


def menu_check():
	print_ast()
	print("WELCOME\n")
	print("Select an option below")
	print("1 - Export the database files")
	print("2 - Export the attachment")
	print("3 - View new apps")
	print("4 - Quit\n")
	print_ast()
	user_val = str(input("Please enter your option: "))

	if user_val=="1":
		user_path=str(input("Please provide the package name to import: "))
		cmd="adb shell su -c \"{tmp_path}./{exe} {user_opt} {user_pack}\" /dev/null 2>&1".format(tmp_path=data_lcl_tmp_path,exe=ndk_executable,user_opt=user_val,user_pack=user_path)
		subprocess.run(cmd.split(),stdout=subprocess.PIPE)

	elif user_val=="2":
		user_path=str(input("Please provide the path to attachment: "))
		cmd="adb shell su -c \"{tmp_path}./{exe} {user_opt} {user_attach}\" /dev/null 2>&1".format(tmp_path=data_lcl_tmp_path,exe=ndk_executable,user_opt=user_val,user_attach=user_path)
		subprocess.run(cmd.split(),stdout=subprocess.PIPE)


def build_push_assign():
	
	cmd="adb shell su -c \"killall -9 //data/local/tmp/./copydbF\" 2>/dev/null"
	subprocess.run(cmd.split(),stdout=subprocess.PIPE)

	cmd="cmake -DCMAKE_TOOLCHAIN_FILE={path_NDK} -DANDROID_ABI=arm64-v8a -DANDROID_NATIVE_API_LEVEL=16 {cur_dir}".format(path_NDK=path_to_NDK_cmake,cur_dir=python_directory_path)
	subprocess.run(cmd.split(),stdout=subprocess.PIPE)

	cmd = "make"
	subprocess.run(cmd, stdout=subprocess.PIPE)


	cmd="adb push {curnt_path}/{ndkexe} {sd_path}/".format(curnt_path=python_directory_path,sd_path=sd_card_path, ndkexe=ndk_executable)
	subprocess.run(cmd.split(),stdout=subprocess.PIPE)

	cmd="adb shell su -c \"cp -rvf {sd_path}/{ndkexe} {and_path}\"".format(and_path=data_lcl_tmp_path,sd_path=sd_card_path, ndkexe=ndk_executable)
	subprocess.run(cmd.split(),stdout=subprocess.PIPE)

	print("Please wait...")
	subprocess.run("sleep 2".split())

	cmd="adb shell su -c \"chmod 777 {and_path}/{ndkexe}\"".format(and_path=data_lcl_tmp_path,ndkexe=ndk_executable)
	subprocess.run(cmd.split(),stdout=subprocess.PIPE)


def main():
	build_push_assign()
	menu_check()


if __name__ == "__main__":
	main()

# #to get the current working directory
# python_directory_path = os.getcwd()

# #Name of the current user
# cmd=subprocess.run("whoami",stdout=subprocess.PIPE)
# user_name=cmd.stdout.decode("utf-8").strip()

# #Change the following as necessary
# desktop_path="/home/{user}/Desktop/".format(user=user_name)

# #NOTE: Change LM if necessary
# path_to_NDK_cmake="{desktop_p}/LM/android-ndk-r25c/build/cmake/android.toolchain.cmake".format(desktop_p=desktop_path)

# #executable name
# ndk_executable="copydbF"

# #Android Paths
# data_lcl_tmp_path="/data/local/tmp/"


# cmd="cmake -DCMAKE_TOOLCHAIN_FILE={path_NDK} -DANDROID_ABI=arm64-v8a -DANDROID_NATIVE_API_LEVEL=16 {cur_dir}".format(path_NDK=path_to_NDK_cmake,cur_dir=python_directory_path)
# subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)

# cmd="cd {curnt_path} && make".format(curnt_path=python_directory_path)
# subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)

# cmd="adb push {curnt_path}/{exe} /sdcard/".format(curnt_path=python_directory_path,and_path=data_lcl_tmp_path,exe=ndk_executable)
# subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)

# # add delay before moving the file
# #killall -9 /data/local/tmp/./copydbF    

# #Change
# cmd="adb shell \"su -c \'mv /sdcard/{ndk_exe} {lcl_tmp}\'\"".format(ndk_exe=ndk_executable,lcl_tmp=data_lcl_tmp_path)
# subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)

# cmd="adb shell \"su -c \'chmod 777 {and_path}{exe}\'\"".format(and_path=data_lcl_tmp_path,exe=ndk_executable)
# subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)

# cmd="adb shell \"su -c \'{and_path}./{exe}\' 2>/dev/null\"".format(and_path=data_lcl_tmp_path,exe=ndk_executable)
# subprocess.run(cmd,shell=True)

# sdcard_path="/sdcard/pull_file"









########################################################################################
#####################################################################
# x = subprocess.run("chmod +x test.sh".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print(x.stdout.decode())
# print(x.stderr.decode())

# x = subprocess.run("./test.sh".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print(x.stdout.decode())
# print(x.stderr.decode())

# #Name of the current user
# cmd=subprocess.run("whoami",stdout=subprocess.PIPE)
# user_name=cmd.stdout.decode("utf-8").strip()
# current_dir = os.getcwd()
# desktop_path="/home/{user}/Desktop/".format(user=user_name)
# path_to_NDK_cmake="{desktop_p}/LM/android-ndk-r25c/build/cmake/android.toolchain.cmake".format(desktop_p=desktop_path)
# cmd="cmake -DCMAKE_TOOLCHAIN_FILE={path_NDK} -DANDROID_ABI=arm64-v8a -DANDROID_NATIVE_API_LEVEL=16 {cur_dir}".format(path_NDK=path_to_NDK_cmake,cur_dir=current_dir)
# subprocess.run(cmd.split(),stdout=subprocess.PIPE)

# x = subprocess.run("make".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print(x.stdout.decode())
# print(x.stderr.decode())

# x = subprocess.run("adb push test /sdcard/".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print(x.stdout.decode())
# print(x.stderr.decode())

# x = subprocess.run("adb shell su -c cp -rvf /sdcard/test /data/local/tmp/".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print(x.stdout.decode())
# print(x.stderr.decode())

# x = subprocess.run("adb shell su -c chmod +x /data/local/tmp/test".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print(x.stdout.decode())
# print(x.stderr.decode())

# x = subprocess.run("adb shell su -c /data/local/tmp/./test".split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# print(x.stdout.decode())
# print(x.stderr.decode())


##########################
# process = subprocess.Popen(shlex.split("""x-terminal-emulator -e 'bash -c "python3 test2.py"'"""), stdout=subprocess.PIPE)
# process.wait()
##############################
#Threading Module

# import threading

# def launch_ter():
# 	subprocess.run(["x-terminal-emulator"])


# x = threading.Thread(target=launch_ter)
# x.daemon = True
# x.start()

##########################

#############################
# #Checking the name 

# cmd=subprocess.run("whoami",stdout=subprocess.PIPE)
# user_name=cmd.stdout.decode("utf-8").strip()

########################
