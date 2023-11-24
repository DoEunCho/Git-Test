import RPi.GPIO as GPIO                    
import time                                

Trig = 4
Echo = 17
Buzzer = 21

GPIO.setmode(GPIO.BCM)                    
GPIO.setup(Trig, GPIO.OUT)                   # Trig=4 초음파 신호 전송핀 번호 지정 및 출력지정
GPIO.setup(Echo, GPIO.IN)                    # Echo=17 초음파 수신 핀 번호 지정 및 입력지정
GPIO.setup(Buzzer, GPIO.OUT)

print “Press SW or input Ctrl+C to quit”   # 메세지 화면 출력
Buzz = GPIO.PWM(Buzzer, 440)              # 부저센서 초기화

try:
    while True:
            GPIO.output(Trig, False)         # Trig핀 초기 설정
            time.sleep(0.5)                    # 0.5초 지연

            GPIO.output(Trig, True)          # Trig핀에 펄스 출력
            time.sleep(0.00001)              # 시간 지연
            GPIO.output(Trig, False) 
            while GPIO.input(Echo) == 0:     # Echo핀 입력 없을 경우
               start = time.time()                # 시간 저장

            while GPIO.input(Echo) == 1:     # Echo핀 입력 있을 경우
               stop = time.time()

            time_interval = stop – start          # 초음파가 수신되는 시간 간격 저장
            distance = time_interval * 17000   # 거리를 계산
            distance = round(distance, 2)       # 소수점 2자리까지 반올림

            print “Distance => “, distance, “cm”
	time.sleep(0.2)

	if(distance <= 40 and distance > 25):     # 26 ~ 40 cm 일때
         		Buzz.start(50)
         		Buzz.ChangeFrequency(523)
         		time.sleep(0.3)
         		Buzz.stop()
         		time.sleep(0.3)

	elif(distance <= 25 and distance > 10):   # 25 ~ 11 cm 일때
         		Buzz.start(50)
         		Buzz.ChangeFrequency(523)
         		time.sleep(0.15)
         		Buzz.stop()
         		time.sleep(0.1)

	elif(distance <= 10):                            # 10cm 이하일때
         		Buzz.start(99)
         		Buzz.ChangeFrequency(523) 
         		time.sleep(0.05)
         		Buzz.stop()
         		time.sleep(0.05)

	else:                                               # 그 외
         		Buzz.stop()
         		time.sleep(0.5)

except KeyboardInterrupt:                  # Ctrl-C 입력 시
    GPIO.cleanup()                         # GPIO 관련설정 Clear
    Print "bye~"
