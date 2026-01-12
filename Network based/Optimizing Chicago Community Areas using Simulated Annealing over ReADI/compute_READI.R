#OBTAIN ALL CENSUS DATA, COMPUTE ReADI VARIABLES, EXPORT ReADI SCORES

#imports
library(tidycensus)
library(dplyr)
library(tidyr)
library(readr)
library(tigris)
library(readxl)
library(psych)
library(statar)
options(tigris_use_cache = TRUE)

census_api_key("KEY HERE")

#OBTAIN CENSUS DATA

#TOTAL POPULATION
total_population_2015_calc<-get_acs(geography="block group", variable="B01003_001", state="IL", county="Cook", year = 2015, cache_table=TRUE)
total_population_2023_calc<-get_acs(geography="block group", variable="B01003_001", state="IL", county="Cook", year = 2023, cache_table=TRUE)

#MEDIAN INCOME
median_income_2015_calc<-get_acs(geography="block group", variable="B19013_001", state="IL", county="Cook", year = 2015, cache_table=TRUE)
median_income_2023_calc<-get_acs(geography="block group", variable="B19013_001", state="IL", county="Cook", year = 2023, cache_table=TRUE)


#INCOME DISPARITY
income_disparity_2015<-get_acs(geography="block group", table="B19001", state="IL", county="Cook", year = 2015, cache_table=TRUE)
income_disparity_2015_calc <- data.frame(GEOID = unique(income_disparity_2015$GEOID))
income_disparity_2015_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(income_disparity_2015), by = 17)){
  numerator <- sum(income_disparity_2015$estimate[seq(from = i+1, to = i+3, by = 1)]) + 1
  denominator <- sum(income_disparity_2015$estimate[seq(from = i+13, to = i+16, by = 1)]) + 1
  income_disparity_2015_calc$estimate[c] <- log((numerator/denominator)*100)
  c<-c+1
}

income_disparity_2023<-get_acs(geography="block group", table="B19001", state="IL", county="Cook", year = 2023, cache_table=TRUE)
income_disparity_2023_calc <- data.frame(GEOID = unique(income_disparity_2023$GEOID))
income_disparity_2023_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(income_disparity_2023), by = 17)){
  numerator <- sum(income_disparity_2023$estimate[seq(from = i+1, to = i+3, by = 1)]) + 1
  denominator <- sum(income_disparity_2023$estimate[seq(from = i+13, to = i+16, by = 1)]) + 1
  income_disparity_2023_calc$estimate[c] <- log((numerator/denominator)*100)
  c<-c+1
}

#PERCENT OF POPULATION BELOW POVERY LEVEL
below_poverty_2015<-get_acs(geography="block group", table="B17017", state="IL", county="Cook", year = 2015, cache_table=TRUE)
below_poverty_2015_calc <- data.frame(GEOID = unique(below_poverty_2015$GEOID))
below_poverty_2015_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(below_poverty_2015), by = 59)){
  numerator <- below_poverty_2015$estimate[i+1]
  denominator <- below_poverty_2015$estimate[i]  
  below_poverty_2015_calc$estimate[c] <- (numerator/denominator)*100
  c<-c+1
}
below_poverty_2023<-get_acs(geography="block group", table="B17017", state="IL", county="Cook", year = 2023, cache_table=TRUE)
below_poverty_2023_calc <- data.frame(GEOID = unique(below_poverty_2023$GEOID))
below_poverty_2023_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(below_poverty_2023), by = 59)){
  numerator <- below_poverty_2023$estimate[i+1]
  denominator <- below_poverty_2023$estimate[i]  
  below_poverty_2023_calc$estimate[c] <- (numerator/denominator)*100
  c<-c+1
}

#PERCENT OF POPULATION BELOW 150% OF POVERY LEVEL
below_poverty_higher_2015<-get_acs(geography="block group", table="C17002", state="IL", county="Cook", year = 2015, cache_table=TRUE)
below_poverty_higher_2015_calc <- data.frame(GEOID = unique(below_poverty_2015$GEOID))
below_poverty_higher_2015_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(below_poverty_higher_2015), by = 8)){
  numerator <- sum(below_poverty_higher_2015$estimate[seq(from = i+1, to = i+4, by = 1)])
  denominator <- below_poverty_higher_2015$estimate[i]  
  below_poverty_higher_2015_calc$estimate[c] <- (numerator/denominator)*100
  c<-c+1
}
below_poverty_higher_2023<-get_acs(geography="block group", table="C17002", state="IL", county="Cook", year = 2023, cache_table=TRUE)
below_poverty_higher_2023_calc <- data.frame(GEOID = unique(below_poverty_2023$GEOID))
below_poverty_higher_2023_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(below_poverty_higher_2023), by = 8)){
  numerator <- sum(below_poverty_higher_2023$estimate[seq(from = i+1, to = i+4, by = 1)])
  denominator <- below_poverty_higher_2023$estimate[i]  
  below_poverty_higher_2023_calc$estimate[c] <- (numerator/denominator)*100
  c<-c+1
}

