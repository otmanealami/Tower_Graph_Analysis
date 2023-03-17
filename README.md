# Context
City dwellers usually move in the city according to predictable patterns, within well defined areas and using quite repetitive routes (everyday home to work travels, for instance). 
This brings the question of what gives a city its unity if people are moving only within small fragmented parts of it. In particular, can we unveil the existence of sub-cities that concentrate movements within their boundaries?
<br>
In this project, we are particularly interested in exploring how movement patterns within the city fragments a city into “bubbles” or communities. We will use a dataset that contains 346,638 data points representing the approximate locations of the home and work places for specific anonymised dwellers from the city of Santiago de Chile.
<br>
Through the building of a network and subsequent analyses, the aim is to describe the community structure that underlies movement patterns in the city.



## Dataset:
 The data was obtained from anonymised mobile phone connections to the closest mobile phone towers

1. The authors processed this data to create two main files:
1. Home_Work.csv: Each row contains both home and work locations of a particular person. Home and work locations are just approximate, as they correspond to the location of the closest cell phone tower to which the person connects.
2. Communities.csv: The authors of [1] created a network from the Home_Work.csv dataset and then applied community detection algorithms and discovered that the network can be divided into six different communities or sub-networks. This file contains the communities, where each cell phone tower contains a label of the community it belongs to.

## Overview 

## Task 1 :

Starting from Home_Work.csv, We built a network where nodes are mobile phone towers, and they are connected through people moving between them.We Constructed  the following networks:\
a) Undirected and unweighted network\
b) Directed and unweighted network\
c) Undirected weighted network\
d) Directed and weighted network

We then discussed the differences between each of the above networks and the advantages or flaws of each network if we want to assess the spreading of a disease through these networks.


## Task 2:
For a network chosen from the Task1 we :\
a) Computed the community detection algorithm  to obtain communities from the network for  5 different “Resolution” values and we showed how each value is influencing the resulting community structure (number of communities, average and standard deviation on the size of communities,
among others).\
b) Compared the communities we have found with the ones available in Communities.csv. We then Discussed any influence that can be attributed to the particular parameter value or the network used (directed/undirected weighted/unweighted).\
c) Built a map that displays each node (the towers) at their corresponding geographical location, and in which each community is denoted by a different colour.


## Task 3:
For this part we used two different centrality measures to explore how important each node (tower) is within the city. We put our findings  in Contrast with the communities found in Task 2 and  Compared the distribution of centrality to the geographical location of the nodes.
