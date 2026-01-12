#SCRIPT TO DISPLAY ReADI PLOTS

#imports
library(tidycensus)
library(sf)
library(dplyr)
library(tidyr)
library(readr)
library(ggplot2)
library(tidyverse)
library(tigris)
options(tigris_use_cache = TRUE)

#LOAD ReADI DATA
ReADI_2015<-read.csv("ReADI_final_2015.csv")
ReADI_2023<-read.csv("ReADI_final_2023.csv")

#LOAD SHAPEFILES
chicago_shapefile <- sf::st_read("Boundaries - Community Areas_20251007\\geo_export_3567708c-82d2-43ee-8fc3-0275b4c786f4.shp")
chicago_shapefile_transformed <- sf::st_transform(chicago_shapefile, crs=4269)
illinois_block_groups_2015 <- block_groups("IL", year=2015)
illinois_block_groups_2023 <- block_groups("IL", year=2023)

#RESTRICT SHAPEFILES TO ONLY CHICAGO AND COMBINE WITH ReADI DATA
illinois_block_groups_2015$GEOID<-as.double(illinois_block_groups_2015$GEOID)
illinois_block_groups_2015<-dplyr::filter(illinois_block_groups_2015,GEOID %in% ReADI_2015$GEOID)
illinois_block_groups_2015<-left_join(illinois_block_groups_2015,ReADI_2015,by="GEOID")
illinois_block_groups_2023$GEOID<-as.double(illinois_block_groups_2023$GEOID)
illinois_block_groups_2023<-dplyr::filter(illinois_block_groups_2023,GEOID %in% ReADI_2023$GEOID)
illinois_block_groups_2023<-left_join(illinois_block_groups_2023,ReADI_2023,by="GEOID")

#PLOT CHICAGO
plot<-ggplot()
plot<-plot + geom_sf(data=chicago_shapefile_transformed)
plot<-plot + geom_sf_text(data=chicago_shapefile_transformed,aes(label=area_num_1))
plot<-plot + theme(axis.text.x = element_blank())+theme(axis.text.y = element_blank())
plot<-plot + theme(axis.title.x = element_blank())+theme(axis.title.y = element_blank())
plot<-plot + labs(title = "Chicago Community Areas")
plot

#PLOT 2015 BLOCK GROUP ReADI and COMMUNITY AREA ReADI
plot<-ggplot()
plot<-plot + geom_sf(data=illinois_block_groups_2015,aes(fill=score))
plot<-plot + theme(axis.text.x = element_blank())+theme(axis.text.y = element_blank())
plot<-plot + scale_fill_viridis_c(option="inferno")
plot<-plot + theme(axis.title.x = element_blank())+theme(axis.title.y = element_blank())
plot<-plot + labs(title = "Chicago ReADI block group scores (2015)",fill="ReADI")
plot

community_areas_readi_2015 <- data.frame(area_num_1 = unique(illinois_block_groups_2015$CA))
community_areas_readi_2015$total<-0
community_areas_readi_2015$count<-0
c<-1
for (i in seq(from = 1, to = nrow(illinois_block_groups_2015))){
  ca<-as.numeric(illinois_block_groups_2015[c,"CA"])
  current<-community_areas_readi_2015[community_areas_readi_2015$area_num_1 == ca[1], "total"]
  current<-current+as.numeric(illinois_block_groups_2015[c,"score"])[1]
  community_areas_readi_2015[community_areas_readi_2015$area_num_1 == ca[1], "total"]<-current
  counter<-community_areas_readi_2015[community_areas_readi_2015$area_num_1 == ca[1], "count"]
  counter<-counter+1
  community_areas_readi_2015[community_areas_readi_2015$area_num_1 == ca[1], "count"]<-counter
  c<-c+1
}
community_areas_readi_2015$average<-community_areas_readi_2015$total/community_areas_readi_2015$count
community_areas_readi_2015$area_num_1<-as.character(community_areas_readi_2015$area_num_1)
chicago_readi_2015<-left_join(chicago_shapefile_transformed,community_areas_readi_2015,by="area_num_1")

plot<-ggplot()
plot<-plot + geom_sf(data=chicago_readi_2015,aes(fill=average))
plot<-plot + theme(axis.text.x = element_blank())+theme(axis.text.y = element_blank())
plot<-plot + scale_fill_viridis_c(option="inferno")
plot<-plot + theme(axis.title.x = element_blank())+theme(axis.title.y = element_blank())
plot<-plot + labs(title = "Chicago ReADI community area scores (2015)",fill="Average\nReADI")
plot

#PLOT 2023 BLOCK GROUP ReADI and COMMUNITY AREA ReADI
plot<-ggplot()
plot<-plot + geom_sf(data=illinois_block_groups_2023,aes(fill=score))
plot<-plot + theme(axis.text.x = element_blank())+theme(axis.text.y = element_blank())
plot<-plot + scale_fill_viridis_c(option="inferno")
plot<-plot + theme(axis.title.x = element_blank())+theme(axis.title.y = element_blank())
plot<-plot + labs(title = "Chicago ReADI block group scores (2023)",fill="ReADI")
plot

