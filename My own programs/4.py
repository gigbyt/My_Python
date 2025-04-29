# Initialize an empty list
my_list = []

# Loop to take inputs from the user
while True:
  user_input = input("Enter a value to add to the list (or type 'done' to finish): ")
  if user_input.lower() == 'done':
    break
  my_list.append(user_input)

# Print the final list
print("Your list:", my_list)