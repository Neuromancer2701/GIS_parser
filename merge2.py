import pandas as pd
csv_read = "/opt/repos/GIS_parser/Bedford_County_Parcels.csv"
csv_zipcodes = "/opt/repos/GIS_parser/Parcels_ZipCodes.csv"
postalkey = "PostalCode"

csv_base = pd.read_csv(csv_read)
csv_zip = pd.read_csv(csv_zipcodes)

csv_base[postalkey] = csv_zip[postalkey]
csv_base.to_csv('output.csv', index=False)