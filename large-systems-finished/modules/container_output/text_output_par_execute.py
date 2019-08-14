# me - this DAT
# par - the Par object that has changed
# val - the current value
# prev - the previous value
# 
# Make sure the corresponding toggle is enabled in the Parameter Execute DAT.

def onValueChange(par, prev):
	# use par.eval() to get current value
	return

def onPulse(par):
	if par.name == "Touchstart":
		parent().Touch_start()

	elif par.name == "Resetnetwork":
		parent().Reset_network()			
	else:
		pass
	return