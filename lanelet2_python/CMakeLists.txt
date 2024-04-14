cmake_minimum_required(VERSION 3.5.1)
project(lanelet2_python VERSION 4.0.0)

cmake_policy(SET CMP0144 NEW)

set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -arch arm64")

find_package(Python3 3.12 EXACT REQUIRED COMPONENTS Interpreter Development)
find_package(Boost 1.58.0 REQUIRED COMPONENTS python312 filesystem) 

find_package(Eigen3 3.3 REQUIRED NO_MODULE)
find_package(pugixml REQUIRED)
find_package(GeographicLib 2.3 REQUIRED)

if(Boost_FOUND)
  message(STATUS "Boost found with all libraries.")
  message(STATUS "Boost include directory: ${Boost_INCLUDE_DIRS}")
  message(STATUS "Boost library directory: ${Boost_LIBRARY_DIRS}")
else()
  message(STATUS "Boost not found or missing required libraries.")
endif()


include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}/include
    ${CMAKE_CURRENT_SOURCE_DIR}/../lanelet2_io/include
    ${CMAKE_CURRENT_SOURCE_DIR}/../lanelet2_core/include
    ${CMAKE_CURRENT_SOURCE_DIR}/../lanelet2_matching/include
    ${CMAKE_CURRENT_SOURCE_DIR}/../lanelet2_projection/include
    ${CMAKE_CURRENT_SOURCE_DIR}/../lanelet2_routing/include
    ${CMAKE_CURRENT_SOURCE_DIR}/../lanelet2_traffic_rules/include
    ${CMAKE_CURRENT_SOURCE_DIR}/include/lanelet2_python
    ${Boost_INCLUDE_DIRS},
    ${EIGEN3_INCLUDE_DIR},
    ${pugixml_INCLUDE_DIRS},
    ${Python3_INCLUDE_DIRS},
    ${GeographicLib_INCLUDE_DIRS},
)

link_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}/../lanelet2_io/build
    ${CMAKE_CURRENT_SOURCE_DIR}/../lanelet2_core/build
    ${CMAKE_CURRENT_SOURCE_DIR}/../lanelet2_matching/build
    ${CMAKE_CURRENT_SOURCE_DIR}/../lanelet2_projection/build
    ${CMAKE_CURRENT_SOURCE_DIR}/../lanelet2_routing/build
    ${CMAKE_CURRENT_SOURCE_DIR}/../lanelet2_traffic_rules/build
)

file(GLOB_RECURSE PROJECT_HEADER_FILES "include/*.h" "include/*.hpp")

add_definitions(-DPYTHON_API_MODULE_NAME=core)

set(MODULES core io matching projection routing traffic_rules geometry)
foreach(MODULE ${MODULES})
  add_library(${MODULE} SHARED "python_api/${MODULE}.cpp")
  set_target_properties(${MODULE} PROPERTIES PREFIX "" OUTPUT_NAME "${MODULE}" SUFFIX ".so")
  set_target_properties(${MODULE} PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/lanelet2")
  target_link_libraries(${MODULE}
    ${Boost_LIBRARIES}
    ${Boost_SYSTEM_LIBRARY}
    ${Boost_PYTHON_LIBRARY}
    ${GeographicLib_LIBRARIES}
    ${PYTHON_LIBRARIES}
    Eigen3::Eigen
    pugixml
    Python3::Python
    lanelet2_core
    lanelet2_io
    lanelet2_matching
    lanelet2_projection
    lanelet2_routing
    lanelet2_traffic_rules
  )
endforeach()
