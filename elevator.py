#!/usr/bin/env python3

from lib import get_args
from elevator_thread import CElevatorThread

args = get_args()
elevator = CElevatorThread(floors = args.floors, floor_height = args.floor_height, speed = args.speed, time_to_open = args.time_to_open)
elevator.start()

while True:

    command = input(">>> ").split()

    try:

        if command[0] == "floor":

            elevator.go_on_floor(int(command[1]))

        elif command[0] == "entrance":

            elevator.go_on_floor(0)

        elif command[0] == "exit":

            elevator.stop()

            break

        else:

            raise ValueError("Некорретная команда, допустимы: floor НОМЕР_ЭТАЖА или entrance (для перемещения на нулевой этаж в подъезд)")

    except ValueError as err:

        print(err)

