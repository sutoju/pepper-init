from naoqi import ALProxy
view = ALProxy("ALTabletService", "192.168.1.19", 9559)
view.showWebview()
view.loadUrl("http://bot-front.eu-gb.mybluemix.net")
