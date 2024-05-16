
#Data Mining the Internet Archive Collection
#https://programminghistorian.org/en/lessons/data-mining-the-internet-archive


sudo pip install internetarchive
sudo pip install pymarc
sudo pip install pandas

#Moley
https://archive.org/details/pub_newsweek-us?and%5B%5D=year%3A%5B1937+TO+1969%5D

#1585 results searching on pub_newsweek-us
https://archive.org/advancedsearch.php

# Newsweek (US Edition) 1945-07-23: Vol 26 Iss 4
# Source: IA1643324-06
# Volume: 26
# Issue: 4
# Published: Jul 23, 1945
# Views: 62
# Topics: General Interest Periodicals--United States, Political Science, Magazines, microfilm
# Collections: Newsweek (US Edition) 1933-2015, Serials in Microfilm, Periodicals
# Newsweek (US Edition) 1945-07-23: Volume 26 , Issue 4. Digitized from IA1643324-06 . Previous issue:


import internetarchive
search = internetarchive.search_items('collection:pub_newsweek-us')
print(search.num_found)

#Accessing an item
#https://archive.org/details/sim_newsweek-us_1945-07-23_26_4
item = internetarchive.get_item('sim_newsweek-us_1945-07-23_26_4')
item.download()

#downloading MARC records from a collection
search = internetarchive.search_items('collection:pub_newsweek-us')

for result in search:   
  print (result['identifier'])
  
  
#Marc records  
import internetarchive
import time

error_log = open('newsweek-marcs-errors.log', 'a')

search = internetarchive.search_items('collection:pub_newsweek-us')

for result in search:
    itemid = result['identifier']
    item = internetarchive.get_item(itemid)
    marc = item.get_file(itemid + '_marc.xml')
    try:
        marc.download()
    except Exception as e:
        error_log.write('Could not download ' + itemid + ' because of error: %s\n' % e)
        print "There was an error; writing to log."
    else:
        print ("Downloading " + itemid + " ...")
        time.sleep(1)

View(error_log)


#Newsweek doesn't have marc records?
#This is the file that names Moley: _djvu.xml
https://ia802507.us.archive.org/22/items/sim_newsweek-us_1945-07-16_26_3/sim_newsweek-us_1945-07-16_26_3_djvu.xml

import internetarchive

# Date range (modify if needed)
start_date = "19370401" 
end_date = "19390401"
 
#search = internetarchive.search_items('collection:pub_newsweek-us') 
search = internetarchive.search_items(f'(collection:pub_newsweek-us) AND date:[{start_date} TO {end_date}]')

for result in search:  
    print(result['identifier'])
    
#download results into a df
import pandas as pd

# Assuming 'search' is a list of dictionaries
data = {'identifier': [result['identifier'] for result in search]}
df = pd.DataFrame(data)

# Save DataFrame to CSV file
df.to_csv('results.csv', index=False)


#scraping for .pdf files
#https://help.archive.org/help/files-formats-and-derivatives-file-definitions-2/


import os
import time
import internetarchive

# Define the directory where you want to save the files
download_directory = '/Users/name/Code/Newsweek'

# Ensure the directory exists; if not, create it
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

# Define a list to store downloaded item identifiers
downloaded_items = []

# Open error log file
error_log = open('error_log.txt', 'w')

# Iterate over search results
for result in search:
    itemid = result['identifier']
    item = internetarchive.get_item(itemid)
    
    try:
        # Get the PDF file associated with the item
        pdf_file = item.get_file(itemid + '.pdf')
        # Download the PDF file
        pdf_file.download()
    except Exception as e:
        # Log errors
        error_log.write('Could not download ' + itemid + ' because of error: %s\n' % e)
        print("There was an error downloading", itemid, "; writing to log.")
    else:
        # Append successfully downloaded item identifier to the list
        downloaded_items.append(itemid)
        print("Downloading", itemid, "...")
        # Add some delay to avoid overwhelming the server
        time.sleep(1)

# Close the error log file
error_log.close()

# Print the list of successfully downloaded items
print("Downloaded items:", downloaded_items)



#scraping for _djvu.xml files
#https://help.archive.org/help/files-formats-and-derivatives-file-definitions-2/

for result in search:
    itemid = result['identifier']
    item = internetarchive.get_item(itemid)
    marc = item.get_file(itemid + '_djvu.xml')
    try:
        marc.download()
    except Exception as e:
        error_log.write('Could not download ' + itemid + ' because of error: %s\n' % e)
        print "There was an error; writing to log."
    else:
        print ("Downloading " + itemid + " ...")
        time.sleep(1)

View(error_log)


### Ended April 26. 
Sucessfully downloaded a full issue of Newsweek and a searchable pdf file. 
#/Users/robwells/Library/CloudStorage/Dropbox/Current_Projects/Moley project 2024/sim_newsweek-us_1945-07-23_26_4/sim_newsweek-us_1945-07-23_26_4.pdf

Found the xml file that names Moley. 
#/Users/robwells/Library/CloudStorage/Dropbox/Current_Projects/Moley project 2024/sim_newsweek-us_1945-07-23_26_4/sim_newsweek-us_1945-07-23_26_4_djvu.xml

Found the raw text from the OCR
#/Users/robwells/Library/CloudStorage/Dropbox/Current_Projects/Moley project 2024/sim_newsweek-us_1945-07-23_26_4/sim_newsweek-us_1945-07-23_26_4_djvu.txt

Now i need to associate the xml file and use it to extract the text



import pymarc

def get_place_of_pub(record):
    place_of_pub = record['1189']
    print (place_of_pub)

pymarc.map_xml(get_place_of_pub, '/Users/robwells/Library/CloudStorage/Dropbox/Current_Projects/Moley project 2024/1937 newsweek xml/sim_newsweek-us_1937-04-03_9_14_djvu.xml')





for item in search:
   print (item['identifier'])
  
import internetarchive

search = internetarchive.search_items('collection:bplscas')

for result in search:
    itemid = result['identifier']
    item = internetarchive.get_item(itemid)
    marc = item.get_file(itemid + '_marc.xml')
    marc.download()
    print "Downloading " + itemid + " ..."


#For one record
search = internetarchive.search_items('sim_newsweek-us_1945-07-23_26_4')

for result in search:
    itemid = result['identifier']
    item = internetarchive.get_item(itemid)
    marc = item.get_file(itemid + '_marc.xml')
    marc.download()
    print "Downloading " + itemid + " ..."


#View sqlite file
def create_connection(db_file):
 """ create a database connection to the SQLite database specified by the db_file :param db_file: database file :return: Connection object or None """ conn = None
try: 
    conn = sqlite3.connect(db_file) except Error as e: 
    print(e) return conn

def select_all_tasks(conn): 
""" Query all rows in the tasks table :param conn: the Connection object :return: """
    cur = conn.cursor() 
    cur.execute("SELECT * FROM tasks")           rows = cur.fetchall() for row in rows: print(row)

