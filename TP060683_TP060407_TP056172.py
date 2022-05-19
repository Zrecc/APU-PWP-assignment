# CHAI YAO YANG # TP060683
# IVAN TAN YEN CHONG # TP060407
# ONG CHEE HOONG # TP056172


import os
import time
from datetime import date, timedelta

AIRLINE_TEXT_FILE = "airline.txt"
ADMIN_CREDENTIALS_TEXT_FILE = "adminCredentials.txt"
BOOKING_TEXT_FILE = "booking.txt"
MEMBER_TEXT_FILE = "member.txt"
CURRENT_YEAR = 2021
FLIGHT_TEXT_FILE = "flight.txt"
CASE_TEXT_FILE = "case.txt"
CASE_ANSWER_TEXT_FILE = "case answer.txt"

def _login(user_type, filename):
    print("Login Page\n"
          "Please enter only alphabets or numbers. No spacing allowed.")
    print("-" * 70)

    username = input("Enter your username: ")
    pwd = input("Enter your password: ")
    if bool(username) and bool(pwd):      # to ensure there is value inputted by user
        handle = open(filename, 'r')
        for x in handle:
            x = x.rstrip()
            txt = x.split("|")
            if txt[0] == username and txt[1] == pwd:
                print("Login Successful")
                if user_type == "Admin":
                    return txt[0]
                elif user_type == "Member":
                    id = txt[2].lstrip("Member ID:")
                    return id
            else:
                continue
    else:
        return None


def _display_menu():
    o3 = int(0)
    while o3 < 1 or o3 > 4:
        print("Display ALL records of\n"
              "---------------------------\n"
              "1. Flight Schedules\n"
              "2. Flight Booked\n"
              "3. Total Ticket Sold\n"
              "4. Go Back\n")
        o3 = int(input("Enter your option: "))
        if o3 == 1:
            schedule = []
            handle = open(FLIGHT_TEXT_FILE, "r")

            for x in handle:
                x = x.rstrip()
                x = x.split("|")
                schedule.append(x)

            for select in range(1, 100, 1):
                if select < 10:
                    planenum = "Flight Number:AB0" + str(select)
                else:
                    planenum = "Flight Number:AB" + str(select)

                for x in schedule:
                    if planenum in x[0]:
                        print(f"[{planenum}]")
                        for e in schedule:
                            if planenum in e[0]:
                                print(e)
                            continue
                        break

            option = -1
            while option < 0 or option > 1:
                option = int(input("Enter 0 to go back previous page or enter 1 to exit the program: "))
                if option == 0:
                    _display_menu()
                elif option == 1:
                    _exitscreen()
                else:
                    print("Invalid input, Please try again!")
            handle.close()
        elif o3 == 2:
            count = int(0)
            handle = open(BOOKING_TEXT_FILE, 'r')
            print("\nRecord of all Flight booked by customer")
            for flight in handle:
                flight = flight.rstrip()
                txt = flight.split("|")
                count += 1
                print("\n")
                for x in txt[0:13]:
                    print(x)
            if count != 0:
                result = "\nTotal {count:d} records found\n"
                print(result.format(count=count))
            else:
                print("\nNo records found\n")

            option = -1
            while option < 0 or option > 1:
                option = int(input("Enter 0 to go back previous page or enter 1 to exit the program: "))
                if option == 0:
                    _display_menu()
                elif option == 1:
                    _exitscreen()
                else:
                    print("Invalid input, Please try again!")
            handle.close()
        elif o3 == 3:
            handle = open(BOOKING_TEXT_FILE,'r')
            print("Total Ticket Sold")

            booking = []
            for x in handle:
                x = x.rstrip()
                txt = x.split("|")
                booking.append(txt)
            handle.close()

            count = 0
            money = 0
            for e in booking:
                if "Payment Status:Paid" in e:
                    count += 1
                    e = e[10].lstrip("Flight Price:RM")
                    money += int(e)
            print("Total tickets sold: ", count)
            print("Up-to-date profits earned : RM", money)

            option = -1
            while option < 0 or option > 1:
                option = int(input("Enter 0 to go back previous page or enter 1 to exit the program: "))
                if option == 0:
                    _display_menu()
                elif option == 1:
                    _exitscreen()
                else:
                    print("Invalid input, Please try again!")

        elif o3 == 4:
            _admin_menu()
        else:
            print("Invalid input, Please try again!")


