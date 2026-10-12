def Quiz1():
    #=============================================================#
    # Quiz 1: Instantiating a Shirt Object
    # Scenario:
    # ==========
    # You've seen what a class looks like and how to instantiate an object.
    # Now it's your turn to write code that instantiates a shirt object.
    # ==========
    # Task:
    # ==========
    # The `shirt_exercise.ipynb` file has an exercise to help guide you
    # through coding with an object in Python. Fill out the TODOs in each
    # section of the Jupyter notebook. You can find a solution in the
    # `answer.py` file. First, run this code cell below to load the `Shirt` class.
    # ==========
    # Solution:
    # ==========
    print("Quiz 1: Instantiating a Shirt Object")

    class Shirt:

        def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
            self.color = shirt_color
            self.size = shirt_size
            self.style = shirt_style
            self.price = shirt_price
    
        def change_price(self, new_price):
            self.price = new_price
        
        def discount(self, discount):
            return self.price * (1 - discount)

    ### TODO:
    # instantiate a shirt object with the following characteristics:
    # color red, size S, style long-sleeve, and price 25
    # store the object in a variable called shirt_one
    shirt_one = Shirt('red', 'S', 'long-sleeve', 25)
    
    ### TODO:
    # print the price of the shirt using the price attribute
    print("shirt_one.price = ", shirt_one.price)
    # use the change_price method to change the price of the shirt to 10
    shirt_one.change_price(10)
    # print the price of the shirt using the price attribute
    print("shirt_one.price after modification = ", shirt_one.price)
    # use the discount method to print the price of the shirt with a 12% discount
    print("shirt_one.price after discount 12% = ", shirt_one.discount(.12))
    
    ### TODO:
    # instantiate another object with the following characteristics:
    # color orange, size L, style short-sleeve, and price 10
    # store the object in a variable called shirt_two
    shirt_two = Shirt('orange', 'L', 'short-sleeve', 10)
    
    ### TODO:
    # calculate the total cost of shirt_one and shirt_two
    # store the results in a variable called total
    total = shirt_one.price + shirt_two.price
    
    ### TODO:
    # use the shirt discount method to calculate the total cost if
    # shirt_one has a discount of 14% and shirt_two has a discount
    # of 6%
    # store the results in a variable called total_discounted
    total_discounted = shirt_one.discount(.14) + shirt_two.discount(.06)
    
    print("#=============================================================#")
    #=============================================================#

def Quiz2():
    #=============================================================#
    # Quiz 2: Pants Class
    # Scenario:
    # ==========
    # Write a Pants class with the following characteristics:
    # * the class name should be `Pants`
    # * the class attributes should include
    #  * `color`
    #  * `waist_size`
    #  * `length`
    #  * `price`
    # * the class should have an init function that initializes
    #   all of the attributes
    # ==========
    # Task:
    # ==========
    # * the class should have two methods
    #  * `change_price()` a method to change the price attribute
    #  * `discount()` to calculate a discount
    # ==========
    # Solution:
    # ==========
    print("Quiz 2: Pants Class")
    ### TODO:
    # code a Pants class with the following attributes
    # color (string) eg 'red', 'yellow', 'orange'
    # waist_size (integer) eg 8, 9, 10, 32, 33, 34
    # length (integer) eg 27, 28, 29, 30, 31
    # price (float) eg 9.28

    ### TODO: Declare the Pants Class 
    class Pants:

        ### TODO: write an __init__ function to initialize the attributes
        def __init__(self, patns_color, patns_waist_size, patns_length, patns_price):
            self.color = patns_color
            self.waist_size = patns_waist_size
            self.length = patns_length
            self.price = patns_price

        ### TODO: write a change_price method:
        #    Args:
        #        new_price (float): the new price of the shirt
        #    Returns:
        #        None
        def change_price(self, new_price):
            self.price = new_price

        ### TODO: write a discount method:
        #    Args:
        #        discount (float): a decimal value for the discount. 
        #            For example 0.05 for a 5% discount.
        #
        #    Returns:
        #        float: the discounted price
        def discount(self, discout_percentage):
            return self.price * (1 - discout_percentage)
            
    print("#=============================================================#")
    #=============================================================#

