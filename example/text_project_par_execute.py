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
	if par.name == "Reloadconfig":
		parent().Load_config()
	
	elif par.name == "Reloadoutputlist":
		parent().Load_outputlist()
	
	elif par.name == "Touchstart":
		parent().Touch_start()
	else:
		pass
	return