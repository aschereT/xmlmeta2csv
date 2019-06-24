#!/usr/bin/env python3

# https://www.geeksforgeeks.org/xml-parsing-python/
# https://stackoverflow.com/questions/1912434/how-do-i-parse-xml-in-python

import csv
from xml.dom import minidom
import sys


def parseXML(xmlfile):

    metaItems = []
    theKey = ""
    xmldoc = minidom.parse(xmlfile)
    keyList = xmldoc.getElementsByTagName('PropertyRef')
    for s in keyList:
        theKey = s.getAttribute('Name')

    itemlist = xmldoc.getElementsByTagName('Property')
    for s in itemlist:
        metaItem = {}
        metaItem['SystemName'] = s.getAttribute('Name')
        if metaItem['SystemName'] == theKey:
          metaItem['Unique'] = 1
        if s.hasAttribute('MaxLength'):
            metaItem['MaximumLength'] = s.getAttribute('MaxLength')
        annot = s.getElementsByTagName('Annotation')
        if annot != []:
            for t in annot:
                metaItem['LongName'] = t.getAttribute('String')
        metaItems.append(metaItem)
    return metaItems


def savetoCSV(metaItems, filename):

    # specifying the fields for csv file
    fields = ['SystemName', 'StandardName', 'LongName', 'DBName', 'ShortName', 'MaximumLength', 'DataType', 'Precision', 'Searchable', 'Interpretation', 'Alignment', 'UseSeparator', 'EditMaskID',
              'LookupName', 'MaxSelect', 'Units', 'Index', 'Minimum', 'Maximum', 'Default', 'Required', 'SearchHelpID', 'Unique', 'MetadataEntryID', 'ModTimeStamp', 'ForeignKeyName', 'ForeignField', 'InKeyIndex']

    # writing to csv file
    with open(filename, 'w') as csvfile:

                # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        writer.writerows(metaItems)


def main():
    if len(sys.argv) < 2:
        print("Usage: xmlmeta2csv <xml file>")
        return

    name = sys.argv[1]

    # parse xml file
    fields = parseXML(name)

    # store news items in a csv file
    savetoCSV(fields, name + '.csv')


if __name__ == "__main__":

    # calling main function
    main()
