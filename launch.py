import serial
import time
from tkinter import *
import random

i = 0
root = Tk()
w = Label(root, text="BlueOrigin Flight-Info Simulator", font='Helvetica 20 bold').grid(row=0, column=1)
root.title("BlueOrigin FlightSim")
text_packet = Label(text="")
restart = Button(root, text="⟲", font='Helvetica 20 bold').grid(row=14, column=2, sticky="e")
connected = False
exp_time = 0


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
                + ','
                + str(altitude.get()) + ','
                + str(x_vel.get()) + ',' + str(y_vel.get()) + ',' + str(z_vel.get()) + ','
                + str(acceleration.get()) + ',0.000000,0.000000'
                + str(x_alt.get()) + ',' + str(y_alt.get()) + ',' + str(z_alt.get()) + ','
                + str(x_ang_vel.get()) + ','
                + str(y_ang_vel.get()) + ','
                + str(z_ang_vel.get()) + ','
                + str(liftoff_warning.get()) + ','
                + str(rcs_warning.get()) + ','
                + str(escape_warning.get()) + ','
                + str(chute_warning.get()) + ','
                + str(landing_warning.get())
                + ',' + str(fault_warning.get()))

        text_packet = Label(text="Text Packet:" + '\n' + "'" + text + "'").grid(row=14, column=1)

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
x_alt = DoubleVar()         # 10
y_alt = DoubleVar()         # 11
z_alt = DoubleVar()         # 12
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

e1 = Entry(root, text="Velocity X-Axis", textvariable=x_vel).grid(row=3, column=2, sticky='w')
e2 = Entry(root, text="Velocity Y-Axis", textvariable=y_vel).grid(row=4, column=2, sticky='w')
e3 = Entry(root, text="Velocity Z-Axis", textvariable=z_vel).grid(row=5, column=2, sticky='w')



running()



