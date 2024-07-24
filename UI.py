def ui():
    axis = input("Axis: ")
    while True:
        try:
            slot = int(input("Slot: "))
            break
        except:
            print("Error")
    return axis, slot


