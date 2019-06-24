try:
    print("Student Result : ")
    Hin = int(input("Enter the marks of Hindi : "))
    Eng = int(input("Enter the marks of English : "))
    Maths = int(input("Enter the marks of Mathematics : "))
    Phy = int(input("Enter the marks of Physics : "))
    Che = int(input("Enter the marks of Chemistry : "))


    total_marks = Hin + Eng + Maths + Phy + Che
    print("Total marks obtained by Student ",total_marks)

    percentage = (total_marks * 100) / 500
    print("Student gets ", percentage, "% marks")

    if percentage < 33:
        print("Student is Fail")
    elif percentage >= 33 and percentage < 45:
        print("Student pass with third division")
    elif percentage >= 45 and percentage < 60:
        print("Student pass with second division")
    elif percentage >= 60 and percentage <=100:
        print("Student pass with First division")
    else:
        print("This is invalid result.")


except ValueError as error:
    print("You cannot enter invalid input --> This error is called : ",error)

except Exception as e: #for unknown error
    print("This error is called : ",e)

finally:
    print("Thanks for the result.")







