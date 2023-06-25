# def update_light(current):
#     if current == 'green':
#         return 'yellow'
#     elif current == 'yellow':
#         return 'red'
#     elif current == 'red':
#         return 'green'
def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]



update_light('green')
