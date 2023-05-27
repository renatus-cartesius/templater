#!/usr/bin/env python3
import generators
import pkgutil as pkg
import os

# env = j2.Environment(loader=j2.FileSystemLoader("../vagrant/"))
# template = env.get_template("Vagrantfile.j2")
#
# print("Please, input the hostname: ")
# hostname = str(input())
#
# content = template.render(hostname=hostname)
#
# print(content)


def main():
    # group = str(input("Pick the template group you want to use: "))
    # Print all template modules
    print("Available modules: ")
    [ print(" - {0}".format(module)) for module in [name for _, name, _ in pkg.iter_modules([os.path.dirname(generators.__file__)])]]
    group = str(input("Pick the template group you want to use: "))

if __name__ == "__main__":
    main()
