import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
leds = [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup(leds, GPIO.OUT)
dynamic_range = 3.3
def nubmer_to_dac(value):
    ans = [int(element) for element in bin(value)[2:].zfill(8)]
    for i  in range(8):
        GPIO.output(leds[i], ans[i])
def voltage_to__number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапозон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print ("Устанавлием 0.0")
        return 0

    return int (voltage / dynamic_range * 255)
try:
    while True:
        try:
            voltage = float(input("Ввидите напряжение в Вольтах: "))
            number = voltage_to__number(voltage)
            nubmer_to_dac(number)
        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз \n")
finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()