education_2015 <- get_acs(geography="block group", table="B15003", state="IL", county="Cook", year = 2015, cache_table=TRUE)
education_2023 <- get_acs(geography="block group", table="B15003", state="IL", county="Cook", year = 2023, cache_table=TRUE)

#PERCENT OF POPULATION OLDER THAN 25 WITH NO HIGH SCHOOL DIPLOMA
no_highschool_2015_calc <- data.frame(GEOID = unique(education_2015$GEOID))
no_highschool_2015_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(education_2015), by = 25)){
  numerator <- sum(education_2015$estimate[seq(from = i+1, to = i+15, by = 1)])
  denominator <- education_2015$estimate[i]  
  no_highschool_2015_calc$estimate[c] <- (numerator/denominator)*100
  c<-c+1
}
no_highschool_2023_calc <- data.frame(GEOID = unique(education_2023$GEOID))
no_highschool_2023_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(education_2023), by = 25)){
  numerator <- sum(education_2023$estimate[seq(from = i+1, to = i+15, by = 1)])
  denominator <- education_2023$estimate[i]  
  no_highschool_2023_calc$estimate[c] <- (numerator/denominator)*100
  c<-c+1
}

#PERCENT OF POPULATION OLDER THAN 25 WITH AT LEAST BACHELORS DEGREE
higher_ed_2015_calc <- data.frame(GEOID = unique(education_2015$GEOID))
higher_ed_2015_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(education_2015), by = 25)){
  numerator <- sum(education_2015$estimate[seq(from = i+21, to = i+24, by = 1)])
  denominator <- education_2015$estimate[i]  
  higher_ed_2015_calc$estimate[c] <- (numerator/denominator)*100
  c<-c+1
}
higher_ed_2023_calc <- data.frame(GEOID = unique(education_2023$GEOID))
higher_ed_2023_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(education_2023), by = 25)){
  numerator <- sum(education_2023$estimate[seq(from = i+21, to = i+24, by = 1)])
  denominator <- education_2023$estimate[i]  
  higher_ed_2023_calc$estimate[c] <- (numerator/denominator)*100
  c<-c+1
}

#PERCENT OF POPULATION OLDER THAN 16 IN WHITE COLLAR OCCUPATIONS
white_collar_2015 <- get_acs(geography="block group", table="C24010", state="IL", county="Cook", year = 2015, cache_table=TRUE)
white_collar_2015_calc <- data.frame(GEOID = unique(white_collar_2015$GEOID))
white_collar_2015_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(white_collar_2015), by = 73)){
  numerator <- white_collar_2015$estimate[i+2]+white_collar_2015$estimate[i+26]+white_collar_2015$estimate[i+38]+white_collar_2015$estimate[i+62]
  denominator <- white_collar_2015$estimate[i]  
  white_collar_2015_calc$estimate[c] <- (numerator/denominator)*100
  c<-c+1
}
white_collar_2023 <- get_acs(geography="block group", table="C24010", state="IL", county="Cook", year = 2023, cache_table=TRUE)
white_collar_2023_calc <- data.frame(GEOID = unique(white_collar_2023$GEOID))
white_collar_2023_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(white_collar_2023), by = 73)){
  numerator <- white_collar_2023$estimate[i+2]+white_collar_2023$estimate[i+26]+white_collar_2023$estimate[i+38]+white_collar_2023$estimate[i+62]
  denominator <- white_collar_2023$estimate[i]  
  white_collar_2023_calc$estimate[c] <- (numerator/denominator)*100
  c<-c+1
}

