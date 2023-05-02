import random

def list_value():
    state_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
                    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
                    "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
                    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia",
                    "Washington", "West Virginia", "Wisconsin", "Wyoming"]
    print(state_of_america[5])

    #change a spelling from the list
    state_of_america[1] = 'Aleska'
    print(state_of_america)

    #add a new value to the list
    state_of_america.append('india')
    print(state_of_america)

    #add multiple values to the list
    state_of_america.extend(['pakistan', 'china'])
    print(state_of_america)

    name_string = input("what are the names that you would like to provide")
    print(name_string)
    names = name_string.split(", ")
    print(names)
    num_items = len(names)
    vales = random.randint(0, num_items - 1)
    print(vales)
    choice = names[vales]
    print(f"person who is going to pay:- {choice}")