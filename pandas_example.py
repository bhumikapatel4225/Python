import pandas as pd

orders = pd.read_csv('/Volumes/Bhumika/Work/Data Engineer/Python/shoefly.csv')

# Inspect first 5 lines
print(orders.head())

emails = orders['email']
frances_palmer = orders[(orders.first_name == 'Frances') & (orders.last_name == 'Palmer')]
comfy_shoes = orders[orders.shoe_type.isin (['clogs', 'boots', 'ballet flats'])]
orders['shoe_source'] = orders.shoe_material.apply(lambda x: 'animal' if x == 'leather' else 'vegan')
orders['salutation'] = orders.apply(lambda x: 'Dear Ms. ' + x.last_name if x.gender == 'female' else 'Dear Mr. '+ x.last_name, axis=1)

# lambda function

double_or_zero = lambda num: num*2 if num > 10 else 0
print(double_or_zero(15))
print(double_or_zero(5))

ends_in_a = lambda word: word[-1] == 'a'
print(ends_in_a("data"))
print(ends_in_a("aardvark"))

long_string = lambda input: len(input) > 12

print(long_string("short"))
print(long_string("photosynthesis"))

# even-odd
even_or_odd = lambda num: "even" if num %2 == 0 else "odd"
print(even_or_odd(10))
print(even_or_odd(5))

multiple_of_three = lambda num: "multiple of three" if num%3 == 0 else "not a multiple"
print(multiple_of_three(9))
print(multiple_of_three(10))

rate_movie = lambda rate: "I liked this movie" if rate > 8.5 else "This movie was not very good"
print(rate_movie(9.2))
print(rate_movie(7.2))

# ones' place
ones_place = lambda num: num % 10
print(ones_place(123))
print(ones_place(4))

# twice the square of num
double_square = lambda num: 2 * num * num
print(double_square(5))
print(double_square(3))

# The function should return num plus a random integer number between 1 and 10 (inclusive)
import random
add_random = lambda num: num + random.randint(1,10)
print(add_random(5))
print(add_random(100))

# get_last_name = lambda string: string.split()[-1]
# orders['last_name'] = orders.name.apply(get_last_name)


# Update Existing DataFrame
df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']
df['Is taxed?'] = 'Yes'  # yes for all row
df['Margin'] = df.Price - df['Cost to Manufacture']
print(df)

# Performing Column Operations
df = pd.DataFrame([
  ['JOHN SMITH', 'john.smith@gmail.com'],
  ['Jane Doe', 'jdoe@yahoo.com'],
  ['joe schmo', 'joeschmo@hotmail.com']
],
columns=['Name', 'Email'])

df['Lowercase Name'] = df.Name.apply(str.lower)
print(df)

# rename column name
df.rename(columns={'name': 'movie_title'}, inplace=True)
print(df)