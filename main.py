# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import save_load
import template

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # cat1 = template.Category("test1")
    # cat1.add("blabla")
    # cat1.add("aboba")
    # cat2 = template.Category("test2")
    # cat2.add("krol")
    # cat2.add("zeliboba")
    # l1 = template.TempList("First list")
    # l1.add(cat1)
    # l1.add(cat2)
    # temp1 = template.Template("First template", "я хачю пиццу")
    # temp1.add(l1)
    # print(temp1.save())
    # save_load.save(temp1.save())

    t = save_load.load("test.json")
    print(t["template"]["lists"])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
