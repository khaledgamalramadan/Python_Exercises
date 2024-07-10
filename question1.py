# Q1:

amount = 47.28
print("The bill amount is: ", amount)
tip_service = 0.15 
tip_amount= amount * tip_service    

total_amount = amount + tip_amount  

Each_person = total_amount /2        

print(f"Each person needs to pay: {Each_person:.2f} dollars")

#Q2
print("----------- #Q2 ----------------")
num1 = float(input("Enter first number : "))

num2 = float(input("Enter second number : "))

result = num1 / num2
print(f"The result is : {result:.2f}")

#Q3
print("----------- #Q3 ----------------")
word1 ,word2 ,word3, word4,word5,word6,word7= "How","do","you","like"," }{","so","far?"
print(word1 +" "+ word2 +" "+ word3 +" "+ word4 +" "+ word5 +" "+ word6 +" "+ word7)

#Q4
print("----------- #Q4 ----------------")
word7 = word7.replace('?', '!')
print(word1 +" "+ word2 +" "+ word3 +" "+ word4 +" "+ word5 +" " + word6 + " "+ word7)

#Q5
print("----------- #Q5 ----------------")
statement = input("Please enter a statement: ")
length_of_statement = len(statement)
print(f"The length of the statement is: {length_of_statement}")

#Q6
print("----------- #Q6 ----------------\n")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide \n")

Choose_op = input("Choose operation from (1,2,3,4): ")
if Choose_op in ['1','2','3','4']:
  number1   = float( input("Enter The first number : "))
  number2   = float( input("Enter The second number : "))

  if Choose_op == '1':
    {
      print(f"The result is : {number1 + number2}")
    }
  elif Choose_op == '2':
    {
      print(f"The result is : {number1 - number2}")
    }
  elif Choose_op == '3' :
    {
      print(f"The result is : {number1 * number2}")
    }
  elif Choose_op == '4' :
    {
      print(f"The result is : {number1 / number2}")
    }
else:
    {
      print("Invalid operation")
    }