def Quiz3():
    #=============================================================#
    # Quiz 3: SalesPerson Class
    # Scenario:
    # ==========
    # The Pants class and Shirt class are quite similar. Here is an
    # exercise to give you more practice writing a class. **This
    # exercise is trickier than the previous exercises.**
    # ==========
    # Task:
    # ==========
    # Write a SalesPerson class with the following characteristics:
    # * the class name should be `SalesPerson`
    # * the class attributes should include
    #  * `first_name`
    #  * `last_name`
    #  * `employee_id`
    #  * `salary`
    #  * `pants_sold`
    #  * `total_sales`
    # * the class should have an init function that initializes
    #   all of the attributes
    # * the class should have four methods
    #  * `sell_pants()` a method to change the price attribute
    #  * `calculate_sales()` a method to calculate the sales
    #  * `display_sales()` a method to print out all the pants sold
    #    with nice formatting
    #  * `calculate_commission()` a method to calculate the salesperson
    #    commission based on total sales and a percentage
    # ==========
    # Solution:
    # ==========
    print("Quiz 3: SalesPerson Class")
    ### TODO:
    #   Code a SalesPerson class with the following attributes
    #   - first_name (string), the first name of the salesperson
    #   - last_name (string), the last name of the salesperson
    #   - employee_id (int), the employee ID number like 5681923
    #   - salary (float), the monthly salary of the employee
    #   - pants_sold (list of Pants objects), 
    #            pants that the salesperson has sold 
    #   - total_sales (float), sum of sales of pants sold

    ### TODO: Declare the SalesPerson Class 
    class Pants:
        ### TODO: write an __init__ function to initialize the attributes
        def __init__(self, patns_color, patns_waist_size, patns_length, patns_price):
            self.color = patns_color
            self.waist_size = patns_waist_size
            self.length = patns_length
            self.price = patns_price

        ### TODO: write a change_price method:
        #    Args:
        #        new_price (float): the new price of the shirt
        #    Returns:
        #        None
        def change_price(self, new_price):
            self.price = new_price

        ### TODO: write a discount method:
        #    Args:
        #        discount (float): a decimal value for the discount. 
        #            For example 0.05 for a 5% discount.
        #
        #    Returns:
        #        float: the discounted price
        def discount(self, discout_percentage):
            return self.price * (1 - discout_percentage)
        
    class SalesPerson:
        ### TODO: write an __init__ function to initialize the attributes
        ###    Input Args for the __init__ function:
        #        first_name (str)
        #        last_name (str)
        #        employee_id (int)
        #        salary (float)
        #
        # You can initialize pants_sold as an empty list
        # You can initialize total_sales to zero.
        #
        ###
        def __init__ (self, person_first_name, person_last_name, person_employee_id, person_salary):
            self.first_name = person_first_name
            self.last_name = person_last_name
            self.employee_id = person_employee_id
            self.salary = person_salary
            self.pants_sold = []
            self.total_sales = 0

        ### TODO: write a sell_pants method:
        #
        #    This method receives a Pants object and appends
        #    the object to the pants_sold attribute list
        #
        #    Args:
        #        pants (Pants object): a pants object
        #    Returns:
        #        None
        def sell_pants(self, pants_object):
            self.pants_sold.append(pants_object)

        ### TODO: write a display_sales method:
        #    
        #    This method has no input or outputs. When this method 
        #    is called, the code iterates through the pants_sold list
        #    and prints out the characteristics of each pair of pants
        #    line by line. The print out should look something like this
        #
        #   color: blue, waist_size: 34, length: 34, price: 10
        #   color: red, waist_size: 36, length: 30, price: 14.15
        ###
        def display_sales(self):
            for pants in self.pants_sold:
                print("color: {}, waist_size: {}, length: {}, price: {}".format(pants.color, pants.waist_size, pants.length, pants.price))


        ### TODO: write a calculate_sales method:
        #      This method calculates the total sales for the sales person.
        #      The method should iterate through the pants_sold attribute list
        #      and sum the prices of the pants sold. The sum should be stored
        #      in the total_sales attribute and then return the total.
        #      
        #      Args:
        #        None
        #      Returns:
        #        float: total sales
        ###
        def calculate_sales(self):
            self.total_sales = 0
            for pants in self.pants_sold:
                self.total_sales += pants.price
            return self.total_sales

        ### TODO: write a calculate_commission method:
        #
        #   The salesperson receives a commission based on the total
        #   sales of pants. The method receives a percentage, and then
        #   calculate the total sales of pants based on the price,
        #   and then returns the commission as (percentage * total sales)
        #
        #    Args:
        #        percentage (float): comission percentage as a decimal
        #
        #    Returns:
        #        float: total commission
        ###
        def calculate_commission(self, percentage):
            return self.calculate_sales() * percentage
    
    pants_one = Pants('red', 35, 36, 15.12)
    pants_two = Pants('blue', 40, 38, 24.12)
    pants_three = Pants('tan', 28, 30, 8.12)

    salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)

    salesperson.sell_pants(pants_one)    
    salesperson.sell_pants(pants_two)
    salesperson.sell_pants(pants_three)

    salesperson.display_sales()
    print("#=============================================================#")
    #=============================================================#

