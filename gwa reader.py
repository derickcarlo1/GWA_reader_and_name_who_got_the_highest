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
        profile = line.strip().rsplit(' ', 1)
        if len(profile) == 2:
            name, gwa = profile
            gwa = float(gwa)
            
            # Check if the current gwa is greater than the maximum gwa
            if gwa < max_gwa: 
                # Update the maximum gwa and student name
                max_gwa = gwa
                max_name = name
        
            # Check if the current name matches the input name
            if user_name.lower() == name.lower():
                user_gwa = gwa
        
    # Print the student with the highest GWA
    print(f"The student with the highest GWA is {max_name} with a GWA of {max_gwa:.2f}.")

    # Print the GWA of the user if it was found
    if user_gwa is not None:
        print(f"Your GWA is {user_gwa:.2f}.")
    else:
        print(f"Sorry, we could not find your GWA in our records.")
        
    print("\nThank you for using this toolSh\n")