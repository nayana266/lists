message = 'Hello world'
print(message)
print(len(message))
print(message[0])
print(message[0:5])
print(message[6:])
print(message.find('World'))

new_message = message.replace('World', 'Universe')
print(new_message)

greeting = 'Hello'
name = 'Michael'
message = greeting + ',' + name + '. Welcome!'
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)