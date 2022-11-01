def main():
    name = input("What time is it? ")
    time = convert(name)
    if 7 <= time <= 8:
        print("breakfast time")
    if 12 <= time <= 13:
        print("lunch time")
    if 18 <= time <= 19:
        print("dinner time")    


def convert(time):
    hours, minutes = time.split(":")
    n_minute = float(minutes) / 60
    return float(hours) + n_minute


if __name__ == "__main__":
    main()         