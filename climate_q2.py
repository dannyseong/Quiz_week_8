import matplotlib.pyplot as plt
import pandas as pd

# pandas setting
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 20)
pd.set_option('display.expand_frame_repr', False)

# read csv file using pandas
df = pd.read_csv('./climate.csv')

# By using 'tolist()' method, transform dataframe into list.
years = df['Year'].tolist()
co2 = df['CO2'].tolist()
temp = df['Temperature'].tolist()

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
# Change the sequence of code line between 28 and 29 for proper operation.
plt.savefig("co2_temp_2.png")
plt.show()

