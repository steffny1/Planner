#import tkinter module to create GUI and datetime module to count number of days
from tkinter import Tk, Canvas
from datetime import date, datetime

#function to get events from external text file
def get_events():
    list_events = []
    with open('events.txt')as file: #open text file
        for line in file: #run the loop for each line in the text file
            line = line.rstrip('\n') #remove the newline character from each line
            current_event = line.split(',') #split each event into two parts as the comma
            event_date = datetime.strptime(current_event[1],'%d/%m/%y').date() #turn the second item in the list from a string into a date
            current_event[1] = event_date #set the second item in the list to be the date of the event
            list_events.append(current_event) #loop back to read the next line from the text file
    return list_events #return complete list of events to the program

#function that counts the number of days between two dates
def days_between_dates(date1, date2):
    time_between =  str(date1 - date2) #convert date into a string
    number_of_days = time_between.split(' ') #split the string at each blank space
    return number_of_days[0] #since number of days is held at position 0 in the list, return 


root = Tk() #create a window
c = Canvas(root, width=800,height=800, bg='purple') #create a canvas
c.pack() #pack the canvas into the window
# add text onto the canvas
c.create_text(100, 50, anchor='w', fill='yellow', \
font='Arial 28 bold underline', text='My Planner.')

events = get_events() #call the get_events() function
today = date.today() #get today's date

vertical_space = 100 #spread out the text displayed on the screen
events.sort(key=lambda x: x[1]) #sort the list of events in order of days to go, and not by the name of the events

#calculate the number of days until each event and display the results on the screen
for event in events:
    event_name = event[0] #get the name of the event
    days_until = days_between_dates(event[1], today) #calculate the number of days between the event and today's date
    display = 'It is %s days until %s' % (days_until, event_name) #display this statement on the screen
    if (int(days_until)<=7): #display event in red if event is happening next week
        text_col = 'red'
    else:
        text_col = 'white'

    #display the text on screen at this position    
    c.create_text(100, vertical_space, anchor='w', fill=text_col, \
                  font='Arial 20 bold', text=display)
    vertical_space = vertical_space + 30



    






