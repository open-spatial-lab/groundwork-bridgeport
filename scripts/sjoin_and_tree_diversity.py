# %%
import pandas as pd
import geopandas as gpd
# remove column limit
pd.set_option('display.max_columns', None)
# %%
geo = gpd.read_file('../data/brigdgeportCT-sdoh.geojson')
# %%
trees = pd.read_csv('../data/treeplotter_export_6_21.csv')
# %%
# make trees geo from Latitude and Longitude columns
trees_geo = gpd.GeoDataFrame(trees, geometry=gpd.points_from_xy(trees.Longitude, trees.Latitude))

# %%
# sjoin trees to geo
trees_geo_sjoin = gpd.sjoin(trees_geo, geo, how='left', op='within')
# %%
trees_geo_sjoin.head()
# %%
# count of trees by GEOID
total_count = trees_geo_sjoin.groupby('GEOID').size()
total_count = total_count.reset_index(name='count')
# %%
def apply_simpson_index_to_grouped_df(group):
    # get total count of trees in group
    total_count = group['counts'].sum()
    # get count of each tree type
    # return total_count
    group['proportion'] = group['counts'] / total_count
    # # get simpson index
    simpson_index = (group['proportion']**2).sum()
    return simpson_index
# %%
# group trees by GEOID and get simpson index for each subset
simpson_index = trees_geo_sjoin[['GEOID', 'Common Name']]
simpson_index = simpson_index.groupby(['GEOID','Common Name']).size().reset_index(name='counts')

#  for rows within each GEOID, get simpson index using simpson_index function
simpson_index = simpson_index.groupby('GEOID').apply(apply_simpson_index_to_grouped_df)
simpson_index = simpson_index.reset_index(name='simpson_index')
# %%
#  join total_count and simpson_index 
simpson_index = simpson_index.merge(total_count, on='GEOID')
# %%
# write to csv
simpson_index.to_csv('../data/simpson_index.csv', index=False)
# %%
