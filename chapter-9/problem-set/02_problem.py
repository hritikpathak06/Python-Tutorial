user_name = input("Enter Your Name: ")
user_score = int(input("Enter The Score: "))


def high_score(score, username):
    with open("hi_score.txt", "a") as fs:
        fs.write(f"{username}: {score}\n")


high_score(user_score, user_name)