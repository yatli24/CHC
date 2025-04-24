# This script takes raw netCDF climate model and chirps data, and aligns them for direct comparison.

# import necessary packages
import numpy as np
import pandas as pd
import xarray as xr

# Set new coordinate index for reindexing models

# -90 to 90 for latitude in steps of 0.5
new_lat = np.arange(-90, 90, 0.5)

# -180 to 180 for logitude in steps of 0.5
new_lon = np.arange(-180, 180, 0.5)

# load climate models into variables
# replace the file paths with your file path

# NMME models
CanESM5 = xr.open_mfdataset('data/NMME/CanESM5/prec/*.nc', parallel=True)
CCSM4 = xr.open_mfdataset('data/NMME/CCSM4/prec/*.nc', parallel=True)
CESM1 = xr.open_mfdataset('data/NMME/CESM1/prec/*.nc', parallel=True)
GEM5 = xr.open_mfdataset('data/NMME/GEM5/prec/*.nc', parallel=True)
GFDL = xr.open_mfdataset('data/NMME/GFDL/prec/*.nc', parallel=True)
NASA = xr.open_mfdataset('data/NMME/NASA/prec/*.nc', parallel=True)
NCEP = xr.open_mfdataset('data/NMME/NCEP/prec/*.nc', parallel=True)

# CDS models
CMCC = xr.open_mfdataset('data/CDS/CMCC/prec/*.nc', parallel=True)
DWD = xr.open_mfdataset('data/CDS/DWD/prec/*.nc', parallel=True)
METEO = xr.open_mfdataset('data/CDS/METEO/prec/*.nc', parallel=True)
ECMWF = xr.open_mfdataset('data/CDS/ECMWF/prec/*.nc', parallel=True)
JMA = xr.open_mfdataset('data/CDS/JMA/prec/*.nc', parallel=True)

# reindex and assign coordinates for each climate model
# asssumes that latitude and longitude are labeled as Y and X in the model data
CanESM5 = CanESM5.assign_coords(X=(((CanESM5.X + 180) % 360) - 180)).sortby(['X'])
CanESM5 = CanESM5.reindex(X=new_lon, Y=new_lat).ffill('X').ffill('Y')

CCSM4 = CCSM4.assign_coords(X=(((CCSM4.X + 180) % 360) - 180)).sortby(['X'])
CCSM4 = CCSM4.reindex(X=new_lon, Y=new_lat).ffill('X').ffill('Y')

CESM1 = CESM1.assign_coords(X=(((CESM1.X + 180) % 360) - 180)).sortby(['X'])
CESM1 = CESM1.reindex(X=new_lon, Y=new_lat).ffill('X').ffill('Y')

GEM5 = GEM5.assign_coords(X=(((GEM5.X + 180) % 360) - 180)).sortby(['X'])
GEM5 = GEM5.reindex(X=new_lon, Y=new_lat).ffill('X').ffill('Y')

GFDL = GFDL.assign_coords(X=(((GFDL.X + 180) % 360) - 180)).sortby(['X'])
GFDL = GFDL.reindex(X=new_lon, Y=new_lat).ffill('X').ffill('Y')

NASA = NASA.assign_coords(X=(((NASA.X + 180) % 360) - 180)).sortby(['X'])
NASA = NASA.reindex(X=new_lon, Y=new_lat).ffill('X').ffill('Y')

NCEP = NCEP.assign_coords(X=(((NCEP.X + 180) % 360) - 180)).sortby(['X'])
NCEP = NCEP.reindex(X=new_lon, Y=new_lat).ffill('X').ffill('Y')

CMCC = CMCC.assign_coords(X=(((CMCC.X + 180) % 360) - 180)).sortby(['X'])
CMCC = CMCC.reindex(X=new_lon, Y=new_lat).ffill('X').ffill('Y')

DWD = DWD.assign_coords(X=(((DWD.X + 180) % 360) - 180)).sortby(['X'])
DWD = DWD.reindex(X=new_lon, Y=new_lat).ffill('X').ffill('Y')

