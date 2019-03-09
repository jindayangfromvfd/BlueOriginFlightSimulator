import serial
import time
from tkinter import *
import random

i = 0
root = Tk()
w = Label(root, text="BlueOrigin Flight-Info Simulator", font='Helvetica 20 bold').grid(row=0, column=1)

text_packet = Label(text="").grid(row=17, column=1)
packet_title = Label(text="Text Packet:").grid(row=16, column=1)
restart = Button(root, text="Restart", font='Helvetica 15 bold').grid(row=0, column=5)
connected = False
exp_time = 0


arduinoOutput = Label(text="Arduino Output", font='Helvetica 18 bold').grid(row=18, column=1)

try:
    s = serial.Serial('/dev/tty.usbmodem1411', 115200, timeout=5)  # BlueOrigin specifies 115,200 baud rate
    connected = True
except:
    errorText = Label(text="Can't connect to /dev/tty.usbmodem1411", fg="red").grid(row=1, column=1)



def running():

    exp_time = 0

    while True:
        exp_time += 0.1
        exp_time += random.randrange(-1, 1, 1)/100  # if second decimal isn't always 0

        time.sleep(.1)  # data sent at 10Hz
        text = (status.get() + "," + "%.2f," % exp_time
                + str(altitude.get()) + ','
                + str(x_vel.get()) + ',' + str(y_vel.get()) + ',' + str(z_vel.get()) + ','
                + str(acceleration.get()) + ',0.000000,0.000000'

                # Attitude is orientation with respect to an inertial frame of reference
                + str(x_att.get()) + ',' + str(y_att.get()) + ',' + str(z_att.get()) + ','
                + str(x_ang_vel.get()) + ','
                + str(y_ang_vel.get()) + ','
                + str(z_ang_vel.get()) + ','
                + str(liftoff_warning.get()) + ','
                + str(rcs_warning.get()) + ','
                + str(escape_warning.get()) + ','
                + str(chute_warning.get()) + ','
                + str(landing_warning.get())
                + ',' + str(fault_warning.get()))

        text_packet = Label(text=text, font='Helvetica 16 bold').grid(row=17, column=1)
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

Label(root, text="Flight Status", font='Helvetica 16 bold').grid(row=2, column=0)
Label(root, text="Warnings", font='Helvetica 16 bold').grid(row=2, column=1)
Label(root, text="Values", font='Helvetica 16 bold').grid(row=2, column=2)

c2 = Checkbutton(root, text='RCS Warning', variable=rcs_warning).grid(row=3, column=1, sticky='w', padx=220)

c3 = Checkbutton(root, text='Escape Warning', variable=escape_warning).grid(row=4, column=1, sticky='w', padx=220)

c4 = Checkbutton(root, text='Chute Warning', variable=chute_warning).grid(row=5, column=1, sticky='w', padx=220)

c5 = Checkbutton(root, text='Landing Warning', variable=landing_warning).grid(row=6, column=1, sticky='w', padx=220)

c6 = Checkbutton(root, text='Fault Warning', variable=fault_warning).grid(row=7, column=1, sticky='w', padx=220)

c7 = Checkbutton(root, text='Liftoff Warning', variable=liftoff_warning).grid(row=8, column=1, sticky='w', padx=220)

# Flight Status

R1 = Radiobutton(root, text="None Reached", variable=status, value='@').grid(row=3, column=0, sticky='w')
status.set('@')

R2 = Radiobutton(root, text="Liftoff", variable=status, value='A').grid(row=4, column=0, sticky='w')

R3 = Radiobutton(root, text="Meco", variable=status, value='B').grid(row=5, column=0, sticky='w')

R4 = Radiobutton(root, text="Coast_Start", variable=status, value='C').grid(row=6, column=0, sticky='w')

R5 = Radiobutton(root, text="Separation", variable=status, value='D').grid(row=7, column=0, sticky='w')

