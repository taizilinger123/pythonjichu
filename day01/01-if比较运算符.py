#!/usr/bin/env python
# -*- coding:utf-8 -*-
age = 19
#if age大于或者等于18:
if age == 18:
    # age >= 18:
    # age <= 18:
    # age != 18:
    print("成年，可以去网吧......")
#print(sum(range(1,101)))

# message = "Hello python world!"
# print(message)

# message = "Hello python Crash Course world!"
# print(message)
#
# name = "ada lovelace"
# print(name.title())
# print(name.upper())
# print(name.lower())

# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"
# print(full_name)
# print("Python")
# print("\tPython")
# print("\nPython")
# print("Languages:\n\tPython\n\tC\n\tJavaScript")

# favorite_language = 'python '
# print(favorite_language.rstrip())
# favorite_language = ' python'
# print(favorite_language.lstrip())
# favorite_language = ' python '
# print(favorite_language.strip())
# message = "One of Python's strengths is its diverse community."
# print(message)
# universe_age = 14_000_000_000
# print(universe_age)
# x = 0
# y = 1
# z = 2
# print(x)
# print(y)
# print(z)
# x,y,z = 0,1,2
# print(x)
# print(y)
# print(z)

# MAX_CONNECTIONS = 5000
# MAX_CONNECTIONS = 4000
# print(MAX_CONNECTIONS)

# # 向大家问好。
# print("hello everyone!")

# import this
# bicycles=['trek','cannondale','redline','specialized']
# #print(bicycles[-2])
# message=f'My first bicyle was a {bicycles[0].title()}.'
# #print(message)
# motorcycles=['honda','yamaha','suzuki']
# #motorcycles[0]='ducati'
# #print(motorcycles)
# motorcycles.append("ducati")
# print(motorcycles)
# motorcycles=[]
# print(motorcycles)
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)
# motorcycles=['honda','yamaha','suzuki']
# motorcycles.insert(0,'ducati')
# print(motorcycles)

# motorcycles=['honda','yamaha','suzuki']
# print(motorcycles)
# del motorcycles[0]
# print(motorcycles)
# del motorcycles[1]
# print(motorcycles)

# motorcycles=['honda','yamaha','suzuki']
# print(motorcycles)
# popped_motocycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motocycle)

# motorcycles=['honda','yamaha','suzuki']
# last_owned = motorcycles.pop(0)
# print(f'The last motorcycle I owned was a {last_owned.title()}.')

# motorcycles=['honda','yamaha','suzuki','ducati']
# print(motorcycles)
# motorcycles.remove('ducati')
# print(motorcycles)

# cars = ['bmw','audi','toyota','subaru']
# print(cars)

# cars.sort(reverse=True)
# print(cars)

# cars = ['bmw','audi','toyota','subaru']
# print(cars)

# print("\nHere is the sorted list:")
# print(sorted(cars))

# print(cars)

# cars = ['bmw','audi','toyota','subaru']
# print(cars)
# cars.reverse()
# print(cars)
# cars.reverse()
# print(cars)

# cars = ['bmw','audi','toyota','subaru']
# print(len(cars))

# magicians = ['alice','david','carolina']
# for magician in magicians:
#     print(f"{magician.title()},that was a great trick!")
#     print(f"I can't wait to see your next trick,{magician.title()}.\n")
# print("Thank you,everyone.That was a great magic show!")

# print(list(range(6)))
# print(list(range(0,6)))
# print(list(range(1,6)))
# print(list(range(0,6,1)))
# print(list(range(0,6,2)))
# numbers = list(range(1,6))
# print(numbers)
# even_numbers = list(range(2,11,2))
# print(even_numbers)
# odd = list(range(1,11,2))
# print(odd)

# squares = []
# for value in range(1,11):
#     square = value ** 2
#     squares.append(square)
# print(squares)

# squares = []
# for value in range(1,11):
#     squares.append(value ** 2)
# print(squares)

# squares = [value ** 2 for value in range(1,11)]
# print(squares)

# digits = [1,2,3,4,5,6,7,8,9,0]
# print(max(digits))
# print(min(digits))
# print(sum(digits))

# players = ['charles','martina','michael','florence','eli']
# print(players[0:3])
# print(players[1:4])
# print(players[:4])
# print(players[0:4])
# print(players[2:])
# print(players[-3:])
# print(players[0:4:2])

# players = ['charles','martina','michael','florence','eli']
# print("Here are the first three players on my team:")
# for player in players[0:3]:
#     print(player.title())

# my_foods = ['pizza','falafel','carrot cake']
# friend_foods = my_foods[:]
# print("my favorite foods are:")
# print(my_foods)
# print("\nMy friend's favourite foods are:")
# print(friend_foods)

# my_foods = ['pizza','falafel','carrot cake']
# friend_foods = my_foods[:]
# # friend_foods = my_foods

# my_foods.append('cannoli')
# friend_foods.append('ice cream')

