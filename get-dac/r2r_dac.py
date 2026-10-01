import RPi.GPIO as GPIO
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
        GPIO.output(self.gpio_bits, ans)
    def set_voltage(self, voltage):
        
        if not (0.0 <= voltage <= self.dynamic_range):
            voltage = 0
        self.set_numbers(int(voltage * 255 / self.dynamic_range))

if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
        while True:
            try:
                voltage = float(input("ВВидите число в Вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввел не число, попытайтесь снова \n")
    finally:
        dac.deinit()