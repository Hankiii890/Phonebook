import csv

data = [
    {'Lastname': 'Ivanov', 'Firstname': "Ivan", 'Surname': "Ivanovich", 'Organization': 'ABC Company', 'Work_phone':'123456789', 'Mobile_phone': '52324421092'},
    {'Lastname': 'Petrov', 'Firstname': "Petr", 'Surname': "Petrovich", 'Organization': 'Hankiii Company', 'Work_phone':'4987654321', 'Mobile_phone': '46382940559'},
    {'Lastname': 'Sidorov', 'Firstname': "Denis", 'Surname': "Dmitrievich", 'Organization': 'Best Company', 'Work_phone':'77453631343', 'Mobile_phone': '64629434325'},
]
with open('data.csv', "w", newline='') as f:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)