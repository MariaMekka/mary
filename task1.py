def calc_avg_marks(marks):
    s = 0

    for element in marks:
        s += element


def maim():
    mark1 = int(input("Input first mark: "))
    mark2 = int(input("Input second mark: "))
    mark3 = int(input("Input third mark: "))

    avg = calc_avg_marks(mark1, mark2, mark3)

    msg = f"Student group has avg marks: {round(avg, 2)}"

    print(msg)

main()
