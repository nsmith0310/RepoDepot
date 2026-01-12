#SCRIPT TO VISUALIZE RESULTS OF LOUVAINS COMMUNITY DETECTION AND SIMULATED ANNEALING
#SCRIPT ALSO COMPARES SIMULATED ANNEALING COMMUNITIES WITH ORIGINAL CHICAGO COMMUNITIES WITH RESPECT TO LOUVAINS

#IMPORTS
library(sf)
library(dplyr)
library(ggplot2)
library(tigris)
options(tigris_use_cache = TRUE)

#CHICAGO SHAPEFILE AND BLOCK GROUPS
chicago_shapefile <- sf::st_read("Boundaries - Community Areas_20251007\\geo_export_3567708c-82d2-43ee-8fc3-0275b4c786f4.shp")
chicago_shapefile_transformed <- sf::st_transform(chicago_shapefile, crs=4269)
illinois_block_groups_2023 <- block_groups("IL", year=2023)
ReADI_2023<-read.csv("ReADI_final_2023.csv")
illinois_block_groups_2023$GEOID<-as.double(illinois_block_groups_2023$GEOID)
illinois_block_groups_2023<-dplyr::filter(illinois_block_groups_2023,GEOID %in% ReADI_2023$GEOID)

#READ SIMULATED ANNEALING COMMUNITY AREAS AND AVERAGE READI SCORES
new_communities_folder<-"community_areas\\minimization\\"
new_communities <- list.files(path=new_communities_folder,full.names = TRUE)
new_communities<-lapply(new_communities, readLines)
new_communities_readi<-"community_areas\\average_readi\\minimization.txt"
new_communities_readi <- readLines(new_communities_readi, warn = FALSE)
nums<-c(1:37)
nums<-sort(as.character(nums))
nums<-as.integer(nums)

#CONVERT TEXT FILE CONTENTS TO SHAPEFILE
for (i in 1:length(new_communities)){
  new_communities[[i]]<-dplyr::filter(illinois_block_groups_2023,GEOID %in% new_communities[[i]])
  new_communities[[i]]<- sf::st_transform(new_communities[[i]], crs=4269)
  new_communities[[i]]<-st_union(new_communities[[i]])
  new_communities[[i]]<-st_as_sf(new_communities[[i]])
  new_communities[[i]]$name<-i
  new_communities[[i]]$avg_readi<-as.integer(new_communities_readi[nums[i]])
}

#RECOVER ORIGINAL CHICAGO COMMUNITY AREAS IN SAME GEOMETRY AS LOUVAINS AND SIMULATED ANNEALING
original_chicago<-left_join(illinois_block_groups_2023,ReADI_2023,by="GEOID")
chicago<-list()
for (i in 1:77){
  original_ca<-dplyr::filter(original_chicago,CA==i)
  temp<-list(as.character(c(original_ca$GEOID)))
  chicago<-append(chicago,temp)
  
}
#CONVERT TEXT FILE CONTENTS TO SHAPEFILE
for (i in 1:length(chicago)){
  chicago[[i]]<-dplyr::filter(illinois_block_groups_2023,GEOID %in% chicago[[i]])
  chicago[[i]]<- sf::st_transform(chicago[[i]], crs=4269)
  chicago[[i]]<-st_union(chicago[[i]])
  chicago[[i]]<-st_as_sf(chicago[[i]])
  chicago[[i]]$name<-i
}

#PLOT CURRENT CHICAGO COMMUNITY AREAS
plot<- ggplot() 
for (i in 1:length(chicago)){
  plot <- plot + geom_sf(data = chicago[[i]])
  plot <- plot + geom_sf_text(data = chicago[[i]],aes(label=name))
}
plot<-plot + theme(axis.text.x = element_blank())+theme(axis.text.y = element_blank())
plot<-plot + theme(axis.title.x = element_blank())+theme(axis.title.y = element_blank())
plot<-plot+labs(title = "Original Chicago community areas")
plot

