'''

When importing objects from a module in Python, the syntax usually is as follows:

from module_name import object

Given a string of an incorrect import statement, return the fixed string. All import statements will be the wrong way round.

'''


def fix_import(s):
    return "from " + s.split(" ")[-1] + " import " + s.split(" ")[1]


if __name__ == "__main__":
    print(fix_import("import object from module_name"))