def _add_flight():
    print("Add New Flight\n"
          "--------------")
    i = []
    flight_number = (input("Flight Number: "))
    i.append("Flight Number:" + flight_number + "|")
    depart_from = (input("Depart From: "))
    i.append("Depart From: " + depart_from + "|")
    depart_at = (input("Depart to: "))
    i.append("Depart to: " + depart_at + "|")
    date = (input("Depart date: "))
    i.append("Depart date: " + date + "|")
    time = (input("Depart time: "))
    i.append("Depart time: " + time + "|")
    return_from = (input("Return From: "))
    i.append("Return From: " + return_from + "|")
    return_to = (input("Return To: "))
    i.append("Return To: " + return_to + "|")
    return_date = (input("Return date: "))
    i.append("Return date: " + return_date + "|")
    return_time = (input("Return time: "))
    i.append("Return time: " + return_time + "|")
    flight_price = (input("Flight Price: "))
    i.append("Flight Price:" + flight_price + "|")
    confirm = str(input("Are you sure you want to add?\n"
                        "Enter Y for yes:\n"))
    confirm = confirm.upper()
    if confirm == "Y":

        add_flight = open(FLIGHT_TEXT_FILE,"a")
        add_flight.write("\n")
        for flight in i:
            add_flight.write(flight)
        add_flight.close()
        print("The Flight is Added")
        _admin_menu()

    else:
        print("Save is not successful")
        _admin_menu()


def _modify_flight():
    print("Modify Flight Details\n"
          "------------------\n")
    flightid  = str(0)
    while True:
        try:
            flightid = str(input("Please enter a Flight Number: "))
        except ValueError:
            print("Please enter a valid Flight Number")
            continue
        else:
            break

    flight_list = []
    handle = open(FLIGHT_TEXT_FILE, "r")
    for flight in handle:
        flight = flight.rstrip()
        flight_list.append(flight)
    handle.close()

    search_result_index = int(0)
    found = False
    for x in flight_list:
        if len(x) > 1:
            temp = x.split("|")
            id = temp[0].lstrip("Flight Number:")
            id = str(id)
            if id == flightid:
                found = True
                search_result_index = flight_list.index(x)
    if not found:
        print("Result not found, Please check the Flight Number")
        _admin_menu()
    else:
        print("Modify Flight Details")
        print("\n<Search Result>")
        flight = flight_list[search_result_index].split("|")
        for x in flight:
            print(x)

        c_option = str(input("\nDo you want to modify this Flight details? (Enter Y for Yes, Anykey for No): "))
        c_option = c_option.upper()

        if c_option == "Y":
            print("Modify Flight Details")
            print("\nFlight Number: " + str(flightid))

            flight_number = "AB" + str(input("Enter the New Flight Number:AB "))

            depart_from = str(input("Enter the new place: "))

            depart_to = str(input("Enter the new place: "))

            depart_date = str(input("Enter the new Date: "))

            depart_time = str(input("Enter the new time: "))

            return_from = str(input("Enter the new place: "))

            return_to = str(input("Enter the new place: "))

            return_date = str(input("Enter the new Date: "))

            return_time = str(input("Enter the new Time: "))

            price = str(input("Enter the new price: "))

            print("Modify Flight Details confirmation")
            result = str("Flight Number: {0}\n"
                         "Depart From: {1}\n"
                         "Depart to: {2}\n"
                         "Depart date: {3}\n"
                         "Depart time: {4}\n"
                         "Return From: {5}\n"
                         "Return To: {6}\n"
                         "Return date: {7}\n"
                         "Return time: {8}\n"
                         "Flight Price: {9}\n")
            print(result.format(str(flight_number),depart_from, depart_to,depart_date, depart_time,return_from,return_to,
                                return_date,return_time,price))

            c_option = str(input("Do you really want make the changes? (Enter Y for Yes, Anykey for No): "))
            c_option = c_option.upper()
            if c_option == "Y":
                new_changes = "Flight Number:" + str(flight_number) + "|" + "Depart From:" + depart_from + "|" + "Depart to:" + depart_to + "|" + \
                              "Depart date:" + depart_date + "|" + "Depart time:" + depart_time + \
                              "|" + "Return From:" + return_from + "|" + "Return To:" + return_to + \
                              "|" + "Return date:" + return_date + \
                              "|" + "Return time:" + return_time + "|" + "Flight Price:RM" + price + "|"
                flight_list[search_result_index] = new_changes

                handle = open(FLIGHT_TEXT_FILE, "w")
                for x in flight_list:
                    handle.write(x)
                    handle.write("\n")
                handle.close()
                print("Successfully modified the Flight's details")
                _admin_menu()
            else:
                print("Modify process was cancelled")
                _admin_menu()
        else:
            _admin_menu()


def _admin_menu():
    ot1 = 0
    while ot1 < 1 or ot1 > 4:
         print("Admin Portal\n"
              "--------------------------\n"
              "1. Add Flight Schedule\n"
              "2. Modify Flight Details\n"
              "3. Display all records\n"
              "4. Exit")

         ot1 = int(input("Enter your option: "))
         if ot1 == 1:
            _add_flight()
         elif ot1 == 2:
            _modify_flight()
         elif ot1 == 3:
            _display_menu()
         elif ot1 == 4:
            _exitscreen()
         else:
            print("Invalid input, Please try again!")


