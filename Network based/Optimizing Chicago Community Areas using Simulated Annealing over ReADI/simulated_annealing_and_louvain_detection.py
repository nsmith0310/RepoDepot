#script to perform simulated annealing

#imports

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import time

#set plotting resolution

plt.rcParams['figure.dpi'] = 600
plt.rcParams['savefig.dpi'] = 600

#seeds for random numbers for reproducability

numpy_seed = 10
sklearn_seed = 0

#set numpy random number generator seed for reproducability

np.random.seed(numpy_seed)

#adjacency matrix, key, and geometric centroids paths

adjacencies_path = "adjacencies.txt"
adjacenties_key_path = "adjacency_key.txt"
centroids_path = "centroids.txt"

adjacencies = []
block_groups = []
centroids = []

#read adjacencies

with open(adjacencies_path, 'r') as file:
    for line in file:
        adjacencies.append(line.split(","))

#read adjacency key

counter = 0
with open(adjacenties_key_path, 'r') as file:
    for line in file:
        if counter<2162:
            block_groups.append(line.strip())
            counter+=1

#read node centroids

read = False
counter = 0
parity = 0
with open(centroids_path, 'r') as file:
    for line in file:
        if counter==28106:
            read = True
        if read == True:
            if parity == 0:
                centroids.append([float(line)])
                parity = 1
            else:
                centroids[-1].append(float(line))
                parity = 0
        counter+=1

#use dictionary to make adjacency list 

graph = dict()
counter = 0
for block_group in block_groups:
    graph[block_group]=[]
    for idx in range(len(adjacencies[counter])):
        if adjacencies[counter][idx]=='TRUE':
            graph[block_group].append(block_groups[idx])
    counter+=1

for node in graph:
    for neighbor in graph[node]:
        if node not in graph[neighbor]:
            graph[neighbor].append(node)

#make dictionary of node centroids for plotting

node_centroids = dict()
for idx in range(len(block_groups)):
    node_centroids[block_groups[idx]]=tuple(centroids[idx])
    

#make linear encoding of adjacencies
#this will be needed to decode bit strings from simulated annealing

unique_pairs = set()
linear_encoding = []
for block_group in graph:
    for neighbor in graph[block_group]:
        pair = tuple(sorted([block_group,neighbor]))
        if pair not in unique_pairs:
            linear_encoding.append(pair)
            unique_pairs.add(pair)

#import ReADI data and populate dictionary to store block group-ReADI pairs

adi_path="ReADI_final_2023.csv"

adi_data = pd.read_csv(adi_path)
block_group_indexes = dict()
for idx,row in adi_data.iterrows():
    block_group_indexes[int(row["GEOID"])] = idx


block_group_data = dict()

for idx, row in adi_data.iterrows():
    geoid = row["GEOID"]
    score = row["score"]
    block_group_data[int(geoid)]=score

#temperature scheduling function for simulated annealing

def schedule(i,t,a):
    return t*np.e**(-i*a)

#function to generate simulated annealing initial solutions
#used prior to deciding to use the chicago community areas as the 
#starting point

def generate_solution(encoding_length,mode="random"):
    if mode=="all_connected": 
        return [1]*encoding_length
    elif mode=="none_connected":
        return [0]*encoding_length
    elif mode == "random":
        encoding = np.random.randint(0, 2, encoding_length)
        return list(encoding)

#function to modify existing simulated annealing solution
#allows choosing how many edges to toggle per iteration though the default
#of one is most consistent with the concepts of local search

def modify_solution(encoding, encoding_length, flips=1): 
    new_encoding = [x for x in encoding]
    indexes = np.random.randint(0, encoding_length-1, flips)
    for idx in indexes:
        if encoding[idx]==1:
            new_encoding[idx]=0
        else:
            new_encoding[idx]=1
    return new_encoding

#plot graph

def graph_plotter(encoding):
    G = nx.Graph()
    G.add_nodes_from(block_groups)
    for i in range(len(encoding)):
        if encoding[i]==1:
            u,v = linear_encoding[i]
            G.add_edge(u,v,weight=.3,type="A")
        else:
            u,v = linear_encoding[i]
            G.add_edge(u,v,weight=.1,type="B")
    color_map = {'A': 'black', 'B': 'red'}
    edge_colors = [color_map[G[u][v]['type']] for u, v in G.edges()]
    edge_weights = nx.get_edge_attributes(G, 'weight').values()
    return G,edge_colors,edge_weights

