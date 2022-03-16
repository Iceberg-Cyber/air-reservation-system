from tkinter import *

root = Tk()
root.title( "Air Reservation System" )

def passenger():

    master = Tk()
    master.geometry("1000x500")
    master.title( "Air Reservation System" )

    textName = StringVar()
    textDob = StringVar()
    textPassNum = StringVar()
    textPassId = StringVar()

    Label(master, font=('comic sans ms','20','italic'),justify='center',text="Name: ").grid(row=0)
    Label(master, font=('comic sans ms','20','italic'),justify='center',text="Date Of Birth: ").grid(row=1)
    Label(master, font=('comic sans ms','20','italic'),justify='center',text="Phone Number: ").grid(row=2)
    Label(master, font=('comic sans ms','20','italic'),justify='center',text="Passenger I.D.: ").grid(row=3)

    Label(master, font=('comic sans ms','20','italic'), justify='center',text="(Example of Name input: User Name)").grid(row=15)
    Label(master, font=('comic sans ms','20','italic'), justify='center',text="(Example of Date Of Birth input: 1998-05-09) ").grid(row=16)
    Label(master, font=('comic sans ms','20','italic'), justify='center',text="(Example of Phone Number input: 8309026408) ").grid(row=17)
    Label(master, font=('comic sans ms','20','italic'), justify='center',text="(Example of Passenger I.D. input: 1234)").grid(row=18)
    Message(master, font=('comic sans ms','15','bold'),justify='center',text="*** In order to change information as a customer, you must delete your information using your passenger I.D. and input new information ***", width = 500).grid(row=30)

    name= Entry(master,font=('comic sans ms','16','italic'),justify='center', text = textName)
    dob= Entry(master, font=('comic sans ms','16','italic'),justify='center',  text = textDob)
    passNum= Entry(master, font=('comic sans ms','16','italic'),justify='center',  text = textPassNum)
    passId = Entry(master,font=('comic sans ms','16','italic'), justify='center',  text = textPassId)

    def done():

        texta = "{}".format(name.get())
        textb = "{}".format(dob.get())
        textc = "{}".format(passNum.get())
        textd = "{}".format(passId.get())
        print(texta)

        dataa = (texta, textb, textc, textd)
        print(dataa)


        #print('"{}"'.format(name.get()))
        # print(texta)

    def deletePassenger():
        deletePass = Tk()
        deletePass.geometry("1300x225")
        deletePass.title("Air Reservation System")
        deletePassInput = StringVar()
        Label(deletePass, font=('comic sans ms','20','italic'),justify='center',text="Passenger Number: ").grid(row=0)
        Label(deletePass, font=('comic sans ms','20','italic'),justify='center',text="You have to know your Passenger Number to delete your passenger data").grid(row=1)
        Label(deletePass, font=('comic sans ms','20','italic'),justify='center',text="(Example of Passenger Number: 1122212232) ").grid(row=2)
        passDelete = Entry(deletePass,font=('comic sans ms','20','italic'),justify='center', text=deletePassInput)
        passDelete.grid(row=0, column=1)


        def delete():
            texta = "{}".format(passDelete.get())
            print(texta)
            dataa = (texta)
            print(dataa)         

        Buttonh = Button(deletePass, font=('comic sans ms','20','italic'),justify='center',bg='black',fg='white',text="Done", command=delete).place(x=1200, y=150)
    Buttonf = Button(master, font=('comic sans ms','20','italic'),justify='center',bg='black',fg='white',text="Done", command=done).place(x=800, y=330)
    Buttong = Button(master, font=('comic sans ms','20','italic'),justify='center',bg='black',fg='white',text="Delete Passenger", command=deletePassenger).place(x=725, y=400)

    name.grid(row=0, column=1)
    dob.grid(row=1, column=1)
    passNum.grid(row=2, column=1)
    passId.grid(row=3, column=1)


def ticket():

    master = Tk()
    master.geometry("825x250")
    master.title("Air Reservation System")

    textTicketNum = StringVar()
    textSeatNum = StringVar()

    Label(master, font=('comic sans ms','20','italic'),text="Ticket Number: ").grid(row=0)
    Label(master, font=('comic sans ms','20','italic'),text="Seat Number: ").grid(row=1)

    Label(master, font=('comic sans ms','20','italic'),text="(Example of Ticket Number input: 12255)").grid(row=15)
    Label(master, font=('comic sans ms','20','italic'),text="(Example of Seat Number input: 128) ").grid(row=16)