# print("my favorite foods are:")
# print(my_foods)
# print("\nMy friend's favourite foods are:")
# print(friend_foods)

# dimensions = (200,50)
# print(dimensions[0])
# print(dimensions[1])

# dimensions = (200,)
# print(dimensions[0])

# dimensions = (200,50)
# print('Original dimensions:')
# for dimension in dimensions:
#     print(dimension)

# dimensions = (400,100)
# print('\nModified dimensions:')
# for dimension in dimensions:
#     print(dimension)

# cars = ['audi','bmw','subaru','toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# car = 'bmw'
# print(car == 'bmw')

# car = "Audi"
# print(car == 'audi')

# car = 'Audi'
# print(car.lower() == 'audi')
# print(car)

# requested_topping = 'anchovies'
# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")

# age = 19
# print(age<=21)
# print(age>=21)

# age_0 = 22
# age_1 = 18
# age_1 = 22
# print((age_0 >= 21) and (age_1 >=21))

# age_0 = 22
# age_1 = 18
# print(age_0>=21 or age_1>=21)

# requested_toppings=['mushroom','onions','pipeapple']
# print('mushrooma' in requested_toppings)

# banned_users = ['andrew','carolina','david']
# user = 'marie'
# if user not in banned_users:
#     print(f"{user.title()},you can post a response if you wish.")
# age = 17
# if age >= 18:
#     print("You are old enough to vote!")
#     print("Have you registered to vote yet?")
# else:
#     print("Sorry,you are too young to vote.")
#     print("Please register to vote as soon as you turn 18!")

# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# else:
#     price = 20

# print(f"Your admission cost is ${price}.")

# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# elif age >= 65:
#     price = 20

# print(f"Your admission cost is ${price}.")

# requested_toppings = ['mushrooms','green peppers','extra cheese']
# for requested_topping in  requested_toppings:
#     if  requested_topping == "green peppers":
#         print("sorry,we are out of green peppers right now.")
#     else:
#         print(f"Adding {requested_topping}.")
# print("\nFinished making your pizza!")

# requested_toppings = []
# if requested_toppings:
#     for request_topping  in  requested_toppings:
#         print(f"Adding {requested_topping}.")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

# available_toppings = ['mushroom','olives','green peppers','pepperoni','pineapple','extra cheese']
# requested_toppings = ['mushroom','french fries','extra cheese']
# for  requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"Adding {requested_topping}.")
#     else:
#         print(f"Sorry,we don't have {requested_topping}.")
# print("\nFinished making your pizza!")

# alien_0 = {'color':'green','point':5}
# # print(alien_0['color'])
# # print(alien_0['point'])
# new_points = alien_0['point']
# print(f"You just earned {new_points} points!")

# alien_0 = {'color':'green','point':5}
# alien_0['x_position']=0
# alien_0['y_position']=25
# print(alien_0)

# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['point'] = 5
# print(alien_0)

# alien_0 = {'x_position':0,
#             'y_position':25,
#             'speed':'medium'}
# print(f"Original x-position:{alien_0['x_position']}")

# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3

# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New x-position:{alien_0['x_position']}")

# alien_0 = {'color':'green','points':5}
# del alien_0['points']
# print(alien_0)

# favorite_languages = {
#     'jen':'python',
#     'sarah':'c',
#     'edward':'ruby',
#     'phil':'python',
# }
# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# alien_0 = {'color':'green','speed':'slow'}
# point_value = alien_0.get('points','No point value assigned.')
# print(point_value)

# alien_0 = {'color':'green','speed':'slow'}
# point_value = alien_0.get('points')
# print(point_value)

# user_0 = {
#     'username':'efermi',
#     'first':'enrico',
#     'last':'fermi',
# }

# for key,value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

# for name,language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# for name in favorite_languages.keys():
#     print(name.title())
# friends = ['phil','sarah']
# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}.")
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()},I see you love {language}!")
# if 'erin' not in favorite_languages.keys():
#     print("Erin,please take our poll!")

# for name in  sorted(favorite_languages.keys()):
#     print(f"{name.title()},thank you for taking the poll.")

for language in favorite_languages.values():
    print(language.title())
    
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

print("The following languages have been mentioned:")
for language in  set(favorite_languages.values()):      #set去重
    print(language.title())
    
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

aliens = []

for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if  alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
    print(alien)

for alien in  aliens[:5]:
    print(alien)

print(".........")

print(f"Totle number of  aliens:{len(aliens)}")

pizza = {
          'crust':'thick',
          'topping':['mushrooms','extra cheese'], 
        }
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings.")

for  topping in  pizza['topping']:
    print("\t" + topping)

favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}

for name,languages in  favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
        
users = {
     'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
     },
     'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
     }
}

for  username,user_info in users.items():
    print(f"\nUsername:{username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name:{full_name.title()}")       ###要在循环内部
    print(f"\tLocation:{location.title()}")         ###要在循环内部
#print(sum(range(1,101)))

