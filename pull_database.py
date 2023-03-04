import subprocess
import os


while True:
	
	package_name=input("Enter the package name: ") 
	
	#to get the current working directory
	python_directory_path = os.getcwd()
	data_lcl_tmp_path="/data/local/tmp"
	sdcard_path="/sdcard/{pack_name}".format(pack_name=package_name)
	desktop_path="/home/kali/Desktop/"
	c_code_path=python_directory_path

	cmd="cmake -DCMAKE_TOOLCHAIN_FILE={curnt_path}/android-ndk-r25c/build/cmake/android.toolchain.cmake -DANDROID_ABI=armeabi-v7a -DANDROID_NATIVE_API_LEVEL=16 {c_code}".format(curnt_path=python_directory_path,c_code=c_code_path)
	subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)

	cmd="cd {curnt_path} && make".format(curnt_path=python_directory_path)
	subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)

	cmd="adb push {curnt_path}/copydbF {and_path}/".format(curnt_path=python_directory_path,and_path=data_lcl_tmp_path)
	subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)

	cmd="adb shell \"su -c \'chmod 777 {and_path}/copydbF\'\"".format(and_path=data_lcl_tmp_path)
	subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)

	cmd="adb shell \"su -c \'{and_path}/copydbF {arg_package}\' 2>/dev/null\"".format(and_path=data_lcl_tmp_path,arg_package=package_name)
	subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)

	cmd="adb pull {sdcard} {desk}".format(sdcard=sdcard_path,desk=desktop_path)
	subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)
	
	print()
	print(50*("*"))
	print(50*("*"))
	decision=input("Would you like to search more apps (y/n): ")
	print(50*("*"))
	print(50*("*"))
	print()
	
	if decision=='n':
		break
