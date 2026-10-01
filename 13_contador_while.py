#contador del 1 al 5 usando while y boton A

def on_button_pressed_a():

    i = 5 
    while i >=1:     
        basic.show_number(i)
        basic.pause(500)
        i = i - 1 
    basic.show_string(" FINAL")
    basic.pause(500)
    basic.clear_screen()
    
input.on_button_pressed(Button.A, on_button_pressed_a)
