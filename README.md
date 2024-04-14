# Lanelet2 for Mac
Lanelet2 for Apple Silicon Mac, eliminating the need for ROS, Catkin, and Conan.

# Tested Environment
- Apple M1
- MacOS Sonoma 14.3.1
- Python 3.11 and 3.12
- Boost 1.84
- Boost_python 3.12
- Geographiclib 2.3
- Eigen 3.4

# Install
## Dependencies

```bash
# install dependencies
brew install python
brew install boost
brew install boost-python
brew install eigen
brew install pugixml
brew install geographiclib

# clone googletest
cd /path/to/Lanelet2_mac/
git submodule add https://github.com/google/googletest.git extern/googletest                                                                                              ✘ 130
git submodule update --init --recursive
```

Change `lanelet2_python/CMakeLists.txt` based on your python version.

For 3.12
```
find_package(Python3 3.12 EXACT REQUIRED COMPONENTS Interpreter Development)
find_package(Boost 1.58.0 REQUIRED COMPONENTS python312 filesystem)```
```

For 3.11
```
find_package(Python3 3.11 EXACT REQUIRED COMPONENTS Interpreter Development)
find_package(Boost 1.58.0 REQUIRED COMPONENTS python311 filesystem)```
```

## Cmake & make
Subsequently, you can run `cmake.py` or cmake individually. 

```
# cmake & make
python cmake.py
```

libraries are generated in `lanelet_python/lanelet2/`. You can move `lanelet2` directory to your python library path.


## Test

You can test each lib at `build` with `make test` command.
```
cd lanelet_core/build
make test
```

After adding `lanelet2` to your python library path, you can test it at `lanelet2_python/test`.
```
python test_lanelet2.py
python test_lanelet2_matching.py
python test_lanelet2_projection.py
```



# Lanelet2

See https://github.com/fzi-forschungszentrum-informatik/Lanelet2
