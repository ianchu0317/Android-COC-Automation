from ppadb.client import Client as AdbClient
from time import sleep
import os

# Some global variables
DEVICE_SERIAL_NUMBER = 'AU4HIZOV6LZ95LX8'
SCREEN_SIZE = (1080, 2400)
CHAT_PANEL = (160, 480)
CLAN_PANEL = (360, 45)
LEAVE_BUTTON = (3815, 735)
CLOSE_BUTTON = (1940, 70)
CONFIRM_LEAVE_BUTTON = (1400, 700) # Remember to add sleep() after this, because it takes time
FIND_CLAN_PANEL = (1380, 75)
FIRST_SUGESTED_CLAN = (1080, 525)
JOIN_CLAN_BUTTON = (1820, 740)
ACCEPT_CONDITIONS = (445, 740)
CHAT_BUTTON = (750, 1024)
ENTER_BUTTON = (2200, 475)

# Start running adb server
def StartAdbServer(port:int):
	os.system('adb -P {} start-server'.format(port))
	os.system('adb usb')

# Kill current adb server
def KillAdbServer(port:int):
	os.system('adb -P {} kill-server'.format(port))

# Function for leaving clan
def LeaveClan(device):
	device.input_tap(CHAT_PANEL[0], CHAT_PANEL[1]) # x, y variables; open chat panel
	device.input_tap(CLAN_PANEL[0], CLAN_PANEL[1]) # open menu panel
	device.input_tap(FIND_CLAN_PANEL[0], FIND_CLAN_PANEL[1])
	device.input_tap(FIRST_SUGESTED_CLAN[0], FIRST_SUGESTED_CLAN[1])
	device.input_tap(JOIN_CLAN_BUTTON[0], JOIN_CLAN_BUTTON[1])
	device.input_tap(CONFIRM_LEAVE_BUTTON[0], CONFIRM_LEAVE_BUTTON[1]) # Leave Clan
	device.input_tap(ACCEPT_CONDITIONS[0], ACCEPT_CONDITIONS[1])
	device.input_tap(CHAT_BUTTON[0], CHAT_BUTTON[1])
	sleep(1)
	device.input_text(message)
	sleep(0.5)
	device.input_tap(ENTER_BUTTON[0], ENTER_BUTTON[1])


def main():
	try:
		#StartAdbService(5037)
		client = AdbClient(host='127.0.0.1', port=5037)
		device = client.device(DEVICE_SERIAL_NUMBER)

		with open('spam-message.txt', 'r') as file:
			message = file.read()

		for x in range(10):
			LeaveClan(device, message)
			sleep(1)

	except KeyboardInterrupt:
		#KillAdbService(5037)
		pass


if __name__ == '__main__':
	main()
