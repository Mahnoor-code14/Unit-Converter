temp=float(input("Enter value to Convert temperature (C -> F,F -> C):"))
Unit=input("Enter unit of temperature:")
if Unit=="Fahrenhiet":
    F=(temp*9/5)+32
    print("Tempareture in Fahrenhiet:",F)
elif Unit=="Celsius":
    C=(temp-32)*5/9
    print("Tempareture in Calsius:",C)
else:
    print("Invalid Unit")