cmake_minimum_required(VERSION 3.0)

project(copy C)

#add_executable(copydbF moving.c)
add_executable(copydbF test.c)

set_target_properties(copydbF PROPERTIES COMPILE_OPTIONS "-march=armv8-a" LINK_OPTIONS "-march=armv8-a")
