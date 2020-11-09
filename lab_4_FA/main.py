states = []
transitions = []
the_alphabet = []
initial_state = ''
set_of_final_states = []

with open('FA.in') as f:
    for count, line in enumerate(f):
        if count == 0:  # read states
            states = line.split(', ')
        elif count == 1:  # read the alphabet
            the_alphabet = line.split(', ')
        elif count == 2:  # read initial state
            initial_state = line
        elif count == 3:  # read final state
            elems = line.split()
        else:  # add transitions
            transitions.append(line.split())

while True:
    print("1. Print states: \n")
    print("2. Print transitions:  \n")
    print("3. Print the alphabet: \n")
    print("4. Print initial state: \n")
    print("5. Set of final states: \n")
    print("6. Exit!.")

    item = str(input('Choose an element from the menu: '))
    if item == '1':
        print(str(states))
    elif item == '2':
        print(str(transitions))
    elif item == '3':
        print(str(the_alphabet))
    elif item == '4':
        print(str(initial_state))
    elif item == '5':
        print(str(set_of_final_states))
    else:
        break


