"""Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the
score is out of range, print an error message. If the score is between 0.0 and 1.0,
print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
~~~
Enter score: 0.95 A ~~
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
Run the program repeatedly as shown above to test the various different values for input. """
##############


try:
    score = float(input("Enter your score: "))
    if score >= 0.90 and score <= 1.0:
        print("A")
    elif score >= 0.80 and score <= 0.89:
        print("B")
    elif score >= 0.70 and score <= 0.79:
        print("C")
    elif score >= 0.60 and score <= 0.69:
        print("D")
    elif score >= 0.0 and score <= 0.59:
        print("Fail")
    else:
        print("Bad Score")
except:
    print("Kindly enter the score bteween 0.0 to 0.9")