library(tidyverse)

setwd("~/Documents/GitHub/groundwork-bridgeport")

sdoh <- read.csv(file = "data/community vars/sdoh - tract/tract-bridgeport.csv")

energy_raw <- read.csv("data/community vars/energy burden - tract/lead-tool-map-data.csv")
str(energy_raw)

energy <- energy_raw %>%
  select(Geography.ID, Is.Disadvantaged.Community = Is.Disadvantaged.Community., energyBurden = Energy.Burden....income., AvgAnnualEnergyCost = Avg..Annual.Energy.Cost....)

energy$Geography.ID <- sprintf("%011s", energy$Geography.ID)

merged <- left_join(sdoh, energy, by = c("FIPS" = "Geography.ID"))

write.csv(merged, "data/community vars/tracts-communityVars-bridgeport.csv",
          row.names = FALSE)