#get node degrees; needed in order to ignore type B edges 

def get_degree(G):
    degrees = [0]*len(block_groups)
    for i in range(len(block_groups)):
        edges = G.edges(block_groups[i], data=True)
        for x in edges:
            if x[2]['type']=='A':
                degrees[i]+=1
    return degrees

#compute degree distribution statistics for plotting

def degree_distribution_statistics(degrees):
    mean_degree = str(round(np.mean(degrees),3))
    degree_std = str(round(np.std(degrees),3))
    label_string = "\nMean degree: "+mean_degree+"; degree standard deviation: "+degree_std
    return label_string

#convert linear encodings used by simulated annealing to graph form

def encoding_to_graph(encoding):
    G = nx.Graph()
    G.add_nodes_from(block_groups)
    for i in range(len(encoding)):
        if encoding[i]==1:
            u,v = linear_encoding[i]
            edge = [(u,v)]
            G.add_edges_from(edge)
    return G

num_block_groups = len(block_groups)

#evaluation function which balances minimizing readi against merging all block groups
#penalize score proportionally to diverging from the average current community area
#size - otherwise simulated annealing will exploit the math of averages and just
#merge everything
 
def evaluate(encoding,average_size,k):
    average_adi = 0
    total_size_penalty = 0
    community_areas_graph = encoding_to_graph(encoding)
    community_areas = list(nx.connected_components(community_areas_graph))
    for community_area in community_areas:
        lth = len(community_area)
        x = [block_group_data[int(val)] for val in community_area]
        x = np.array(x)
        penalty = max(1,100*k*abs(lth-average_size)/(num_block_groups-average_size))
        total_size_penalty+= penalty
        average_adi+=np.mean(x)
    
    if k!=0:
        return (average_adi/len(community_areas))+total_size_penalty
    else: 
        return average_adi/len(community_areas)

#compute average readi for each community area

def compute_average_readi(encoding):
    readi_scores = []
    community_areas_graph = encoding_to_graph(encoding)
    community_areas = list(nx.connected_components(community_areas_graph))
    for community_area in community_areas:
        x = [block_group_data[int(val)] for val in community_area]
        x = np.array(x)
        readi_scores.append(np.mean(x))
    return readi_scores,community_areas
        
#primary simulated annealing algorithm

def simulated_annealing(initial_solution,T,a,reheats,average_size,k,flips=1):
    encoding_length = len(initial_solution)
    initial_T = T
    temperatures, scores, iterations = [],[],[]
    best_score = float("inf")
    best_solution = [x for x in initial_solution]
    current_solution = [x for x in initial_solution]
    current_cost = evaluate(initial_solution,average_size,k)
    #iterate until temperature and reheats are exhausted
    i = 1
    iteration = 1
    while True:
        #obtain current temperature from schedule
        T = float(schedule(i,T,a))
        temperatures.append(T)
        scores.append(current_cost)
        iterations.append(iteration)
        
        #if temperature and reheats are exhausted, return results
        if T<=0:
            if reheats==0:
                return [best_solution,best_score,temperatures, scores, iterations]
            else:
                reheats-=1
                T = initial_T
                i = 1
        #get random successor of current solution
        successor = modify_solution(current_solution,encoding_length,flips)
        #get cost of successor
        successor_cost = evaluate(successor,average_size,k)
        #calculate delta
        delta = float(current_cost - successor_cost)
        #if new solution is better, move to it
        if delta>0:
            current_solution = [x for x in successor]
            current_cost = successor_cost
        #otherwise use delta and current temperature to probabilistically
        #accept the worse successor
        else:
            if np.e**(delta/T)>np.random.rand():
                current_solution = [x for x in successor]
                current_cost = successor_cost
        #increment counter used for temperature scheduling
        if current_cost<best_score:
            best_score=current_cost
            best_solution = [x for x in current_solution]
        i+=1
        iteration+=1

