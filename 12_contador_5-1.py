#contador de numeros en retroceso del 5 al 1

def on_button_pressed_b():

    for i in range(5, 0, -1):
        basic.show_number(i)
        basic.pause(300)
        
    basic.show_icon(IconNames.YES)
    basic.show_string(" FINAL")
    basic.pause(500)
    basic.clear_screen()
    
input.on_button_pressed(Button.B, on_button_pressed_b)
