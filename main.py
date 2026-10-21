# import random means when we click "run" it grabs one of the options we choose.
import random 

# Here we create what the computer says when we run the script
options = ["no", "maybe", "yes"]

# When we say this we mean that pythoon should now choose one of these options that we created.
computer_guess = random.choice(options)

# Now here we tell python to guess between " no, maybe, yes"
print(f"I guess: {computer_guess}")

# I give this difficulty 7/10 but its my first pythoon script.