def _exitscreen():
    print("Thank you for using our system")
    exit(0)

def _Online_Checkin(user):
    print("-" * 35)
    print("Online Check In Portal")

    allbook = []
    checkin_list = []
    handle = open(BOOKING_TEXT_FILE, "r")
    for x in handle:
        x = x.rstrip()
        x = x.split("|")
        allbook.append(x)
        if "Member ID:" + user in x:
            while "Payment Status:Paid" in x and "Check in:No" in x:
                    checkin_list.append(x)
                    break
    handle.close()

    num = 0
    for e in checkin_list:
        print("-" * 35)
        print(f"Check in no. [{num + 1}]")
        print("-" * 35)
        num += 1
        for y in e[0: 12]:
            print(y)

    if num != 0:
        while True:
            try:
                print("-" * 35)
                select_checkin = int(input("Select the check in no. that you want to check in\n"
                                           "Enter the number in the ( [?] ): "))

                if select_checkin < 1 or select_checkin > num:
                    print("Please select the available booking number only.")

                else:
                    print("-" * 35)
                    confirm = str(input("Are you sure you want to check in\n"
                                        "(Enter Y for Yes, Anykey for No): "))

                    confirm = confirm.upper()
                    if confirm == "Y":
                        location = allbook.index(checkin_list[select_checkin - 1])
                        allbook[location][12] = "Check in:Yes"
                        handle = open(BOOKING_TEXT_FILE, "w")
                        for x in allbook:
                            for e in x[0: 13]:
                                handle.write(e)
                                handle.write("|")
                            handle.write("\n")
                        handle.close()

                        print("Your check in is confirmed. Thank you!")
                        time.sleep(2.0)
                        _member_menu(user)

                    else:
                        print("Check in cancelled.")
                        time.sleep(2.0)
                        _member_menu(user)

            except ValueError:
                print("Please enter number only.")

    else:
        print("\nYou don't have any flight to check in\n")
        time.sleep(2.0)
        _member_menu(user)


def _Membership_Points(user):
    print("-" * 35)
    print("My Membership points")
    print("-" * 35)

    handle = open(BOOKING_TEXT_FILE, "r")
    point = 0
    for e in handle:
        e = e.rstrip()
        e = e.split("|")
        if "Member ID:" + user in e:
            if "Class:Economy" in e and "Payment Status:Paid" in e:
                    point += 50
                    print(f"Class:Economy, point + 50 {e[0], e[2], e[10]}")

            elif "Class:Premium" in e and "Payment Status:Paid" in e:
                    point += 100
                    print(f"Class:Premium, point + 100 {e[0], e[2], e[10]}")
    print("My membership points: ", point)
    handle.close()

    while True:
        print("-" * 25)
        print("Option\n"
              "0. Go back previous page\n"
              "1. Exit the program")
        print("-" * 25)
        try:
            option = int(input("Enter your option: "))
            if option < 0 or option > 1:
                print("Invalid input, please enter number 0 or 1 only!")
            if option == 0:
                _member_menu(user)
            elif option == 1:
                _exitscreen()
        except ValueError:
            print("Invalid input, please enter number 0 or 1 only!")


def _Create_Case(user):
    print("-" * 35)
    print("Create case for any enquiries, requests, and feedback")
    print("-" * 35)

    caseid = _get_new_case_id()
    id = "Member ID:" + user

    while True:
        print("Option\n"
              "0. Create a case\n"
              "1. Go back previous page")
        print("-" * 25)
        try:
            option = int(input("Enter your option: "))
            if option < 0 or option > 1:
                print("Invalid input, please enter number 0 or 1 only!")
            if option == 0:
                print("Enter your enquiries, requests, or feedback")
                content = input("Enter here: ")
                confirmation = str(input("Are you sure you want to create the case? \n"
                                        "(Enter Y for Yes, Anykey for No): "))

                confirmation = confirmation.upper()
                if confirmation == "Y":
                    handle = open(CASE_TEXT_FILE, "a")
                    caseline = "\nCase ID:" + str(caseid) + "|" + str(id) + "|" + "Case:" + str(content)
                    handle.write(caseline)
                    handle.close()

                    print("Your case is created, go back to previous page in 3 seconds")
                    time.sleep(3.0)
                    _member_menu(user)

                else:
                    print("The case is not saved, go back to previous page in 3 seconds")
                    time.sleep(3.0)
                    _member_menu(user)

            elif option == 1:
                _member_menu(user)

        except ValueError:
            print("Invalid input, please enter number 0 or 1 only!")