R6 = Radiobutton(root, text="Apogee", variable=status, value='E').grid(row=8, column=0, sticky='w')

R7 = Radiobutton(root, text="Coast_End", variable=status, value='F').grid(row=9, column=0, sticky='w')

R8 = Radiobutton(root, text="Under_Chutes", variable=status, value='G').grid(row=10, column=0, sticky='w')

R9 = Radiobutton(root, text="Landing", variable=status, value='H').grid(row=11, column=0, sticky='w')

R10 = Radiobutton(root, text="Safing", variable=status, value='I').grid(row=12, column=0, sticky='w')

R11 = Radiobutton(root, text="Finished", variable=status, value='J').grid(row=13, column=0, sticky='w')

# Values

l1 = Label(root, text="Velocity X-Axis        ").grid(row=3, column=2, sticky='w')
e1 = Entry(root, text="Velocity X-Axis        ", textvariable=x_vel, width=5).grid(row=3, column=2, sticky='e')
l2 = Label(root, text="Velocity Y-Axis        ").grid(row=4, column=2, sticky='w')
e2 = Entry(root, text="Velocity Y-Axis        ", textvariable=y_vel, width=5).grid(row=4, column=2, sticky='e')
l1 = Label(root, text="Velocity Z-Axis        ").grid(row=5, column=2, sticky='w')
e3 = Entry(root, text="Velocity Z-Axis        ", textvariable=z_vel, width=5).grid(row=5, column=2, sticky='e')
l1 = Label(root, text="Acceleration (g)       ").grid(row=6, column=2, sticky='w')
e4 = Entry(root, text="Acceleration           ", textvariable=x_vel, width=5).grid(row=6, column=2, sticky='e')
l1 = Label(root, text="Altitude               ").grid(row=7, column=2, sticky='w')
e5 = Entry(root, text="Altitude               ", textvariable=y_vel, width=5).grid(row=7, column=2, sticky='e')
l1 = Label(root, text="Angular Velocity X-Axis").grid(row=8, column=2, sticky='w')
e1 = Entry(root, text="Angular Velocity X-Axis", textvariable=x_vel, width=5).grid(row=8, column=2, sticky='e')
l1 = Label(root, text="Angular Velocity Y-Axis").grid(row=9, column=2, sticky='w')
e2 = Entry(root, text="Angular Velocity Y-Axis", textvariable=y_vel, width=5).grid(row=9, column=2, sticky='e')
l1 = Label(root, text="Angular Velocity Z-Axis").grid(row=10, column=2, sticky='w')
e3 = Entry(root, text="Angular Velocity Z-Axis", textvariable=z_vel, width=5).grid(row=10, column=2, sticky='e')
l1 = Label(root, text="Attitude X-Axis        ").grid(row=11, column=2, sticky='w')
e1 = Entry(root, text="Attitude X-Axis        ", textvariable=x_vel, width=5).grid(row=11, column=2, sticky='e')
l1 = Label(root, text="Attitude X-Axis        ").grid(row=12, column=2, sticky='w')
e2 = Entry(root, text="Attitude Y-Axis        ", textvariable=y_vel, width=5).grid(row=12, column=2, sticky='e')
l1 = Label(root, text="Attitude X-Axis        ").grid(row=13, column=2, sticky='w')
e3 = Entry(root, text="Attitude Z-Axis        ", textvariable=z_vel, width=5).grid(row=13, column=2, sticky='e')


# display everything

root.title("BlueOrigin FlightSim")

top = root.winfo_toplevel()
menuBar = Menu(top)
top['menu'] = menuBar
subMenu = Menu(menuBar)

menuBar.add_cascade(label='Representative Flight Simulation', menu=subMenu)
subMenu.add_command(label='Run', command=root.quit())
subMenu.add_command(label='Run x10 Speed', command=root.quit())
subMenu.add_command(label='Stop', command=root.quit())


#create window for viewing

running()



