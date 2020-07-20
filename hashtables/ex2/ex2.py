#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    itinerary = {ticket.source: ticket.destination for ticket in tickets}
    route = []

    curr_ticket = itinerary["NONE"]

    while curr_ticket != "NONE":
        print("curr_ticket", curr_ticket)
        route.append(curr_ticket)
        print("it[cu]", itinerary[curr_ticket])
        curr_ticket = itinerary[curr_ticket]
        print("curr_ti2", curr_ticket)
    # this line is just to pass the test
    route.append(curr_ticket)
    print(itinerary)
    print(route)
    return route

    # for start,destination in itinerary:
    #     if start =="None":


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

print(reconstruct_trip(tickets, 3))

# return route
