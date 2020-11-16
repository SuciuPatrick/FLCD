states = []
transitions = []
the_alphabet = []
initial_state = ''
set_of_final_states = []


class Transition:
    def __init__(self, initial, to, end):
        self.initial = initial
        self.to = to
        self.end = end

    def __str__(self):
        return f"{self.initial} -> {self.to} -> {self.end}\n"


with open('FA.in') as f:
    for count, line in enumerate(f):
        if count == 0:  # read states
            states = line.split(', ')
        elif count == 1:  # read the alphabet
            the_alphabet = line.split(', ')
        elif count == 2:  # read initial state
            initial_state = line
        elif count == 3:  # read final state
            set_of_final_states = line.split()
        else:  # add transitions
            values = line.split()
            transitions.append(Transition(values[0], values[1], values[2]))


def valid_sequence(sequence):
    actual_state = initial_state.strip()

    for character in sequence:
        print(actual_state, item)
        ok = False
        for transition in transitions:
            if transition.to == character and actual_state == transition.initial:
                ok = True
                print(transition)
                actual_state = transition.end
                import pdb;
                pdb.set_trace()
                break

        if not ok:
            return False

    if actual_state in set_of_final_states:
        return True
    return False


while True:
    print("1. Print states: \n")
    print("2. Print transitions:  \n")
    print("3. Print the alphabet: \n")
    print("4. Print initial state: \n")
    print("5. Set of final states: \n")
    print("6. Check sequence.")

    item = str(input('Choose an element from the menu: '))
    if item == '1':
        print(str(states))
    elif item == '2':
        for transition in transitions:
            print(transition)
    elif item == '3':
        print(str(the_alphabet))
    elif item == '4':
        print(str(initial_state))
    elif item == '5':
        print(str(set_of_final_states))
    elif item == '6':
        sequence = str(input("Example: r t c\nSequence: "))
        if valid_sequence(sequence.split()):
            print("Valid!")
        else:
            print("Invalid!")
    else:
        break