#Change seat number

    ticketNum = Entry(master, font=('comic sans ms','16','italic'),justify='center',text=textTicketNum)
    seatNum = Entry(master, font=('comic sans ms','16','italic'),justify='center',text=textSeatNum)

    def done():

        texta = "{}".format(ticketNum.get())
        textb = "{}".format(seatNum.get())

        print(texta)

        dataa = (texta, textb)
        print(dataa)

        #print('"{}"'.format(name.get()))
        # print(texta)

    def deleteTicket():

        deleteTick = Tk()
        deleteTick.geometry("800x150")
        deleteTick.title("Air Reservation System")

        deleteTickInput = StringVar()

        Label(deleteTick, font=('comic sans ms','20','italic'),justify='center',text="Ticket Number: ").grid(row=0)

        Label(deleteTick, font=('comic sans ms','20','italic'),justify='center',text="Example of Ticket Number: 12211 ").grid(row=1)

        ticketDelete = Entry(deleteTick, font=('comic sans ms','20','italic'),justify='center',text=deleteTickInput)

        ticketDelete.grid(row=0, column=1)

        def delete():

            texta = "{}".format(ticketDelete.get())
            print(texta)
            dataa = (texta)
            print(dataa)

        Buttonf = Button(deleteTick, font=('comic sans ms','15','italic'),bg='black',fg='white',text="Done", command=delete).place(x=575, y=65)

    Buttonf = Button(master, font=('comic sans ms','12','italic'),bg='black',fg='white',text="Done", justify='center',command=done).place(x=650, y=100)
    Buttong = Button(master, font=('comic sans ms','12','italic'),bg='black',fg='white',text="Delete Ticket",command=deleteTicket).place(x=650, y=150)

    ticketNum.grid(row=0, column=1)
    seatNum.grid(row=1, column=1)

def flight():

    master = Tk()
    master.geometry("800x600")
    master.title("Air Reservation System")

    textFlightId = StringVar()
    textFlightTerm = StringVar()
    textFlighTicket = StringVar()
    textNumFlights = StringVar()

    Label(master, font=('comic sans ms','20','italic'),justify='center',text="Flight I.D.: ").grid(row=0)
    Label(master, font=('comic sans ms','20','italic'),justify='center',text="Flight Terminal: ").grid(row=1)
    Label(master, font=('comic sans ms','20','italic'),justify='center',text="Flight Ticket: ").grid(row=2)
    Label(master, font=('comic sans ms','20','italic'),justify='center',text="Number of Flights: ").grid(row=3)

    Label(master, font=('comic sans ms','20','italic'),justify='center',text="(Example of Flight I.D.: 1221) ").grid(row=15)
    Label(master, font=('comic sans ms','20','italic'),justify='center',text="(Example of Flight Terminal: A-5) ").grid(row=16)
    Label(master, font=('comic sans ms','20','italic'),justify='center',text="(Example of Flight Ticket: 128)  ").grid(row=17)
    Label(master, font=('comic sans ms','20','italic'),justify='center',text="(Example of Number of Flights: 1) ").grid(row=18)
    Message(master, font=('comic sans ms','20','bold'),justify='center',text="*** In order to change flight information, you must delete it using your flight I.D. number and then insert another one***", width = 500).grid(row=19)

    flightId = Entry(master, font=('comic sans ms','16','italic'),justify='center',text=textFlightId)
    flightTerm = Entry(master, font=('comic sans ms','16','italic'),justify='center',text=textFlightTerm)
    flightTicket = Entry(master, font=('comic sans ms','16','italic'),justify='center',text=textFlighTicket)
    numFlights = Entry(master, font=('comic sans ms','16','italic'),justify='center',text=textNumFlights)
    

    def done():

        texta = "{}".format(flightId.get())
        textb = "{}".format(flightTerm.get())
        textc = "{}".format(flightTicket.get())
        textd = "{}".format(numFlights.get())
        print(texta)

        dataa = (texta, textb, textc, textd)
        print(dataa)
      

        #print('"{}"'.format(name.get()))
        # print(texta)

    def deleteFlight():
        deleteFli = Tk()
        deleteFli.geometry("850x175")
        deleteFli.title("Air Reservation System")

        deleteFliInput = StringVar()

        Label(deleteFli, font=('comic sans ms','20','italic'),justify='center',text="Flight Number: ").grid(row=0)
        Label(deleteFli, font=('comic sans ms','16','italic'),justify='center',text="You have to know your Flight I.D. to delete your flight data").grid(row=1)
        Label(deleteFli, font=('comic sans ms','16','italic'),justify='center',text="Example of Flight Number: 1122212232 ").grid(row=2)

        fliDelete = Entry(deleteFli, font=('comic sans ms','14','italic'),justify='center',text=deleteFliInput)

        fliDelete.grid(row=0, column=1)

        def delete():
            texta = "{}".format(fliDelete.get())
            print(texta)
            dataa = (texta)
            print(dataa)

        Buttonh = Button(deleteFli, font=('comic sans ms','16','italic'),justify='center',bg='black',fg='white',text="Done", command=delete).place(x=675, y=75)

    Buttonf = Button(master, font=('comic sans ms','16','italic'),justify='center',bg='black',fg='white',text="Done", command=done).place(x=640, y=280)
    Buttong = Button(master, font=('comic sans ms','16','italic'),justify='center',bg='black',fg='white',text="Cancel Flight", command=deleteFlight).place(x=600, y=350)

    flightId.grid(row=0, column=1)
    flightTerm.grid(row=1, column=1)
    flightTicket.grid(row=2, column=1)
    numFlights.grid(row=3, column=1)

