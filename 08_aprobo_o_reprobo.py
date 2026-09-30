#mostrar si aprobo o reprobo

nota = 0

def on_button_pressed_a():
    global nota
    nota = randint(1, 70)
    basic.show_number(nota )
    basic.pause(1000)
    if nota >= 50 :
        basic.show_icon(IconNames.YES)
        basic.show_string(" APROBADO")
    else:
        basic.show_icon(IconNames.NO)
        basic.show_string(" REPROBADO")
    basic.pause(500)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)
