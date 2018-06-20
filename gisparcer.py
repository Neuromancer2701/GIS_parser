import csv
import os.path
from pygeocoder import Geocoder


"""     
main
"""

def main():

    addresskey = "LocAddr"
    postalkey  = "PostalCode"
    countystate = "Bedford County, Va"
    csv_file = "/opt/repos/GIS_parser/Bedford_County_Parcels.csv"
    gc = Geocoder("")
    gc.set_proxy("http://SK1033:Cheese29@cdcwsa02.commscope.com:3128")

    if os.path.isfile(csv_file):
        #print "Files exists."
        with open(csv_file, 'rb') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                street = row[addresskey].strip()
                if addresskey in row and len(street) > 0:
                    fulladdress = street + ", " + countystate
                    #print fulladdress
                    result = gc.geocode(fulladdress)
                    if result.count > 0 and result.administrative_area_level_2 == "Bedford County":
                        print result.postal_code
                        row[postalkey] = result.postal_code
    else:
        print "No File :(\n"

if __name__ == '__main__':
    main()
