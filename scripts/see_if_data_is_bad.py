# %%
import pandas as pd
import geopandas as gpd
# %%
tracts = gpd.read_file("../data/geo/cb_2021_09_bg_500k.zip")
# %%
sdoh = pd.read_csv("../data/community vars/tract-bridgeport.csv").iloc[1:]
# %%
joined = sdoh[['FIPS', "Qualifying Name"]].merge(tracts[["GEOID", "NAME"]], left_on="FIPS", right_on="GEOID", how="right")
# %%
# yep its bad