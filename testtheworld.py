from random import randint
from time import sleep

successful_tests = 0
failed_tests = 0

def calculate_universe_answer():
    global successful_tests
    global failed_tests
    answer = 0
    
    print "\n> Performing extremely complicated calculations on the answer to life..."
    while answer != 42:
        answer = randint(-500000, 500000)
    
    if answer == 42:
        print "> Universe is ok."
        successful_tests += 1
    else:
        print "> Universe is not working correctly."
        failed_tests += 1

def check_maths():
    global successful_tests
    global failed_tests
    print "\n> Generating super-quantic-equations to test maths..."
    sleep(randint(3, 7))
    
    if 10 > 29:
        print "> Mathematics are not working correctly."
        failed_tests += 1
    else:
        print "> Mathematics are ok."
        successful_tests += 1

def check_people():
    global successful_tests
    global failed_tests
    print "\n> Analyzing your brain through ultrasonic waves from the PC..."
    sleep(randint(3, 7))
    
    your_opinion_about_me = "very very very handsome and intelligent"
    
    if your_opinion_about_me != "very very very handsome and intelligent":
        print "> People's minds are not working correctly."
        failed_tests += 1
    else:
        print "> People's minds are ok."
        successful_tests += 1

def check_food():
    global successful_tests
    global failed_tests
    print "\n> Retrieving food's chemical compositions database..."
    sleep(randint(3, 7))
    
    most_epic_food = "pizza"
    
    if most_epic_food != "pizza":
        print "> Food is not working correctly."
        failed_tests += 1
    else:
        print "> Food chemicals are ok."
        successful_tests += 1

def check_wozniak():
    global successful_tests
    global failed_tests
    print "\n> Comparing The Big and Powerful Woz to everyone else..."
    sleep(randint(3, 7))
    
    woz = 999999
    everyone_else = 1
    
    if not woz > everyone_else:
        print "> Steve Wozniak is not working correctly."
        failed_tests += 1
    else:
        print "> Steve Wozniak is super-ok."
        successful_tests += 1

def check_money():
    global successful_tests
    global failed_tests
    print "\n> Counting Bill Gates' money..."
    
    bills_money = 0
    all_the_money_in_the_world = 2000000000
    while bills_money < all_the_money_in_the_world:
        bills_money += 10
    
    if bills_money < all_the_money_in_the_world:
        print "> Bill Gates or the money are not working correctly."
        failed_tests += 1
    else:
        print "> All the money are in the right place."
        successful_tests += 1
    



def main():
    global successful_tests
    global failed_tests
    
    print "\n\n"
    print "Welcome to the best tool for analyzing how the world is going."
    print "Don't be afraid of when the world is gonna blow up, we will now check it.\n"
    
    raw_input("Press ENTER when you are ready to start the test...")
    
    print "\n"
    
    
    
    print "Initializing virtualized parallel universe atomic bla bla bla emulator...\n"
    sleep(randint(4,7))
    
    check_maths()
    sleep(randint(2,4))
    
    calculate_universe_answer()
    sleep(randint(2,4))
    
    check_people()
    sleep(randint(2,4))
    
    check_food()
    sleep(randint(2,4))
    
    check_wozniak()
    sleep(randint(2,4))
    
    check_money()
    sleep(randint(2,4))
    
    
    
    print "\n\n"
    
    print "The test has ended. ", successful_tests, " tests went ok and ", failed_tests, " tests have failed.\n"
    
    if failed_tests == 0:
        print "Since no tests have failed, you have not to be worried, the whole world is ok."
    elif successful_tests == 0:
        print "Wait... What?? Ehm... See you on Jupiter!"
    elif failed_tests < successful_tests:
        print "This is not a big problem, most of the tests went ok... To be sure please run this test every time you can, nobody knows when the world is gonna finish..."
    elif failed_tests >= successful_tests:
        print "Urgh... This is not very good... How about starting to look for a flat on Mars..?"
    else:
        print "If you're reading this... Neither if statements are working... And probably it is too late to escape to the Moon... Well, it's been a pleasure!"
    
    print "\n\n"
    
main()