#PLOT SIMULATED ANNEALING COMMUNITY AREAS
plot<- ggplot() 
for (i in 1:length(new_communities)){
  plot <- plot + geom_sf(data = new_communities[[i]])
  plot <- plot + geom_sf_text(data = new_communities[[i]],aes(label=name))
}
plot<-plot + theme(axis.text.x = element_blank())+theme(axis.text.y = element_blank())
plot<-plot + theme(axis.title.x = element_blank())+theme(axis.title.y = element_blank())
plot<-plot+labs(title = "New Chicago community areas")
plot

#PLOT SIMULATED ANNEALING COMMUNITY AREAS WITH AVERAGE READI
plot<- ggplot() 
for (i in 1:length(new_communities)){
  plot <- plot + geom_sf(data = new_communities[[i]],aes(fill=avg_readi))
  plot <- plot + geom_sf_text(data = new_communities[[i]],aes(label=name),color="green")
}
plot<-plot + theme(axis.text.x = element_blank())+theme(axis.text.y = element_blank())
plot<-plot + theme(axis.title.x = element_blank())+theme(axis.title.y = element_blank())
plot<-plot + scale_fill_viridis_c(option="inferno")
plot<-plot+labs(title = "New Chicago community areas\naverage ReADI",fill="Average\nReADI")
plot

#READ LOUVAINS COMMUNITY AREAS AND AVERAGE READI SCORES
detected_communities_folder<-"community_areas\\louvains\\"
detected_communities <- list.files(path=detected_communities_folder,full.names = TRUE)
detected_communities<-lapply(detected_communities, readLines)
detected_communities_readi<-"community_areas\\average_readi\\louvains.txt"
detected_communities_readi <- readLines(detected_communities_readi, warn = FALSE)
nums<-c(1:23)
nums<-sort(as.character(nums))
nums<-as.integer(nums)

#CONVERT TEXT FILE CONTENTS TO SHAPEFILE 
for (i in 1:length(detected_communities)){
  detected_communities[[i]]<-dplyr::filter(illinois_block_groups_2023,GEOID %in% detected_communities[[i]])
  
  detected_communities[[i]]<- sf::st_transform(detected_communities[[i]], crs=4269)
  detected_communities[[i]]<-st_union(detected_communities[[i]])
  detected_communities[[i]]<-st_as_sf(detected_communities[[i]])
  detected_communities[[i]]$name<-i
  detected_communities[[i]]$avg_readi<-as.integer(detected_communities_readi[nums[i]])
}

#PLOT LOUVAINS COMMUNITY AREAS
plot<- ggplot() 
for (i in 1:length(detected_communities)){
  plot <- plot + geom_sf(data = detected_communities[[i]])
  plot <- plot + geom_sf_text(data = detected_communities[[i]],aes(label=name))
}
plot<-plot + theme(axis.text.x = element_blank())+theme(axis.text.y = element_blank())
plot<-plot + theme(axis.title.x = element_blank())+theme(axis.title.y = element_blank())
plot<-plot+labs(title = "Chicago Louvain community areas")
plot

#PLOT LOUVAINS COMMUNITY AREAS WITH AVERAGE READI
plot<- ggplot() 
for (i in 1:length(detected_communities)){
  plot <- plot + geom_sf(data = detected_communities[[i]],aes(fill=avg_readi))
  plot <- plot + geom_sf_text(data = detected_communities[[i]],aes(label=name),color="green")
}
plot<-plot + theme(axis.text.x = element_blank())+theme(axis.text.y = element_blank())
plot<-plot + theme(axis.title.x = element_blank())+theme(axis.title.y = element_blank())
plot<-plot + scale_fill_viridis_c(option="inferno")
plot<-plot+labs(title = "Chicago Louvain community areas\naverage ReADI",fill="Average\nReADI")
plot

#OVERLAY LOUVAINS COMMUNITIES ON TOP OF ORIGINAL CHICAGO COMMUNITIES
plot<- ggplot() 
for (i in 1:length(chicago)){
  plot <- plot + geom_sf(data = chicago[[i]],color="black")
}
for (i in 1:length(detected_communities)){
  plot <- plot + geom_sf(data = detected_communities[[i]],color="red",alpha=.1)
}
plot<-plot + theme(axis.text.x = element_blank())+theme(axis.text.y = element_blank())
plot<-plot + theme(axis.title.x = element_blank())+theme(axis.title.y = element_blank())
plot<-plot+labs(title = "Chicago Louvain community areas (red)\non top of original community areas (black)")
plot


