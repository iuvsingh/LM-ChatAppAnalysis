cmake_minimum_required(VERSION 3.0)

project(my_project C)

add_executable(copydbF moving.c)
set_target_properties(copydbF PROPERTIES COMPILE_OPTIONS "-march=armv8-a" LINK_OPTIONS "-march=armv8-a")

#add_executable(permissions permissions.c)
#set_target_properties(my_program PROPERTIES COMPILE_OPTIONS "-march=armv8-a" LINK_OPTIONS "-march=armv8-a")

#set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -I/usr/include/x86_64-linux-gnu")
#set(CMAKE_SYSTEM_PROCESSOR "aarch64")