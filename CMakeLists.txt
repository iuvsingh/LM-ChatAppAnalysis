cmake_minimum_required(VERSION 3.0)

project(copy C)

add_executable(copydbF moving.c)

set_target_properties(copydbF PROPERTIES COMPILE_OPTIONS "-m32" LINK_OPTIONS "-m32")