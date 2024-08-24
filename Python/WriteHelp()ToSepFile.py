import io
import sys

# Create a StringIO object to capture output
stdout_buffer = io.StringIO()

# Redirect stdout to the StringIO object
sys.stdout = stdout_buffer

# Call the function whose output you want to capture
help(exit)

# Get the captured output
captured_output = stdout_buffer.getvalue()

# Reset stdout to its original value
sys.stdout = sys.__stdout__

# Write the captured output to the file
with open("help_exit.txt", "w") as file:
    file.write(captured_output)