METEO = METEO.assign_coords(X=(((METEO.X + 180) % 360) - 180)).sortby(['X'])
METEO = METEO.reindex(X=new_lon, Y=new_lat).ffill('X').ffill('Y')

ECMWF = ECMWF.assign_coords(X=(((ECMWF.X + 180) % 360) - 180)).sortby(['X'])
ECMWF = ECMWF.reindex(X=new_lon, Y=new_lat).ffill('X').ffill('Y')

JMA = JMA.assign_coords(X=(((JMA.X + 180) % 360) - 180)).sortby(['X'])
JMA = JMA.reindex(X=new_lon, Y=new_lat).ffill('X').ffill('Y')

# load in chirps
chirps = xr.open_dataset('data/CHIRPS/chirps-v2.0.monthly.nc')


# define dictionary of region coordinates
region_coords = {'south_sudan': {'latitude': (3.5, 12.5),
                                 'longitude': (25, 35)},
                 'eastern_east_africa':  {'latitude': (-3.5, 8),
                                 'longitude': (38, 50)},
                 'eastern_ukraine': {'latitude': (45, 51),
                                     'longitude': (31, 40)},
                 'southern_africa': {'latitude': (-23, -15),
                                     'longitude': (25, 34)},
                 'west_africa': {'latitude': (10, 13.5),
                                     'longitude': (-10, 0)},
                 'sri_lanka': {'latitude': (5.5, 10),
                                     'longitude': (79, 82)},
                 'lake_victoria_basin': {'latitude': (-4, 1.5),
                                     'longitude': (29, 36)}}


# define dictionary of loaded models
models = {'CanESM5': CanESM5,
          'CCSM4': CCSM4,
          'CESM1': CESM1,
          'GEM5': GEM5,
          'GFDL': GFDL,
          'NASA': NASA,
          'NCEP': NCEP,
          'CMCC': CMCC,
          'DWD': DWD,
          'METEO': METEO,
          'ECMWF': ECMWF,
          'JMA': JMA}

