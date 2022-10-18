def calc_avg_marks(marks):
    s = 0

    for element in marks:
        s += element

    return s / len(marks)







def main():
    marks = []

    mark = 0

    print("Intup students marks.\nFor  exit input -1\n")

    while mark != -1:
        mark = int(input("Input mark: "))

        marks.append()

    marks.remove(-1)
    print("Your marks: + str(marks)")





def maim():
    mark1 = int(input("Input first mark: "))
    mark2 = int(input("Input second mark: "))
    mark3 = int(input("Input third mark: "))

    avg = calc_avg_marks(mark1, mark2, mark3)

    msg = f"Student group has avg marks: {round(avg, 2)}"

    print(msg)

main()