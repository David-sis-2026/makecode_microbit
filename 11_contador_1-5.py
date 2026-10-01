#contador usando por y boton A 

def on_button_pressed_a():

    for i in range(1, 5 + 1):
        basic.show_number(i)
        basic.pause(300)
        
    basic.show_icon(IconNames.YES)
    basic.show_string(" FINAL")
    basic.pause(500)
    basic.clear_screen()
    
input.on_button_pressed(Button.A, on_button_pressed_a)