#PERCENT OF POPULATION OLDER THAN 16 AND UNEMPLOYED
unemployed_2015<-get_acs(geography="block group", table="B23025", state="IL", county="Cook", year = 2015, cache_table=TRUE)
unemployed_2015_calc <- data.frame(GEOID = unique(unemployed_2015$GEOID))
unemployed_2015_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(unemployed_2015), by = 7)){
  numerator <- unemployed_2015$estimate[i+4]
  denominator <- unemployed_2015$estimate[i+2]  
  unemployed_2015_calc$estimate[c] <- (numerator/denominator)*100
  c<-c+1
}
unemployed_2023<-get_acs(geography="block group", table="B23025", state="IL", county="Cook", year = 2023, cache_table=TRUE)
unemployed_2023_calc <- data.frame(GEOID = unique(unemployed_2023$GEOID))
unemployed_2023_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(unemployed_2023), by = 7)){
  numerator <- unemployed_2023$estimate[i+4]
  denominator <- unemployed_2023$estimate[i+2]  
  unemployed_2023_calc$estimate[c] <- (numerator/denominator)*100
  c<-c+1
}

#MEDIAN HOME VALUE
median_home_value_2015_calc<-get_acs(geography="block group", variable="B25077_001", state="IL", county="Cook", year = 2015, cache_table=TRUE)
median_home_value_2023_calc<-get_acs(geography="block group", variable="B25077_001", state="IL", county="Cook", year = 2023, cache_table=TRUE)

#MEDIAN GROSS RENT
median_gross_rent_2015_calc<-get_acs(geography="block group", variable="B25064_001", state="IL", county="Cook", year = 2015, cache_table=TRUE)
median_gross_rent_2023_calc<-get_acs(geography="block group", variable="B25064_001", state="IL", county="Cook", year = 2023, cache_table=TRUE)

#MEDIAN MONTHLY MORTGAGE
median_monthly_mortgage_2015_calc<-get_acs(geography="block group", variable="B25088_002", state="IL", county="Cook", year = 2015, cache_table=TRUE)
median_monthly_mortgage_2023_calc<-get_acs(geography="block group", variable="B25088_002", state="IL", county="Cook", year = 2023, cache_table=TRUE)

#PERCENT OWNER-OCCUPIED HOUSING UNITS
owner_occupied_2015<-get_acs(geography="block group", table="B25003", state="IL", county="Cook", year = 2015, cache_table=TRUE)
owner_occupied_2015_calc <- data.frame(GEOID = unique(owner_occupied_2015$GEOID))
owner_occupied_2015_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(owner_occupied_2015), by = 3)){
  numerator <- owner_occupied_2015$estimate[i+1]
  denominator <- owner_occupied_2015$estimate[i]  
  owner_occupied_2015_calc$estimate[c] <- (numerator/denominator)*100
  c<-c+1
}
owner_occupied_2023<-get_acs(geography="block group", table="B25003", state="IL", county="Cook", year = 2023, cache_table=TRUE)
owner_occupied_2023_calc <- data.frame(GEOID = unique(owner_occupied_2023$GEOID))
owner_occupied_2023_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(owner_occupied_2023), by = 3)){
  numerator <- owner_occupied_2023$estimate[i+1]
  denominator <- owner_occupied_2023$estimate[i]  
  owner_occupied_2023_calc$estimate[c] <- (numerator/denominator)*100
  c<-c+1
}

#PERCENT OF HOUSEHOLDS WITH SINGLE PARENTS AND CHILDREN UNDER 18
single_parents_2015<-get_acs(geography="block group", table="B11003", state="IL", county="Cook", year = 2015, cache_table=TRUE)
single_parents_2015_calc <- data.frame(GEOID = unique(single_parents_2015$GEOID))
single_parents_2015_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(single_parents_2015), by = 20)){
  numerator <- single_parents_2015$estimate[i+9]+single_parents_2015$estimate[i+15]
  denominator <- single_parents_2015$estimate[i]  
  single_parents_2015_calc$estimate[c] <- (numerator/denominator)*100
  c<-c+1
}
single_parents_2023<-get_acs(geography="block group", table="B11003", state="IL", county="Cook", year = 2023, cache_table=TRUE)
single_parents_2023_calc <- data.frame(GEOID = unique(single_parents_2023$GEOID))
single_parents_2023_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(single_parents_2023), by = 20)){
  numerator <- single_parents_2023$estimate[i+9]+single_parents_2023$estimate[i+15]
  denominator <- single_parents_2023$estimate[i]  
  single_parents_2023_calc$estimate[c] <- (numerator/denominator)*100
  c<-c+1
}