def _Manage_Case(user):
    print("-" * 35)
    print("Manage the cases created by customer")
    print("-" * 35)

    while True:
        print("Option\n"
              "0. Provide answer to the case\n"
              "1. Go back previous page")
        print("-" * 25)
        try:
            option = int(input("Enter your option: "))
            print("-" * 35)
            if option < 0 or option > 1:
                print("Invalid input, please enter number 0 or 1 only!")
            if option == 0:

                casenum = 0
                allcase = []
                allcase_ans = []
                handle = open(CASE_TEXT_FILE, "r")
                handle1 = open(CASE_ANSWER_TEXT_FILE, "r")

                for row in handle1: # save the case answer to the list
                    row = row.rstrip()
                    row = row.split("|")
                    allcase_ans.append(row)
                for x in handle:  # save the cases to the list
                    x = x.rstrip()
                    x = x.split("|")
                    allcase.append(x)
                    casenum += 1

                    for e in x:  # display the cases
                        print(e)
                        for i in allcase_ans:  # check is there any suitable answer or not
                            if i[0] == e:
                                print("Previous answer: ", i) # print the found answer
                    print("-" * 35)
                handle.close()
                handle1.close()

                while True:
                    try:
                        print("Enter the case id you want to answer.")
                        caseid = int(input("Case ID: "))
                        if caseid < 0 or caseid > casenum:
                            print("Enter the available CASE ID only.")
                        else:
                            answer = input("Enter you answer here: ")

                            confirmation = str(input("Are you sure you want to answer the case? \n"
                                                     "(Enter Y for Yes, Anykey for No): "))
                            confirmation = confirmation.upper()
                            if confirmation == "Y":
                                caseid = "Case ID:" + str(caseid)
                                memid = "Member ID:" + str(user)
                                formatanswer = "Answer:" + str(answer)

                                answerline = "\n" + str(caseid) + "|" + str(memid) + "|" + str(formatanswer)

                                handle = open(CASE_ANSWER_TEXT_FILE, "a")
                                handle.write(answerline)
                                handle.close()

                                print("Your answer is saved, back to previous page in 2 seconds.")
                                time.sleep(2.0)
                                _member_menu(user)

                            else:
                                print("Your answer is not saved, back to previous page in 2 seconds.")
                                time.sleep(2.0)
                                _member_menu(user)

                    except ValueError:
                        print("Enter number only.")

            elif option == 1:
                _member_menu()

        except ValueError:
            print("Enter number only.")


def _Make_Payment(user):
    print("-" * 35)
    print("Make Payment")

    booking_list = []
    handle = open(BOOKING_TEXT_FILE, "r")
    for booking in handle:
        booking = booking.rstrip()
        txt = booking.split("|")
        booking_list.append(txt)
    handle.close()

    unpaid_list = []
    for x in booking_list:
        if len(x) > 1:
            temp = x
            status = temp[11].lstrip("Payment Status:")
            mid = temp[1].lstrip("Member ID:")
            if status == "Unpaid" and mid == str(user):
                unpaid_list.append(x)

    num = 0
    for e in unpaid_list:
        print("-" * 35)
        print(f"Booking no. [{num + 1}]")
        print("-" * 35)
        num += 1
        for y in e[0: 13]:
            print(y)

    if num != 0:
        while True:
            try:
                print("-" * 35)
                select_booking = int(input("Select the booking no. that you want to make payment\n"
                                           "Enter the number in the ( [?] ): "))

                if select_booking < 1 or select_booking > num:
                    print("Please select the available booking number only.")

                else:
                    print("-" * 35)
                    print("Thank you for choosing us! Please kindly make the payment by CDM or Online Banking\n"
                          "Bank Account: 150689870698\n"
                          "Bank: Malayan Banking Berhad (MayBank)\n"
                          "Account Holder: Super Airline Reservations System (ARS)")
                    print("-" * 35)
                    confirmation = str(input("Have you transfer the payment to our account?\n"
                                             "(Enter Y for Yes, Anykey for No): "))

                    confirmation = confirmation.upper()
                    if confirmation == "Y":
                        location = booking_list.index(unpaid_list[select_booking - 1])
                        booking_list[location][11] = "Payment Status:Paid"
                        handle = open(BOOKING_TEXT_FILE, "w")
                        for x in booking_list:
                            for e in x[0: 13]:
                                handle.write(e)
                                handle.write("|")
                            handle.write("\n")
                        handle.close()

                        print("We received your payment, your booking is confirmed. Thank you!")
                        time.sleep(2.0)
                        _member_menu(user)

                    else:
                        print("Transaction cancelled, Please make the payment ASAP")
                        time.sleep(2.0)
                        _member_menu(user)

            except ValueError:
                print("Please enter number only")

    else:
        print("\nYou don't have any unpaid booking\n")
        time.sleep(2.0)
        _member_menu(user)


