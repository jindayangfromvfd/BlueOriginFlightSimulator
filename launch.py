import serial
import time
from tkinter import *
import random


i = 0
root = Tk()

# Colors
darkish = '#%02x%02x%02x' % (29, 30, 38)
whitish = '#%02x%02x%02x' % (214, 216, 218)
code_green = '#%02x%02x%02x' % (80, 200, 70)
code_dark = '#%02x%02x%02x' % (23, 24, 30)


class sim:
    simRunning = False
    simStart = False
    exp_time = 0
    msgSim = Label(root)


flightSim = sim

timesTen = False

root.configure(bg=darkish)

w = Label(root, text="BlueOrigin FlightSim", font='Helvetica 20 bold', bg=darkish, fg=whitish).grid(row=0, column=0, columnspan=5, padx=10)

text_packet = Label(text="", bg=darkish, fg=whitish).grid(row=18, column=4)
packet_title = Label(text="Text Packet:", bg=darkish, fg=whitish).grid(row=11, column=4)
restart = Button(root, text="Restart", font='Helvetica 15 bold', bg=darkish, highlightbackground=darkish, highlightthickness=30, foreground=whitish).grid(row=0, column=5)
connected = False
exp_time = 0

simRunning = False
simStart = False

arduinoOutput = Label(text="Arduino Output   \n", font='Helvetica 18 bold', bg=darkish, fg=whitish).grid(row=19, column=4)

try:
    s = serial.Serial('/dev/tty.usbmodem1411', 115200, timeout=5)  # BlueOrigin specifies 115,200 baud rate
    connected = True
except:
    errorText = Label(text="Can't connect to /dev/tty.usbmodem1411", fg="red", bg=darkish).grid(row=21, column=4)


def running():

    while True:
        if timesTen:
            flightSim.exp_time += 1
        else:
            flightSim.exp_time += 0.1

        if flightSim.simStart:
            flightSim.msgSim = Label(root, text="[0:00] Main Engine Ignition Command", font='Helvetica 18 bold', bg=darkish,
                           fg=whitish).grid(row=2, rowspan=7, column=4)
            flightSim.exp_time = 0
            time.sleep(2)
            flightSim.simStart = False

        if flightSim.simRunning:
            if flightSim.exp_time > 7 and flightSim.exp_time < 8 :
                flightSim.msgSim = Label(root, text="[0:07] Liftoff", font='Helvetica 18 bold', bg=darkish,
                               fg=whitish).grid(row=2, rowspan=7, column=4)
                altitude.set(3750)
                status.set('A')

        flightSim.exp_time += random.randrange(-1, 1, 1)/100  # if second decimal isn't always 0

        time.sleep(.1)  # data sent at 10Hz
        text = ('['+status.get() + "," + "%.2f," % flightSim.exp_time
                + str(altitude.get()) + ','
                + str(x_vel.get()) + ',' + str(y_vel.get()) + ',' + str(z_vel.get()) + ','
                + str(acceleration.get()) + ',0.000000,0.000000'

                # Attitude is orientation with respect to an inertial frame of reference
                + str(x_att.get()) + ',' + str(y_att.get()) + ',' + str(z_att.get()) + ','
                + str(x_ang_vel.get()) + ',\n'
                + str(y_ang_vel.get()) + ','
                + str(z_ang_vel.get()) + ','
                + str(liftoff_warning.get()) + ','
                + str(rcs_warning.get()) + ','
                + str(escape_warning.get()) + ','
                + str(chute_warning.get()) + ','
                + str(landing_warning.get())
                + ',' + str(fault_warning.get())+']')

        text_packet = Label(text=text, font='Helvetica 17 bold', bg=darkish, fg=code_green).grid(row=12, column=4)
        expTime = Label(text="Experimental Time : " + "%.1f seconds" % flightSim.exp_time, font='Helvetica 18 bold', bg=darkish, fg=whitish).grid(
            row=2, column=4)
        if connected:
            s.write('A')
        root.update_idletasks()
        root.update()



