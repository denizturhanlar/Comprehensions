##################################################
# List Comprehensions

# # GÖREV 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
# ###############################################

# Beklenen Çıktı
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
#Notlar:
#Numerik olmayanların da isimleri büyümeli.
#Tek bir list comp yapısı ile yapılmalı.

#kütüpahaneyi import edelim
import seaborn as sns
df = sns.load_dataset("car_crashes")

#List Comp ile yapalım önce:
df = sns.load_dataset("car_crashes")
df.columns

["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]

#Klasik olarak yani list comp kullanmadan da yapabilirdik:
df.columns
df.info()

NEW_COLUMNS =[]
for col in df.columns:
    if df[col].dtype != "O":
       NEW_COLUMNS.append("NUM_" + col.upper())
    else:
        NEW_COLUMNS.append(col.upper())


################################################
# # GÖREV 2: List Comprehension yapısı kullanarak car_crashes verisindeki isminde "no" barındırmayan değişkenlerin isimlerininin sonuna "FLAG" yazınız.


#Notlar:
#Tüm değişken isimleri büyük olmalı.
#Tek bir list comp ile yapılmalı.

#Beklenen çıktı:
#
# # ['TOTAL_FLAG',
# #  'SPEEDING_FLAG',
# #  'ALCOHOL_FLAG',
# #  'NOT_DISTRACTED',
# #  'NO_PREVIOUS',
# #  'INS_PREMIUM_FLAG',
# #  'INS_LOSSES_FLAG',
# #  'ABBREV_FLAG']


#List Comp kullanarak yazıyoruz:
df = sns.load_dataset("car_crashes")
df.columns

[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]


#List Comp kullanmadan da yazabilirdik:
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
# # Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.


og_list = ["abbrev", "no_previous"]

#Notlar:
#Önce yukarıdaki listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
#Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz adını new_df olarak isimlendiriniz.

# # Beklenen çıktı:
#
# #    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# # 0 18.800     7.332    5.640          18.048      784.550     145.080
# # 1 18.100     7.421    4.525          16.290     1053.480     133.930
# # 2 18.600     6.510    5.208          15.624      899.470     110.350
# # 3 22.400     4.032    5.824          21.056      827.340     142.390
# # 4 12.000     4.200    3.360          10.920      878.410     165.630

# List Comp kullanarak yazalım:
df = sns.load_dataset("car_crashes")
og_list = ["abbrev", "no_previous"]

new_columns = [col for col in df.columns if col not in og_list]

new_df =df[new_columns]

new_df.head()

#List comp kullanmadan da yazabilirdik :
df = sns.load_dataset("car_crashes")
og_list = ["abbrev", "no_previous"]

b=[]
for col in df.columns:
    if col not in og_list:
        b.append(col)



