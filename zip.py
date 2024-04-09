names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heores = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
for name, hero in zip(names, heores):
    print(f'{name} is actually {hero}')