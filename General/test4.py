from pynput import mouse

def on_move(x, y):
	print(x, y)
def on_click(x, y, button, pressed):
	if pressed:
		return False

with mouse.Listener(on_move=on_move, on_click=on_click) as listener:
	listener.join()