def _Add_Flight_Booking(user):
    memberid = user
    print("Make a booking\n"
          "----------------")
    handle = open(FLIGHT_TEXT_FILE, "r")
    count = 0
    print("Record of all airlines that are available")

    allflight = []
    result_list = []  # this list only store the plane id
    for airline in handle:
        airline = airline.rstrip()
        count += 1
        txt = airline.split("|")
        result_list.append(txt[0])  # only take the plane id
        allflight.append(txt)

        print("-" * 35)
        for x in txt:
            print(x)

    handle.close()

    if count != 0:
        print("-" * 25)
        print(f"Total {count} records found")
        print("-" * 25)
        flinum = input("Please insert the flight number that you want to book.\nFlight Number: ")
        print("-" * 25)
        if ("Flight Number:" + flinum) in result_list:
            print("Please select the flight details")
            id = _get_new_booking_id()

            # below is the plane details selection
            while True:
                try:
                    print("-" * 35)
                    print("Ticket type\n"
                          "1. One way ticket\n"
                          "2. Return ticket")
                    tictype = int(input("Please choose your ticket type: "))

                    if tictype < 1 or tictype > 2:
                        print("-" * 35)
                        print("Invalid input, please enter number 1 or 2 only!")
                    elif tictype == 1:
                        tictype = "One way ticket"
                        break
                    elif tictype == 2:
                        tictype = "Return ticket"
                        break
                except ValueError:
                    print("-" * 35)
                    print("Invalid input, please enter number 1 or 2 only!")

            while True:
                try:
                    print("-" * 35)
                    print("Class type\n"
                          "1. Economy\n"
                          "2. Premium")
                    class1 = int(input("Please choose your cLass type: "))

                    if class1 < 1 or class1 > 2:
                        print("-" * 35)
                        print("Invalid input, please enter number 1 or 2 only!")
                    elif class1 == 1:
                        class1 = "Economy"
                        break
                    elif class1 == 2:
                        class1 = "Premium"
                        break
                except ValueError:
                    print("-" * 35)
                    print("Invalid input, please enter number 1 or 2 only!")

            while True:
                try:
                    print("-" * 35)
                    print("Passenger type\n"
                          "1. Child\n"
                          "2. Adult")
                    passen = int(input("Please choose the passenger type: "))

                    if passen < 1 or passen > 2:
                        print("-" * 35)
                        print("Invalid input, please enter number 1 or 2 only!")
                    elif passen == 1:
                        passen = "Child"
                        break
                    elif passen == 2:
                        passen = "Adult"
                        break
                except ValueError:
                    print("-" * 35)
                    print("Invalid input, please enter number 1 or 2 only!")

            while True:
                try:
                    print("-" * 35)
                    print("Seatings\n"
                          "1. Random\n"
                          "2. Window\n"
                          "3. Aisle\n"
                          "4. Extra legroom")
                    seat = int(input("Please choose your seating: "))

                    if seat < 1 or seat > 4:
                        print("-" * 35)
                        print("Invalid input, please enter number 1 to 4 only!")
                    elif seat == 1:
                        seat = "Random"
                        break
                    elif seat == 2:
                        seat = "Window"
                        break
                    elif seat == 3:
                        seat = "Aisle"
                        break
                    elif seat == 4:
                        seat = "Extra legroom"
                        break
                except ValueError:
                    print("-" * 35)
                    print("Invalid input, please enter number 1 to 4 only!")

            while True:
                try:
                    print("-" * 35)
                    print("Cabin baggage\n"
                          "1. Yes\n"
                          "2. No")
                    cabinbag = int(input("Do you need cabin baggage?: "))

                    if cabinbag < 1 or cabinbag > 2:
                        print("-" * 35)
                        print("Invalid input, please enter number 1 or 2 only!")
                    elif cabinbag == 1:
                        cabinbag = "Yes"
                        break
                    elif cabinbag == 2:
                        cabinbag = "No"
                        break
                except ValueError:
                    print("-" * 35)
                    print("Invalid input, please enter number 1 or 2 only!")

            while True:
                try:
                    print("-" * 35)
                    print("Checked baggage\n"
                          "1. Yes\n"
                          "2. No")
                    checkedbag = int(input("Do you need checked baggage?: "))

                    if checkedbag < 1 or checkedbag > 2:
                        print("-" * 35)
                        print("Invalid input, please enter number 1 or 2 only!")
                    elif checkedbag == 1:
                        checkedbag = "Yes"
                        break
                    elif checkedbag == 2:
                        checkedbag = "No"
                        break
                except ValueError:
                    print("-" * 35)
                    print("Invalid input, please enter number 1 or 2 only!")
            while True:
                try:
                    print("-" * 35)
                    print("Insurance\n"
                          "1. Yes\n"
                          "2. No")
                    insurance = int(input("Do you need insurance?: "))

                    if insurance < 1 or insurance > 2:
                        print("-" * 35)
                        print("Invalid input, please enter number 1 or 2 only!")
                    elif insurance == 1:
                        insurance = "Yes"
                        break
                    elif insurance == 2:
                        insurance = "No"
                        break
                except ValueError:
                    print("-" * 35)
                    print("Invalid input, please enter number 1 or 2 only!")

            for i in allflight:
                if "Flight Number:" + flinum in i:
                    fliprice = str(i[9])

            print("Booking confirmation\n")
            result = str(f"Booking ID: {id}\n"
                         f"Member ID: {memberid}\n"
                         f"Flight Number: {flinum}\n"
                         f"Ticket Type: {tictype}\n"
                         f"Class: {class1}\n"
                         f"Passenger Type: {passen}\n"
                         f"Seatings: {seat}\n"
                         f"Cabin Baggage: {cabinbag}\n"
                         f"Checked Baggage: {checkedbag}\n"
                         f"Insurance: {insurance}\n"
                         f"{fliprice}")

            print(result)
            c_option = str(input("Do you really want to make this booking? (Enter Y for Yes, Anykey for No): "))
            c_option = c_option.upper()
            if c_option == "Y":
                handle = open("booking.txt", "a")
                write_line = "\nBooking ID:" + str(id) + "|" + "Member ID:" + str(memberid) + "|" + "Flight Number:" + \
                             flinum + "|" + "Ticket Type:" + str(tictype) + "|" + "Class:" + \
                             str(class1) + "|" + "Passenger Type:" + str(passen) + "|" + "Seatings:" + str(seat) + "|" + \
                             "Cabin Baggage:" + str(cabinbag) + "|" "Checked Baggage:" + str(checkedbag) + "|" + \
                             "Insurance:" + str(insurance) + "|" + str(fliprice) + "|" \
                             + "Payment Status:Unpaid" + "|" + "Check in:No"

                handle.write(write_line)
                handle.close()

                print("Booking Made Successfully\n"
                      "But your booking is not confirm yet, Please make the payment ASAP to confirm your booking")
                time.sleep(3.0)

                _member_menu(user)
            else:
                print("Booking cancelled")
                time.sleep(2.0)
                _member_menu(user)
        else:
            print("Invalid Flight Number, Please try again")
            time.sleep(2.0)
            _member_menu(user)
    else:
        print("No flight is available right now, Please try again tomorrow")
        time.sleep(2.0)
        _member_menu(user)

