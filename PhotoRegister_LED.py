import spidev, time
import RPi.GPIO as GPIO

LED = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

spi = spidev.SpiDev()

# SPI 통신 시작하기
spi.open(0, 0)

# SPI 통신 속도 설정
spi.max_speed_hz = 1350000

def analog_read(channel) :
    r = spi.sfer2([1, (8+channel) << 4, 0])
    adc_out = ((r[1]&3) << 8) + r[2]
    return adc_out
print(“Press SW or input Ctrl+C to quit”)   # 메세지 화면 출력

try:

while True :
    reading = analog_read(1)
    voltage = read * 3.3/1024
    print(“Reading=%d\tVoltage=%f” %(adc_out, voltage))
    time.sleep(1)
    
    if reading < 100 :
       GPIO.output(led, GPIO.HIGH)
       print(“LED ON”)
    else :
       GPIO.output(led, GPIO.LOW)
       print(“LED OFF”)

except KeyboardInterrupt:                  # Ctrl-C 입력 시
    GPIO.cleanup()                              # GPIO 설정 Clear