#PERCENT OF HOUSEHOLDS WITHOUT A MOTOR VEHICLE
no_vehicle_2015<-get_acs(geography="block group", table="B25044", state="IL", county="Cook", year = 2015, cache_table=TRUE)
no_vehicle_2015_calc <- data.frame(GEOID = unique(no_vehicle_2015$GEOID))
no_vehicle_2015_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(no_vehicle_2015), by = 15)){
  numerator <- no_vehicle_2015$estimate[i+9]+no_vehicle_2015$estimate[i+2]
  denominator <- no_vehicle_2015$estimate[i]  
  no_vehicle_2015_calc$estimate[c] <- (numerator/denominator)*100
  c<-c+1
}
no_vehicle_2023<-get_acs(geography="block group", table="B25044", state="IL", county="Cook", year = 2023, cache_table=TRUE)
no_vehicle_2023_calc <- data.frame(GEOID = unique(no_vehicle_2023$GEOID))
no_vehicle_2023_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(no_vehicle_2023), by = 15)){
  numerator <- no_vehicle_2023$estimate[i+9]+no_vehicle_2023$estimate[i+2]
  denominator <- no_vehicle_2023$estimate[i]  
  no_vehicle_2023_calc$estimate[c] <- (numerator/denominator)*100
  c<-c+1
}

#PERCENT OF HOUSEHOLDS WITHOUT PHONES
no_phone_2015<-get_acs(geography="block group", table="B25043", state="IL", county="Cook", year = 2015, cache_table=TRUE)
no_phone_2015_calc <- data.frame(GEOID = unique(no_phone_2015$GEOID))
no_phone_2015_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(no_phone_2015), by = 19)){
  numerator <- no_phone_2015$estimate[i+6]+no_phone_2015$estimate[i+15]
  denominator <- no_phone_2015$estimate[i]  
  no_phone_2015_calc$estimate[c] <- (numerator/denominator)*100
  c<-c+1
}
no_phone_2023<-get_acs(geography="block group", table="B25043", state="IL", county="Cook", year = 2023, cache_table=TRUE)
no_phone_2023_calc <- data.frame(GEOID = unique(no_phone_2023$GEOID))
no_phone_2023_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(no_phone_2023), by = 19)){
  numerator <- no_phone_2023$estimate[i+6]+no_phone_2023$estimate[i+15]
  denominator <- no_phone_2023$estimate[i]  
  no_phone_2023_calc$estimate[c] <- (numerator/denominator)*100
  c<-c+1
}

#PERCENT OF HOUSEHOLDS WITHOUT PLUMBING
no_plumbing_2015<-get_acs(geography="block group", table="B25049", state="IL", county="Cook", year = 2015, cache_table=TRUE)
no_plumbing_2015_calc <- data.frame(GEOID = unique(no_plumbing_2015$GEOID))
no_plumbing_2015_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(no_plumbing_2015), by = 7)){
  numerator <- no_plumbing_2015$estimate[i+3]+no_plumbing_2015$estimate[i+6] + 1
  denominator <- no_plumbing_2015$estimate[i] + 1 
  no_plumbing_2015_calc$estimate[c] <- log((numerator/denominator)*100)
  c<-c+1
}
no_plumbing_2023<-get_acs(geography="block group", table="B25049", state="IL", county="Cook", year = 2023, cache_table=TRUE)
no_plumbing_2023_calc <- data.frame(GEOID = unique(no_plumbing_2023$GEOID))
no_plumbing_2023_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(no_plumbing_2023), by = 7)){
  numerator <- no_plumbing_2023$estimate[i+3]+no_plumbing_2023$estimate[i+6] + 1
  denominator <- no_plumbing_2023$estimate[i] + 1 
  no_plumbing_2023_calc$estimate[c] <- log((numerator/denominator)*100)
  c<-c+1
}