#  Order of Data Fields:
status = StringVar()        # 1
# experimental time         # 2
altitude = IntVar()         # 3
x_vel = DoubleVar()         # 4
y_vel = DoubleVar()         # 5
z_vel = DoubleVar()         # 6
acceleration = DoubleVar()  # 7
# reserved                  # 8
# reserved                  # 9
x_att = DoubleVar()         # 10
y_att = DoubleVar()         # 11
z_att = DoubleVar()         # 12
x_ang_vel = DoubleVar()     # 13
y_ang_vel = DoubleVar()     # 14
z_ang_vel = DoubleVar()     # 15
liftoff_warning = IntVar()  # 16
rcs_warning = IntVar()      # 17
escape_warning = IntVar()   # 18
chute_warning = IntVar()    # 19
landing_warning = IntVar()  # 20
fault_warning = IntVar()    # 21

Label(root, text="Flight Status", font='Helvetica 16 bold', bg=darkish, fg=whitish).grid(row=2, column=0, padx=30)
Label(root, text="Warnings", font='Helvetica 16 bold', bg=darkish, fg=whitish).grid(row=2, column=1)
Label(root, text="Values", font='Helvetica 16 bold', bg=darkish, fg=whitish).grid(row=2, column=2)

c2 = Checkbutton(root, text='RCS Warning', variable=rcs_warning, bg=darkish, fg=whitish).grid(row=3, column=1, sticky='w', padx=60)

c3 = Checkbutton(root, text='Escape Warning', variable=escape_warning, bg=darkish, fg=whitish).grid(row=4, column=1, sticky='w', padx=60)

c4 = Checkbutton(root, text='Chute Warning', variable=chute_warning, bg=darkish, fg=whitish).grid(row=5, column=1, sticky='w', padx=60)

c5 = Checkbutton(root, text='Landing Warning', variable=landing_warning, bg=darkish, fg=whitish).grid(row=6, column=1, sticky='w', padx=60)

c6 = Checkbutton(root, text='Fault Warning', variable=fault_warning, bg=darkish, fg=whitish).grid(row=7, column=1, sticky='w', padx=60)

c7 = Checkbutton(root, text='Liftoff Warning', variable=liftoff_warning, bg=darkish, fg=whitish).grid(row=8, column=1, sticky='w', padx=60)

# Flight Status

R1 = Radiobutton(root, text="None Reached", variable=status, value='@', bg=darkish, fg=whitish).grid(row=3, column=0, sticky='w', padx=60)
status.set('@')

R2 = Radiobutton(root, text="Liftoff", variable=status, value='A', bg=darkish, fg=whitish).grid(row=4, column=0, sticky='w', padx=60)

R3 = Radiobutton(root, text="Meco", variable=status, value='B', bg=darkish, fg=whitish).grid(row=5, column=0, sticky='w', padx=60)

R4 = Radiobutton(root, text="Coast_Start", variable=status, value='C', bg=darkish, fg=whitish).grid(row=6, column=0, sticky='w', padx=60)

R5 = Radiobutton(root, text="Separation", variable=status, value='D', bg=darkish, fg=whitish).grid(row=7, column=0, sticky='w', padx=60)

R6 = Radiobutton(root, text="Apogee", variable=status, value='E', bg=darkish, fg=whitish).grid(row=8, column=0, sticky='w', padx=60)

R7 = Radiobutton(root, text="Coast_End", variable=status, value='F', bg=darkish, fg=whitish).grid(row=9, column=0, sticky='w', padx=60)

R8 = Radiobutton(root, text="Under_Chutes", variable=status, value='G', bg=darkish, fg=whitish).grid(row=10, column=0, sticky='w', padx=60)

R9 = Radiobutton(root, text="Landing", variable=status, value='H', bg=darkish, fg=whitish).grid(row=11, column=0, sticky='w', padx=60)

R10 = Radiobutton(root, text="Safing", variable=status, value='I', bg=darkish, fg=whitish).grid(row=12, column=0, sticky='w', padx=60)

R11 = Radiobutton(root, text="Finished", variable=status, value='J', bg=darkish, fg=whitish).grid(row=13, column=0, sticky='w', padx=60)

# Values

