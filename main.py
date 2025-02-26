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
    # cat1 = template.Category()
    # cat1.name = "test1"
    # cat1.add("blabla")
    # cat1.add("aboba")
    # cat2 = template.Category()
    # cat2.name = "test2"
    # cat2.add("krol")
    # cat2.add("zeliboba")
    # l1 = template.TempList()
    # l1.name = "First list"
    # l1.add(cat1)
    # l1.add(cat2)
    # temp1 = template.Template()
    # temp1.name = "First template"
    # temp1.description = "я хачю пиццу"
    # temp1.add(l1)
    # print(temp1.save())
    # save_load.save(temp1.save())

    # t = save_load.load("test.json")
    # print(t["lists"])
    # temp = template.Template().load(t)
    # print(temp.lists[0].name)

    new_Temp = template.Template()
    new_Temp.set_name_description("Тестовый для проверки записи", "Здесь будет тестовое описание")
    new_Temp.add(template.TempList())
    new_Temp.lists[0].set_name("Первый список")
    new_Temp.lists[0].add(template.Category())
    new_Temp.lists[0].categories[0].set_name("Первая категория")
    new_Temp.lists[0].categories[0].add("Ну и наконец первый элемент")
    new_Temp.lists[0].categories[0].add("Второй тоже не помешает")
    save_load.save(new_Temp.save())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
