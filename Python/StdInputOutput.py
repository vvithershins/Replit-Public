import sys

# Write to stdout without newline
sys.stdout.write("Hello world\n")  
sys.stdout.write('What is your name? ')
sys.stdout.flush()  # Force the output to be written immediately

# Read a single line of input
name = sys.stdin.readline()

# Write the output to stdout
sys.stdout.write("Hello, " + name)