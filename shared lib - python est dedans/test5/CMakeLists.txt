cmake_minimum_required(VERSION 3.21)
project(test5 C)

set(CMAKE_C_STANDARD 99)

add_library(test5 SHARED library.c)
