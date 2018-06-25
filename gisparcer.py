import csv
import os.path
from pygeocoder import Geocoder
import subprocess

addresskey = "LocAddr"
postalkey = "PostalCode"
objectkey = '\xef\xbb\xbfOBJECTID'
fieldnames = [objectkey, addresskey, postalkey]

csv_read = "/opt/repos/GIS_parser/Bedford_County_Parcels.csv"
csv_zipcodes = "/opt/repos/GIS_parser/Parcels_ZipCodes.csv"


def initreader():
    if os.path.isfile(csv_read):
        with open(csv_read, 'rb') as csvfile:
            return csv.DictReader(csvfile)
    else:
        print "No File :(\n"
        return None


def writeobjectid(objectid, address, postalcode):

    with open(csv_zipcodes, 'a+') as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        row = dict()
        row[objectkey] = objectid
        row[addresskey] = address
        row[postalkey] = postalcode
        writer.writerow(row)


def findlastid():
    if os.path.isfile(csv_zipcodes):
        last_line = subprocess.check_output(["tail", "-1", csv_zipcodes])
        reader = csv.reader([last_line])
        rows = list(reader)
        return rows[0][0]
    else:
        return 0


def main():

    countystate = "Bedford County, Va"
    gc = Geocoder("")
    #gc.set_proxy("http://SK1033:Cheese29@cdcwsa02.commscope.com:3128")

    lastid = findlastid()
    if os.path.isfile(csv_read):
        with open(csv_read, 'rb') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if objectkey in row  and row[objectkey] < lastid:
                    continue
                street = row[addresskey].strip()
                if addresskey in row and len(street) > 0:
                    fulladdress = street + ", " + countystate
                    result = gc.geocode(fulladdress)
                    if result.count > 0 and result.administrative_area_level_2 == "Bedford County":
                        writeobjectid(row[objectkey], row[addresskey], result.postal_code)
                    else:
                        writeobjectid(row[objectkey], row[addresskey], 77777)
                else:
                    writeobjectid(row[objectkey], row[addresskey], 33333)
    else:
        print "No File :(\n"
        return None


if __name__ == '__main__':
    main()
