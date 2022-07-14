import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import base64

# parse CSV into a DF, assuming local dir
df = pd.read_csv ('data.csv')

# Use Seaborn to generate a plt and save in PNG
sns.heatmap(df, cmap ='RdYlGn', linewidths = 0.30, annot = True)
plt.savefig('out.png')

# create an base 64 string from the PNG 
with open("out.png", "rb") as img_file:
    b64img = base64.b64encode(img_file.read())

# create an horrible HTML here for test purposes, what matters is the <img>
with open('out.html', 'w') as f:
    f.write("<!DOCTYPE html><html><head/><body><img style='display:block; ' id='base64image' src='data:image/png;base64,"+b64img.decode('utf-8')+" ' /></body></html>")

# Debug out here
# print(df)
# print(b64img.decode('utf-8'))


print ('ciao KP, mi devi una birra')
