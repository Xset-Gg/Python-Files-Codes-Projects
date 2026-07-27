def calculate_percentage_diff(a, b):

    difference = a - b
    
    percentage = (difference * 100) / a
    return percentage


result = calculate_percentage_diff(80, 60)
print(result)

a = 50
b = 10
profit = calculate_percentage_diff(a, b)

print(profit)


profit = calculate_percentage_diff(a, b)


print(type(profit))



def calculate_percentage_diff(a:float, b: float)-> float:

    difference = a - b
    
    percentage = (difference * 100) / a
    return percentage 


# First, define the missing function so Python knows what it is
def calc_total_expanse(*expenses):
    total = sum(expenses)
    print(f"Total expense: {total}")

# Now, define your first function
def calculate_percentage_diff(*args):
    print("Arguments passed:", args)
    # This will now work because the function is defined above
    calc_total_expanse(2, 3, 5)

# Test the function
calculate_percentage_diff(80, 60)


name1 = "abubkar"
salary1 = 800000

name2 = "azan"
salary2 = 400000

# 1. This function ONLY does the math and returns the result
def calculate_bonus(salary, bonus_percentage=10):
    # Let's assume a 10% bonus for this calculation
    return salary * (bonus_percentage / 100)

# 2. Call the function and print the results outside of it
print(f"{name1}'s bonus: {calculate_bonus(salary1)}")
print(f"{name2}'s bonus: {calculate_bonus(salary2)}")
  
class Employee:
    def __init__(self,name,salary):
       self.name=name
       self.salary=salary
       
       # Bug 1: This function is inside __init__ (nested), 
       # so it cannot be called on the employee object later.
       def calculate_bonus(self):
          return self.salary * 0.10
          
       # Bug 2: Creating the object inside the constructor 
       # of its own class will cause a crash/infinite loop if run.
       emp1= Employee("abubkar",80000000)
       emp1.salary

  from google import genai
client = genai.Client()
abu = client.models.generate_contebt(
    model = "my name is abubkar",
    ali = "my name is azan"
)
print(abu.text)


from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in a few words"
)

print(interaction.output_text)

