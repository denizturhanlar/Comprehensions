##################################################
# List Comprehensions

#TASK 1: Using the List Comprehension structure, capitalize the names of the numeric variables in the car_crashes data and add NUM to the beginning.
# ###############################################

# Expected Output
#
# # ['NUM_TOTAL',
# #  'NUM_SPEEDING',
# #  'NUM_ALCOHOL',
# #  'NUM_NOT_DISTRACTED',
# #  'NUM_NO_PREVIOUS',
# #  'NUM_INS_PREMIUM',
# #  'NUM_INS_LOSSES',
# #  'ABBREV']
#
#Notes:
#Non-numeric names should also grow.
#Must be done with a single list comp structure.

#import the libraries
import seaborn as sns
df = sns.load_dataset("car_crashes")

#by using list comprehensions
df = sns.load_dataset("car_crashes")
df.columns

["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]

#we can write without using comprehensions
df.columns
df.info()

NEW_COLUMNS =[]
for col in df.columns:
    if df[col].dtype != "O":
       NEW_COLUMNS.append("NUM_" + col.upper())
    else:
        NEW_COLUMNS.append(col.upper())


################################################
#TASK 2: Using the List Comprehension structure, write "FLAG" after the names of the variables in the car_crashes data that do not contain "no" in their names.


#Notes:
#Non-numeric names should also grow.
#Must be done with a single list comp structure

#Expected Output:
#
# # ['TOTAL_FLAG',
# #  'SPEEDING_FLAG',
# #  'ALCOHOL_FLAG',
# #  'NOT_DISTRACTED',
# #  'NO_PREVIOUS',
# #  'INS_PREMIUM_FLAG',
# #  'INS_LOSSES_FLAG',
# #  'ABBREV_FLAG']


#Using by List Comp
df = sns.load_dataset("car_crashes")
df.columns

[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]


#Without using bu list comp
df = sns.load_dataset("car_crashes")
df.columns

a = []
for col in df.columns:
    if "no" not in col:
        a.append(col.upper() + "_FLAG")
    else:
        a.append(col.upper())

a


# ###############################################
#Task 3: Using the List Comprehension structure, select the names of the variables that are DIFFERENT from the variable names given below and create a new dataframe.


og_list = ["abbrev", "no_previous"]

# Notes:
#First, create a new list named new_cols using list comprehension according to the list above.
#Then create a new df by selecting these variables with df[new_cols] and name it new_df.

#Expected Output:
#
# #    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# # 0 18.800     7.332    5.640          18.048      784.550     145.080
# # 1 18.100     7.421    4.525          16.290     1053.480     133.930
# # 2 18.600     6.510    5.208          15.624      899.470     110.350
# # 3 22.400     4.032    5.824          21.056      827.340     142.390
# # 4 12.000     4.200    3.360          10.920      878.410     165.630

# by using list comp
df = sns.load_dataset("car_crashes")
og_list = ["abbrev", "no_previous"]

new_columns = [col for col in df.columns if col not in og_list]

new_df =df[new_columns]

new_df.head()

#Without using bu list comp:
df = sns.load_dataset("car_crashes")
og_list = ["abbrev", "no_previous"]

b=[]
for col in df.columns:
    if col not in og_list:
        b.append(col)



