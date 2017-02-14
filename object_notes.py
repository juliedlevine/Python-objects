# list attributes of any object
# dir(object)
string = "hello, my name is Julie."
dir(string)

# get info on a certain method
# help(object.method)
help(string.uppercase)

# Make a class - classes are capitalized
class Person(object):
    # Always add self as first parameter in class methods
    def greet(self):
        print 'Hello'

# Make an instance of a person object
janice = Person()

# Call greet method on Janice instance / Person object. Outputs hello
janice.greet()

# Constructor - set instance variables, these variables can be used in later methods
class Person(object):
    def __init__(self, name):
        self.name = name

    def greet(self, other_person):
        print 'Hello %s, I am %s' % (other_person.name, self.name)
janice = Person("Janice")
kareem = Person("Kareem")
janice.greet(kareem)

# Example:
    class Hello(object):
        def __init__(self):
            self.count = 0

        def count_hello(self):
            print "Hello"
            self.count += 1

# Objects as records
class Contact(object):
    def __init__(self, first_name, last_name, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

contact = Contact("Janice", "LaGrange", "jancie@yahoo.com", "202-444-2521")

contact.last_name
