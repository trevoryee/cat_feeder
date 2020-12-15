#actual function
def cat_feed:
	get_weight= food_weight
	if food_weight <= 500
	full= false
	while full = false:
		SetAngle(90)
		sleep(5)
		SetAngle(-90)
		sleep(5)
		SetAngle(90)
		sleep(5)
		pwm.stop()
		GPIO.cleanup()
		print ("The food weight is now" + get_weight)
		full= true
		sleep (10800)
		if get_weight <= 500:
			full= false
	else:
		print ("The dish is full")
		full= true
		sleep(10800)
		if get_weight <= 500
			full= false
tare
cat_feed