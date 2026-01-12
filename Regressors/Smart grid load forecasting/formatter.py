#import MinMaxScaler, StandardScaler
from sklearn.preprocessing import MinMaxScaler, StandardScaler
#import pands
import pandas as pd
#import numpy 
import numpy as np
#import polynomial features
from sklearn.preprocessing import PolynomialFeatures

#function to remove June 2008
def remove_june2008(temps,loads,inverse=False):
    #regular removal removes June 2008
    if not inverse:
        #drop June 2008 in both Temperatures and Loads
        temps = temps.drop(temps[(temps.year == 2008) & (temps.month==6)].index)
        loads = loads.drop(loads[(loads.year == 2008) & (loads.month==6)].index)
    #inverse removal selects June 2008
    else:
        #drop everything except June 2008 in Temperatures and Loads
        temps = temps.drop(temps[(temps.year != 2008) | (temps.month!=6)].index)
        loads = loads.drop(loads[(loads.year != 2008) | (loads.month!=6)].index) 
    return temps,loads

#function to remove columns 2-4 (day, date, month)
def remove_data(temps,loads):
    #select columns 1-4 from Temperatures
    columns_to_drop = temps.columns[1:4]
    #drop columns 1-4 from Temperatures
    temps.drop(columns=columns_to_drop, axis=1, inplace=True)
    #select columns 1-4 from Loads
    columns_to_drop = loads.columns[1:4]
    #drop columns 1-4 from Loads
    loads.drop(columns=columns_to_drop, axis=1, inplace=True)
    return temps,loads

#function to pair up load zone and temperature station data based on a mapping
#between 1 load zone and k temperature stations; converts dataframes to NumPy
def apply_mapping(temps,loads,maps):
    #empty list to contain Load zone data and Temperature station data
    load_zones = []
    #for each mapping, concatentate all Temperature station data by columns
    for mapping in maps:
        zone,stations = mapping[0],mapping[1]
        station_dfs = [temps[temps["station_id"] == idx] for idx in stations]
        for idx in range(len(station_dfs)):
            station_dfs[idx] = station_dfs[idx].drop(columns=["station_id"], axis=1).to_numpy()
        cat_stations=np.concatenate(station_dfs,axis=1)
        load_zone = loads[loads["zone_id"] == zone].to_numpy()
        load_zone = np.delete(load_zone, 0, axis=1)
        load_zones.append([load_zone,cat_stations])
    return load_zones

#summarize stations: take each station and create 1 single temperature value for
#each hour by summarizing the stations values for that hour; summary methods allowed
#are mean, median, range, and variance 
def summarize_stations(maps,summary):
    #if summarizing create new Temperature station data for each Load zone
    if summary!=None:
        new_pairs = []
        for zone in maps:
            temps,new_temps = zone[1],[]
            for idx in range(24):
                #select values for each temperature station for a given hour
                hour = temps[:,idx::24]
                #take mean of hour values
                if summary=='mean':
                    hour = np.mean(hour,axis=1)
                #take median of hour values
                elif summary=='median':
                    hour = np.median(hour,axis=1)
                #take range of hour values
                elif summary=='range':
                    hour = np.ptp(hour,axis=1)
                #take variance of hour values
                elif summary=='var':
                    hour = np.var(hour,axis=1)
                #add new values
                new_temps.append(hour)
            #add new Load zone, Temperature station(s) pairing
            new_pairs.append([zone[0],np.asarray(new_temps).T])      
        return new_pairs
    else:
        return maps

#split both load zone and temperature stations into individual columns
def splitter(maps):
    #for each Load zone, Temperature station(s) pairing, split into individual
    #columns
    for idx in range(len(maps)):
        maps[idx][0] = np.hsplit(maps[idx][0],maps[idx][0].shape[1])
        maps[idx][1] = np.hsplit(maps[idx][1],maps[idx][1].shape[1])
    return maps
   
