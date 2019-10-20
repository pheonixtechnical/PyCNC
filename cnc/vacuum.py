import serial

port = serial.serial("/dev/ttyS0", baudrate=115200, timeout=3.0)


def enable_tank_vacuum():
    port.write("<TV>")


def run_tank_pump():
    port.write("<TR>")


def disable_tank_pump():
    port.write("<TS>")


def do_pick(param):
    port.write("<" + param + "V>")


def release_pick(param):
    port.write("<" + param + "R>")
