from collections import namedtuple

template = namedtuple('Student', ['name', 'age', 'department'])
alina = template('Alina', '22', 'linguistics')
alex = template('Alex', '25', 'programming')
kate = template('Kate', '19', 'art')
print(alina)
print(alex)
print(kate)
