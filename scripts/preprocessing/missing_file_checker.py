import os
from collections import defaultdict

# define list missing months function
def list_missing_files(file_path):
  """This function takes a model file path, such as the GFDL model, and lists
  the missing months and years in the file names.

  For example, if the year 1997 had the missing month of September, the
  function will print '1997 missing Sep'.

  Additionally, if the entire year of 1999 is missing, it will print '1999 missing entirely'.

  Assumptions
  -----------
  Assumes that the path given to the function leads to a folder that has files
  with naming convention similar to 'prec.GFDL-SPEAR.1997.mon_Aug.nc'

  This function slices the last part of the file name to get the year and month
  information. It ignores the "front" part of the file name. So, in theory, as long
  as the format is 'some_variable.some_model_name.YYYY.mon_MMM.nc', this function will
  be able to check all missing months.

  Dependencies
  ------------
  Make sure to import the os module and the defaultdict object using these import statements.
  These are native to python and require no additional installation.

  import os
  from collections import defaultdict
  """

  # use os module to list all file names
  file_list = os.listdir(file_path)

  # Extract year and month info from filenames
  # for the GFDL model, the file names are in the format of 'prec.GFDL-SPEAR.1997.mon_Aug.nc'
  # Thus, the year and month are indexed by file_name[16:20] and file_name[25:28] respectively

  # define year_month dictionary
  year_month_dict = defaultdict(set)

  full_year_set = set(range(1991, 2025))

  years_available = []

  for file in file_list:
      if len(file) >= 28:  # Ensure the filename is long enough
          year = file[-15:-11]  # Extract year (e.g., "2024")
          month = file[-6:-3]  # Extract month (e.g., "Sep")
          year_month_dict[year].add(month)
          years_available.append(year)

  # Define the complete set of months
  full_month_set = {'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'}

  # Check for missing months
  for year, months in year_month_dict.items():
      missing_months = full_month_set - months  # Find missing months
      if missing_months:
          missing_str = ', '.join(sorted(missing_months))
          print(f"{year} missing {missing_str}")

  # check for missing years
  
  for year in full_year_set:
    if str(year) not in years_available:
      print(f"{year} missing entirely")

# Example usage

# Define the file path of GFDL model
file_path = '/content/drive/My Drive/capstone_data/NMME/GFDL-SPEAR/prec'

# call the function
list_missing_files(file_path)
