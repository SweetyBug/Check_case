def menu_interface():
    print('-----------------------------')
    print('            МЕНЮ:')
    print('-----------------------------')
    menu_list = ['1. Добавить задачу','2. Задача выполнена' ,'3. Список невыполненных задач', '4. Список выполненных задач', '5. Выход']
    for i in menu_list:
        print(i, sep = '\n')
    print('-----------------------------')


menu_interface()