# Get the current timestamp
current_time = Time.now

# Format the timestamp in different ways
new_time = current_time - (4 * 3600)
formatted_new_time = new_time.strftime("%Y-%m-%d %H:%M:%S")
puts "Formatted timestamp after subtracting 4 hours: #{formatted_new_time}"
