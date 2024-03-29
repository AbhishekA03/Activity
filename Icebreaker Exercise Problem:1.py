"""
Problem -I 
the wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
spectrum is continuous, it is often divided into 6 colors as shown below:

Violet 380 to less than 450
Blue 450 to less than 495
Green 495 to less than 570
Yellow 570 to less than 590
Orange 590 to less than 620
Red 620 to 750

Write a program that reads a wavelength from the user and reports its color. Display
an appropriate error message if the wavelength entered by the user is outside of the
visible spectrum.
"""
a=int(input("Enter wavelength of visible light in nm "))
if 380<=a<=750:
    if 380<=a<450:
        print("Violet")
    elif 450<=a<495:
        print("Blue")
    elif 495<=a<570:
        print("Green")
    elif 570<=a<590:
        print("Yellow")
    elif 590<=a<620:
        print("Orange")
    elif 620<=a<=750:
        print("Red")
else:
    print("Entered wavelength is outside of visible spectrum")
