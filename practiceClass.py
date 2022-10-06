'''Create two class definitions

1) a Play class that has attributes for
id, name, number of seats, date and status. Set the value of
the status attribute to True as default. Create an accessor
method each for the name, seats and status attributes only. 
Create a method called 'seats_left' that will reduce the 
number of seats by 1 every time it is called.
Create a mutator method called 'set_status' that will
change the status attribute to False.

2) a Booking class that has attributes for customer name and
seat number. Create accessor methods for both attributes.'''
        
import csv



class Play: 
    def __init__(self,id,name,date): 
        self.Identification = id
        self.Name = name
        self.Seats = 0
        self.Date = date
        self.Status = True

    def get_name(self): 
        self.Name()

    def get_seats(self):
        return self.Seats

    def get_status(self):
        return self.Status

    def seats_left(self,Seats):
        for x in Seats:
            x = x - 1
        return x 
    def set_status(self):
        self.Status = False
        return self.Status


class Booking(Play): 
    def __init__(self,name,seat_number):
        #self.Name = name
        #self.Seat_number = seat_number
        Play.__init__(self,name)
        self.seat_number = seat_number

    def get_names(self):
        return self.Name
        
    def get_seat_number(self):
        return self.seat_number


        










