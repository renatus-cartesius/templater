#!/usr/bin/env python3
import pkgutil as pkg
import os
import importlib
from lib import generators


def main():
    print("Available modules: ")
    [print(" - {0}".format(module)) for module in [name for _, name, _ in pkg.iter_modules([os.path.dirname(generators.__file__)])]]
    choosed_module = str(input("Please choose needed module: "))
    try:
        generator = importlib.import_module(str('lib.generators.' + choosed_module))
    except Exception as e:
        raise e
        print("Error by importing module ", choosed_module)
        return 1
    generator.main()


if __name__ == "__main__":
    main()
