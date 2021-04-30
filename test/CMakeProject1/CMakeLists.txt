cmake_minimum_required (VERSION 3.8)

#--------------------------------------------                                   
# Preprocess                                                            
#--------------------------------------------   

# 提前运行Linux命令
#if($ENV{USER} STREQUAL "magiclab")
#execute_process(COMMAND asn1c -S /home/zixuanchen/asn1c-0.9.28/skeletons/ -fcompound-names -fskeletons-copy -gen-PER -pdu=all MsgFrame.asn)                                         
#elif($ENV{USER} STREQUAL "alvin")
#execute_process(COMMAND asn1c -S /home/zixuanchen/asn1c-0.9.28/skeletons/ -fcompound-names -fskeletons-copy -gen-PER -pdu=all MsgFrame.asn)
#endif
#--------------------------------------------                                   
# Project setting                                                               
#--------------------------------------------  

#INCLUDE(cmake/messagecolor.cmake)

#项目名称 如果混合编程需要添加CXX C并打开CXX C COMPLIER
PROJECT("CMakeProject1" )

IF (CMAKE_SYSTEM_NAME MATCHES "Linux")
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -g -Wall -Wno-unused-variable -pthread -lstdc++")  #设置c++的编译选项
SET(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c99 ")  #设置c的编译选项
SET(CMAKE_TOOLCHAIN_FILE "/home/$ENV{USER}/vcpkg/scripts/buildsystems/vcpkg.cmake")
SET(CMAKE_SYSTEM_NAME Linux)
ELSEIF (CMAKE_SYSTEM_NAME MATCHES "Windows")
#SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -g -Wall -pthread -lstdc++")  #设置c++的编译选项
#SET(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=c99 ")  #设置c的编译选项
SET(CMAKE_SYSTEM_NAME Windows)
SET(CMAKE_TOOLCHAIN_FILE "C:/Users/nxyct/Documents/Visual Studio 2019/vcpkg/scripts/buildsystems/vcpkg.cmake")
ELSE ()
	MESSAGE(STATUS "other platform: ${CMAKE_SYSTEM_NAME}")
ENDIF (CMAKE_SYSTEM_NAME MATCHES "Linux")

SET(CMAKE_SYSTEM_PROCESSOR x86 )
SET(CMAKE_BUILD_TYPE Debug )
#SET(CMAKE_C_COMPILER "gcc")
#SET(CMAKE_CXX_COMPILER "gcc")
#SET(CMAKE_PREFIX_PATH "")
SET(EXECUTABLE_OUTPUT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/bin/${CMAKE_BUILD_TYPE})
SET(LIBRARY_OUTPUT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/lib )
#SET(CMAKE_FIND_ROOT_PATH /home/alvin/asn1cFull)

#--------------------------------------------                                   
# Library setting                                                               
#--------------------------------------------   
# 引入所使用的包
find_package(Flatbuffers CONFIG OPTIONAL_COMPONENTS)
find_package(OpenCV  CONFIG OPTIONAL_COMPONENTS )

#常用变量
# PROJECT_SOURCE_DIR 声明project的Cmake路径
# CMAKE_SOURCE_DIR  最顶层CMakeLists.txt的路径
# CMAKE_CURRENT_SOURCE_DIR 当前CMakeLists.txt的路径

#添加头文件目录
include_directories(
"${CMAKE_CURRENT_SOURCE_DIR}/includes"
)

#添加需要链接的库文件目录
LINK_directories(
#"/home/alvin/asn1c-0.9.28/skeletons/"
)

#添加需要链接的库文件路径
#link_libraries(library1 <debug | optimized> library2 ...)

#若有新生成文件，使用GLOB 寻找 或 GLOB_RECURSE递归寻找
#FILE(GLOB generated_sources "${CMAKE_CURRENT_BINARY_DIR}/*.c")
#FILE(GLOB generated_includes "${CMAKE_CURRENT_BINARY_DIR}/*.h")

#包含目录下所有源文件但不会递归
aux_source_directory(${CMAKE_CURRENT_SOURCE_DIR}/src  TEST_SOURCE_FILE)

#--------------------------------------------                                   
# Executable                                                              
#--------------------------------------------   

#添加链接后的so库
#add_library(dedicated_lane SHARED "dedicated_lane.cpp" "dedicated_lane.h")

# 为工程生成目标文件
# 将源代码添加到此项目的可执行文件。
add_executable (CMakeProject1 ${TEST_SOURCE_FILE})

#add_subdirectory(3rdparty)

# 设置要链接的库文件的名称，该方法具有私密性PUBLIC PRIVATE INTERFACE，可以添加到固定的项目target中
#target_include_directories(RSU private "${PROJECT_SOURCE_DIR}/3rdparty")
#target_link_libraries(dedicated_lane PRIVATE flatbuffers::flatbuffers)


#--------------------------------------------                                   
# Install                                                            
#--------------------------------------------   


