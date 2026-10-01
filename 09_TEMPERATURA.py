#PROGRAMA SIMULADOR DE TEMPERATURA

temperatura = 0

def on_button_pressed_a():
    global temperatura
    temperatura = randint(1, 40)
    basic.show_number(temperatura)
    basic.pause(1000)
    if temperatura <= 15:
        basic.show_string(" FRIO")
    else:
        basic.show_string(" CALOR")
    basic.pause(500)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)
