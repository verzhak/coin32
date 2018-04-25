
import argparse

def get_args():

    parser = argparse.ArgumentParser()
    parser.add_argument("--floors", type = int, required = True, help = "Количество этажей в подъезде (от 5 до 20)")
    parser.add_argument("--floor_height", type = float, required = True, help = "Высота одного этажа")
    parser.add_argument("--speed", type = float, required = True, help = "Скорость лифта при движении в метрах в секунду")
    parser.add_argument("--time_to_open", type = float, required = True, help = "Время между открытием и закрытием дверей")
    args = parser.parse_args()

    if args.floors < 5 or args.floors > 20:

        raise ValueError("Количество этажей должно находится в диапазоне от 5 до 20")

    if args.floor_height <= 0:

        raise ValueError("Высота одного этажа должна быть больше 0")

    if args.speed <= 0: # Можно, конечно, проверять еще и на теоретический предел - скорость света

        raise ValueError("Скорость лифта должна быть больше 0")

    if args.time_to_open <= 0:

        raise ValueError("Время между открытием и закрытием дверей должно быть больше 0")
    
    return args