def Quiz4():
    #=============================================================#
    # Quiz 4: Inheritance Exercise Clothing
    # Scenario:
    # ==========
    # The following code contains a Clothing parent class and two
    # children classes: Shirt and Pants.
    # ==========
    # Task:
    # ==========
    # Your job is to code a class called Blouse. Read through the
    # code and fill out the TODOs. Then check your work with the
    # unit tests
    # at the bottom of the code.
    # ==========
    # Solution:
    # ==========
    print("Quiz 4: Inheritance Exercise Clothing")
    class Clothing:
    
        def __init__(self, color, size, style, price):
            self.color = color
            self.size = size
            self.style = style
            self.price = price
        
        def change_price(self, price):
            self.price = price
        
        def calculate_discount(self, discount):
            return self.price * (1 - discount)

        # TODO: Add a method to the clothing class called calculate_shipping.
        #   The method has two inputs: weight and rate. Weight is a float
        #   representing the weight of the article of clothing. Rate is a float
        #   representing the shipping weight. The method returns weight * rate
        def calculate_shipping(self, weight, rate):
            return weight * rate

        
    class Shirt(Clothing):

        def __init__(self, color, size, style, price, long_or_short):

            Clothing.__init__(self, color, size, style, price)
            self.long_or_short = long_or_short

        def double_price(self):
            self.price = 2*self.price
    
    class Pants(Clothing):

        def __init__(self, color, size, style, price, waist):

            Clothing.__init__(self, color, size, style, price)
            self.waist = waist

        def calculate_discount(self, discount):
            return self.price * (1 - discount / 2)
    
    # TODO: Write a class called Blouse, that inherits from the Clothing class
    # and has the the following attributes and methods:
    #   attributes: color, size, style, price, country_of_origin
    #     where country_of_origin is a string that holds the name of a 
    #     country
    #
    #   methods: triple_price, which has no inputs and returns three times
    #     the price of the blouse
    #
    #
    class Blouse(Clothing):

        def __init__(self, color, size, style, price, country_of_origin):
            Clothing.__init__(self, color, size, style, price)
            self.country_of_origin = country_of_origin
        
        def triple_price(self):
            return 3 * self.price
            
    print("#=============================================================#")
    #=============================================================#

def main():
    print("=" * 60)
    print("OOP Quiz System")
    print("=" * 60)
    print()
    print("Available Quizzes:")
    print("Quiz 1: Instantiating a Shirt Object")
    print("Quiz 2: Pants Class")
    print("Quiz 3: SalesPerson Class")
    print("Quiz 4: Inheritance Exercise Clothing")
    print("0. Exit")
    print()
    while True:
        try:
            choice = int(input("Enter your choice (0-8): "))
            print()
            if choice == 0:
                print("Goodbye!")
                break
            elif choice == 1:
                Quiz1()
            elif choice == 2:
                Quiz2()
            elif choice == 3:
                Quiz3()
            elif choice == 4:
                Quiz4()
        except ValueError:
                print("Invalid input. Please enter a number.")
    
    print("\n" + "-" * 60 + "\n")

if __name__ == "__main__":
    main()