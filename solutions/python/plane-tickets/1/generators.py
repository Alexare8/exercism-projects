"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D
    """
    i = 0
    while i < number:
        yield ["A", "B", "C", "D"][i % 4]
        i += 1


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B
    """
    seats = 0
    row = 1
    letters = generate_seat_letters(number)
    while seats < number:
        yield f'{row}{next(letters)}'
        seats += 1
        if seats % 4 == 0:
            row += 1
        if row == 13:
            row += 1

    
def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    assignments = {}
    seats = generate_seats(len(passengers))
    for passenger in passengers:
        assignments.update({passenger: next(seats)})
    return assignments
    

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        ticket_number = seat + flight_id
        ticket_number += "0" * (12 - len(ticket_number))
        yield ticket_number