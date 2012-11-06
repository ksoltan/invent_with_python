def Greet(first_name, last_name, greeting = 'Hello', fairwell = 'Bye', say_goodbye = False):
	print greeting, first_name, last_name
	if say_goodbye:
		print fairwell, first_name
