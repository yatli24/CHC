# A function that converts CDS data to NMME

# Import necessary libraries
import xarray as xr
import os

def convert_CDS_to_NMME(CDS_folder_path, NMME_file_path, save_path):
  """ This function takes a folder path containing CDS NETCDF files, and
      converts them so that it follows a similar variable naming convention
      and spatial extent as a reference NMME dataset. Each modified file is
      stored to a defined save path with an extension of "_modified.nc"

      Arguments: CDS_folder_path - a folder path to CDS data to be modified
                 NMME_file_path - a file path to NMME data for spatial reference
                 save_path - a folder path to save the modified CDS files

      Function Outline:
      1. Open NMME reference file, store for spatial reference
      2. Loop through all files in CDS folder
          a. Open the current CDS NETCDF file and change all variable names to match
         NMME data (manually named, e.g. "longitude" renamed to "X")
          b. Convert 'tprate' from m/sec to mm/day with rate of 86400000, rename to 'prec'
          c. Use nearest neighbors to estimate and reindex CDS data to NMME grid.
             The tolerance parameter for this method can be experiemnted with.
             (If the absolute difference between a source coordinate and a
             target coordinate is less than or equal to the tolerance value,
             they are considered a match.)
          d. Save file to save_path folder with extension "_modified.nc"

      Assumptions and Usage Guidelines:
      1. Python and Package Versions:
         a. Python - 3.10
         b. pandas - 2.2.3 (xarray dependency)
         c. xarray - 2025.1.1
      2. Ensure that the intended file paths follow this format:
         a. CDS folder path: "C:/Users/name/OneDrive/Documents/CDS_folder"
         b. NMME file path: "C:/Users/name/OneDrive/Documents/NMME_folder/NMME_data1.nc"
         c. Save path: "C:/Users/name/OneDrive/Documents/save_folder"
         d. Do not have any slashes at the end of the input paths
         e. You can name the folders anything you desire and at any location, as long as the true path is specified.
  """

  # Load a reference NMME file to get spatial extent
  nmme_ds = xr.open_dataset(NMME_file_path)

  # Get CDS file names from CDS folder
  file_names = os.listdir(CDS_folder_path)

  # Loop through all CDS files
  for file in file_names:

    print(f'Currently Modifying: {file}')

    # Load the dataset (CDS)
    current_file = f'{CDS_folder_path}/{file}'

    # Assign current dataset
    current_ds = xr.open_dataset(current_file)

    # rename tprate to prec to match NMME data, and convert m/sec to mm/day.
    current_ds['prec'] = current_ds['tprate'] * 86400000

    # Rename longitude to X
    current_ds = current_ds.rename({'longitude': 'X'})

    # Rename latitude to Y
    current_ds = current_ds.rename({'latitude': 'Y'})

    # Rename forecast_month to L (do we need to subtract by 0.5?)
    current_ds = current_ds.rename({'forecastMonth': 'L'})

    # Rename number to M
    current_ds = current_ds.rename({'number': 'M'})

    # Rename forecast_reference_time to S
    current_ds = current_ds.rename({'forecast_reference_time': 'S'})

    # drops the original tprate variable
    current_ds = current_ds.drop_vars('tprate')

    # Reindex to NMME grid using nearest-neighbor
    # Adjust tolerance if needed
    current_ds = current_ds.reindex(
            Y=nmme_ds['Y'],
            X=nmme_ds['X'],
            method='nearest',
            tolerance=1
        )

    # Save the file to the CDS_converted folder, with the same name + _modified
    current_ds.to_netcdf(f'{save_path}/{file[0:-3]}_modified.nc')

    print(f'Successfully Modified: {file}')
    print(f"Saved in: {save_path}/{file[0:-3]}_modified.nc")

"""
Example usage
# CDS folder path to modify
CDS_folder_path = '/content/drive/My Drive/capstone_data/CDS'

# NMME file as a spatial reference
NMME_file_path = '/content/drive/My Drive/capstone_data/NMME/prec.CanESM5.1991.mon_Apr.nc'

# Path to save modifed CDS files
save_path = '/content/drive/My Drive/capstone_data/CDS_converted'

# call the function
convert_CDS_to_NMME(CDS_folder_path, NMME_file_path, save_path)
"""
