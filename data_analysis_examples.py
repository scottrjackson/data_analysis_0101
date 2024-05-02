# beginning data analysis examples

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

number_list = [1, 4, 22, 89.33]
string_list = ["a", "c", "something", "else"]
mixed_list = [1, "c", 22, "something"]

number_array = np.array(number_list)
print(number_array)
type(number_array)
number_array.dtype

string_array = np.array(string_list)
print(string_array)
type(string_array)
string_array.dtype

mixed_array = np.array(mixed_list)
print(mixed_array)
type(mixed_array)
mixed_array.dtype

# what does an array get us?

# make a dictionary to hold some data
fruit_dictionary = {"apples" : 3.49,
                "bananas" : 1.79,
                "strawberries" : 5.99}

fruit_dictionary["bananas"]

fruit_prices = list(fruit_dictionary.values())
print(fruit_prices)

fruit_tax = 0.1

taxed_prices = []
for price in fruit_prices:
    taxed_price = price * (1 + fruit_tax)
    taxed_price = round(taxed_price, 2)
    taxed_prices.append(taxed_price)
print(taxed_prices)    

# list comprehension example
# new_list = [thing_to_do for var in iter]
taxed_prices2 = [round(price * (1 + fruit_tax), 2) for price in fruit_prices]
print(taxed_prices2)

taxed_prices3 = np.array(fruit_prices) * (1 + fruit_tax)
print(taxed_prices3)
taxed_prices3 = taxed_prices3.round(2)
print(taxed_prices3)

# arange
range(10)
print(np.arange(10))
print(np.arange(3, 9))
print(np.arange(3, 28, 3))

#############################
fruit_dictionary = {"apples" : 3.49,
                "bananas" : 1.79,
                "strawberries" : 5.99}

fruit_dictionary["bananas"] = 1.59

fruit_names = list(fruit_dictionary.keys())

fruit_data = {"fruit" : fruit_names,
              "price" : fruit_prices}
print(fruit_data)

fruit_dataframe = pd.DataFrame(data = fruit_data)
print(fruit_dataframe)

# using dataframe
fruit_dataframe.describe()
# a column is an object called a "Series"
type(fruit_dataframe["price"])
fruit_dataframe["price"].dtype
fruit_dataframe["price"].mean()

# reading a file
iris_dataframe = pd.read_csv("iris_data.csv")
print(iris_dataframe)
iris_dataframe.head(10)
iris_dataframe.tail(7)

iris_dataframe.describe()
iris_dataframe["Length"].mean()

# visualizing data with matplotlib
print(fruit_dataframe)

plt.bar(x = "fruit", height = "price", data = fruit_dataframe)
plt.show()

plt.scatter(x = "Length", y = "Width", data = iris_dataframe)
plt.show()

plt.hist("Length", data = iris_dataframe)
plt.show()