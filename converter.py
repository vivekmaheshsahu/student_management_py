import pandas as pd

# reading csv file
readIT = pd.read_csv("E:/FYND/Final Project/Data Creation /it.csv")

# csv file to save as table in html file
readIT.to_html("IT.html")

# assign it to a
# variable (string)
html_file = readIT.to_html()
