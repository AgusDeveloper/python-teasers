display = []
buttons = []

def make_button(n):
  return lambda: display.append(n)

for n in range(10):
  buttons.append(make_button(n))

btn = buttons[8]
btn()
print(display)

