# Gunda Esra Altınışık Karaca

#######################
# PROJECT TASKS
#######################

#######################
# TASK 1: Answer the following questions.
#######################

# Question 1: Read the persona.csv file and show general information about the data set.

import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option("display.width", 500)
df = pd.read_csv("W2/persona.csv")

def check_df(dataframe, head=5):
    print("###################### Shape ######################")
    print(dataframe.shape)
    print("###################### Types ######################")
    print(dataframe.dtypes)
    print("###################### Head ######################")
    print(dataframe.head(head))
    print("###################### Tail ######################")
    print(dataframe.tail(head))
    print("###################### NA ######################")
    print(dataframe.isnull().sum())
    print("###################### Quantiles ######################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 1]).T)

check_df(df)

# Question 2: How many unique SOURCE are there? What are their frequencies?

df["SOURCE"].nunique()
df["SOURCE"].value_counts()

# Question 3: How many unique PRICE are there?

df["PRICE"].unique()

# Question 4: How many sales were made according to each different price?

df["PRICE"].value_counts()

# Question 5: How many sales were made from each country?

df["COUNTRY"].value_counts()

# Question 6: How much was earned from sales in total by country?

df.groupby("COUNTRY")["PRICE"].sum()

# Question 7: How many sales were made according to SOURCE types?

df["SOURCE"].value_counts()              # Source'a göre satış sayısı
df.groupby("SOURCE")["PRICE"].sum()      # Source kırılımında satış değişkeninin toplamı.

# Question 8: What are the PRICE averages by country?

df.groupby("COUNTRY")["PRICE"].mean()

# Question 9: What are the PRICE averages according to SOURCE?

df.groupby("SOURCE")["PRICE"].mean()

# Question 10: What are the PRICE averages in the COUNTRY-SOURCE breakdown?

df.groupby(["COUNTRY", "SOURCE"]).agg({"PRICE": ["mean"]})

#######################
# TASK 2: What are the average earnings in the COUNTRY, SOURCE, SEX, AGE breakdown?
#######################

df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": ["mean"]})

#######################
# TASK 3: Sort the output by PRICE.
#######################
# To better see the output in the previous question, apply the sort_values method to PRICE in decreasing order.
# Save the output as agg_df.

agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
agg_df

#######################
# TASK 4: Convert the names in the index into variable names.
#######################
# All variables except PRICE in the output of the third question are index names.
# Convert these names to variable names.
# Hint: reset_index()
# agg_df.reset_index(inplace=True)

agg_df.reset_index(inplace=True)

#######################
# TASK 5: Convert the AGE variable to a categorical variable and add it to agg_df.
#######################
# Convert the numeric variable Age to a categorical variable.
# Create the intervals in a way that you think will be convincing.
# For example: '0_18', '19_23', '24_30', '31_40', '41_70'

df["AGE"].min()
df["AGE"].max()
bins = [14, 18, 25, 40, 67]
labels = ["14_18", "19_25", "26_40", "41_67"]
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], bins=bins, labels=labels)
agg_df.head()

#######################
# TASK 6: Define new level based customers and add them to the data set as a variable.
#######################
# Define a variable called customers_level_based and add this variable to the data set.
# Attention!
# After creating customers_level_based values with list comp, these values need to be deduplicated.
# For example, there may be more than one of: USA_ANDROID_MALE_0_18
# It is necessary to take these to groupby and get the price averages.

agg_df["AGE_CAT"] = agg_df["AGE_CAT"].astype(str)
agg_df["customers_level_based"] = agg_df["COUNTRY"] + "_" + agg_df["SOURCE"] + "_" + agg_df["SEX"] + "_" + agg_df["AGE_CAT"]
agg_df.groupby("customers_level_based")["PRICE"].mean()
agg_df.head()

#######################
# TASK 7: Segment new customers (USA_ANDROID_MALE_0_18).
#######################
# Segment by PRICE,
# add the segments to agg_df with the name "SEGMENT",
# describe the segments

agg_df["PRICE"].hist()
agg_df["SEGMENT"] = pd.cut(agg_df["PRICE"], bins=[0, 29, 39, 60], labels=["low", "mid", "high"])
agg_df.groupby(["SEGMENT"]).agg({"PRICE": ["sum", "max", "mean"]})

#######################
# TASK 8: Classify new customers and estimate how much income they can bring.
#######################

def predict_sp(dataframe, customer_ıd):
    predict_s = dataframe.loc[dataframe["customers_level_based"] == customer_ıd, "SEGMENT"].mode()
    predict_p = dataframe.loc[dataframe["customers_level_based"] == customer_ıd, "PRICE"].mean()

    return pd.DataFrame({"Segment:": predict_s, "Price:": predict_p})

# To which segment does a 33-year-old Turkish woman using ANDROID belong and how much revenue on average is she expected
# to bring to?

predict_sp(agg_df, "tr_android_female_26_40")

# Which segment does a 35-year-old French woman using IOS belong to and how much revenue is she expected to bring to
# the company on average?

predict_sp(agg_df, "fra_ios_female_26_40")
