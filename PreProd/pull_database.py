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

#Android Paths
data_lcl_tmp_path="/data/local/tmp/"
# sdcard_path="/sdcard/{pack_name}".format(pack_name=package_name)

cmd="cmake -DCMAKE_TOOLCHAIN_FILE={path_NDK} -DANDROID_ABI=arm64-v8a -DANDROID_NATIVE_API_LEVEL=16 {cur_dir}".format(path_NDK=path_to_NDK_cmake,cur_dir=current_dir)
subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)


subprocess.run(["make"])
subprocess.run(["adb","push", "copydbF", "/sdcard/"])
subprocess.run(["adb","push", "permissions", "/sdcard/"])

cmd="adb shell \"su -c \'mv /sdcard/permissions /data/local/tmp/\'\""
subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)

cmd="adb shell \"su -c \'chmod 777 /data/local/tmp/permissions\'\""
subprocess.run(cmd,stdout=subprocess.PIPE,shell=True)

#cmd="adb shell \"su -c \'{and_path}./{exe} {arg_package}\' 2>/dev/null\"".format(and_path=data_lcl_tmp_path,arg_package=package_name,exe=ndk_executable)
cmd="adb shell su -c /data/local/tmp/./permissions"
process = subprocess.Popen(cmd.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

while True:
    output = process.stdout.readline().decode('utf-8').strip()
    error = process.stderr.readline().decode('utf-8').strip()
    
    if not output and not error and process.poll() is not None:
        break
        
    if output:
        print(output)
    
    if error:
        print(error)
    
    # Get input from the user and send it to the process
    user_input = input()
    process.stdin.write(user_input.encode('utf-8') + b'\n')
    process.stdin.flush()
    
rc = process.poll()


