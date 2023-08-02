# Excpetion handling is used in situations where errors may arise during exwcutionof our programs
# try-except-finally
try:
    x = int(input("Enter a number:"))
    y = int(input("Enter a number:"))
    result = x/y
    print("My output is", result)
except ZeroDivisionError:
    print("Zero Division Error")
except TypeError:
    print("TypeError occurred in your input")
except ValueError:
    print("ValueError occurred in your input")   
except Exception as e:
   print("An error occurred")  
finally:
    print("Am always printed")

#Custom exceptions
#class-try-except
class MyException(Exception):
    pass
try:
    player_age= int(input("Enter player age:"))
    if not (15<=player_age<=22):
        raise MyException("Player is not eligible to participate in the world cup")
except MyException as me:
    print("My exception occurred:",str(me))
except Exception as e:
    print("Exception occurred:",str(e))
     
#File handling
file_path = 'myfile.txt'

# Writing to a file
with open(file_path, 'w') as file:
    file.write('My name is Bindya Philip')

print("File created and content written successfully.")
#reading a file
with open('myfile.txt', 'r') as file:
    content = file.read()
    print(content)
#Appending(adding more content to the file)
with open('myfile.txt','a') as file:
    file.write( ",I am a football fan and i spent all my childhood playing football before i was sent into early retirement")
    print("Your content has be added to the file")
#Error handling in files
try:
    file = open('file.txt', 'r')
    filecontent = file.read()
    print(filecontent)
except FileNotFoundError:
    print('File not found.')
finally:
    file.close()



