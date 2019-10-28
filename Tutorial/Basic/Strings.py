msg = "Hello world"
print(msg)          #prints the message

print(msg[0])       #prints the first letter in the string

print(len(msg))     #length of message

print(msg[0:5])     #prints 0 to 4 index
print(msg[:5])      #automatically assumes start at index 0
print(msg[6:])      #prints the last word
print(msg.lower())  #prints msg in lowercase, upper() for uppercase

print(msg.count('o'))  #prints the count of o's in msg
print(msg.find('world'))  #prints the index where world starts

new_message = msg.replace("world", "bro")       #replace world with bro
print(new_message)

greeting = "Hello"
name = "Earl"
message = greeting + ', ' + name
print(message)
message = "{}, {}. My bro!".format(greeting, name)      #formatting strings
print(message)

message = f"{greeting}, {name}. My Fstring!"
print(message)


                    #to see what else you can do with a string pass it to the directory
print(dir(message))

                    #to see what it does
print(help(str))
print(help(str.lower))


helloworld = "Hello world"
print("Hello" in helloworld)
