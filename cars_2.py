#list of cars
cars = ['audi', 'bmw', 'subaru', 'toyota']
# if statement checks for bmw if it finds it, it prints i
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
