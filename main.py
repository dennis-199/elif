# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Create one conditional to find whether “false” is in string str1.
# If so, assign variable output the string “False. You aren’t you?”.
# Check to see if “true” is in string str1 and if it
# is then assign “True! You are you!” to the variable output.
# If neither are in str1, assign “Neither true nor false!” to output.
str1 = "Today you are you! That is truer than true! There is no one alive who is you-er than you!"
if "false" in str1:
    output = "False. You aren't you?"
elif "true" in str1:
    output = "True! You are you!"
else:
    output = "Neither true nor false!"

