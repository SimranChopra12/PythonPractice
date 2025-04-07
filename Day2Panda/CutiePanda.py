import pandas as panda

#default index
df = panda.read_csv('employee_data.csv')
nums = [1, 2, 3, 4,5]
s = panda.Series(nums)
print(s)
print(type(nums))

#custom index
nums = [1, 2, 3, 4, 5]
s = panda.Series(nums, index=[1, 2, 3, 4, 5])
print(s)


data = {'Name': ['John', 'Mike', 'Sally', 'Anna', 'Bob', 'Liz'],
        'Age': [28, 34, 29, 42, 36, 24],
        'City': ['NY', 'LA', 'SF', 'CHI', 'DAL', 'MIA']}
df = panda.DataFrame(data, index=[1, 2, 3, 4, 5,6])
print(df.head(3))


# appending data to existing csv
newData = panda.DataFrame({
    'name': ['Sim'],
    'age': ['22']

})
# a = append
# header = false: no column name
# index = false: ensures a clean CSV file that includes only the columns from your DataFrame.
newData.to_csv('employee_data.csv', mode='a', header=False)
df = panda.read_csv('employee_data.csv')
print(df)
print("")
print("")

# deleting duplicates
df.drop_duplicates(inplace=True)
print(df)