#PERCENT OF HOUSEHOLDS WITH MORE THAN 1 PERSON PER ROOM
crowding_2015<-get_acs(geography="block group", table="B25014", state="IL", county="Cook", year = 2015, cache_table=TRUE)
crowding_2015_calc <- data.frame(GEOID = unique(crowding_2015$GEOID))
crowding_2015_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(crowding_2015), by = 13)){
  numerator <- sum(crowding_2015$estimate[seq(from = i+4, to = i+6, by = 1)])
  numerator <- numerator+ sum(crowding_2015$estimate[seq(from = i+10, to = i+12, by = 1)])
  denominator <- crowding_2015$estimate[i]  
  crowding_2015_calc$estimate[c] <- (numerator/denominator)*100
  c<-c+1
}
crowding_2023<-get_acs(geography="block group", table="B25014", state="IL", county="Cook", year = 2023, cache_table=TRUE)
crowding_2023_calc <- data.frame(GEOID = unique(crowding_2023$GEOID))
crowding_2023_calc[,"estimate"] <- NA
c<-1
for (i in seq(from = 1, to = nrow(crowding_2023), by = 13)){
  numerator <- sum(crowding_2023$estimate[seq(from = i+4, to = i+6, by = 1)])
  numerator <- numerator+ sum(crowding_2023$estimate[seq(from = i+10, to = i+12, by = 1)])
  denominator <- crowding_2023$estimate[i]  
  crowding_2023_calc$estimate[c] <- (numerator/denominator)*100
  c<-c+1
}

#REPLACE MISSING VALUES FOR 2015
total_population_2015_calc[is.na(total_population_2015_calc)] <- 0
median_income_2015_calc[is.na(median_income_2015_calc)] <- 0
income_disparity_2015_calc[is.na(income_disparity_2015_calc)] <- 0
below_poverty_2015_calc[is.na(below_poverty_2015_calc)] <- 0
below_poverty_higher_2015_calc[is.na(below_poverty_higher_2015_calc)] <- 0
no_highschool_2015_calc[is.na(no_highschool_2015_calc)] <- 0
higher_ed_2015_calc[is.na(higher_ed_2015_calc)] <- 0
white_collar_2015_calc[is.na(white_collar_2015_calc)] <- 0
unemployed_2015_calc[is.na(unemployed_2015_calc)] <- 0
median_home_value_2015_calc[is.na(median_home_value_2015_calc)] <- 0
median_gross_rent_2015_calc[is.na(median_gross_rent_2015_calc)] <- 0
median_monthly_mortgage_2015_calc[is.na(median_monthly_mortgage_2015_calc)] <- 0
owner_occupied_2015_calc[is.na(owner_occupied_2015_calc)] <- 0
single_parents_2015_calc[is.na(single_parents_2015_calc)] <- 0
no_vehicle_2015_calc[is.na(no_vehicle_2015_calc)] <- 0
no_phone_2015_calc[is.na(no_phone_2015_calc)] <- 0
no_plumbing_2015_calc[is.na(no_plumbing_2015_calc)] <- 0
crowding_2015_calc[is.na(crowding_2015_calc)] <- 0

#CALCULATE Z SCORES FOR 2015
median_income_2015_calc$scaled<-scale(median_income_2015_calc$estimate)
income_disparity_2015_calc$scaled<-scale(income_disparity_2015_calc$estimate)
below_poverty_2015_calc$scaled<-scale(below_poverty_2015_calc$estimate)
below_poverty_higher_2015_calc$scaled<-scale(below_poverty_higher_2015_calc$estimate)
no_highschool_2015_calc$scaled<-scale(no_highschool_2015_calc$estimate)
higher_ed_2015_calc$scaled<-scale(higher_ed_2015_calc$estimate)
white_collar_2015_calc$scaled<-scale(white_collar_2015_calc$estimate)
unemployed_2015_calc$scaled<-scale(unemployed_2015_calc$estimate)
median_home_value_2015_calc$scaled<-scale(median_home_value_2015_calc$estimate)
median_gross_rent_2015_calc$scaled<-scale(median_gross_rent_2015_calc$estimate)
median_monthly_mortgage_2015_calc$scaled<-scale(median_monthly_mortgage_2015_calc$estimate)
owner_occupied_2015_calc$scaled<-scale(owner_occupied_2015_calc$estimate)
single_parents_2015_calc$scaled<-scale(single_parents_2015_calc$estimate)
no_vehicle_2015_calc$scaled<-scale(no_vehicle_2015_calc$estimate)
no_phone_2015_calc$scaled<-scale(no_phone_2015_calc$estimate)
no_plumbing_2015_calc$scaled<-scale(no_plumbing_2015_calc$estimate)
crowding_2015_calc$scaled<-scale(crowding_2015_calc$estimate)

#CALCULATE POPULATIONS WEIGHTS AND APPLY FOR 2015
all_population_2015<-sum(total_population_2015_calc$estimate)
total_population_2015_calc$weight <- sqrt(total_population_2015_calc$estimate/all_population_2015)+1

