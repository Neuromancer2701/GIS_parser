import csv

csv_read = "/opt/repos/GIS_parser/Bedford_County_Parcels.csv"
csv_zipcodes = "/opt/repos/GIS_parser/Parcels_ZipCodes.csv"
objectkey = '\xef\xbb\xbfOBJECTID'
postalkey = "PostalCode"

zipDictionary = dict()
with open(csv_zipcodes, 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        zipDictionary[row[objectkey]] = row[postalkey]


with open(csv_read, 'rb') as csvfile:
    baseDictionary = csv.DictReader(csvfile)
    for row in baseDictionary:
        for row2 in zipDictionary:
            if row[objectkey] == row2[objectkey]:
                row[postalkey] = row2[postalkey]
                break

    with open("Bedford_County_Parcels_zipcodes.csv", 'rb') as csvfile:
        writer = csv.DictWriter(csvfile)
        writer.writerows(baseDictionary)


