# Groundwork Bridgeport: Tree Equity Explorer

## About

### OSL Data Collaboratory
This project is part of the Open Spatial Lab's 2023 Data Collaboratory. The Collaboratory is a 6-month program where OSL engages with social impact organizations to build a customized tool for data management, analysis, communication, and visualization. Engagement and feedback from Groundwork Bridgeport directly informed this work. 

Based at the University of Chicago Data Science Institute, the Open Spatial Lab creates open source data tools and analytics to solve problems using geospatial data science. Read more about OSL at https://datascience.uchicago.edu/research/open-spatial-lab/. 

### Project Scope
**About**: [Groundwork Bridgeport](https://www.groundworkbridgeport.org/) is a community-based non-profit organization in Bridgeport, CT, with a mission to bring about the sustained regeneration, improvement, and management of the physical environment by empowering people, businesses, and organizations. Groundwork Bridgeport works convert blighted areas into gardens, parks, playgrounds, and other open spaces that instill pride in the community. 

**Project**: OSL worked with Groundwork Bridgeport to develop an interactive data platform for tracking its tree planting and impact spanning multiple programs. The tool is integrated with existing tree databases to track and visualize metrics, including environmental and social impact trends over time. The tree data tool will also integrate socioeconomic data to highlight communities disproportionately harmed by environmental racism or opportunities for more equitable tree planting and coverage. OSL and Groundwork Bridgeport will expand this work in a project funded by the USDA Forest Service Urban and Community Forestry Program in 2024. 

## Data Biography

### Community variables
`data/community vars`

Demographic and socioeconomic variables are from the American Community Surveys (2021 5-Year Estimates) via [Social Explorer](https://www.socialexplorer.com/explore-tables). Demographic variables include:
- Census Tract GEOID
- A14006. Median Household Income (In 2021 Inflation Adjusted Dollar)
- A13003A. Poverty Status in 2020 for Children Under 18
- A12002. Highest Educational Attainment for Population 25 Years and Over
- A17005. Unemployment Rate for Civilian Population in Labor Force 16 Years and Over
- A04001. Hispanic or Latino by Race - Total Population; Hispanic or Latino; Non Hispanic or Latino: White Alone, Black or African American Alone, American Indian and Alaska Native Alone, Asian Alone, Native Hawaiin and Pacticic Islander Alone

#### Energy burden
Energy burden and average annual energy costs are from the [US Department of Energy's LEAD Tool](https://www.energy.gov/scep/slsc/lead-tool).* **Energy burden** is defined through [DoE LEAD Tool methodology](https://lead.openei.org/docs/LEAD-Tool-Methodology.pdf) as the average annual housing energy costs divided by the average annual household income. It is shown as a percent (%) of household income and ranges from 1 - 15%. **Average annual housing energy costs** are based on household monthly expenditures for electricity, gas (utility and bottled), and other fuels (including fuel oil, wood, etc.). The variable is shown in US dollars ($). 

#### Disadvantaged Community status
The Disadvantaged Community status variable is from the [Climate and Economic Justice (CEJST) Screening Tool](https://screeningtool.geoplatform.gov/en/#3/33.47/-97.5). The CEJST Screening Tool was developed by the US Digital Service in partnership with the White House Council on Environmental Quality and released in 2022. The CEJST Tool highlights disadvantaged census tracts across all 50 states, the District of Columbia, and the U.S. territories. Communities are considered disadvantaged: 1) If they are in census tracts that meet the thresholds for at least one of the tool’s categories of burden, or 2) If they are on land within the boundaries of Federally Recognized Tribes.

*_Ma, Ookie, Krystal Laymon, Megan Day, Ricardo Oliveira, Jon Weers, and Aaron Vimont. 2019. Low-Income Energy Affordability Data (LEAD) Tool Methodology. Golden, CO: National Renewable Energy Laboratory. NREL/TP-6A20-74249. https://www.nrel.gov/docs/fy19osti/74249.pdf._


### Geographic boundaries / spatial data
`data/geo`
Fairfield County Census tract and block group boundaries from [2021 US Census TIGER/Line files](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.2021.html#list-tab-790442341)


### Tree data
`data/trees`
Tree data is from an export of Groundwork Bridgeport's Treeplotter inventory as of August 2023. Tree date represented is date added to GB's inventory (not date planted). 



