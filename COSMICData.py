###
# Download COSMIC 2 data and unzip it
# 
# May need to adjust adjust the base_url and the filename variables baed on what file is of interest
# Currently implemented for COSMIC-2 ion profile data 
#
# Author: Nick Dietrich
#
###

import urllib.request
import os
import tarfile

# Controls:
year = 2020
base_url = 'https://data.cosmic.ucar.edu/gnss-ro/cosmic2/provisional/spaceWeather/level2/{}/'.format(year)
# Specify the start day and the number of days of interest.
start = 1
num_days = 121


# Create Temporary Directory (May not be necessary)
# Example: download_path = '/glade/p/univ/ucub0056/Event_study_2020/COSMIC2/'
download_path = ''

# Not sure if these commands work.. maybe don't have permission
try:
    os.mkdir(download_path)
except OSError:
    print('Temp directory %s already created or failed' % download_path)
else:
    print('Successfully created temp directory %s' % download_path)

# Download files
for i in range(start, num_days+1):
    # Formatting file to download
    index = "{0:03}".format(i)
    filename = "ionPrf_prov1_{}_{:03}.tar.gz".format(year, i)
    url = base_url + "{:03}/".format(i) + filename
    download_file_path = download_path + filename
    # Downloading File
    urllib.request.urlretrieve(url, download_file_path)

    # Extract File
    extract_path = download_path + "{}.{:03}".format(year, i)
    tar = tarfile.open(download_file_path, "r:gz")
    tar.extractall(path=extract_path)
    tar.close()
    os.remove(download_file_path) # not sure if this deleting works..

    print('Day %i / %i Complete' % (i, num_days))
