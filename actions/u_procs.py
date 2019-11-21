from sys import stdout

def part_of_a_day(tim):
    return (
        "Morning" if 5 <= tim <= 11
       else
        "Afternoon" if 12 <= tim <= 17
       else
        "Evening" if 18 <= tim <= 22
	   else
        "Night" if 23 <= tim <= 24	   
       else
        "Invalid Input")    