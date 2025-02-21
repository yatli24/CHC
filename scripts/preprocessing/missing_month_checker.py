import os
from collections import defaultdict

def list_missing_months(file_path):
  """This function takes a local model file path, such as the GFDL model, and lists
  any missing months in the files.

  For example, if my local file path for GFDL had the missing month of September for 1997, the
  function will print '1997 missing Sep'.

  Assumptions
  -----------
  Assumes that the path given to the function leads to a folder that has files
  with naming convention similar to 'prec.GFDL-SPEAR.1997.mon_Aug.nc'

  This function slices the last part of the file name to get the year and month
  information. It ignores the "front" part of the file name. So, in theory, as long
  as the format is '----something_here_any_text----YYYY.mon_MMM.nc', this function will
  be able to check for all missing months.

  Dependencies
  ------------
  Make sure to import the os module and the defaultdict object using the import statements below.
  These are native to python and require no additional installation.

  import os
  from collections import defaultdict
  """

  # use os module to list all file names
  file_list = os.listdir(file_path)

  # Extract year and month info from filenames

  # define year_month dictionary
  year_month_dict = defaultdict(set)

  for file in file_list:
      if len(file) >= 28:  # Ensure the filename is long enough
          year = file[-15:-11]  # Extract year from end of string (e.g., "2024")
          month = file[-6:-3]  # Extract month from end of string (e.g., "Sep")
          year_month_dict[year].add(month)

  # Define the complete set of months
  full_month_set = {'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'}

  # Check for missing months
  for year, months in year_month_dict.items():
      missing_months = full_month_set - months  # Find missing months
      if missing_months:
          missing_str = ', '.join(sorted(missing_months))
          print(f"{year} missing {missing_str}")

# Example usage

# Define the file path of GFDL model
file_path = '/content/drive/My Drive/capstone_data/NMME/GFDL-SPEAR/prec'

# call the function
list_missing_months(file_path)