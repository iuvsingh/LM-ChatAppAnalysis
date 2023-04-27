
cmake_minimum_required(VERSION 3.0)

#naming the project and specifying the coding language
project(my_project C)

#adding the executable to the project with source code within moving.c
add_executable(copydbF moving.c)

#sets the properties for the executable
set_target_properties(copydbF PROPERTIES COMPILE_OPTIONS "-march=armv8-a" LINK_OPTIONS "-march=armv8-a")


