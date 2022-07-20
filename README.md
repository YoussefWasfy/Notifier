# Notifier
Notifier is a program for notifying people that a certain date and time is reached.
## Program
### number_of_entries()
This function takes an integer from user as input that states how many notifications will be created.
### get_d_t_from_user()
This function takes 2 inputs from the user the first one is the date to be notified on and the second one is the time to be notified on.
### calculate_and_display_dates()
This function finds the nearest date and time to the current time and calculate the difference between them, then the program sleeps until this time is reached and notify the users.
### numbers_to_ordinals(n)
This function takes as an input a number and return the ordinal form of it.
### Libraries used
* datetime
* time
## Testing
The program is tested using unit testing. There are 2 tests are normal cases and the rest of the tests are edge cases
### Libraries Used in Testing
* unittest
