import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
gpio_bits = [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup(gpio_bits, GPIO.OUT)
dynamic_range = 3.3
class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
    def set_numbers(self, numbers):
        ans = [int(element) for element in bin(numbers)[2:].zfill(8)]
        for i  in range(8):
            GPIO.output(gpio_bits[i], ans[i])
    def set_voltage(self, voltage):
        voltage = int(voltage)
        ans = [int(element) for element in bin(voltage)[2:].zfill(8)]
        for i  in range(8):
            GPIO.output(gpio_bits[i], ans[i])
if __name__ == "__main__":
    try:
        dac = R2R_DAC([6, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
        while True:
            try:
                voltage = float(input("ВВидите число в Вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввел не число, попытайтесь снова \n")
    finally:
        dac.deinit()