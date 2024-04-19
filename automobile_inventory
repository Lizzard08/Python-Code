# Automobile Inventory
# Liz Nelson
# ITS 320-2
# Final Project - 7/10/22
# This program is a simple inventory program that creates a new car object as a dictionary
# and saves it to a list. It gives the option for the user to print the final inventory list to a file.

class Automobile_Inventory:

    def __init__(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def add_vehicle(self):
        make = input("Enter make: ")
        model = input("Enter model: ")
        color = input("Enter color: ")
        
        if make.isdigit() or model.isdigit() or color.isdigit():
            raise ValueError('Invalid entry')
        
        year = input("Enter year: ")
        mileage = input("Enter mileage: ")
        
        if (not year.isdigit()) or (not mileage.isdigit()):
            raise ValueError('Invalid entry')

        new_vehicle = Automobile_Inventory(make, model, color, year, mileage)
        vehicles[n] = {'Make:':make, 'Model:':model, 'Color:':color, 'Year:':year, 'Mileage:':mileage}
        n += 1
            

    def remove_vehicle(self):
        make = input('Enter the make: ')
        model = input('Enter the model: ')
        
        if make.isdigit() or model.isdigit():
            raise ValueError('Invalid entry')

        if make in vehicles:
            models = vehicle[make]
            if model == vehicle[0][models]:
                del vehicles[make]
        else:
            print('Could not find vehicle')
                

    def update_vehicle(self):
        update = input('What would you like to update:')

        if update == 'make':
            make = input('Enter updated make: ')
            vehicles.update({'Make': make})
        elif update == 'model':
            model = input('Enter updated model: ')
            vehicles.update({'Model': model})
        elif update == 'color':
            color = input('Enter updated color: ')
            vehicles.update({'Color': color})
        elif update == 'year':
            year = input('Enter updated year: ')
            vehicless.update({'Year': year})
        elif update == 'mileage':
            mileage = input('Enter updated mileage: ')
            vehicle.update({'Mileage': mileage})
        else:
            print('Cannot find information, please try again.')

def main():
    veichles = []
    n = 0
    user_input = True

    
    print('1. Add a vehicle')
    print('2. Remove a vehicle')
    print('3. Update a vehicle')
    print('4. Print inventory to file')
    print('5. Exit')
    user_selection = input('Select an option:')


    while user_input:
        try:
            if user_selection == '1':
                Automobile_Inventory.add_vehicle()
            elif user_selection == '2':
                Automobile_Inventory.remove_vehicle()
            elif user_selection == '3':
                Automobile_Inventory.update_vehicle()
            elif user_selection == '4':
                file = open("my_cars.txt", "w")
                for i in range(len(Automobile_Inventory)):
                    file.write(str(Automobile[i]))
                file.close()
            elif user_selection == '5':
                break
            else:
                print('Unexpected Error...')
                break

        except (IOError, TypeError, SyntaxError):
            print('Something went wrong...')
            break

if __name__ == "__main__":
    main()