community_areas_readi_2023 <- data.frame(area_num_1 = unique(illinois_block_groups_2023$CA))
community_areas_readi_2023$total<-0
community_areas_readi_2023$count<-0
c<-1
for (i in seq(from = 1, to = nrow(illinois_block_groups_2023))){
  ca<-as.numeric(illinois_block_groups_2023[c,"CA"])
  current<-community_areas_readi_2023[community_areas_readi_2023$area_num_1 == ca[1], "total"]
  current<-current+as.numeric(illinois_block_groups_2023[c,"score"])[1]
  community_areas_readi_2023[community_areas_readi_2023$area_num_1 == ca[1], "total"]<-current
  counter<-community_areas_readi_2023[community_areas_readi_2023$area_num_1 == ca[1], "count"]
  counter<-counter+1
  community_areas_readi_2023[community_areas_readi_2023$area_num_1 == ca[1], "count"]<-counter
  c<-c+1
}
community_areas_readi_2023$average<-community_areas_readi_2023$total/community_areas_readi_2023$count
community_areas_readi_2023$area_num_1<-as.character(community_areas_readi_2023$area_num_1)
chicago_readi_2023<-left_join(chicago_shapefile_transformed,community_areas_readi_2023,by="area_num_1")

plot<-ggplot()
plot<-plot + geom_sf(data=chicago_readi_2023,aes(fill=average))
plot<-plot + theme(axis.text.x = element_blank())+theme(axis.text.y = element_blank())
plot<-plot + scale_fill_viridis_c(option="inferno")
plot<-plot + theme(axis.title.x = element_blank())+theme(axis.title.y = element_blank())
plot<-plot + labs(title = "Chicago ReADI community area scores (2023)",fill="Average\nReADI")
plot

#COMPUTE AND DISPLAY DIFFERENCE PLOT BETWEEN 2023 AND 2015 COMMUNITY AREAS

chicago_readi_2023$difference<-100*(chicago_readi_2023$average - chicago_readi_2015$average)/chicago_readi_2015$average
plot<-ggplot()
plot<-plot + geom_sf(data=chicago_readi_2023,aes(fill=difference))
plot<-plot + theme(axis.text.x = element_blank())+theme(axis.text.y = element_blank())
plot<-plot + scale_fill_viridis_c(option="inferno")
plot<-plot + theme(axis.title.x = element_blank())+theme(axis.title.y = element_blank())
plot<-plot + labs(title = "Chicago ReADI community area scores\npercent change between 2023 and 2015",fill="Percent change")
plot

#COMPUTE AND DISPLAY METRICS (MEAN AND STANDARD DEVIATION)

block_group_average_readi_2015 <- round(mean(illinois_block_groups_2015$score),4)
block_group_std_readi_2015 <- round(sd(illinois_block_groups_2015$score),4)

block_group_average_readi_2023 <- round(mean(illinois_block_groups_2023$score),4)
block_group_std_readi_2023 <- round(sd(illinois_block_groups_2023$score),4)

community_average_readi_2015 <- round(mean(chicago_readi_2015$average),4)
community_std_readi_2015 <- round(sd(chicago_readi_2015$average),4)

community_average_readi_2023 <- round(mean(chicago_readi_2023$average),4)
community_std_readi_2023 <- round(sd(chicago_readi_2023$average),4)

percent_change_readi <- round(mean(chicago_readi_2023$difference),4)
percent_std_readi <- round(sd(chicago_readi_2023$difference),4)

block_group_average_readi_2015<-paste0("Average ReADI over block groups (2015): ",block_group_average_readi_2015)
block_group_std_readi_2015<-paste0("ReADI standard deviation over block groups (2015): ",block_group_std_readi_2015)
block_group_average_readi_2023<-paste0("Average ReADI over block groups (2023): ",block_group_average_readi_2023)
block_group_std_readi_2023<-paste0("ReADI standard deviation over block groups (2023): ",block_group_std_readi_2023)

community_average_readi_2015<-paste0("Average ReADI over community areas (2015): ",community_average_readi_2015)
community_std_readi_2015<-paste0("ReADI standard deviation over community areas (2015): ",community_std_readi_2015)
community_average_readi_2023<-paste0("Average ReADI over community areas (2023): ",community_average_readi_2023)
community_std_readi_2023<-paste0("ReADI standard deviation over community areas (2023): ",community_std_readi_2023)

percent_change_readi<-paste0("Average percent increase from 2015 to 2023: ",percent_change_readi)
percent_std_readi<-paste0("Standard deviation in percent increase from 2015 to 2023: ",percent_std_readi)

block_group_average_readi_2015
block_group_std_readi_2015
block_group_average_readi_2023
block_group_std_readi_2023
community_average_readi_2015
community_std_readi_2015
community_average_readi_2023
community_std_readi_2023
percent_change_readi
percent_std_readi