def _View_Available_Flight_Non_Member():
    print("All available airline schedules\n"
          "----------------")
    handle = open(FLIGHT_TEXT_FILE, "r")
    count = 0
    print("Record of all airlines that are available")

    allflight = []
    result_list = []  # this list only store the plane id
    for airline in handle:
        airline = airline.rstrip()
        count += 1
        txt = airline.split("|")
        result_list.append(txt[0])  # only take the plane id
        allflight.append(txt)

        print("-" * 35)
        for x in txt:
            print(x)

    option = -1
    while option < 0 or option > 1:
        option = int(input("Enter 0 to go back previous page\n"
                           "Enter 1 to exit the program: "))
        if option == 0:
            _visitor_menu()
        elif option == 1:
            _exitscreen()
        else:
            print("Invalid input, Please try again!")
    handle.close()

def _Search_Available_Flight_Non_Member():
    print("Search airline\n"
          "----------------")
   # obtain input, add the missing part with string
    fromp = "Depart From: " + input("Depart from: ")
    top = "Depart to: " + input("Depart to: ")
    datedepart = "Depart date: " + input("Date departure: ")
    datereturn = "Return date: " + input("Date return: ")

    print("----------------\n"
          "Result\n"
          "----------------")
    count = 0
    handle = open("flight.txt", "r")  # check in the file
    for flightlist in handle:
        flightlist = flightlist.rstrip()
        flightlist = flightlist.split("|")
        if (fromp in flightlist) and (top in flightlist) and (datedepart in flightlist) \
                and (datereturn in flightlist):
            count += 1
            for element in flightlist:
                print(element)  # break it to small
    if count == 0:
        print("No airline found")
    handle.close()

    option = -1
    while option < 0 or option > 1:
        option = int(input("Enter 0 to go back previous page\n"
                           "Enter 1 to exit the program: "))
        if option == 0:
            _visitor_menu()
        elif option == 1:
            _exitscreen()
        else:
            print("Invalid input, Please try again!")


def _View_My_Booking(user):
    handle = open(BOOKING_TEXT_FILE, 'r')
    id = "Member ID:" + user
    count = 0
    print("View my booking\n"
          "-----------------------")
    for booking in handle:
        booking = booking.rstrip()
        if id in booking:
            x = booking.split("|")
            txt = x[0: 13]
            count += 1
            for x in txt:
                print(x)
            print("-" * 30)
    if count != 0:
        print(f"Total {count} records found\n")

    else:
        print("\nNo records found\n")
    handle.close()

    while True:
        try:
            print("-" * 25)
            print("Option\n"
                  "0. Go back previous page\n"
                  "1. Exit the program")
            print("-" * 25)
            option = int(input("Enter your option: "))
            if option < 0 or option > 1:
                print("Invalid input, Please try again!")
            if option == 0:
                _member_menu(user)
            elif option == 1:
                _exitscreen()
        except ValueError:
            print("Invalid input, please enter number 0 or 1 only!")


