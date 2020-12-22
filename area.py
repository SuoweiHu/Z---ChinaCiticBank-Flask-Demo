from const import PI

def calc_round_are(radius):
    return PI * (radius**2)

def main():
    print(__name__)
    print("Round area ", calc_round_are(2))


main()