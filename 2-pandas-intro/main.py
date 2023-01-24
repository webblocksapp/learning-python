import pandas as pd

# Creates an indexed series of numbers
series = pd.Series([5, 10, 15, 20, 25])
print(series)

# Prints the info at index 3
print(series[3])

# Creates a data frame
lst = ['Hola', 'mundo', 'robótico']
df = pd.DataFrame(lst)
print(df)

# Complex data structure printed as a table using a data frame
data = {'Name': ['Juan', 'Ana', 'Jose', 'Arturo'],
        'Age': [25, 18, 23, 27], 'Country': ['MX', 'CO', 'BR', 'MX']}

df = pd.DataFrame(data)
print(df)

# Prints only the columns Name and Country
print(df[['Name', 'Country']])

# Read csv file and prints first 5 elements
data = pd.read_csv('files/songs-2018.csv')
print(data.head(5))

# Stores the artists column
artists = data.artists
print(artists)

# Retrieves the artist at index 5
artist = artists[5]
print(artist)

# Retrieves the details of a record from index 15
detail = data.iloc[15]
print(detail)

# Retrieves data at the end
print(data.tail())

# Retrieves the length of the file
print(data.shape)

# Retrieves column tags
print(data.columns)

# Gives a description of a specific column
print(data['tempo'].describe())

# Orders the data
print(data.sort_index(axis=0, ascending=False))