def _View_My_Profile(user):
    handle = open(MEMBER_TEXT_FILE, 'r')
    id = "Member ID:" + user

    print("View Personal Details\n"
          "-----------------------")

    for members in handle:
        members = members.rstrip()
        if id in members:
            txt = members.split("|")
            username = txt[0]
            wpwd = txt[2: 9]  # skip the password, it is not shown
            print("Username:", username)
            for x in wpwd:
                print(x)
    if x is None:
        print("Something goes wrong, Please restart the system")
    handle.close()

    while True:
        print("-" * 25)
        print("Option\n"
              "0. Go back previous page\n"
              "1. Exit the program")
        print("-" * 25)
        try:
            option = int(input("Enter your option: "))
            if option < 0 or option > 1:
                print("Invalid input, please enter number 0 or 1 only!")
            elif option == 0:
                _member_menu(user)
            elif option == 1:
                _exitscreen()
        except ValueError:
            print("Invalid input, please enter number 0 or 1 only!")


def _get_new_booking_id():
    booking_list = []
    handle = open(BOOKING_TEXT_FILE, "r")
    for booking in handle:
        booking = booking.rstrip()
        booking_list.append(booking)
    handle.close()

    latest = 0
    for x in booking_list:
        if len(x) > 1:
            temp = x.split("|")
            id = temp[0].lstrip("Booking ID:")
            id = int(id)
            if id > latest:
                latest = id

    return latest + 1


def _get_new_member_id():
    members_list = []
    handle = open(MEMBER_TEXT_FILE, "r")
    for member in handle:
        member = member.rstrip()
        members_list.append(member)
    handle.close()

    latest = int(0)
    for x in members_list:
        if len(x) > 1:
            temp = x.split("|")
            id = temp[2].lstrip("Member ID:")
            id = int(id)
            if id > latest:
                latest = id

    return latest + 1


def _get_new_case_id():
    case_list = []
    handle = open(CASE_TEXT_FILE, "r")
    for x in handle:
        x = x.rstrip()
        case_list.append(x)
    handle.close()

    latest = 0
    for x in case_list:
        if len(x) > 1:
            temp = x.split("|")
            id = temp[0].lstrip("Case ID:")
            id = int(id)
            if id > latest:
                latest = id

    return latest + 1


def _modify_personal_detail(user):
    memberid = "Member ID:" + user

    members_list = []
    handle = open(MEMBER_TEXT_FILE, "r")
    for members in handle:
        members = members.rstrip()
        members = members.split("|")
        members_list.append(members)
        if memberid in members:
            temp = members
        elif memberid is None:
            print("Something goes wrong, Please restart the system")
    handle.close()
    option = 0
    while option < 1 or option > 2:
        option = int(input("Enter 1 to change personal details\n"
                           "Enter 2 to go back previous page: "))
    if option == 1:
        print("Personal details")
        print("-" * 25)

        name = input("Enter your Name: ")
        gen = input("Enter your Gender (F = Female, M = Male): ")
        ic = input("Enter your IC Number: ")
        email = input("Enter your Email Address: ")
        phone = input("Enter you phone number: ")
        ephone = input("Enter an emergency contact number: ")

        confirm = input("Are you sure you want to save the changes? Enter Y for Yes, N for No").upper()
        chan_lin = temp
        if confirm == "Y":
            chan_lin[3] = "Name:" + name
            chan_lin[4] = "Gender:" + gen
            chan_lin[5] = "IC No:" + ic
            chan_lin[6] = "Email:" + email
            chan_lin[7] = "Phone:" + phone
            chan_lin[8] = "Emergency contact:" + ephone

            x = members_list.index(temp)
            members_list[x] = chan_lin
            handle = open(MEMBER_TEXT_FILE, "w")
            for x in members_list:
                for e in x[0: 9]:
                    handle.write(e)
                    handle.write("|")
                handle.write("\n")
            handle.close()
            print("Your changes is saved, back to member menu in 3 second.")
            time.sleep(3.0)
            _member_menu(user)

        elif confirm == "N":
            print("Modify failed, your profile details is not changed.")
            _member_menu(user)

        else:
            print("Something goes wrong, please restart the system.")
            _member_menu(user)

    if option == 2:
        _member_menu(user)

