import serial

port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=3.0)


def enable_tank_vacuum():
    port.write("<TV>")


def run_tank_pump():
    port.write("<TR>")


def disable_tank_pump():
    port.write("<TS>")


def do_pick(param):
    port.write("<%iV>" % param)


def release_pick(param):
    port.write("<%iR>" % param)


def clear_channel(param):
    port.write("<%iC>" % param)
