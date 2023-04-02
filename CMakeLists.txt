cmake_minimum_required(VERSION 3.0)

project(copy C)

add_executable(copydbF moving.c)
#set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -I/usr/include/x86_64-linux-gnu")
#set(CMAKE_SYSTEM_PROCESSOR "aarch64")
set_target_properties(copydbF PROPERTIES COMPILE_OPTIONS "-march=armv8-a" LINK_OPTIONS "-march=armv8-a")
