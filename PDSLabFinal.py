# print("Hello World")

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print("ADDITION: ",a+b)
# print("DIFFERENCE: ",a-b)
# print("PRODUCT: ",a*b)
# print("QUOTIENT: ",a/b)
# print("FLOOR QUOTIENT: ",a//b)
# print("REMAINDER: ",a%b)
# print("EXPONENT: ",a**b)


# f = open("sample.txt","w")
# f.write("Hi\n")
# f.write("How\n")
# f.write("Are\n")
# f.write("You\n")
# f.close()

# f = open("sample.txt","r")
# con=f.read()
# print(con)
# f.close()

# f = open("sample.txt","a")
# f.write("This line is appended\n")
# f.close()

# print("AFTER APPENDING\n")

# f = open("sample.txt","r")
# con=f.read()
# print(con)
# f.close()


# import csv
# data=[["ID","NAME","MARKS"],
#       [1,"A",85],
#       [2,"B",75],
#       [3,"C",99]]
# f = open("data.csv","w",newline="")
# wo=csv.writer(f)
# wo.writerows(data)
# f.close()

# f = open("data.csv","r")
# ro=csv.reader(f)
# for i in ro:
#     print(i)
# f.close()



# f = open("sample.txt","w")
# f.write("Hi\n")
# f.write("How\n")
# f.write("Are\n")
# f.write("You\n")
# f.close()

# filename = "sample.txt"

# file = open(filename, "r")
# text = file.read()
# file.close()

# frequency = {}

# for char in text:
#     if char.isalpha():              # count only letters
#         if char in frequency:
#             frequency[char] += 1
#         else:
#             frequency[char] = 1

# print("Letter Frequency:")
# for letter in sorted(frequency):
#     print(letter, ":", frequency[letter])

# file.close()



# import numpy as np
# import random as rd 

# arr = np.array(10)
# a = np.array([1,2,3,4,5])
# b = np.array([10,20,30,40,50])
# print(a)
# print(b)
# print(a.ndim)

# print(a[:3])
# print(a[-2:])


# ar = np.random.rand(10)
# print(ar)
# print(ar.ndim)


# array = np.arange(1,10)
# print(array)
# print(array.reshape(3,3))







# import numpy as np
# import pandas as pd


# data = {
#     'Name': ['Alice', 'Bob ', 'Alice', 'Bob ', np.nan],
#     'Age': [25, 30, 25, 30, np.nan],
#     'Salary': [50000, 60000, 50000, 60000, 55000],
#     'Department': ['HR', 'IT', 'HR', 'IT', 'HR']
# }

# df = pd.DataFrame(data)
# print("Original DataFrame:\n", df)


# df["Age"].fillna(df["Age"].mean(),inplace=True)
# df["Name"].fillna("Biscuit",inplace=True)
# print("\n")
# print(df)


# df.drop_duplicates(inplace=True)
# print("\n")
# print(df)


# df["Age"] = df["Age"].astype(int)
# print("\n")
# print(df)


# df.rename(columns={"Salary":"Monthly_Salary"},inplace=True)
# print("\n")
# print(df)


# df['Name'] = df['Name'].str.upper()
# print("\n")
# print(df)


# filtered_df = df[df['Monthly_Salary'] > 55000]
# print("\n")
# print(filtered_df)


# grouped_df = df.groupby('Department')['Monthly_Salary'].mean()
# print("\n")
# print(grouped_df)


# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
# import pandas as pd

# x = np.array([1,2,3,4,5])
# y = np.array([2,4,6,8,10])
# plt.plot(x,y,color="blue",marker="o",label="y=2x")
# plt.title("LINE PLOT")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.legend()
# plt.show()


# cat=["A","B","C","D"]
# val=["10","20","30","40"]
# plt.bar(cat,val,color="red")
# plt.title("BAR CHART")
# plt.xlabel("CATEGORIES")
# plt.ylabel("VALUES")
# plt.show()


# data = np.random.randn(100)
# plt.hist(data,color="green",bins=15,edgecolor="black")
# plt.title("HISTOGRAM")
# plt.xlabel("VALUES")
# plt.ylabel("FREQUENCIES")
# plt.show()


# df = sns.load_dataset("tips")
# sns.scatterplot(x="total_bill",y="tip",hue="sex",color="pink",marker="o",data=df)
# plt.title("SCATTER PLOT")
# plt.xlabel("Total Bill")
# plt.ylabel("Tip")
# plt.show()


# df = sns.load_dataset("tips")
# sns.boxplot(x="day",y="total_bill",palette="Set2",hue="sex",data=df)
# plt.title("BOX PLOT")
# plt.xlabel("Day")
# plt.ylabel("Total Bill")
# plt.show()

# sns.pairplot(df)
# plt.title("PAIR PLOT")
# plt.show()


