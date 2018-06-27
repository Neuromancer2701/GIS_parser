import pandas as pd

postalkey = "PostalCode"

zipcode_data = "/opt/repos/GIS_parser/Bedford_County_Parcels_zipcodes.csv"


df = pd.read_csv(zipcode_data)


df_24503 = df[(df.PostalCode == 24503.0)]
df_24502 = df[(df.PostalCode == 24502.0)]

print len(df_24502)
print len(df_24503)