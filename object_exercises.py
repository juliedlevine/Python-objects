# Basics
class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.count = 0
        self.greeted_set = set()

    def __repr__(self):
        return '<Person: %s, %s, %s>' % (self.name, self.email, self.phone)

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.count += 1
        self.greeted_set.add(other_person.name)

    def greeting_count(self):
        print self.count

    def num_unique_people_greeted(self):
        print len(self.greeted_set)

    def print_contact_info(self):
        print "%s's email: %s, %s's phone number: %s." % (self.name, self.email, self.name, self.phone)

    def add_friend(self, new_friend):
        self.friends.append(new_friend)

    def num_friends(self):
        print len(self.friends)


sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
sally = Person("Sally", "sally@aol.com", "245-324-3411")

jordan.greet(sonny)
jordan.greet(sonny)
jordan.greet(sonny)
jordan.greet(sally)

jordan.num_unique_people_greeted()


# Make your own class
# class Vehicle(object):
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def print_info(self):
#         print "%s %s %s" % (self.make, self.model, self.year)
#
# car = Vehicle("Nissan", "Leaf", 2015)
# car.print_info()
