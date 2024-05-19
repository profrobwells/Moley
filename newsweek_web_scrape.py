
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


 #-------------
#Download articles by sample defined year stratified sample
 
import os
import internetarchive
from requests.exceptions import ReadTimeout

# Define the stratified sample
sample = [
      "sim_newsweek-us_1952-01-21_39_3", 
      "sim_newsweek-us_1952-02-18_39_7" ,
      "sim_newsweek-us_1952-03-03_39_9", 
      "sim_newsweek-us_1952-04-14_39_15",
      "sim_newsweek-us_1952-05-19_39_20",
      "sim_newsweek-us_1952-06-23_39_25",
      "sim_newsweek-us_1952-07-21_40_3", 
      "sim_newsweek-us_1952-08-18_40_7", 
      "sim_newsweek-us_1952-09-22_40_12",
      "sim_newsweek-us_1952-10-27_40_17",
      "sim_newsweek-us_1952-11-24_40_22",
      "sim_newsweek-us_1952-12-29_40_27"
]

# Define the directory where you want to save the files within your home directory
home_directory = os.path.expanduser("~")
download_directory = os.path.join(home_directory, 'Code', 'Moley', 'Newsweek_52')

if not os.path.exists(download_directory):
    os.makedirs(download_directory)

print(f"Files will be saved in: {download_directory}")

# Construct the query
query = ' OR '.join([f'identifier:{issue}' for issue in sample])

# Perform the search and download the files
search = internetarchive.search_items(query)

# Function to download item with retry mechanism
def download_item(item, destdir, retries=3):
    for attempt in range(retries):
        try:
            item.download(glob_pattern='*.pdf', destdir=destdir)
            print(f"Downloaded {item.identifier} to {destdir}")
            break
        except ReadTimeout:
            if attempt < retries - 1:
                print(f"Timeout occurred, retrying... ({attempt + 1}/{retries})")
            else:
                print(f"Failed to download {item.identifier} after {retries} attempts")

# Iterate over the search results and download
for result in search:
    identifier = result['identifier']
    item = internetarchive.get_item(identifier)
    download_item(item, download_directory)


 #--------------
 1937 sample
 sample = [
    "sim_newsweek-us_1937-01-09_9_2",
    "sim_newsweek-us_1937-02-27_9_9",
    "sim_newsweek-us_1937-03-13_9_11",
    "sim_newsweek-us_1937-04-10_9_15",
    "sim_newsweek-us_1937-05-22_9_21",
    "sim_newsweek-us_1937-06-05_9_23",
    "sim_newsweek-us_1937-07-31_10_5",
    "sim_newsweek-us_1937-08-14_10_7",
    "sim_newsweek-us_1937-09-06_10_10",
    "sim_newsweek-us_1937-10-25_10_17",
    "sim_newsweek-us_1937-11-15_10_20",
    "sim_newsweek-us_1937-12-06_10_23"
]

 
 1948 sample
 sample = [
    "sim_newsweek-us_1948-01-26_31_4", 
    "sim_newsweek-us_1948-02-09_31_6",
    "sim_newsweek-us_1948-03-01_31_9", 
    "sim_newsweek-us_1948-04-19_31_16",
    "sim_newsweek-us_1948-05-10_31_19",
    "sim_newsweek-us_1948-06-07_31_23",
    "sim_newsweek-us_1948-07-26_32_4", 
    "sim_newsweek-us_1948-08-09_32_6", 
    "sim_newsweek-us_1948-09-06_32_10",
    "sim_newsweek-us_1948-10-18_32_16",
    "sim_newsweek-us_1948-11-15_32_20",
    "sim_newsweek-us_1948-12-06_32_23"
]
 
 
 
 #-------------------------#
 
 
#using simple date range
import internetarchive

# Date range (modify if needed)
start_date = "19480101" 
end_date = "19680101"

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
df.to_csv('newsweek_index_48_68_results.csv', index=False)


 
 
#search by date range to build an index 
#search = internetarchive.search_items('collection:pub_newsweek-us') 
search = internetarchive.search_items(f'(collection:pub_newsweek-us) AND date:[{start_date} TO {end_date}]')

# Construct the query
query = ' OR '.join([f'identifier:{issue}' for issue in sample])

# Perform the search
search = internetarchive.search_items(query)

for result in search:  
    print(result['identifier'])
    
    
    
    
    
#-----------------------------------------    
    
#download results into a df
import pandas as pd

# Assuming 'search' is a list of dictionaries
data = {'identifier': [result['identifier'] for result in search]}
df = pd.DataFrame(data)

# Save DataFrame to CSV file
#df.to_csv('results.csv', index=False)


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


#-------------------------------------------------------

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



#Stratified sample for 1937 (see newsweeekscraper.rmd)
 [1] "sim_newsweek-us_1937-01-09_9_2"  
 [2] "sim_newsweek-us_1937-02-27_9_9"  
 [3] "sim_newsweek-us_1937-03-13_9_11" 
 [4] "sim_newsweek-us_1937-04-10_9_15" 
 [5] "sim_newsweek-us_1937-05-22_9_21" 
 [6] "sim_newsweek-us_1937-06-05_9_23" 
 [7] "sim_newsweek-us_1937-07-31_10_5" 
 [8] "sim_newsweek-us_1937-08-14_10_7" 
 [9] "sim_newsweek-us_1937-09-06_10_10"
[10] "sim_newsweek-us_1937-10-25_10_17"
[11] "sim_newsweek-us_1937-11-15_10_20"
[12] "sim_newsweek-us_1937-12-06_10_23"



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

