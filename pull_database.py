import subprocess
import os


#to get the current working directory
python_directory_path = os.getcwd()

#Name of the current user
cmd=subprocess.run("whoami",stdout=subprocess.PIPE)
user_name=cmd.stdout.decode("utf-8").strip()

#Change the following as necessary
desktop_path="/home/{user}/Desktop/".format(user=user_name)
path_to_NDK_cmake="{desktop_p}/LM/android-ndk-r25c/build/cmake/android.toolchain.cmake".format(desktop_p=desktop_path)
current_dir=python_directory_path

#executable name
ndk_executable="copydbF"

# while True:
package_name=input("Enter the package name: ") 

#Android Paths
data_lcl_tmp_path="/data/local/tmp/"
sdcard_path="/sdcard/{pack_name}".format(pack_name=package_name)

cmd="cmake -DCMAKE_TOOLCHAIN_FILE={path_NDK} -DANDROID_ABI=arm64-v8a -DANDROID_NATIVE_API_LEVEL=16 {cur_dir}".format(path_NDK=path_to_NDK_cmake,cur_dir=current_dir)
subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)

cmd="cd {curnt_path} && make".format(curnt_path=python_directory_path)
subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)

cmd="adb push {curnt_path}/{exe} /sdcard/".format(curnt_path=python_directory_path,and_path=data_lcl_tmp_path,exe=ndk_executable)
subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)

#Change
cmd="adb shell \"su -c \'mv /sdcard/{ndk_exe} {lcl_tmp}\'\"".format(ndk_exe=ndk_executable,lcl_tmp=data_lcl_tmp_path)
subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)

cmd="adb shell \"su -c \'chmod 777 {and_path}{exe}\'\"".format(and_path=data_lcl_tmp_path,exe=ndk_executable)
print(cmd)
subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)

#cmd="adb shell \"su -c \'{and_path}./{exe} {arg_package}\' 2>/dev/null\"".format(and_path=data_lcl_tmp_path,arg_package=package_name,exe=ndk_executable)
cmd="adb shell \"su -c \'{and_path}./{exe} {arg_package}\'\"".format(and_path=data_lcl_tmp_path,arg_package=package_name,exe=ndk_executable)
print(cmd)
subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)

cmd="adb pull {sdcard} {desk}".format(sdcard=sdcard_path,desk=desktop_path)
subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)

# print()
# print(50*("*"))
# print(50*("*"))
# decision=input("Would you like to search more apps (y/n): ")
# print(50*("*"))
# print(50*("*"))
# print()

# if decision=='n':
# 	break


#Test: 
# test=subprocess.run("whoami",stdout=subprocess.PIPE)
# print(test.stdout.decode("utf-8"))
