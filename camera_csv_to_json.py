"""
1. Understand CSV Structure: Rows & Columns
- Rows are distinct devices
- Columns have specific values/attributes:

Search Source
( Shipper )
Sold by/Retailer
Keyword(s)
Link
Device Name
Brand
-buffer1-
Overview = Col_val 7
-buffer2-
Specifications = Col_val 9
Type
\n
"""

"""
2. Read CSV into Python Structure

3. Look at First 5-10 Device "Overviews" & Identify Intestin Keywords

"""
import csv

devices = []

with open("iot.tsv", newline='') as csv_file:
  csvReader = csv.reader(csv_file,delimiter="\t")
  for row in csvReader:
    devices.append( {"src" : row[0].lower(),
      "shipr":row[1].lower(),
      "retailer":row[2].lower(),
      "name":row[5].lower(),
      "txt1":row[7].lower(),
      "txt2":row[9].lower(),
      "txtAll":row[7].lower() + " " + row[9].lower(),
      "ptype":row[10].lower() })

# ind = {}
# i = 0
# for key in devicesb.keys():
#   ind.update( {i:list(devices.keys())[i] }  )
#   i+= 1

# Device Ontology
# Device = Connectivity Wifi PoE Other
#
#
#
#
#
#
#
#
#
#
#
#
#

