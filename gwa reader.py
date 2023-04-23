# Greetings for the user
user_name = input("\nHi, welcome! Please enter your name: ")
print(f"\nHi {user_name}! Please wait...Uploading your GWA data.\n")

# Set variables for maximum gwa and for the student name
max_gwa = 5.00
max_name = ""
user_gwa = None

# Open gwa.txt (read)
with open("studentgwa.txt", "r") as input_file:
    
    # Read gwa.txt line by line
    for line in input_file:
# Split each line into name and gwa
            
# Check if the current gwa is greater than the maximum gwa
                
# Check if the current name matches the input name
        
# Print the student with the highest GWA
    
# Print the GWA of the user if it was found