#OVERLAY LOUVAINS COMMUNITIES ON TOP OF SIMULATED ANNEALING COMMUNITIES
plot<-ggplot()
for (i in 1:length(new_communities)){
  plot <- plot + geom_sf(data = new_communities[[i]],color="black")
}
for (i in 1:length(detected_communities)){
  plot <- plot + geom_sf(data = detected_communities[[i]],color="red",alpha=.1)
}
plot<-plot + theme(axis.text.x = element_blank())+theme(axis.text.y = element_blank())
plot<-plot + theme(axis.title.x = element_blank())+theme(axis.title.y = element_blank())
plot<-plot+labs(title = "Chicago Louvain community areas (red)\non top of new community areas (black)")
plot


#OVERLAY 10 WORST LOUVAINS COMMUNITIES ON TOP OF ORIGINAL CHICAGO COMMUNITIES
plot<- ggplot() 
for (i in 1:length(chicago)){
  plot <- plot + geom_sf(data = chicago[[i]],color="black")
}
for (i in 1:10){
  plot <- plot + geom_sf(data = detected_communities[[i]],color="red",linewidth=1.5,alpha=.1)
  plot <- plot + geom_sf_text(data = detected_communities[[i]],aes(label=name),color="blue")
}
plot<-plot + theme(axis.text.x = element_blank())+theme(axis.text.y = element_blank())
plot<-plot + theme(axis.title.x = element_blank())+theme(axis.title.y = element_blank())
plot<-plot+labs(title = "10 Highest ReADI Louvain community areas (red)\non top of original community areas (black)")
plot

#OVERLAY 10 WORST LOUVAINS COMMUNITIES ON TOP OF SIMULATED ANNEALING COMMUNITIES
plot<-ggplot()
for (i in 1:length(new_communities)){
  plot <- plot + geom_sf(data = new_communities[[i]],color="black")
}
for (i in 1:10){
  plot <- plot + geom_sf(data = detected_communities[[i]],color="red",linewidth=1.5,alpha=.1)
  plot <- plot + geom_sf_text(data = detected_communities[[i]],aes(label=name),color="blue")
}
plot<-plot + theme(axis.text.x = element_blank())+theme(axis.text.y = element_blank())
plot<-plot + theme(axis.title.x = element_blank())+theme(axis.title.y = element_blank())
plot<-plot+labs(title = "10 Highest ReADI Louvain community areas (red)\non top of new community areas (black)")
plot

#CALCULATE JACCARD INDEX BETWEEN ORIGINAL COMMUNITY AREAS AND 10 WORST LOUVAIN COMMUNITIES
original_total_iou <- 0
original_count <- 0
for (i in 1:length(chicago)){
  original_community<-chicago[[i]]
  for (j in 1:10){
    louvain_community<-detected_communities[[j]]
    intersection<-st_area(st_intersection(original_community,louvain_community))[1]
    if (!is.na(intersection)){
      union<-st_area(st_union(original_community,louvain_community))[1]
      iou<-as.numeric(intersection/union)
      original_total_iou<-original_total_iou+iou
      original_count<-original_count+1
    }
  }
}
original_mean_iou<-original_total_iou/original_count

#CALCULATE JACCARD INDEX BETWEEN NEW COMMUNITY AREAS AND 10 WORST LOUVAIN COMMUNITIES
new_total_iou <- 0
new_count <- 0
for (i in 1:length(new_communities)){
  original_community<-new_communities[[i]]
  for (j in 1:10){
    louvain_community<-detected_communities[[j]]
    intersection<-st_area(st_intersection(original_community,louvain_community))[1]
    if (!is.na(intersection)){
      union<-st_area(st_union(original_community,louvain_community))[1]
      iou<-as.numeric(intersection/union)
      new_total_iou<-original_total_iou+iou
      new_count<-original_count+1
    }
  }
}
new_mean_iou<-new_total_iou/new_count

print("Original Chicago community areas")
print(paste0("Average Jaccard Index against 10 worst Louvain regions: ",round(original_mean_iou,4)))
print("Simulated annealing community areas")
print(paste0("Average Jaccard Index against 10 worst Louvain regions: ",round(new_mean_iou,4)))