l1 = Label(root, text="Velocity X-Axis               ", bg=darkish, fg=whitish).grid(row=3, column=2, sticky='w')
e1 = Entry(root, text="Velocity X-Axis               ", bg=darkish, fg=whitish, textvariable=x_vel, width=4, highlightbackground=code_dark).grid(row=3, column=2, sticky='e', padx=20)
l2 = Label(root, text="Velocity Y-Axis               ", bg=darkish, fg=whitish).grid(row=4, column=2, sticky='w')
e2 = Entry(root, text="Velocity Y-Axis               ", bg=darkish, fg=whitish, textvariable=y_vel, width=4, highlightbackground=code_dark).grid(row=4, column=2, sticky='e', padx=20)
l1 = Label(root, text="Velocity Z-Axis               ", bg=darkish, fg=whitish).grid(row=5, column=2, sticky='w')
e3 = Entry(root, text="Velocity Z-Axis               ", bg=darkish, fg=whitish, textvariable=z_vel, width=4, highlightbackground=code_dark).grid(row=5, column=2, sticky='e', padx=20)
l1 = Label(root, text="Acceleration (g)              ", bg=darkish, fg=whitish).grid(row=6, column=2, sticky='w')
e4 = Entry(root, text="Acceleration                  ", bg=darkish, fg=whitish, textvariable=x_vel, width=4, highlightbackground=code_dark).grid(row=6, column=2, sticky='e', padx=20)
l1 = Label(root, text="Altitude                      ", bg=darkish, fg=whitish).grid(row=7, column=2, sticky='w')
e5 = Entry(root, text="Altitude                      ", bg=darkish, fg=whitish, textvariable=y_vel, width=4, highlightbackground=code_dark).grid(row=7, column=2, sticky='e', padx=20)
l1 = Label(root, text="Angular Velocity X-Axis       ", bg=darkish, fg=whitish).grid(row=8, column=2, sticky='w')
e1 = Entry(root, text="Angular Velocity X-Axis       ", bg=darkish, fg=whitish, textvariable=x_vel, width=4, highlightbackground=code_dark).grid(row=8, column=2, sticky='e', padx=20)
l1 = Label(root, text="Angular Velocity Y-Axis       ", bg=darkish, fg=whitish).grid(row=9, column=2, sticky='w')
e2 = Entry(root, text="Angular Velocity Y-Axis       ", bg=darkish, fg=whitish, textvariable=y_vel, width=4, highlightbackground=code_dark).grid(row=9, column=2, sticky='e', padx=20)
l1 = Label(root, text="Angular Velocity Z-Axis       ", bg=darkish, fg=whitish).grid(row=10, column=2, sticky='w')
e3 = Entry(root, text="Angular Velocity Z-Axis       ", bg=darkish, fg=whitish, textvariable=z_vel, width=4, highlightbackground=code_dark).grid(row=10, column=2, sticky='e', padx=20)
l1 = Label(root, text="Attitude X-Axis               ", bg=darkish, fg=whitish).grid(row=11, column=2, sticky='w')
e1 = Entry(root, text="Attitude X-Axis               ", bg=darkish, fg=whitish, textvariable=x_vel, width=4, highlightbackground=code_dark).grid(row=11, column=2, sticky='e', padx=20)
l1 = Label(root, text="Attitude X-Axis               ", bg=darkish, fg=whitish).grid(row=12, column=2, sticky='w')
e2 = Entry(root, text="Attitude Y-Axis               ", bg=darkish, fg=whitish, textvariable=y_vel, width=4, highlightbackground=code_dark).grid(row=12, column=2, sticky='e', padx=20)
l1 = Label(root, text="Attitude X-Axis               ", bg=darkish, fg=whitish).grid(row=13, column=2, sticky='w')
e3 = Entry(root, text="Attitude Z-Axis               ", bg=darkish, fg=whitish, textvariable=z_vel, width=4, highlightbackground=code_dark).grid(row=13, column=2, sticky='e', padx=20)

output = Frame(root, width=600, height=150, bg=code_dark).grid(row=20, column=4, sticky='e', padx=20)

info = Frame(root, width=600, height=150, bg=code_dark).grid(row=2, rowspan=7, column=4, sticky='e', padx=20)
msg = Label(root, text="", font='Helvetica 18 bold', bg=darkish, fg=whitish).grid(row=2, rowspan=7, column=4, sticky='e', padx=20)
# display everything

root.title("BlueOrigin FlightSim")

top = root.winfo_toplevel()
menuBar = Menu(top)
top['menu'] = menuBar
subMenu = Menu(menuBar)





def normalSpeed():
    timesTen = False


def timesTen():
    timesTen = True


def runSimulation():

    flightSim.simRunning = True
    flightSim.simStart = True


menuBar.add_cascade(label='Representative Flight Simulation', menu=subMenu)
subMenu.add_command(label='Run Simulation', command=runSimulation)
subMenu.add_command(label='x10 Speed', command=timesTen)
subMenu.add_command(label='Regular Speed', command=normalSpeed)


#create window for viewing

running()



