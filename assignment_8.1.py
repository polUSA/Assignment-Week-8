class Vehicle:
    def __init__ (self, make, model, color, fuelType, options):
        '''
        initialize instances variables
        '''
        self.make = make
        self.model = model
        self.color = color
        self.fuelType = fuelType
        self.options = options
    def getMake(self):
        return self.make  
    def getModel(self):
        return self.model   
    def getColor(self):
        return self.color
    def getFuelType(self):
        return self.fuelType   
    def getOptions(self):
        return self.options

class Car(Vehicle):
    def __init__(self, make, model, color, fuelType, options, engineSize, numDoors):
        super().__init__(make, model, color, fuelType, options)
        self.engineSize = engineSize
        self.numDoors = numDoors
    
    def getEngineSize(self):
        return self.engineSize

    def getNumDoors(self):
        return self.numDoors

class Pickup(Vehicle):
    def __init__(self, make, model, color, fuelType, options, cabStyle, bedLength):
        super().__init__(make, model, color, fuelType, options)
        self.cabStyle = cabStyle
        self.bedLength = bedLength
    
    def getCabStyle(self):
        return self.cabStyle
    
    def getBedLength(self):
        return self.bedLength

# create a list of vehicles (user's garage)
vehicles = list()

# create two options package the user can choose from
options_1 = [
        'power mirrors', 'power locks', 'remote start', 'backup camera',
        'bluetooth', 'cruise control', 'apple car play', 'full led light']

options_2 = ['power mirrors', 'power locks', 'remote start', 'backup camera',
        'bluetooth', 'adaptive cruise control', 'android auto - apple car play',
        'leather seats', 'self-parking radar']


def make_vehicle(choice):
    '''
    Ask user for vehicle details before register it to their garage
    '''    
    make = input('\nPlease enter the make of your vehicle: ')
    model =  input('Please enter the model of your vehicle: ')
    color = input('Please enter the color of your vehicle: ')
    fuelType =  input('Please enter fuel type of your vehicle: ')
    
    # Show user optional packages available
    print('\nPackage 1:', options_1)
    print('Package 2:', options_2)
    
    # ask user to choose between package 1 or 2
    while True:
        package = input('Please enter \'1\' for Package 1, or \'2\' for Package 2: ')
        if package == '1':
            options = options_1
            break
        elif package == '2':
            options = options_2
            break
        else:
            print('Invalid option. Enter 1 or 2.')
            continue

    # attributes are different if it is car or a pickup
    if choice.lower() == 'c' : 
        engineSeize = input('Please enter engine size in cc: ')
        numDoors = input('Please enter the number of doors: ')
        return Car(make, model, color, fuelType, options, engineSeize, numDoors)
    elif choice.lower() == 'p':
        cabStyle = input('Please enter the cabStyle of your pickup: ')
        bedLength = input('Please enter the bed length of your pickup in ft: ')
        return Pickup(make, model, color, fuelType, options, cabStyle, bedLength)

    
# main function that launches the "garage"
def garage():
    print('Welcome to your Garage.')
    print('To exit the garage enter \'quit\' at any time.')
    while True:
        choice = input('To add a car enter \'c\', to add a pickup enter \'p\': ')
        if choice.lower() == 'quit': break
        if choice.lower() == 'p' or choice.lower() == 'c':
            vehicle = make_vehicle(choice)
            # add a car or pickup to the garage 
            vehicles.append(vehicle)
            done = input('Would you like to add another vehicle? enter \'y\' for yes: ')
            if done.lower() == 'y': continue
            else: 
                break
        else:
            print('\nPlease enter a valid option (\'c\' or \'p\'): ')
            continue

# start the garage program
garage()

# print garage
print('\nYour garage has these vehicles: ')

# here I used the range function to print a number for each vehicle (1, 2, 3, etc) for styling purposes
for i in range(len(vehicles)):
    print(f'Vehicle #{i+1}: ')
    # using vehicles.items() did not work. The traceback said the object was not iterable
    # reference: https://stackoverflow.com/questions/25150955/python-iterating-through-object-attributes
    for attr, value in vehicles[i].__dict__.items():
        if isinstance(value, list):
            # It may be a bit convoluted, but to print the options (that is a list) I had to add another for loop with a conditional
            print(f'\t Options: ', end=' ')
            for option in value:
                print(f'{option.title()}', end=', ')
            # add an empty line after the last iteration of options
            print()
        else:
            print(f'\t {attr.title()}: {value.title()}')

