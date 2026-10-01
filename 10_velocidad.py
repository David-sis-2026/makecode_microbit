#REALIZA UN PROGRAMA QUE SIMULE VELOCIDAD

velocidad = 0

def on_button_pressed_b():
    global velocidad
    velocidad = randint(1, 100)
    basic.show_number(velocidad )
    basic.pause(1000)
    if velocidad >=70 :
        
        basic.show_string(" RAPIDO")
    else:
        
        basic.show_string(" LENTO")
    basic.pause(500)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)
