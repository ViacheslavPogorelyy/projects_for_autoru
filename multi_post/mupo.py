#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, os.path
import glob
import shutil
import csv
import datetime


# In[7]:


now = datetime.datetime.now()


# In[9]:


day = str(now.day)
month = str(now.month)
year = str(now.year)
hour = str(now.hour)
minute = str(now.minute)
second = str(now.second)
microsecond = str(now.microsecond)


# In[17]:


csv_n = 'https://docs.google.com/spreadsheets/d/1FLgQtch4aZWjdVnRYh_ts9DReIS0gp2LvUyzt7E8XXk/export?format=csv'


# In[10]:


files = glob.glob("raw/*.csv")
file_count = len(files)
dir = "raw/"


# In[11]:


def ConvertToXML():
    for i in range(len(files)):

        # Take input.csv and set the file output to have a unique name
        csvFile = files[i]
        xmlFile = 'complete/13088' + day + month + year + hour + minute + second + str(i) + '.xml'

        # Remove directorry
        file = csvFile.strip(dir)

        # Open the csv file to read
        csvData = csv.reader(open(csvFile))

        # Open xml file created earlier and write a header
        xmlData = open(xmlFile, 'w')
        xmlData.write('<?xml version="1.0" encoding="ISO-8859-1" ?>' + "\n")
        xmlData.write('<Orders>' + "\n")
        xmlData.write('<Order>' + "\n")
        xmlData.write('<Order_Date><![CDATA[' + day + '/' + month +'/' + year + ']]></Order_Date>' + "\n")

        # Add your order ID format - example. ID-00000
        xmlData.write('<Order_ID><![CDATA[DT-13088' + day + month + year + hour + minute + second + str(i) + ']]></Order_ID>' + "\n")

        # Add your customer ID - example. ID000
        xmlData.write('<Customer_ID><![CDATA[DEPN000]]></Customer_ID>' + "\n")
        xmlData.write('<Products>' + "\n")

        # Parse the csv file and write the styled information to an xml file
        rowNum = 0

        for row in csvData:
            if rowNum == 0:
                tags = row
                for i in range(len(tags)):
                    tags[i] = tags[i].replace(' ', '_')
                    # Fix SKU
                    if tags[i] == '_SKU':
                        tags[i] = tags[i].replace('_SKU', 'SKU')
                    else:
                        tags[i] == tags[i]
                    # Fix Quantity
                    if tags[i] == '_Quantity':
                        tags[i] = tags[i].replace('_Quantity', 'Quantity')
                    else:
                        tags[i] == tags[i]

                    # Fix Item Description
                    if tags[i] == '_Item_Description':
                        tags[i] = tags[i].replace('_Item_Description', 'Item_Description')
                    else:
                        tags[i] == tags[i]

                    # Fix Product Variation Details
                    if tags[i] == '_Product_Variation_Details':
                        tags[i] = tags[i].replace('_Product_Variation_Details', 'Product_Variation_Details')
                    else:
                        tags[i] == tags[i]

            else:
                xmlData.write('<Item>' + "\n")
                for i in range(len(tags)):

                    if len(row) < 5:
                        while len(row) < 5:
                            row.append("null")

                    # Write to xml file
                    xmlData.write('<' + tags[i] + '>'                                       + '<![CDATA[' + row[i] + ']]>' + '</' + tags[i] + '>' + "\n")

                xmlData.write('</Item>' + "\n")

            rowNum +=1

        xmlData.write('</Products>' + "\n")
        xmlData.write('</Order>' + "\n")
        xmlData.write('</Orders>' + "\n")

        xmlData.close()
        MoveFile(file)

def MoveFile( FileToMove ):
    os.remove("raw/" + FileToMove)


# In[12]:


ConvertToXML()

