import subprocess
import os
import time

def print_ast():
	print()
	print(50 * "#")
	print()


def menu():
	print_ast()
	print("This window will allow you to specify which application/attachement to pull")
	print_ast()
	print("1 - Pull Files")
	print("2 - Don't Pull Files")
	print("3 - Quit")
	print_ast()


#to get the current working directory
python_directory_path = os.getcwd()

#Name of the current user
cmd=subprocess.run("whoami",stdout=subprocess.PIPE)
user_name=cmd.stdout.decode("utf-8").strip()

#Change the following as necessary
desktop_path="/home/{user}/Desktop/".format(user=user_name)

#NOTE: Change LM if necessary
path_to_NDK_cmake="{desktop_p}/LM/android-ndk-r25c/build/cmake/android.toolchain.cmake".format(desktop_p=desktop_path)

#executable name
ndk_executable="copydbF"

#Android Paths
data_lcl_tmp_path="/data/local/tmp/"


cmd="cmake -DCMAKE_TOOLCHAIN_FILE={path_NDK} -DANDROID_ABI=arm64-v8a -DANDROID_NATIVE_API_LEVEL=16 {cur_dir}".format(path_NDK=path_to_NDK_cmake,cur_dir=python_directory_path)
subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)

cmd="cd {curnt_path} && make".format(curnt_path=python_directory_path)
subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)

cmd="adb push {curnt_path}/{exe} /sdcard/".format(curnt_path=python_directory_path,and_path=data_lcl_tmp_path,exe=ndk_executable)
subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)

# add delay before moving the file
#killall -9 /data/local/tmp/./copydbF    

#Change
cmd="adb shell \"su -c \'mv /sdcard/{ndk_exe} {lcl_tmp}\'\"".format(ndk_exe=ndk_executable,lcl_tmp=data_lcl_tmp_path)
subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)

cmd="adb shell \"su -c \'chmod 777 {and_path}{exe}\'\"".format(and_path=data_lcl_tmp_path,exe=ndk_executable)
subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)

cmd="adb shell \"su -c \'{and_path}./{exe}\' 2>/dev/null\"".format(and_path=data_lcl_tmp_path,exe=ndk_executable)
subprocess.run(cmd,shell=True)

sdcard_path="/sdcard/pull_file"

menu()
while True:
	decision=input("Please choose your option: ").lower()
	if decision=='3' or decision=='Q' or decision=='q':
		subproess.run("exit",shell=True)
		break
	elif decision=='1' or decision=='2':
		if decision=='1':
				cmd="adb pull {sdcard} {desk}".format(sdcard=sdcard_path,desk=desktop_path)
				subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)
		else:
			continue
	else:
		print("Invalid Option")

	menu()


#Test: 
# test=subprocess.run("whoami",stdout=subprocess.PIPE)
# print(test.stdout.decode("utf-8"))
