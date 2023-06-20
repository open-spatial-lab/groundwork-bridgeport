library(tidyverse)
library(tidycensus)
library(sf)

census_api_key("4c645df575f0b945d20f4fd8d66f679017b08dca", install = TRUE)

v21 <- load_variables(2021, "acs5", cache = TRUE)
view(v21)

#### San Diego, San Diego County, CA ####
sd <- get_acs(
  year = 2021,
  geography = "tract",
  state = "CA",
  county = "san diego",
  variables = c(
    pop = "C02003_001",
    whitepop = "C02003_003",
    blackpop = "C02003_004",
    nativepop = "C02003_005",
    asianpop = "C02003_006",
    hpipop = "C02003_007",
    latinopop = "B01001I_001",
    insured = "C27021_001",
    medincome = "B06011_001",
    medage = "B01002_001",
    pubTransitToWork = "B08101_025"
  ),
  geometry = TRUE
)

sandiego_clean <- sd %>% group_by(GEOID, geometry) %>%
  select(-moe) %>%
  pivot_wider(names_from = "variable", values_from = "estimate")

st_write(sandiego_clean, "sandiego-sdoh.geojson")

# test viz
ggplot(sandiego_clean, aes(fill=pubTransitToWork)) +
  geom_sf() +
  theme_void()

#### Portland, Multnomah County, OR ####

portland <- get_acs(
  year = 2021,
  geography = "tract",
  state = "OR",
  county = "Multnomah",
  variables = c(
    pop = "C02003_001",
    whitepop = "C02003_003",
    blackpop = "C02003_004",
    nativepop = "C02003_005",
    asianpop = "C02003_006",
    hpipop = "C02003_007",
    latinopop = "B01001I_001",
    insured = "C27021_001",
    medincome = "B06011_001",
    medage = "B01002_001",
    pubTransitToWork = "B08101_025"
  ),
  geometry = TRUE
)

pdx_clean <- portland %>% 
  group_by(GEOID, geometry) %>%
  select(-moe) %>%
  pivot_wider(names_from = "variable", values_from = "estimate")

# save portland data
st_write(pdx_clean, "pdx-sdoh.geojson")

# test viz
ggplot(pdx_clean, aes(fill = pop)) +
  geom_sf() +
  theme_void()

#### Bridgeport, Fairfield County, CT ####

bridgeport <- get_acs(
  year = 2021,
  geography = "tract",
  state = "CT",
  county = "Fairfield",
  variables = c(
    pop = "C02003_001",
    whitepop = "C02003_003",
    blackpop = "C02003_004",
    nativepop = "C02003_005",
    asianpop = "C02003_006",
    hpipop = "C02003_007",
    latinopop = "B01001I_001",
    insured = "C27021_001",
    medincome = "B06011_001",
    medage = "B01002_001",
    pubTransitToWork = "B08101_025"
  ),
  geometry = TRUE
)

bport_clean <- bridgeport %>%
  group_by(GEOID, geometry) %>%
  select(-moe) %>%
  pivot_wider(names_from = "variable", values_from = "estimate")

# test viz
ggplot(bport_clean, aes(fill = blackpop)) +
  geom_sf() +
  theme_void()

# export bridgeport data
st_write(bport_clean, "brigdgeportCT-sdoh.geojson")

#### Chicago, Cook County, IL ####

chicago <- get_acs(
  year = 2021,
  geography = "tract",
  state = "IL",
  county = "Cook",
  variables = c(
    pop = "C02003_001",
    whitepop = "C02003_003",
    blackpop = "C02003_004",
    nativepop = "C02003_005",
    asianpop = "C02003_006",
    hpipop = "C02003_007",
    latinopop = "B01001I_001",
    insured = "C27021_001",
    medincome = "B06011_001",
    medage = "B01002_001",
    pubTransitToWork = "B08101_025"
  ),
  geometry = TRUE
)

chi_clean <- chicago %>%
  group_by(GEOID, geometry) %>%
  select(-moe) %>%
  pivot_wider(names_from = "variable", values_from = "estimate")

# test viz
ggplot(chi_clean, aes(fill = latinopop)) +
  geom_sf() +
  theme_void()

# export chicago data
st_write(chi_clean, "cookcounty-sdoh.geojson")

         