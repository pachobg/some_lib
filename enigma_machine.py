rotor_1 = "1234"
rotor_2 = "5678"
rotor_3 = "90?!"


wheel_1 = 0
wheel_2 = 0
wheel_3 = 0
combinations = 0

letter = input()

while True:
    if wheel_3 == 4:
        wheel_2 += 1
        wheel_3 = 0
    if wheel_2 == 4:
        wheel_1 += 1
        wheel_3 = 0
        wheel_2 = 0
    print(rotor_1[wheel_1] + rotor_2[wheel_2] + rotor_3[wheel_3])
    wheel_3 += 1

    combinations += 1
    letter = input()
    if combinations == 300:
        break
