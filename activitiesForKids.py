# Define four Python functions named run, swing, slide, and hide_and_seek.
#  Each function should take varying number of children's names as the argument.

# For example, the run function would be defined as follows:


def run(*kids):
# Loop through all the kids and print that the child performed the activity.
    for kid in kids: 
        print(f"{kid} ran!")
run("Pam", "Sam", "Andrea", "Will")

# Do the same for the following children:
# Swinging kids: Marybeth, Ariel, Kevin, Courtney
# Sliding kids: Mike, Jack, Jennifer, Earl
# Hiding kids: Henry, Heather, Hayley, Hugh

def swing(*kids):
    for kid in kids: 
        print(f"{kid} swung!")

swing("Marybeth", "Ariel", "Kevin", "Courtney")


def slide(*kids):
    for kid in kids: 
        print(f"{kid} slid!")
slide("Mike", "Jack", "Jennifer", "Earl")

def hide(*kids):
    for kid in kids: 
        print(f"{kid} hid!")
hide("Henry", "Heather", "Hayley", "Hugh")