#louvains helper functions

def louvains():
    similarities = dict()

    for block_group_u in block_groups:
        similarity_dict = dict()
        for block_group_v in block_groups:
            v1 = block_group_data[int(block_group_u)]
            v2 = block_group_data[int(block_group_v)]
            similarity_dict[block_group_v] = abs(v1-v2)
        similarities[block_group_u] = similarity_dict

    weighted_edges = set()

    for block_group in graph:
        for neighbor in graph[block_group]:
            similarity = similarities[block_group][neighbor]
            ordered_edge = sorted([block_group,neighbor])+[similarity]
            weighted_edges.add(tuple(ordered_edge))
            
    G = nx.Graph()
    
    G.add_nodes_from(block_groups)
    G.add_weighted_edges_from(list(weighted_edges))
    
    #184 is the seed discovered resulting in lowest known count of detected 
    #communities: 23
    detected_communities = list(nx.community.louvain_communities(G,seed=184))
    
    louvains_encoding = [0]*len(linear_encoding)
    #convert to linear encoding for plotting
    for i in range(len(linear_encoding)):
        node1 = linear_encoding[i][0]
        node2 = linear_encoding[i][1]
        for community in detected_communities:
            if node1 in community and node2 in community:
                louvains_encoding[i]=1
    return detected_communities,louvains_encoding

#display graph of all chicago block groups connected geographically and the
#degree distribution; ignores community area boundaries

G,edge_colors,edge_weights = graph_plotter([1]*len(linear_encoding))
nx.draw(G, edge_color=edge_colors,pos=node_centroids,node_size=2, width=list(edge_weights),node_color="blue")
plt.title("Complete Chicago block group graph")
plt.show()
plt.clf()

degrees = sorted(get_degree(G))
plt.plot([i for i in range(len(block_groups))],degrees)
plt.xticks([])
plt.xlabel("Block Groups")
plt.ylabel("Degree")
plt.title("Chicago block groups degree distribution\n"+degree_distribution_statistics(degrees))
plt.show()
plt.clf()

print()

#run louvain community detection on chicago; ignores community area boundaries

detected_communities,louvains_encoding = louvains()
louvains_scores,louvains_areas = compute_average_readi(louvains_encoding)
louvains_average_readi = sum(louvains_scores)/len(louvains_scores)

print("Louvain's community detection completed.")
print(str(len(detected_communities))+" communities detected.")
print("Louvain's community detection average ReADI: "+str(round(louvains_average_readi,4)))
print()

#plot detected communities; edges removed between separate community areas

G,edge_colors,edge_weights = graph_plotter(louvains_encoding)
nx.draw(G, edge_color=edge_colors,pos=node_centroids,node_size=2, width=list(edge_weights),node_color="blue")
plt.title("Louvain's communities")
plt.show()
plt.clf()

degrees = sorted(get_degree(G))
plt.plot([i for i in range(len(block_groups))],degrees)
plt.xticks([])
plt.xlabel("Block Groups")
plt.ylabel("Degree")
plt.title("Louvain's communities degree distribution\n"+degree_distribution_statistics(degrees))
plt.show()
plt.clf()

#display graph of all chicago community areas as they currently are and the 
#degree distribution

base_chicago_community_encoding = [0]*len(linear_encoding)

for i in range(len(linear_encoding)):
    node1 = linear_encoding[i][0]
    node2 = linear_encoding[i][1]
    node1_ca = int(adi_data.loc[block_group_indexes[int(node1)]]["CA"])
    node2_ca = int(adi_data.loc[block_group_indexes[int(node2)]]["CA"])
    if node1_ca==node2_ca:
        base_chicago_community_encoding[i]=1

G = encoding_to_graph(base_chicago_community_encoding)
community_areas = list(nx.connected_components(G))
average_size = sum([len(community) for community in community_areas])/len(community_areas)


G,edge_colors,edge_weights = graph_plotter(base_chicago_community_encoding)
nx.draw(G, edge_color=edge_colors,pos=node_centroids,node_size=2, width=list(edge_weights),node_color="blue")
plt.title("Current Chicago community areas graph")
plt.show()
plt.clf()

