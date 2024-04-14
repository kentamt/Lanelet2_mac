cmake_minimum_required(VERSION 3.5.1)
project(lanelet2_io VERSION 4.0.0)


# Set C++ Standard to C++14 or later
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Find required packages
find_package(Boost REQUIRED COMPONENTS system filesystem serialization)
find_package(Eigen3 3.3 REQUIRED NO_MODULE)
find_package(pugixml REQUIRED)

link_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}/../lanelet2_core/build
    ${CMAKE_CURRENT_SOURCE_DIR}/../lanelet2_io/build
    ${CMAKE_CURRENT_SOURCE_DIR}/../lanelet2_matching/build
    ${CMAKE_CURRENT_SOURCE_DIR}/../lanelet2_projection/build
    ${CMAKE_CURRENT_SOURCE_DIR}/../lanelet2_routing/build
    ${CMAKE_CURRENT_SOURCE_DIR}/../lanelet2_traffic_rules/build
)


# Include directories for the current project and dependencies
include_directories(
  ${CMAKE_CURRENT_SOURCE_DIR}/include
  ${CMAKE_CURRENT_SOURCE_DIR}/include/lanelet2_core
  ${CMAKE_CURRENT_SOURCE_DIR}/../lanelet2_core/include
  ${CMAKE_CURRENT_SOURCE_DIR}/../lanelet2_io/include
  ${CMAKE_CURRENT_SOURCE_DIR}/../lanelet2_matching/include
  ${CMAKE_CURRENT_SOURCE_DIR}/../lanelet2_traffic_rules/include
  ${CMAKE_CURRENT_SOURCE_DIR}/../lanelet2_projection/include
  ${Boost_INCLUDE_DIRS}
  ${EIGEN3_INCLUDE_DIR}
  ${pugixml_INCLUDE_DIRS}
)

# Gather source and header files
file(GLOB_RECURSE PROJECT_SOURCE_FILES "src/*.cpp")
file(GLOB_RECURSE PROJECT_HEADER_FILES "include/*.h" "include/*.hpp")

# Define the library to be built from the sources
add_library(${PROJECT_NAME} SHARED
  ${PROJECT_SOURCE_FILES} ${PROJECT_HEADER_FILES})
target_link_libraries(${PROJECT_NAME}
  ${Boost_LIBRARIES}
  Eigen3::Eigen
  pugixml
  lanelet2_core
)


#############
## Install ##
#############

# Install the library to appropriate locations
install(TARGETS ${PROJECT_NAME}
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
    INCLUDES DESTINATION include
)

# Install header files
install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/
    DESTINATION include
    FILES_MATCHING PATTERN "*.h" PATTERN "*.hpp"
)

# Optionally install additional resources
install(DIRECTORY res/
    DESTINATION share/${PROJECT_NAME}/res
)


#############
## Testing ##
#############
enable_testing()
# add_subdirectory(../extern/googletest)
add_subdirectory(../extern/googletest googletest_build)

file(GLOB TEST_SOURCES "${CMAKE_CURRENT_SOURCE_DIR}/test/*.cpp")

set(TEST_FILES  # we need to change 
  # TestBinHandler 
  TestLanelet2Io
  TestOsmFile
  TestOsmHandler
  # TestSetup
  # TestSimpleUsage
)

include_directories(
  ${gtest_SOURCE_DIR}/include ${gtest_SOURCE_DIR}
)

foreach(testfile ${TEST_FILES})
  add_executable(${testfile} test/${testfile}.cpp)
  target_link_libraries(${testfile}
    gtest
    gtest_main
    # lanelet2_core
    lanelet2_io
    # lanelet2_matching
    # lanelet2_projection
    # lanelet2_routing
    # lanelet2_traffic_rules    
  )
  add_test(NAME ${testfile} COMMAND ${testfile})
endforeach()