# message = "Hello python world!"
# print(message)

# message = "Hello python Crash Course world!"
# print(message)
#
# name = "ada lovelace"
# print(name.title())
# print(name.upper())
# print(name.lower())

# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"
# print(full_name)
# print("Python")
# print("\tPython")
# print("\nPython")
# print("Languages:\n\tPython\n\tC\n\tJavaScript")

# favorite_language = 'python '
# print(favorite_language.rstrip())
# favorite_language = ' python'
# print(favorite_language.lstrip())
# favorite_language = ' python '
# print(favorite_language.strip())
# message = "One of Python's strengths is its diverse community."
# print(message)
# universe_age = 14_000_000_000
# print(universe_age)
# x = 0
# y = 1
# z = 2
# print(x)
# print(y)
# print(z)
# x,y,z = 0,1,2
# print(x)
# print(y)
# print(z)

# MAX_CONNECTIONS = 5000
# MAX_CONNECTIONS = 4000
# print(MAX_CONNECTIONS)

# # 向大家问好。
# print("hello everyone!")

# import this

# message = input("Tell me something, and i will repeat it back to you:")
# print(message)

# name = input("Please enter your name:")
# print(f"\nHello,{name}!")

# prompt="If you tell us who you are,we can personalize the messages you see."
# prompt+="\nWhat is your first name?"
# name = input(prompt)
# print(f"\nHello,{name}!")

# age = input("How old are you?")
# print(int(age)>=18)

# height=input("How tall are you,in inches?")
# height=int(height)
# if height>=48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")
# print(7%3)
# number=input("Enter a number,and I'll tell you if it's even or odd:")
# number=int(number)
# if number%2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")
# current_number = 1
# while current_number<=5:
#     print(current_number)
#     current_number+=1
# prompt="\nTell me something,and I will repeat it back to you:"
# prompt+="\nEnter 'quit' to end the program."
# message=""
# while message!='quit':
#     message=input(prompt)
#
#     # if message!='quit':
#     #    print(message)
#     if message=='quit':
#        break
# prompt="\nTell me something,and I will repeat it back to you:"
# prompt+="\nEnter 'quit' to end the program."
# active=True
# while active:
#     message=input(prompt)
#     if message=='quit':
#         #while循环不再运行
#         active=False
#     else:
#         print(message)
# prompt="\nTell me something,and I will repeat it back to you:"
# prompt+="\nEnter 'quit' to end the program."
# while True:
#     city=input(prompt)
#     if city=='quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")
# current_number=0
# while current_number<10:
#     #current_number=current_number+1
#     current_number+=1
#     if current_number%2==0:
#         continue
#     print(current_number)
# x=1
# while x<=5:
#     print(x)
#     x+=1
# unconfirmed_users=['alice','brian','candace']
# confirmed_users=[]
# while unconfirmed_users:
#     current_user=unconfirmed_users.pop()
#     print(f"Verifying user:{current_user.title()}")
#     confirmed_users.append(current_user)
# #显示所有已验证的用户
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user)
# pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

# responses={}
# polling_active=True
# while polling_active:
#     name=input("\nWhat is your name?")
#     mountain_name=input("Which mountain would you like to climb someday?")
#     responses[name]=mountain_name
#     repeat=input("Would you like to let another person response?(yes/no)")
#     if repeat=='no':
#         polling_active=False
# #调查结束，显示结果
# print("\n---Poll Results----")
# for name,mountain_name in responses.items():
#     print(f"{name} would like to climb {mountain_name}.")

# def greet_user():
#     """显示简单的问候语"""
#     print("Hello!")
# greet_user()

# def greet_user(username):
#     """显示简单的问候语"""
#     print(f"Hello,{username.title()}!")
# greet_user("zhangsan")

# def describe_pet(animal_type,pet_name):
#     """显示宠物的信息"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet('hamster','harry')
# describe_pet('dog','whillie')

# def describe_pet(animal_type,pet_name):
#     """显示宠物的信息"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet(animal_type='hamster',pet_name='harry')

# def describe_pet(pet_name,animal_type='dog'):
#     """显示宠物的信息"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet(pet_name='willie')

# def get_formatted_name(first_name,last_name):
#     """返回整洁的姓名"""
#     full_name=f"{first_name} {last_name}"
#     return full_name.title()
# musician=get_formatted_name('jimi','hendrix')
# print(musician)

# def get_formatted_name(first_name,middle_name,last_name):
#     """返回整洁的姓名"""
#     full_name=f"{first_name} {middle_name} {last_name}"
#     return full_name.title()
# musician=get_formatted_name('john','lee','hooker')
# print(musician)

def get_formatted_name(first_name,last_name,middle_name=''):
    """返回整洁的姓名"""
    #检查是否提供了中间名
    if middle_name:
        full_name=f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician=get_formatted_name('jimi','hendrix')
print(musician)

musician=get_formatted_name('john','hooker','lee')
print(musician)
