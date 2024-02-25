class Passenger:
    def __init__(self, name, ticket_information, passport, arrival_status):
        self.passengerName = name
        self.ticketInformation = ticket_information
        self.boardingPassticket = None
        self.passengerPassport = passport
        self.arrivalStatus = arrival_status #This function will show the statue of the passenger whether they have arrived to the airport or no

    def setPassengerName(self, name): #Here it will set the passenger's name
        self.passengerName = name
        return self

    def getPassengerName(self): #Here it will retrive and return the passenger's name
        return self.passengerName

    def setTicketInformation(self, ticket_information): # Here it will set the ticket infromation
        self.ticketInformation = ticket_information
        return self

    def getTicketInformation(self):#Here it will retrive and return the ticket's information
        return self.ticketInformation

    def setPassengerPassport(self, passport): # Here it will set the passenger's passport
        self.passengerPassport = passport
        return self

    def confirmPassengerArrival(self, arrival_status):#Here it will confirm the passneger's arrival
        self.arrivalStatus = arrival_status

    def __str__(self):
        return f"Passenger Name: {self.passengerName}, Ticket Information: {self.ticketInformation}, Passport: {self.passengerPassport}, Arrival Status: {self.arrivalStatus}"
class Staff:
    def __init__(self, name, role, arrival_status):
        self.staffName = name
        self.staffRole = role
        self.arrivalStatus = arrival_status

    def setStaffName(self, name):
        self.staffName = name

    def getStaffName(self):
        return self.staffName

    def setStaffRole(self, role):
        self.staffRole = role

    def getStaffRole(self):
        return self.staffRole

    def confirmPassengerArrival(self, arrival_status):
        self.arrivalStatus = arrival_status

    def __str__(self):
        return f"Staff Name: {self.staffName}, Role: {self.staffRole}, Arrival Status of the customer: {self.arrivalStatus}"

class AirportSystem:
    def __init__(self):
        self.passengerInformation = []
        self.passengerTicket = []
        self.boardingPassTicket = []

    def displayPassengerInformation(self):
        # This is supposed to display the passenger information
        pass

    def displayPassengerTicket(self):
        # This is supposed to display the passenger ticket
        pass

    def displayBoardingPass(self):
        # This will display the boarding pass information
        pass

    def confirmPassengerArrival(self, arrival_status):
        # This will confirms whether the passenger has arrived mentioned before in the passenger attribute
        pass

    def setPassengerInformation(self, passenger_information):
        self.passengerInformation.append(passenger_information)

    def setPassengerTicket(self, ticket_information):
        self.passengerTicket.append(ticket_information)

    def setBoardingPassTicket(self, boarding_pass_ticket):
        self.boardingPassTicket.append(boarding_pass_ticket)


class BoardingPass:
    def __init__(self, flightDetails, passengerDetails, departureLocation, arrivalLocation, scheduledDepartureTime, scheduledArrivalTime, boardingPassTicket):
        self.flightDetails = flightDetails
        self.passengerDetails = passengerDetails
        self.departureLocation = departureLocation
        self.arrivalLocation = arrivalLocation
        self.scheduledDepartureTime = scheduledDepartureTime
        self.scheduledArrivalTime = scheduledArrivalTime
        self.boardingPassTicket = boardingPassTicket

    def setFlightDetails(self, flight):
        self.flightDetails = flight

    def setPassengerDetails(self, passenger):
        self.passengerDetails = passenger

    def setDepartureLocation(self, departureLocation):
        self.departureLocation = departureLocation

    def setArrivalLocation(self, arrivalLocation):
        self.arrivalLocation = arrivalLocation

    def setScheduledDepartureTime(self, scheduledDepartureTime):
        self.scheduledDepartureTime = scheduledDepartureTime

    def setScheduledArrivalTime(self, scheduledArrivalTime):
        self.scheduledArrivalTime = scheduledArrivalTime

    def setBoardingPassTicket(self, passengerName, passengerSeat, passengerSeatType, passport):
        self.boardingPassTicket = {
            "passengerName": passengerName,
            "passengerSeat": passengerSeat,
            "passengerSeatType": passengerSeatType,
            "passport": passport
        }

    def setBoardingPassTicketType(self, boardingPassTicketType):
        self.boardingPassTicketType = boardingPassTicketType

#Objects:
# Creating the Passenger
passenger1 = Passenger("Zainab Alareefi", "332211", "125RFD", False)

# Creating the Staff
staff1 = Staff("Budoor Albraiki", "Staff Check In", False)

# Creaing an instance of AirportSystem
airport_system = AirportSystem()


airport_system.setPassengerInformation({
    "Name of the passenger" : passenger1.getPassengerName(),
    "Passport of the passenger is": passenger1.getTicketInformation(),
    "The arrival Status of the passenger is": passenger1.arrivalStatus
})

# This will set the passenger ticket
ticket_info = {"The ticker number of the passenger ": "5A6BCD78", "The passenger's destination": "New York"}
airport_system.setPassengerTicket(ticket_info)

# This will set the boarding pass ticket
boarding_pass_info = {"Gate number in the ticket is": "Gate1", "seat number in the ticket is": "A23"}
airport_system.setBoardingPassTicket(boarding_pass_info)

# Here it will display all the infromation
print(passenger1)
print(staff1)
print(airport_system.passengerInformation)
print(airport_system.passengerTicket)
print(airport_system.boardingPassTicket)

# Creating an instance of the BoardingPass some attributes are already mentioned in the passenger1
boarding_pass1 = BoardingPass(
    flightDetails="Flight123",
    passengerDetails="Zainab Alareefi",
    departureLocation="Airport A",
    arrivalLocation="Airport B",
    scheduledDepartureTime="12:00 PM",
    scheduledArrivalTime="2:00 PM",
    boardingPassTicket=None  
)

# Seting more information so it can print the whole output
boarding_pass1.setBoardingPassTicket(
    passengerSeat="A23",
    passengerSeatType="Economy"
)