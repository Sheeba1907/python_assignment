from io import StringIO
import sys

def print_formatted(number):
    width = len(bin(number)[2:])   
    for i in range(1, number + 1):
        decimal_val = str(i).rjust(width)
        octal_val = oct(i)[2:].rjust(width)        
        hex_val = hex(i)[2:].upper().rjust(width)  
        binary_val = bin(i)[2:].rjust(width)       
        print(decimal_val, octal_val, hex_val, binary_val)


def capture_output(number):
    """Return what print_formatted prints, as a list of strings."""
    buffer = StringIO()
    sys.stdout = buffer
    print_formatted(number)        
    sys.stdout = sys.__stdout__    
    return buffer.getvalue().strip().split("\n")