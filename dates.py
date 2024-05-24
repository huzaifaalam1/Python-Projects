'''
File: dates.py
Author: Syed Muhammad Huzaifa Alam
Course: CSC-120
Purpose: This program reads a file
        with dates with related events.
        It returns dates and the events
        in a specific format. 
'''
class Date:
    '''
    A class to represent a date and associated events.
    '''
    def __init__(self, date, event):
        '''
        Initialize a Date object.

        Args:
            date: The date in string format.
            event: The initial event associated with the date.
        '''
        self._date = date
        self._events = [event]
    
    def add_event(self, event):
        '''
        Add an event to the list of events for this date.

        Args:
            event: The event to be added
        '''
        self._events.append(str(event))
        
    def get_date(self):
        '''
        Get the date associated with this Date object.

        Returns:
            str: The date in string format
        '''
        return self._date
    
    def get_events(self):
        '''
        Get the list of events associated with this Date object.

        Returns:
            list: A list of events.
        '''
        return self._events
    
    def __str__(self):
        '''
        Get a string representation of this Date object.

        Returns:
            str: A string representation containing the date and associated events
        '''
        events_str = ""
        for event in self._events:
            events_str += event + ', '
        events_str = events_str[:-2] 
        return str(self._date) + ': ' + events_str
    
class DateSet:
    '''
    A class to represent a set of dates and their associated events.
    '''
    def __init__(self):
        '''
        Initialize an empty DateSet object.
        '''
        self._dates = {}

    def add_date(self, date, event):
        '''
        Add a date and its associated event to the DateSet.

        Args:
            date: The Date object to add.
            event: The event associated with the date.
        '''
        self._dates[date._date] = date

    def get_date(self, date):
        '''
        Get the Date object associated with a specific date.

        Args:
            date: The date in string format.

        Returns:
            Date: The Date object associated with the given date.
        '''
        return self._dates[date]

    def get_dict(self):
        '''
        Get a dictionary representation of the DateSet.

        Returns:
            dict: A dictionary where keys are dates and values are Date objects.
        '''
        return self._dates
    
    def __str__(self):
        '''
        Get a string representation of the DateSet.

        Returns:
            str: A string representation of the DateSet in the required format.
        '''
        string = '{'
        i = 1
        for key in self._dates:
            if i != len(self._dates):
                string += "'" + key + "': '" + str(self._dates[key]) + "',"
                i += 1
            else:
                string += "'" + key + "': '" + str(self._dates[key]) + "'}"
        return string
    
def canonicalize_date(date_str):
    '''
    The function converts the date into
    the 'yyyy-mm-dd' format using if statements
    and slicing. 
    Parameters: a string date
    Returns: a formatted string
    '''
    date_list = date_str.replace("-", " ").replace("/", " ").split(" ")
    
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    len_of_date_list = len(date_list[0])
    # Check the length of the first element for format of the date
    if len_of_date_list == 4:
        yyyy = date_list[0]
        mm = date_list[1]
        dd = date_list[2]
    elif len_of_date_list == 3:
        index = 1
        for month in months:
            # Check if the first element is a month abbreviation
            if date_list[0] == month or index == " ":
                yyyy = date_list[2]
                mm = index
                dd = date_list[1]
                break
            else:
                index += 1
    # Day first format
    else:
        dd = date_list[1]
        mm = date_list[0]
        yyyy = date_list[2]

    return "{:d}-{:d}-{:d}".format( int(yyyy ), int(mm), int(dd))

def convert_to_date(file):
    '''
    The function takes a file, stores it and 
    creates a set/object of DateSet class, and the Date
    class. The function calls the above function and put 
    the date in required format. The function then
    provides output as mentioned in the assignment.
    '''
    lines = file.read().split("\n")
    dates = DateSet()

    for line in lines:
        if line != "":
            # Remove extra spaces from the line
            line = " ".join(line.split())
            # Get the operation type
            oper_type = line[0][0]

            if oper_type == "R":
                # Split the line at the first colon
                line = line.split(":", 1)
                # Get date information
                date_info = line[0].strip("I ").strip("R ")
                # Canonicalize the date format
                date_info = canonicalize_date(date_info)
                # Check if the date exists in the DateSet
                if date_info in dates.get_dict():
                    date_object = dates.get_date(date_info)
                    # Get the list of events for the date
                    events = date_object.get_events()
                    events.sort()
                    for event in events:
                        print ("{}: {}".format(date_info, event))

            elif oper_type == "I":
                # Split the line at the first colon
                line = line.split(":", 1)
                # Get date information
                date_info = line[0].strip("I ").strip("R ")
                date_info = canonicalize_date(date_info)
                # Get event information
                event_info = line[1].strip(" ")
                if date_info not in dates.get_dict():
                    current_date = Date(date_info, event_info)
                    # Add the Date object to the DateSet
                    dates.add_date(current_date, event_info)
                else:
                    current_date = dates.get_dict()[date_info]
                    # Add the event to the Date object
                    current_date.add_event(event_info)
                    dates.add_date(current_date, event_info)

            else:
                print("Error - Illegal operation.")

def main():
    file = input()
    filename = open(file,'r')
    convert_to_date(filename)
    filename.close()

main()
