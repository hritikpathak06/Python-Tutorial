
# Quetsion 1==> Print the pattern
# *
# **
# ***
# ****



for i in range(1, 5):  # Outer loop for rows
    for j in range(1, i + 1):  # Inner loop for columns
        print("*", end="")  # Print * without a newline
    print()  # Print a newline after each row