degrees = sorted(get_degree(G))
plt.plot([i for i in range(len(block_groups))],degrees)
plt.xticks([])
plt.xlabel("Block Groups")
plt.ylabel("Degree")
plt.title("Chicago community areas degree distribution\n"+degree_distribution_statistics(degrees))
plt.show()
plt.clf()

#simulated annealing hyperparameters

T=.5  
a=.0005 
reheats = 10 
flips=1 
k=.9 

print("Running Simulated Annealing...")
print()

#run simulated annealing

start_time = time.time()
best_solution,best_score,temperatures, scores, iterations = simulated_annealing(base_chicago_community_encoding,T,a, reheats,average_size,k,flips)
end_time = time.time()
search_minutes = (end_time-start_time)/60

#draw graph and degree distribution for repartitioning found by simulated annealing

new_graph = encoding_to_graph(best_solution)

G,edge_colors,edge_weights = graph_plotter(best_solution)
nx.draw(G, edge_color=edge_colors,pos=node_centroids,node_size=2, width=list(edge_weights),node_color="blue")
plt.title("New community areas graph")
plt.show()
plt.clf()

degrees = sorted(get_degree(G))
G = encoding_to_graph(best_solution)
plt.plot([i for i in range(len(block_groups))],degrees)
plt.xticks([])
plt.xlabel("Block Groups")
plt.ylabel("Degree")
plt.title("New community areas degree distribution\n"+degree_distribution_statistics(degrees))
plt.show()
plt.clf()

#display results of simulated annealing 

new_community_areas = list(nx.connected_components(new_graph))

print("Simulated Annealing search completed.")
print("Search time (minutes): "+str(round(search_minutes,2)))
print()

print("Number of new community areas: "+str(len(new_community_areas)))
print("New Chicago average ReADI:")
print(round(evaluate(best_solution,average_size,0),4))
print()

#plot simulated annealing temperature as a function of iterations

plt.plot(iterations,temperatures)
plt.xlabel("Iteration")
plt.ylabel("Temperature")
plt.title("Temperature as a function of iterations\n(with "+str(reheats)+" reheats)")
plt.show()
plt.clf()

#plot simulated annealing objective function as a function of iterations
#objective function scores account for size penalty

plt.plot(iterations,scores)
plt.xlabel("Iteration")
plt.ylabel("Objective function")
plt.title("Objective function value\nover iterations")
plt.show()
plt.clf()

#compute average readi for each community area

minimization_scores,minimization_areas = compute_average_readi(best_solution)


sorted_louvains = [[louvains_scores[i],louvains_areas[i]] for i in range(len(louvains_scores))]
sorted_louvains = sorted(sorted_louvains,reverse=True)
louvains_scores = [sorted_louvains[i][0] for i in range(len(louvains_scores))]
louvains_areas = [sorted_louvains[i][1] for i in range(len(louvains_scores))]

sorted_minimization = [[minimization_scores[i],minimization_areas[i]] for i in range(len(minimization_scores))]
sorted_minimization = sorted(sorted_minimization,reverse=True)
minimization_scores = [sorted_minimization[i][0] for i in range(len(minimization_scores))]
minimization_areas = [sorted_minimization[i][1] for i in range(len(minimization_scores))]


#uncomment the following to write data
'''
path = "community_areas\\minimization\\"

c = 0
for new_community in minimization_areas:
    new_community_area = list(new_community)

    with open(path+"new_ca"+str(c+1)+".txt", 'w') as file:
        for item in new_community_area:
            file.write(f"{item}\n") 
    c+=1

path = "community_areas\\average_readi\\minimization.txt"

with open(path, "w") as f:
    for item in minimization_scores:
        f.write(f"{item}\n")

path = "community_areas\\louvains\\"

c = 0
for new_community in louvains_areas:
    new_community_area = list(new_community)

    with open(path+"new_ca"+str(c+1)+".txt", 'w') as file:
        for item in new_community_area:
            file.write(f"{item}\n") 
    c+=1
    
path = "community_areas\\average_readi\\louvains.txt"

with open(path, "w") as f:
    for item in louvains_scores:
        f.write(f"{item}\n")
'''