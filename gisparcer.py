import csv
import os.path


"""     
main
"""
def main():
    kml_file = "/opt/repos/GIS_parser/Bedford_County_Parcels.csv"
    if os.path.isfile(kml_file):
        print "Files exists."
        with open(kml_file, 'rb') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print row
    else:
        print "No File :(\n"

if __name__ == '__main__':
    main()