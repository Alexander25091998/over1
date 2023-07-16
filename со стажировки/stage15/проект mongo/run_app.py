from mongo_client import MongoCl

MONGO_URL = "mongodb://localhost:27017"
PERSONS_COLLECTION_NAME = 'persons'

# persons = [
#     {
#         "name": "Андрей",
#         "age": 33
#     },
#     {
#         "name": "Василий",
#         "age": 24
#     },
#     {
#         "name": "Мария",
#         "age": 19
#     }
# ]
cars = [
    {
        'brend': 'Порше',
        'mark1': 'Панамера'
    },
    {
        'brend': 'Пежо',
        'mark2': '307'
    }
]


mongo_client = MongoCl(MONGO_URL, PERSONS_COLLECTION_NAME)
mongo_client.insert(PERSONS_COLLECTION_NAME, cars)
# items = mongo_client.get_collection('persons')
items = mongo_client.find_all('persons', 'age', 19)
for item in items:
    print(item)

