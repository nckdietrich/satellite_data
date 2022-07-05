###
# Download Swarm data, unzip
#
# Currently written for Swarm neutral density data 
#
# Author: Nick Dietrich
###

import datetime
import urllib.request
import os
import zipfile

# *Controls:
# Adjust based on the information wanted. Will need to adjust the filename and the base_url depending on the data of interest
year = 2020
# Swarm_name = 'A'
# Swarm_name = 'B'
Swarm_name = 'C'
base_url = 'ftp://swarm-diss.eo.esa.int/Level2daily/Latest_baselines/DNS/POD/Sat_' + Swarm_name + '/'

# Create Temporary Directory
# Example: download_path = '/glade/p/univ/ucub0056/Event_study_2020/SWARM_all/'
download_path = ''


#try:
#    os.mkdir(download_path)
#except OSError:
#    print('Temp directory %s already created or failed' % download_path)
#else:
#    print('Successfully created temp directory %s' % download_path)

# Download files
num_days = 121
for i in range(1, num_days+1):
    # Formatting file to download
    time_int = datetime.datetime.strptime(str(year) + ' ' + str(i), '%Y %j')
    date = time_int.strftime('%Y%m%d')
    filename = 'SW_OPER_DNS' + Swarm_name + 'POD_2__' + date + 'T{0:06}_'.format(0) + date + 'T235930_0201.ZIP' #*Likely need to adjust
    url = base_url + filename
    download_file_path = download_path + filename

    # Download File
    urllib.request.urlretrieve(url, download_file_path)

    # Extract File
    extract_path = download_path + "{}.{:03}".format(year, i)
    with zipfile.ZipFile(download_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    os.remove(download_file_path) # Maybe delete it? its fine it doesnt work

    print('Day %i / %i Complete' % (i, num_days))
