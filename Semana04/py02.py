message = 'Hello World'
print(message)

message = 'Bob\'s World'
print(message)

message = "Bob's World"
print(message)

message = """Bobbys's World
was a Good Cartoon"""
print(message)

print(len(message))

print(message[0])
print(message[32])
print(message[0:8])
print(message[:8])
print(message[8:])

message = 'Hello World'

print(message.lower())
print(message.upper())
message = 'Hello World'
print(message.count('Hello'))
print(message.count('l'))

print(message.find('World'))

print(message.replace('World', 'Universe'))

print(message)

greeting = 'Hello'
name = 'Michael'

message = greeting + ' ' + name + '. Welcome!'
print(message)

message = '{} {}. Welcome!'.format(greeting, name)
print(message)

message = f'{greeting} {name}. Welcome!'
print(message)

message = f'{greeting} {name.upper()}. Welcome!'
print(message)

print(dir(message))

#print(help(type(message)))
#print(help(str.lower))


