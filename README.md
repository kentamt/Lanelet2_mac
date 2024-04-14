# Lanelet2 for Mac
This repository is for Lanelet2 on Apple Silicon Mac. It eliminates the need for ROS, catkin, and conan, and installs dependencies from Homebrew.

# Tested Environment

- Apple M1
- MacOS Sonoma 14.3.1
- Python 3.11
- Boost 1.84
- Python 3.11 and 3.12
- 

# Install

```bash
brew install python
brew install boost
brew install boost-python
brew install eigen
brew install pugixml
brew install geographiclib
```

libraries are generated in `lanelet_python/lanelet2/`. You can move `lanelet2` directory to your python library path.

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
