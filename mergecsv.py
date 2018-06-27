import csv
from collections import OrderedDict

csv_read = "/opt/repos/GIS_parser/Bedford_County_Parcels.csv"
csv_zipcodes = "/opt/repos/GIS_parser/Parcels_ZipCodes.csv"
objectkey = "OBJECTID"
postalkey = "PostalCode"

objectkey2 = '\xef\xbb\xbfOBJECTID'


zipDictionary = OrderedDict()
with open(csv_zipcodes, 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        zipDictionary[row[objectkey]] = row[postalkey]


with open(csv_read, 'rb') as csvfile:
    baseDictionary = csv.DictReader(csvfile)
    for row in baseDictionary:
        delete = False
        for key, value in zipDictionary.iteritems():
            if row[objectkey2] == key:
                row[postalkey] = value
                delete = True
                break
        if delete:
            del zipDictionary[row[objectkey2]]


    with open("Bedford_County_Parcels_zipcodes.csv", 'wb') as csvfile:
        writer = csv.DictWriter(csvfile)
        writer.writerows(baseDictionary)


