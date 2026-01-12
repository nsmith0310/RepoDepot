#imports
library(tidycensus)
library(sf)
library(dplyr)
library(tidyr)
library(readr)
library(ggplot2)
library(tigris)
library(tidyverse)
library(readxl)
options(tigris_use_cache = TRUE)

community_areas_path <- "2020_Census_Tracts_to_Chicago_Community_Area_Equivalency_File.xlsx"

community_areas <- read_excel(community_areas_path)

chicago_geoid <- substr(community_areas$GEOID20,1,11)

chicago_shapefile <- sf::st_read("Boundaries - Community Areas_20251007\\geo_export_3567708c-82d2-43ee-8fc3-0275b4c786f4.shp")

chicago_shapefile_transformed <- sf::st_transform(chicago_shapefile, crs=4269)

illinois_block_groups <- block_groups("IL", year=2023)

illinois_block_groups$TRACT <- substr(illinois_block_groups$GEOID,1,11)

filtered_illinois_block_groups <- dplyr::filter(illinois_block_groups,TRACT %in% community_areas$GEOID20)



adjacency_key_path<-"adjacency_key.txt"
adjacency_key<-as.list(filtered_illinois_block_groups[,"GEOID"])
#writeLines(unlist(adjacency_key), con = adjacency_key_path)

centroids_path<-"centroids.txt"
centroids<-as.list(st_centroid(filtered_illinois_block_groups))
#writeLines(unlist(centroids), con = centroids_path)

adjacencies_path<-"adjacencies.txt"
adjacencies <- st_touches(filtered_illinois_block_groups)
adjacency_matrix <-as.matrix(adjacencies)
#write.table(adjacency_matrix, file = adjacencies_path, sep = ",", row.names = FALSE, col.names = FALSE)