def plane():

    master = Tk()
    master.geometry("1200x450")
    master.title("Air Reservation System")

    textArrival = StringVar()
    textDeparture = StringVar()
    textPlaneNum = StringVar()
    textSeatNum = StringVar()
    textPlaneSize = StringVar()

    Label(master, font=('comic sans ms','16','italic'),justify='center', text="Arrival: ").grid(row=0)
    Label(master, font=('comic sans ms','16','italic'),justify='center',text="Departure: ").grid(row=1)
    Label(master, font=('comic sans ms','16','italic'),justify='center',text="Plane Number: ").grid(row=2)
    Label(master, font=('comic sans ms','16','italic'),justify='center',text="Number of Seats: ").grid(row=3)
    Label(master, font=('comic sans ms','16','italic'),justify='center',text="Plane Size: ").grid(row=4)

    Label(master, font=('comic sans ms','16','italic'), justify='center',text="(Example of Arrival Time: 11:00:00 (Insert time based on 24 hour clock)) ").grid(row=15)
    Label(master, font=('comic sans ms','16','italic'),justify='center',text="(Example of Departure Time: 12:00:00 (Insert time based on 24 hour clock)) ").grid(row=16)
    Label(master, font=('comic sans ms','16','italic'),justify='center',text="(Example of Plane Number: 125588) ").grid(row=17)
    Label(master, font=('comic sans ms','16','italic'),justify='center',text="(Example of Number of Seats: 200) ").grid(row=18)
    Label(master, font=('comic sans ms','16','italic'),justify='center',text="(Example of Plane Size: Small,Medium, or Large) ").grid(row=19)
    Label(master, font=('comic sans ms','16','italic'),justify='center',text="For reference on Plane Size, Small(150 feet long), Medium(200 feet long), Large(250 feet long)").grid(row=20)

    arrival= Entry(master, font=('comic sans ms','12','italic'), justify='center',text = textArrival)
    departure= Entry(master,  font=('comic sans ms','12','italic'), justify='center',text = textDeparture)
    planeNum= Entry(master,  font=('comic sans ms','12','italic'), justify='center',text = textPlaneNum)
    seatNum = Entry(master,  font=('comic sans ms','12','italic'), justify='center',text = textSeatNum)
    planeSize = Entry(master, font=('comic sans ms','12','italic'), justify='center',text=textPlaneSize)


    def done():

        texta = "{}".format(arrival.get())
        textb = "{}".format(departure.get())
        textc = "{}".format(planeNum.get())
        textd = "{}".format(seatNum.get())
        texte = "{}".format(planeSize.get())
        print(texta)

        dataa = (texta, textb, textc, textd, texte)
        print(dataa)
    

        #print('"{}"'.format(name.get()))
       # print(texta)

    Buttonf = Button(master, font=('comic sans ms','12','italic'), justify='center',text="Done",bg='black',fg='white', command=done).place(x=1025, y=270)

    arrival.grid(row=0, column=1)
    departure.grid(row=1, column=1)
    planeNum.grid(row=2, column=1)
    seatNum.grid(row=3, column=1)
    planeSize.grid(row=4, column=1)

'''mainloop( ): This is the main menu'''

label = Label(root, font=('comic sans ms','20','bold'),text="WELCOME TO THE AIR RESERVATION SYSTEM")
label.pack()

myButtonb = Button(root, font=('comic sans ms','16','italic'),text = "Flights", justify='center',bg='black',fg='white',command=flight)
myButtonb.pack()
myButtonc = Button(root, font=('comic sans ms','16','italic'),text = "Tickets",justify='center', bg='black',fg='white',command=ticket)
myButtonc.pack()
myButtond = Button(root,font=('comic sans ms','16','italic'),text = "Plane", justify='center',bg='black',fg='white',command=plane)
myButtond.pack()
myButtone = Button(root,font=('comic sans ms','16','italic'), text = "Passenger", justify='center',bg='black',fg='white',command=passenger)
myButtone.pack()


root.mainloop()


