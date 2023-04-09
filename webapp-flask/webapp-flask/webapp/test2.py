# tasks = open('todos.txt')
# for chore in tasks:
#     print(chore)
# tasks.close()
with open('todos.txt') as tasks:
    for i in tasks:
        print(i, end='')