#COMBINE ALL 2015 VARIABLES 
all_variables <- data.frame(GEOID = unique(crowding_2015$GEOID))
all_variables$median_income<-median_income_2015_calc$estimate
all_variables$income_disparity<-income_disparity_2015_calc$estimate
all_variables$below_poverty<-below_poverty_2015_calc$estimate
all_variables$below_poverty_higher<-below_poverty_higher_2015_calc$estimate
all_variables$no_highschool<-no_highschool_2015_calc$estimate
all_variables$higher_ed<-higher_ed_2015_calc$estimate
all_variables$white_collar<-white_collar_2015_calc$estimate
all_variables$unemployed<-unemployed_2015_calc$estimate
all_variables$median_home_value<-median_home_value_2015_calc$estimate
all_variables$median_gross_rent<-median_gross_rent_2015_calc$estimate
all_variables$median_monthly_mortgage<-median_monthly_mortgage_2015_calc$estimate
all_variables$owner_occupied<-owner_occupied_2015_calc$estimate
all_variables$single_parents<-single_parents_2015_calc$estimate
all_variables$no_vehicle<-no_vehicle_2015_calc$estimate
all_variables$no_phone<-no_phone_2015_calc$estimate
all_variables$no_plumbing<-no_plumbing_2015_calc$estimate
all_variables$crowding<-crowding_2015_calc$estimate
all_variables$GEOID<-NULL

#APPLY FACTOR ANALYSIS OVER 2015 VARIABLES
ReADI_2015.fa<-fa(all_variables, nfactors = 1, fm = "pa", weight = total_population_2015_calc$weight)
raw_scores_2015<-ReADI_2015.fa$scores
scaled_scores_2015<-xtile(raw_scores_2015, n = 100, wt = total_population_2015_calc$estimate)
ReADI_final_2015<- data.frame(GEOID = unique(crowding_2015$GEOID))
ReADI_final_2015$score<-scaled_scores_2015

all_variables<-NULL

#REPLACE MISSING VALUES FOR 2023
total_population_2023_calc[is.na(total_population_2023_calc)] <- 0
median_income_2023_calc[is.na(median_income_2023_calc)] <- 0
income_disparity_2023_calc[is.na(income_disparity_2023_calc)] <- 0
below_poverty_2023_calc[is.na(below_poverty_2023_calc)] <- 0
below_poverty_higher_2023_calc[is.na(below_poverty_higher_2023_calc)] <- 0
no_highschool_2023_calc[is.na(no_highschool_2023_calc)] <- 0
higher_ed_2023_calc[is.na(higher_ed_2023_calc)] <- 0
white_collar_2023_calc[is.na(white_collar_2023_calc)] <- 0
unemployed_2023_calc[is.na(unemployed_2023_calc)] <- 0
median_home_value_2023_calc[is.na(median_home_value_2023_calc)] <- 0
median_gross_rent_2023_calc[is.na(median_gross_rent_2023_calc)] <- 0
median_monthly_mortgage_2023_calc[is.na(median_monthly_mortgage_2023_calc)] <- 0
owner_occupied_2023_calc[is.na(owner_occupied_2023_calc)] <- 0
single_parents_2023_calc[is.na(single_parents_2023_calc)] <- 0
no_vehicle_2023_calc[is.na(no_vehicle_2023_calc)] <- 0
no_phone_2023_calc[is.na(no_phone_2023_calc)] <- 0
no_plumbing_2023_calc[is.na(no_plumbing_2023_calc)] <- 0
crowding_2023_calc[is.na(crowding_2023_calc)] <- 0

