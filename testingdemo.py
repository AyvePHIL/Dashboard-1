# Here we go
import pandas as pd
import matplotlib.pyplot as plt
def expanddf():
    pd.set_option('display.max_rows', 100)
    pd.set_option('display.max_columns', 10)
    pd.set_option('display.width', 30)
    pd.set_option('display.max_colwidth', 10)
expanddf()
directory = "C:\\Users\\phila\\OneDrive\\Desktop\\Data Science\\SampleCSVFile_2kb.csv"
df = pd.read_csv(directory)
df.plot(x="Muhammed MacIntyre", y = 3)
plt.show()
print(df)
