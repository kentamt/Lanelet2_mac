import os
from pathlib import Path
import subprocess


def clean(directory):
    build_dir = os.path.join(directory, "build")

    # remove build directory if it exists
    if Path(build_dir).exists():
        print(f"Removing {build_dir}")
        os.system(f"rm -rf {build_dir}")


def main():
    root_dir = os.getcwd()
    target_dir = ["lanelet2_core",
                  "lanelet2_io",
                  "lanelet2_traffic_rules",
                  "lanelet2_matching",
                  "lanelet2_projection",
                  "lanelet2_routing",
                  "lanelet2_validation",
                  "lanelet2_python"
                  ]

    for target in target_dir:
        target = os.path.join(root_dir, target)
        print(f"Configuring in {target}")
        clean(target)
        # run_cmake(target)


if __name__ == "__main__":
    main()
