from dao.createTables import createTables
from dao.addCar import addVehicle
from dao.addCustomer import addCustomer
from dao.createLease import createLease
from dao.recordPayment import recordPayment
from dao.listAvailableCars import listAvailableCars
from dao.listRentedCars import listRentedCars
from dao.findCarsByID import findCarsByID
from dao.listCustomer import listCustomers
from dao.findCustomerByID import findCustomerByID
from dao.listLeaseHistory import listLeaseHistory
from dao.removeCar import removeCar
from dao.removeCustomer import removeCustomer
from dao.updateCarInfo import UpdateCarAvailability
from dao.paymentAmount import paymentHistory
if __name__=="__main__":
    try:
        print("\n-----------------MAIN MENU------------------------")
        print("\nEnter 1 for car management")
        print("\nEnter 2 for customer management")
        print("\nEnter 3 for lease management")
        print("\nEnter 4 for payment management")
        while(1>0):
            ch=input("\nEnter your choice from main menu: ")
            if ch=='1':
                print("\nCAR MANAGEMENT")
                print("\nEnter 1 to add new car")
                print("\nEnter 2 to remove car")
                print("\nEnter 3 to list available cars")
                print("\nEnter 4 to list rented cars")
                print("\nEnter 5 to find cars by ID")
                print("\nEnter 6 to Update car Availabitity")
                while(1>0):
                    c=input("\nEnter Choice: ")
                    if c=='1':
                        addVehicle()
                    elif c=='2':
                        removeCar()
                    elif c=='3':
                        listAvailableCars()
                    elif c=='4':
                        listRentedCars()
                    elif c=='5':
                        findCarsByID()
                    elif c=='6':
                        UpdateCarAvailability()
                    elif c=='7':
                        break
            elif ch=='2':
                print("\nCUSTOMER MANAGEMENR\n")
                print("\nEnter 1 to add new customer")
                print("\nEnter 2 to remove customer")
                print("\nEnter 3 to list customers")
                print("\nEnter 4 to find cars by ID")
                while(1>0):
                    c=input("\nEnter Choice: ")
                    if c=='1':
                        addCustomer()
                    elif c=='2':
                        removeCustomer()
                    elif c=='3':
                        listCustomers()
                    elif c=='4':
                        findCustomerByID()
                    elif c=='5':
                        break
            elif ch=='3':
                print("\nLEASE MANAGEMENR\n")
                print("\nEnter 1 to create new Lease")
                print("\nEnter 2 to List lease history")
                print("\nEnter 3 to list customers")
                while(1>0):
                    c=input("\nEnter Choice: ")
                    if c=='1':
                        createLease()
                    elif c=='2':
                        listLeaseHistory()
                    elif c=='3':
                        break
            elif ch=='4':
                print("\nPAYMENT MANAGEMNET\n")
                print("\nEnter 1 to record new Payment")
                print("\nEnter 2 to retrive payment history")
                print("\nEnter 3 to exit")
                while(1>0):
                    c=input("\nEnter Choice: ")
                    if c=='1':
                        recordayment()
                    elif c=='2':
                        paymentHistory()
                    elif c=='3':
                        break
            elif ch=='5':
                break
            else:
                print("Invalid Choice")

    except Exception as E:
        print(f"\nAn error has occured: {E}")