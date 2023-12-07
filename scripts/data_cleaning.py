# %%
import pandas as pd
import geopandas as gpd
# %%
col_dict = {
  "FIPS": "FIPS",
    "Area Name":"Area Name",
    "Civilian Population in Labor Force 16 Years and Over:": "Population in labor force",
    "Civilian Population in Labor Force 16 Years and Over: Employed": "Population employed",
    "Civilian Population in Labor Force 16 Years and Over: Unemployed": "Population unemployed",
    "Population 25 Years and Over:": "Population 25 Years and Over",
    "Population 25 Years and Over: Less than High School": "Less than High School Over 25",
    "Population 25 Years and Over: High School Graduate or More (Includes Equivalency)": "High School Graduate or More Over 25",
    "Population 25 Years and Over: Some College or More": "Some College or More Over 25",
    "Population 25 Years and Over: Bachelor's Degree or More": "Bachelor's Degree or More Over 25",
    "Population 25 Years and Over: Master's Degree or More": "Master's Degree or More Over 25",
    "Population 25 Years and Over: Professional School Degree or More": "Professional School Degree or More Over 25",
    "Population 25 Years and Over: Doctorate Degree": "Doctorate Degree Over 25",
    "Families:": "Families",
    "Families: Income Below Poverty Level": "Families Below Poverty Level",
    "Families: Income Below Poverty Level: Married Couple Family: with Related Child Living  Below Poverty Level": "Married Couple Family: with Related Child Living  Below Poverty Level",
    "Families: Income Below Poverty Level: Married Couple Family: No Related Children Under 18 Years": "Married Couple Family: No Related Children Under 18 Years",
    "Families: Income Below Poverty Level: Male Householder, No Wife Present": "Male Householder",
    "Families: Income Below Poverty Level: Male Householder, No Wife Present: with Related Children Under 18 Years": "Male Householder with Children",
    "Families: Income Below Poverty Level: Male Householder, No Wife Present: No Related Children Under 18 Years": "Male Householder without Children",
    "Families: Income Below Poverty Level: Female Householder, No Husband Present": "Female Householder",
    "Families: Income Below Poverty Level: Female Householder, No Husband Present: with Related Children Under 18 Years": "Female Householder with Children",
    "Families: Income Below Poverty Level: Female Householder, No Husband Present: No Related Children Under 18 Years": "Female Householder without Children",
    "Families: Income At or Above Poverty Level": "Families At or Above Poverty Level",
    "Median Household Income (In 2021 Inflation Adjusted Dollars)": "Median Household Income (2021 Dollars)",
    "Total Population": "Total Population",
    "Total Population: Not Hispanic or Latino": "Total Non-Hispanic or Latino Population",
    "Total Population: Not Hispanic or Latino: White Alone": "White NH",
    "Total Population: Not Hispanic or Latino: Black or African American Alone": "Black or AA NH",
    "Total Population: Not Hispanic or Latino: American Indian and Alaska Native Alone": "AIAN NH",
    "Total Population: Not Hispanic or Latino: Asian Alone": "AA NH",
    "Total Population: Not Hispanic or Latino: Native Hawaiian and Other Pacific Islander Alone": "NHPI NH",
    "Total Population: Not Hispanic or Latino: Some Other Race Alone": "Other NH",
    "Total Population: Not Hispanic or Latino: Two or More Races": "Two or More NH",
    "Total Population: Hispanic or Latino": "Hispanic or Latino",
}
energy_data_cols = {
    'Geography ID': "FIPS",
    'Is Disadvantaged Community?': "Disadvantaged Community",
    'Energy Burden (% income)': "Energy Burden",
    'Avg. Annual Energy Cost ($)': "Average Annual Energy Cost",
}

def handle_sjoin_index_cols(df: pd.DataFrame) -> pd.DataFrame:
    if "index_right" in df.columns:
        df = df.drop(columns=["index_right"])
    if "index_left" in df.columns:
        df = df.drop(columns=["index_left"])
    return df
# %%
# bg_data = pd.read_csv('../data/community vars/R13516212_SL150.csv').iloc[1:]
# bg_data = bg_data[[col for col in bg_data.columns if col in col_dict.keys()]]
# bg_data = bg_data.rename(columns=col_dict)
# bg_data.to_parquet('../data/community vars/bg_data.parquet')
# %%
def handle_tract_data():
    tract_data = pd.read_csv('../data/community vars/R13516211_SL140.csv').iloc[1:]
    energy_data = pd.read_csv('../data/community vars/source data/energy burden - tract/lead-tool-map-data.csv').iloc[1:]
    # filter for cols in keys of col_dict
    tract_data = tract_data[[col for col in tract_data.columns if col in col_dict.keys()]]
    # rename cols
    tract_data = tract_data.rename(columns=col_dict)
    energy_data = energy_data[[col for col in energy_data.columns if col in energy_data_cols.keys()]]
    energy_data = energy_data.rename(columns=energy_data_cols)
    tract_data['FIPS'] = tract_data['FIPS'].astype(str).str.zfill(11)
    energy_data['FIPS'] = energy_data['FIPS'].astype(str).str.zfill(11)
    joined = tract_data.merge(energy_data, on='FIPS')
    # for col except fips, convert to numeric
    for col in joined.columns:
        if col != 'FIPS':
            joined[col] = pd.to_numeric(joined[col], errors='ignore')
    return joined
    
# %%
# convert to parquet
tract_data = handle_tract_data()
tract_data.to_parquet('../data/community vars/tract_data.parquet')
# %%
def handle_tree_data():
    # import data
    trees_data = gpd.read_file('../data/trees/11_15_2023_trees.zip')
    tract_geo = gpd.read_file('../data/geo/cb_2021_09_tract_500k.zip')[['GEOID', 'geometry']]
    bg_geo = gpd.read_file('../data/geo/cb_2021_09_bg_500k.zip')[['GEOID', 'geometry']]
    # clean up dfs
    tract_geo = tract_geo.rename(columns={'GEOID': 'TRACT_ID'})
    bg_geo = bg_geo.rename(columns={'GEOID': 'CBG_ID'})
    trees_data = trees_data.to_crs('EPSG:4326')
    # sjoin
    # sjoin trees to geo
    trees_geo_sjoin = gpd.sjoin(trees_data, bg_geo, how='left', op='within')
    trees_geo_sjoin = handle_sjoin_index_cols(trees_geo_sjoin)
    trees_geo_sjoin = gpd.sjoin(trees_geo_sjoin, tract_geo, how='left', op='within')
    trees_geo_sjoin = handle_sjoin_index_cols(trees_geo_sjoin)
    
    return trees_geo_sjoin
# %%
tree_data = handle_tree_data()
tree_data.to_parquet('../data/trees/trees_geo_sjoin.parquet')
# %%
def handle_tract_geo(tract_id_list: list[str]):
    tract_data = gpd.read_file('../data/geo/cb_2021_09_tract_500k.zip')
    # filter for tracts in tract_id_list
    tract_data = tract_data[tract_data['GEOID'].isin(tract_id_list)]
    return tract_data
# %%
tract_geo = handle_tract_geo(tract_data['FIPS'].tolist())
tract_geo.to_parquet('../data/geo/tract_geo.parquet')
# %%