#add features based on user selection; supports day of month, day of year, year
#month, day of week, fiscal quarter, indexes, and whether the day is a weekend
def add_features(maps,columns,features=None):
    new_maps = []   
    #number of rows
    length = maps[0][1][0].shape[0]
    #get day of month and year from dataframe
    day_of_month = np.asarray(columns.iloc[:,2]).T
    year = np.asarray(columns.iloc[:,0]).T
    #copy of year 
    year_copy = year.copy()
    #get month from dataframe
    month = np.asarray(columns.iloc[:,1]).T
    #initialize new feature lists
    day_of_year,day_of_week,weekend,fisc_q = [],[],[],[]
    #initialize counters
    counter,current_year,current_day,season=1,2004,4,1
    #iterate over rows and populate features
    for idx in range(len(year)):
        day_of_year.append(counter)
        day_of_week.append(current_day)
        weekend.append(1*(day_of_week==6 or day_of_week==7))
        counter,current_day,year_copy[idx] = counter+1,current_day+1,current_year-2004+1
        fisc_q.append(month[idx]//4 + 1)           
        if current_day==8:
            current_day=1
        if year[idx]!=current_year:
            counter=1
            current_year+=1
    
    #convert feature lists to NumPy columns
    day_of_year,day_of_week = np.asarray(day_of_year).T,np.asarray(day_of_week).T
    weekend,fisc_q,season = np.asarray(weekend).T,np.asarray(fisc_q).T,np.asarray(season).T
    year,indexes = year_copy,np.asarray([idx+1 for idx in range(length)]).T

    #create dictionary of new features 
    feature_dict = dict()
    feature_dict['day_of_year']=day_of_year
    feature_dict['fisc_q']=fisc_q
    feature_dict['day_of_week']=day_of_week
    feature_dict['weekend']=weekend
    feature_dict['month']=month
    feature_dict['day_of_month']=day_of_month
    feature_dict['year']=year
    feature_dict['indexes']=indexes
    
    #based on selected features, add columns from dictionary
    for idx in range(len(maps)):       
        for col in range(len(maps[idx][1])):
            for feature_name in features:                
                maps[idx][1][col]=np.insert(maps[idx][1][col],0,feature_dict[feature_name],axis=1)              
        new_maps.append([maps[idx][0],maps[idx][1]])               
    return new_maps

#allows for standardizing and normalizing the data
def preprocessor(maps,mode=1):
    for idx in range(len(maps)):
        for col in range(len(maps[idx])):
            #normalize data if mode 1
            if mode==1:
                maps[idx][1][col] = MinMaxScaler().fit_transform(maps[idx][1][col])
            #standardize data if mode 2
            elif mode==2:
                maps[idx][1][col] = StandardScaler().fit_transform(maps[idx][1][col])
    return maps

#format predictions for conversion to csv
def format_june2008(predictions,original_dataframe):
    #select June 2008 from original dataframe
    june2008=original_dataframe[(original_dataframe.year == 2008) & (original_dataframe.month==6)]
    #drop hour values from new June 2008 dataframe
    columns_to_drop = original_dataframe.columns[4:]    
    june2008 = june2008.drop(columns=columns_to_drop, axis=1)    
    #get hour predictions
    predictions = pd.DataFrame(predictions,columns=columns_to_drop)
    #set correct indexes
    predictions.index = june2008.index
    #concatenate June 2008 with predictions
    formatted = pd.concat([june2008,predictions],axis=1)
    return formatted

#save csv file
def save_csv(dataframe):
    dataframe.to_csv('Load_prediction.csv',index=False)

#add polynomial features 
def feature_adder(stations,order=2):
    new_data = []    
    poly = PolynomialFeatures(degree=order, include_bias=False)
    #for each station, transform columns
    for station in stations:
        cols = []
        for col in station:
            cols.append(poly.fit_transform(col))
        new_data.append(cols)
    return new_data

#main driver function
def format_dataset(temps,loads,maps,remove=True,preprocess=1,summary=None,features=2,june2008=False):
    #remove June 2008
    temps,loads = remove_june2008(temps, loads,inverse=june2008)    
    #remove columns 1-4 but save to be readded if desired
    if remove==True:
        columns = temps.loc[:1613,temps.columns[1:4]]
        temps,loads = remove_data(temps,loads)
    #apply mapping
    maps = apply_mapping(temps, loads, maps)    
    #apply summary statistic
    maps = summarize_stations(maps,summary)
    #split by columns
    maps = splitter(maps)
    #add selected features if desired
    if features!=False:
        maps = add_features(maps,columns,features)
    #preprocess data if desired
    if preprocess==1 or preprocess==2:
        maps = preprocessor(maps,mode=preprocess)       
    return maps
        
    
    