def _register_member():
    print("Register as a member\n"
          "-----------------------\n")

    username_valid = str(_check_username())
    password_valid = str(_check_password())

    id = _get_new_member_id()

    print("Your Customer ID is " + str(id))

    name = input("Enter your Name: ")
    age = input("Enter your Age: ")
    gen = input("Enter your Gender (F = Female, M = Male): ")
    ic = input("Enter your IC Number: ")
    email = input("Enter your Email Address: ")
    phone = input("Enter you phone number: ")
    ephone = input("Enter an emergency contact number: ")

    handle = open(MEMBER_TEXT_FILE, "a")
    write_line = "\n" + username_valid + "|" + password_valid + "|" + "Member ID:" + str(id) + "|" + "Name:" + \
                 name + "|" + "Gender:" + gen + "|" + "IC No:" + ic + "|" + "Email:" + email + "|" + "Phone:" + phone + \
                 "|" + "Emergency contact:" + ephone


    handle.write(write_line)
    handle.close()
    print("Register Successful\n"
          "You may log in at the Login Page")
    time.sleep(2.0)
    main()


def _check_username():
    replicate = True
    username = ""
    while replicate:
        username = input("Enter a username:")
        with open(MEMBER_TEXT_FILE, "r") as file:
            for row in file:
                row = row.rstrip()
                if username in row:
                    print("Username replicated, Please try another one")
                    username = input("Enter a username:")
                    replicate = True
                else:
                    replicate = False

    return username


def _check_password():
    password = input("Enter a password:")
    passwordC = input("Confirm password:")
    same = True
    while same:
        if password == passwordC:
            return password
        else:
            same = False
            print("Password not match, please try again!")
            password = input("Enter a password:")
            passwordC = input("Confirm password:")

    return password


def _visitor_menu():
     print("All customer portal\n"
           "-----------------------------\n"
           "1. View available Airline Schedule\n"
           "2. Search Airline\n"
           "3. Become a Member\n"
           "4. Exit\n")
     choice2 = int(input("Please select your choice: "))
     if choice2 == 1:
         _View_Available_Flight_Non_Member()
     elif choice2 == 2:
         _Search_Available_Flight_Non_Member()
     elif choice2 == 3:
         _register_member()
     elif choice2 == 4:
         main()


def _member_menu(user):
    print("Welcome Back, " + user + "\n"
                                    "--------------------------------\n"
                                    "Option\n"
                                    "1. VIEW My Profile\n"
                                    "2. VIEW My Booking\n"
                                    "3. ADD Flight booking & Select details\n"
                                    "4. MAKE Payment to confirm booking\n"
                                    "5. MODIFY My Profile\n"
                                    "6. Online Check In\n"
                                    "7. My Membership points\n"
                                    "8. CREATE case (enquiries, requests, and feedback)\n"
                                    "9. MANAGE case created by customer\n"
                                    "10. Exit")


    while True:  # to obtain int only and no kicking user
        try:
            choice = int(input("Enter your option: "))
            if choice < 1 or choice > 10:
                print("Invalid input, please enter number 1 to 10 only!")
            if choice == 1:
                _View_My_Profile(user)
            elif choice == 2:
                _View_My_Booking(user)
            elif choice == 3:
                _Add_Flight_Booking(user)
            elif choice == 4:
                _Make_Payment(user)
            elif choice == 5:
                _modify_personal_detail(user)
            elif choice == 6:
                _Online_Checkin(user)
            elif choice == 7:
                _Membership_Points(user)
            elif choice == 8:
                _Create_Case(user)
            elif choice == 9:
                _Manage_Case(user)
            elif choice == 10:
                main()
        except ValueError:
            print("Invalid input, please enter number 1 to 10 only!")


def main():
    user = None
    option = 0
    print("Welcome to our Airline Reservations System (ARS)\n"
          "-------------------------------------------------------------\n"
          "Please select a user type to enter corresponding portal.\n"
          "1. Admin\n"
          "--------------------------------------------------\n"
          "2. Member        | Log in to book flight\n"
          "--------------------------------------------------\n"
          "3. All customer  | Check/search airline schedules\n"
          "                 | Sign in to member\n"
          "--------------------------------------------------\n"
          "4. Exit\n")

    while True:
        try:
            while option < 1 or option > 4:  # set the range
                option = int(input("Enter your option: "))

                if option < 1 or option > 4:
                    print("Invalid input, please enter number 1 to 4 only!")

                elif option == 1:
                    while user is None:
                        user = _login("Admin", ADMIN_CREDENTIALS_TEXT_FILE)
                        if user is not None:
                            _admin_menu()
                        else:
                            print("Login Unsuccessful, Please check your username and password")

                elif option == 2:
                    while user is None:  # user is None or no value will keep looping
                        user = _login("Member", MEMBER_TEXT_FILE)
                        if user is not None:
                            _member_menu(user)
                        else:
                            print("Login Unsuccessful, Please check your username and password")

                elif option == 3:
                    _visitor_menu()
                elif option == 4:
                    _exitscreen()

        except ValueError:  # to obtain integer only
            print("Invalid input, please enter number 1 to 4 only!")


main()
