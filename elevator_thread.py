
import threading
import enum
import time

class EElevatorDirection(enum.Enum):

    UP = 1
    DOWN = 2
    STAY = 3

class CElevatorThread(threading.Thread):

    def __init__(self, floors, floor_height, speed, time_to_open):

        super().__init__()

        self.__floors = floors
        self.__floor_height = floor_height
        self.__speed = speed
        self.__time_to_open = time_to_open

        self.__stop_event = threading.Event()

        self.__floor_lock = threading.Lock()
        self.__floors_state = [ False ] * (floors + 1)
        self.__current_floor = 0
        self.__direction = EElevatorDirection.STAY

    def stop(self):

        self.__stop_event.set()

    def go_on_floor(self, floor_ind):

        if floor_ind > self.__floors:

            raise ValueError("Некорретный номер этажа")

        self.__floor_lock.acquire()
        self.__floors_state[floor_ind] = True
        self.__floor_lock.release()

    def __next_floor(self):

        print("### Лифт на этаже %u" % self.__current_floor)
        
        time.sleep(self.__floor_height / self.__speed)

    def __door(self):

        print("### Дверь открыта на этаже %u" % self.__current_floor)
        
        time.sleep(self.__time_to_open)

        print("### Дверь закрыта на этаже %u" % self.__current_floor)

    def run(self):

        while not self.__stop_event.is_set():

            self.__floor_lock.acquire()
            
            # Определяем, есть ли целевые этажы сверху и снизу
            is_up = any(self.__floors_state[self.__current_floor : ])
            is_down = any(self.__floors_state[ : self.__current_floor ])

            self.__floor_lock.release()

            # Едем вверх на один этаж
            if self.__direction == EElevatorDirection.UP:

                self.__next_floor()

                if is_up:

                    self.__current_floor += 1

                elif is_down:
                        
                    self.__direction = EElevatorDirection.DOWN

                else:

                    self.__direction = EElevatorDirection.STAY

            # Едем вниз на один этаж
            elif self.__direction == EElevatorDirection.DOWN:

                self.__next_floor()

                if is_down:

                    self.__current_floor -= 1

                elif is_up:

                    self.__direction = EElevatorDirection.UP

                else:

                    self.__direction = EElevatorDirection.STAY

            else:

                time.sleep(1)

                if is_up:

                    self.__direction = EElevatorDirection.UP

                elif is_down:

                    self.__direction = EElevatorDirection.DOWN

            # Открываем дверь, если нужно
            if self.__floors_state[self.__current_floor]:

                self.__floor_lock.acquire()
                self.__floors_state[self.__current_floor] = False
                self.__floor_lock.release()

                self.__door()

