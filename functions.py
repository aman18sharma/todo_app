FREEZING_POINT = 0
BOILING_POINT = 100


def get_todos():
    file = open("todos.txt", "r")
    todos = file.readlines()
    file.close()
    for index, todo in enumerate(todos):
        row = f"{index + 1}-{todo.capitalize()}"
        print(row)


def write_todo(todo):
    file = open("todos.txt", "a")
    file.writelines(todo + "\n")
    file.close()


def water_state(temperature):
    if temperature <= FREEZING_POINT:
        print('Solid')
    elif FREEZING_POINT < temperature < BOILING_POINT:
        print('Liquid')
    elif temperature >= BOILING_POINT:
        print('Gas')


def foo(temperature):
    if temperature > 25:
        return 'Hot'
    elif temperature >= 15 and temperature <= 25:
        return 'Warm'
    else:
        return 'Cold'