#CALCULATE Z SCORES FOR 2023
median_income_2023_calc$scaled<-scale(median_income_2023_calc$estimate)
income_disparity_2023_calc$scaled<-scale(income_disparity_2023_calc$estimate)
below_poverty_2023_calc$scaled<-scale(below_poverty_2023_calc$estimate)
below_poverty_higher_2023_calc$scaled<-scale(below_poverty_higher_2023_calc$estimate)
no_highschool_2023_calc$scaled<-scale(no_highschool_2023_calc$estimate)
higher_ed_2023_calc$scaled<-scale(higher_ed_2023_calc$estimate)
white_collar_2023_calc$scaled<-scale(white_collar_2023_calc$estimate)
unemployed_2023_calc$scaled<-scale(unemployed_2023_calc$estimate)
median_home_value_2023_calc$scaled<-scale(median_home_value_2023_calc$estimate)
median_gross_rent_2023_calc$scaled<-scale(median_gross_rent_2023_calc$estimate)
median_monthly_mortgage_2023_calc$scaled<-scale(median_monthly_mortgage_2023_calc$estimate)
owner_occupied_2023_calc$scaled<-scale(owner_occupied_2023_calc$estimate)
single_parents_2023_calc$scaled<-scale(single_parents_2023_calc$estimate)
no_vehicle_2023_calc$scaled<-scale(no_vehicle_2023_calc$estimate)
no_phone_2023_calc$scaled<-scale(no_phone_2023_calc$estimate)
no_plumbing_2023_calc$scaled<-scale(no_plumbing_2023_calc$estimate)
crowding_2023_calc$scaled<-scale(crowding_2023_calc$estimate)

#CALCULATE POPULATIONS WEIGHTS AND APPLY FOR 2023
all_population_2023<-sum(total_population_2023_calc$estimate)
total_population_2023_calc$weight <- sqrt(total_population_2023_calc$estimate/all_population_2023)+1

#COMBINE ALL 2023 VARIABLES 
all_variables <- data.frame(GEOID = unique(crowding_2023$GEOID))
all_variables$median_income<-median_income_2023_calc$estimate
all_variables$income_disparity<-income_disparity_2023_calc$estimate
all_variables$below_poverty<-below_poverty_2023_calc$estimate
all_variables$below_poverty_higher<-below_poverty_higher_2023_calc$estimate
all_variables$no_highschool<-no_highschool_2023_calc$estimate
all_variables$higher_ed<-higher_ed_2023_calc$estimate
all_variables$white_collar<-white_collar_2023_calc$estimate
all_variables$unemployed<-unemployed_2023_calc$estimate
all_variables$median_home_value<-median_home_value_2023_calc$estimate
all_variables$median_gross_rent<-median_gross_rent_2023_calc$estimate
all_variables$median_monthly_mortgage<-median_monthly_mortgage_2023_calc$estimate
all_variables$owner_occupied<-owner_occupied_2023_calc$estimate
all_variables$single_parents<-single_parents_2023_calc$estimate
all_variables$no_vehicle<-no_vehicle_2023_calc$estimate
all_variables$no_phone<-no_phone_2023_calc$estimate
all_variables$no_plumbing<-no_plumbing_2023_calc$estimate
all_variables$crowding<-crowding_2023_calc$estimate
all_variables$GEOID<-NULL

#APPLY FACTOR ANALYSIS OVER 2023 VARIABLES
ReADI_2023.fa<-fa(all_variables, nfactors = 1, fm = "pa", weight = total_population_2023_calc$weight)
raw_scores_2023<-ReADI_2023.fa$scores
scaled_scores_2023<-xtile(raw_scores_2023, n = 100, wt = total_population_2023_calc$estimate)
ReADI_final_2023<- data.frame(GEOID = unique(crowding_2023$GEOID))
ReADI_final_2023$score<-scaled_scores_2023

#ADD COMMUNITY AREAS
community_areas_path <- "2020_Census_Tracts_to_Chicago_Community_Area_Equivalency_File.xlsx"
community_areas <- read_excel(community_areas_path)
ReADI_final_2015$GEOID20<-substr(ReADI_final_2015$GEOID,1,11)
ReADI_final_2023$GEOID20<-substr(ReADI_final_2023$GEOID,1,11)
community_areas$GEOID20<-as.character(community_areas$GEOID20)
ReADI_final_2015<-dplyr::filter(ReADI_final_2015,GEOID20 %in% community_areas$GEOID20)
ReADI_final_2023<-dplyr::filter(ReADI_final_2023,GEOID20 %in% community_areas$GEOID20)
ReADI_final_2015<-left_join(ReADI_final_2015,community_areas,by="GEOID20")
ReADI_final_2023<-left_join(ReADI_final_2023,community_areas,by="GEOID20")

#WRITE ReADI DATA
#UNCOMMENT AND SET PATHS APPROPRIATELY TO ENABLE
#ReADI_final_2015_path<-"ReADI_final_2015.csv"
#ReADI_final_2023_path<-"ReADI_final_2023.csv"

#write.csv(ReADI_final_2015, ReADI_final_2015_path)
#write.csv(ReADI_final_2023, ReADI_final_2023_path)