# for every model, subset a region, merge it with CHIRPS, and save the netcdf file
def merge_chirps_and_model(model_dict, region_coord_dict, chirps, save_path):
    """After loading in climate model data and CHIRPS data,
    This function generates monthly regional data for given
    climate models by merging CHIRPS data with climate model data so that
    they can be compared side to side, ensuring that the climate model
    data is spatially and temporally aligned to CHIRPS.

    Arguments
    ---------
    model_dict - dictionary of models loaded in as xarray datasets,
                 where the key is the model name and the value is the xarray dataset
    region_coord_dict - a dictionary of region coordinates, where the key is the region name
                        and the value is a dictionary of latitude and longitude coordinates
    chirps - CHIRPS dataset loaded in as xarray dataset
    save_path - path to save merged netcdf files

    Outputs
    -------
    netcdf files of merged data for each model and region in save_path

    Columns of output merged netcdf data:
    lead_time - number of months between date of prediction and realization time
    time - realization time of precipitation
    M - ensemble member of climate model
    latitude - latitude coordinate of predicted/actual precipitation
    longitude - longitude coordinate of predicted/actual precipitation
    predicted_precip - climate model's predicted precipitation
    precip - CHIRPS's observed actual precipitation

    There will be instances where precip shows up as NaN, but the model has a
    value for predicted_precip. This indicates that CHIRPS did not have an
    observed precipitation measurement for that location and time. (i.e. ocean areas)

    Function Outline:
    1. Loop through all loaded models in model_dict
        a. Loop through all regions in region_coord_dict
            i. Subset a region for the current model
            ii. Subset CHIRPS to the same region and
                interpolate to match spatial resolution of current model
                (nearest neighbor interpolation)
            iii. Convert both subsetted datasets to dataframes
            iV. Calculate realized dates for the current model. This is what
                will be used to merge with CHIRPS.
            V. Merge CHIRPS and subsetted model data
            vi. Save to netCDF as region_model_merged.nc in save_path

    Assumpitons and Usage Guidelines
    --------------------------------
    1. Python and Package Versions:
        a. Python - 3.10
        b. pandas - 2.2.3 (xarray dependency)
        c. xarray - 2025.1.1
    2. Assumes that each loaded model in model_dict has the following variables:
        a. 'Y' - latitude coordinate
        b. 'X' - longitude coordinate
        c. 'prec' - precipitation
        d. 'S' - date of prediction
        e. 'L' - lead time
    3. Ensure that the intended file save path follows this format:
         a. save_path: "C:/Users/name/OneDrive/Documents/data/netCDF/merged/"
         b. ensure that there is a slash (/) at the end of the save path
         c. ensure that the folder exists at the specified location
    """
    for model_name, model_data in model_dict.items():
        for region_name, coord_dict in region_coord_dict.items():
            # Status message
            print(f'Currently merging {model_name} and CHIRPS for {region_name}')

            # Subset a region for the current model, rename variables
            current_model_region = (model_data.sel(Y=slice(coord_dict['latitude'][0], coord_dict['latitude'][1]), X=slice(coord_dict['longitude'][0], coord_dict['longitude'][1]))
                                .rename(
                {'Y': 'latitude', 'X': 'longitude', 'prec': 'predicted_precip', 'S': 'date_of_prediction', 'L': 'lead_time'}))

            # Interpolate and subset CHIRPS to match spatial resolution of current model
            # must add 0.5 degrees to each lat/long value to chirps subset for slicing to not return an empty array
            chirps_region = chirps.sel(latitude=slice(coord_dict['latitude'][0] - 0.5, coord_dict['latitude'][1] + 0.5),
                                            longitude=slice(coord_dict['longitude'][0] - 0.5, coord_dict['longitude'][1] + 0.5)).interp_like(current_model_region,
                                                                                                            method='nearest')
            # Calculate realized dates for the current model and region
            # realized date is date_of_prediction + lead_time
            current_model_region_df = current_model_region.to_dataframe().reset_index()
            current_model_region_df['realization time'] = current_model_region_df['date_of_prediction'] + (
                        current_model_region_df['lead_time'] * 30).astype('timedelta64[D]')

            # After computing realization time, split month and year into separate columns for merging
            current_model_region_df['month'] = current_model_region_df['realization time'].dt.month
            current_model_region_df['year'] = current_model_region_df['realization time'].dt.year

            # Convert CHIRPS to dataframe, split month and year into separate columns for merging
            chirps_region_df = chirps_region.to_dataframe().reset_index()
            chirps_region_df['month'] = chirps_region_df['time'].dt.month
            chirps_region_df['year'] = chirps_region_df['time'].dt.year

            # Merge CHIRPS and current_model_region dataframe on month, year, latitude, and longitude
            # drop all values where time has no prediction. This ensures that each monthly prediction has a CHIRPS value to compare to.
            # this does not drop values where CHIRPS has no observed precipitation measurement, but the model has a prediction (i.e. ocean areas)
            current_model_region_merged_df = current_model_region_df.merge(chirps_region_df, how='left', on=['month', 'year', 'latitude', 'longitude']).dropna(subset=['time'])

            print(current_model_region_merged_df.head())

            # using the model name, region name, and save_path, create a unique save path for the current model and region
            model_region_save_path = f'{save_path}{region_name}_{model_name}_merged.nc'

            # Save merged results to netCDF
            current_model_region_merged_df.drop(['date_of_prediction', 'month', 'year', 'realization time'], axis=1).set_index(['lead_time', 'time', 'M', 'latitude', 'longitude']).to_xarray().to_netcdf(model_region_save_path)

            # Status message
            print(f'Successfully Merged and Saved {region_name}_{model_name}_merged.nc in {save_path}')


# call the function, run for all models and regions
save_path = 'data/netCDF/merged/'
merge_chirps_and_model(models, region_coords, chirps, save_path)
