#realiza un programa que muestre la division de dos numero al azar
#usando el boton a en el lenguaje pyton para microsoft

#creamos dos variables
n1=0
n2=0

def on_button_pressed_b():
   global n1,n2
   n1=randint(1, 9)
   basic.show_number(n1)
   basic.pause(500)
   basic.show_leds("""
   . . . . #
   . . . # .
   . . # . .
   . # . . .
   # . . . .
   """)
   basic.pause(500)
   n2=randint(1, 9)
   basic.show_number(n2)
   basic.pause(500)
   basic.show_leds("""
   . . . . .
   # # # # #
   . . . . .
   # # # # #
   . . . . .
   """)
   basic.pause(500)
   basic.show_number(n1/n2)
   basic.pause(500)
   basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)
