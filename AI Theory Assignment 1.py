#!/usr/bin/env python
# coding: utf-8

# # 22k-4005 Mujtaba Saqib, 22k-4115 Hilal Aziz

# # Q1

# Q1: Read Turing's original paper on AI (Turing, 1950). In the paper, he discusses several potential objections
# to his proposed enterprise and his test for intelligence. Which objections still carry some weight? Are his
# refutations valid? Can you think of new objections arising from developments since he wrote the paper? In
# the paper, he predicts that by the year 2000, a computer will have a 30% chance of passing a five-minute
# Turing Test with an unskilled interrogator. Do you think this is reasonable?

# Objections Which Carry Weight:
# •	Mathematical Objection
# •	Argument From Consciousness
# •	Arguments from various disabilities
# •	Lady Lovelace’s
# 
# Valid Refutations:
# •	Religious Objections: 
#                         Turing ignores this objection by saying that his approach focuses on thinking perspective rather than thinking on meta physical one. His refutation is valid because AI focuses on observable behavior rather than people religious beliefs.
# 
# •	Heads in Sand objections:
#                              Turing said our vision is to construct AI in such a way that we consider the consequences and designing AI in such a way that it is fruitful for us rather than destructive thing. This refutation is valid because now a days AI development emphasis on responsible and ethical considerations. 
# 
# •	Mathematical Objection: 
#                           Turing accepted these objections, but these limitations does not prevent computer from being intelligent. This refutation is valid because AI is not designed to solve all possible problems.                                  
# 
# •	Lady Lovelace’s objection: 
#                              Turing suggests that computer might not learn like humans but they may suggest unexpected solutions to a problem. This refutation is valid as now a days many machine learning tools give such outcomes which are unexpected. 
# 
# New Objections:
# •	Security/Privacy:  issues like privacy automatic weaponary, impact of AI on labour force or on working class.
# •	Black Box Problems: AI machine learning models sometime generates outcomes which are difficult to understand through which origin they came from.
# 
# by the year 2000, a computer will have a 30% chance of passing a five-minute Turing Test with an unskilled interrogator?
# 
# •	Through the passage of time AI has made enormous progress in terms of intelligence, but if we see intelligence as how human think or behave and if we see the turing test where a machine has to behave like a human and give wrong outcomes like human and sometimes correct outcomes so we think that the AI computer doesn’t had 30% chance of passing turing Test in early 2000’s.
# 

# # Q2

# Q2: Examine the AI literature to discover whether or not the following tasks can currently be solved by
# computers. (Any five)
# 1. Playing a decent game of table tennis (ping-pong).
# 2. Driving in the centre of Karachi.
# 3. Playing a decent game of bridge at a competitive level.
# 4. Discovering and proving new mathematical theorems.
# 5. Writing an intentionally funny story.
# 6. Giving competent legal advice in a specialized area of law.
# 7. Translating spoken English into spoken Urdu in real time.

# 2) No, The inability to enforce traffic laws, the erratic conduct of Karachi residents, congested traffic, and unforeseen circumstances will make driving a car in Karachi challenging.
# 
# 4) No, since deciphering a mathematical theorem and solving it calls for in-depth knowledge, originality, and sound mathematical reasoning.
# 
# 
# 5) Yes, AI is capable of producing humorous stories to a certain degree, but whether or not a person thinks anything funny relies on their sense of humor.
# 
# 6) No, since in order for a machine to provide effective advice, it needs to fully comprehend the context, which includes difficult-to-understand ethical considerations. AI can assist in this regard, but it is not capable of providing flawless legal advice. 
# 
# 7) Yes, It can translate commonly or widely used words, but it may not be as accurate when translating words from different cultures, such as Punjabi or Sindhi. While it may eventually translate these words, the accuracy might be lower.

# # Q3

# Q3: Choose a domain that you are familiar with, and write a PAGE description of an agent for the environment.
# Characterize the environment as being accessible, deterministic, episodic, static, and continuous or not. What
# agent architecture is best for this domain?

# 1.Functionalities: Vital Signs Monitoring, Activity Tracking, Sleep Analysis, EKG and Arrhythmia Detection, Medication Reminders
#     Health Data Analysis and Advice, Emergency Alert, Integration with Healthcare Systems
#     
# 2) Environment Characterization
# 
# •Accessible: The environment is partially accessible. The smart watch has access to a range of physiological and activity data from the user but lacks full access to the user's environmental context and internal health state without additional medical tests.
# 
# •Deterministic: The environment is not deterministic. While the smart watch can predict certain outcomes based on data trends, individual health responses and external factors introduce unpredictability.
# 
# •Episodic: The environment is not episodic; it is continuous. Health monitoring and advice provision are ongoing processes without distinct episodes.
# 
# •Static: The environment is dynamic, not static, as the user's health status and environmental conditions can change frequently.
# 
# •Continuous: The environment is continuous. Health monitoring and lifestyle advice need to be provided in real-time or near-real-time, without clear breaks.
# 
# 
# Recommended Agent Architecture
# given the complexity and dynamic nature of the healthcare and wellness domain, a Hybrid Agent Architecture combining both reactive and deliberative components would be most suitable. This architecture allows the smart watch to respond in real-time to critical health alerts while also supporting longer-term planning and decision-making based on accumulated health data

# # Q4

# Q4: For each of the following activities, give a PEAS description of the task environment. (Any five)
# - Playing soccer.
# - Exploring the subsurface of Arabian Sea.
# - Shopping for used AI books on the Internet.
# - Playing a tennis match.
# - Practicing tennis against a wall.
# - Performing a high jump.
# - Knitting a sweater.
# - Bidding on an item at an auction.
Playing soccer

Environment Type: Partially observable, stochastic, sequential, dynamic, continuous, multiagent
Performance Measure: Scoring goals, defending, winning, injuries and teamwork
Environment: Soccer playground, Players, ball, goals, referees
Actuators: Player's legs, head and hands
Sensors: Camera, orientation sensor, players locatorExploring the subsurface of Arabian Sea.

Environment Type: Partially observable, stochastic, sequential, dynamic, continuous, multiagent
Performance Measure: Images quality, video quality, safety
Environment: Ocean, water, organisms
Actuators: Mobile diver, steering, brake, accelerator
Sensors: Depth sensor, GPS, CameraShopping for used AI books on the Internet

Environment Type: Partially observable, deterministic, sequential, static, discrete, single agent
Performance Measure: Price, authors, book review, interested books, cost minimization
Environment: Websites, vendors, shippers
Actuators: Keyboard, mouse (hands)
Sensors: Camera, price monitorPerforming a high jump

Environment Type: Fully observable, stochastic, sequential, static, continuous, single agent
Performance Measure: Height range, safety landing
Environment: Wall
Actuators: Jumping apparatus (e.g., legs)
Sensors: Camera, height sensorBidding on an item at an auction

Environment Type: Fully observable, stochastic, sequential, static, discrete, multiagent
Performance Measure: Cost, value, quality, winning
Environment: Items, bidders
Actuators: Speaker
Sensors: Camera, price monitor
# # Q5

# Q5: For each of the following assertions, say whether it is true or false and support your answer with
# examples or counter examples where appropriate. (Any five)
# 1. An agent thatsenses only partial information about the state cannot be perfectly rational.
# 2. There exist task environments in which no pure reflex agent can behave rationally.
# 3. There exists a task environment in which every agent isrational.
# 4. The input to an agent program is the same as the input to the agent function.
# 5. Every agent function isimplementable by some program/machine combination.
# 6. Suppose an agentselects its action uniformly at random from the set of possible actions. There exists a
# deterministic task environment in which this agent is rational.
# 7. It is possible for a given agent to be perfectly rational in two distinct task environments.

# 1) False. The ability to make wise decisions based on the sensor data obtained is referred to as reason.As an agent can only act on what it observes, it is operating as rationally as it can while having some factors unaccounted for via no fault of its own, hence it would be foolish to blame it for not responding rationally for having just incomplete information.
# 
# 2) True. In a partially visible environment, a pure reflex agent cannot obtain an optimal state estimate since it disregards prior perceptions. However, because of its extensive multitasking, there's a chance that the agent will behave rationally in the right situation. 
# 
# 3) True, It is true that there are countless task settings that might be made, and that there is probably at least one out there where each agent is rational in its action.
# 
# 4) True, because the inputs are the percepts which remain same for the agent functions and program
# 
# 5) False,  because some agents need infinite resources or solving problems which seems impossible.
# 

# 

# # Q6

# Q6: You are clear about uninformed and informed strategies now. The example discussed in the class
# regarding Romania map has to get implemented in this assignment.
# 
# The map is directly taken up from your book together with the heuristics table. The task is to reach
# from a particular source to destination using different strategies. This means that user will be
# facilitated with the option of choosing any random source and destination point at run time.
# Following are the strategies to be implemented.
# a) Breadth first search
# b) Uniform cost search
# c) Greedy best firstsearch
# d) Iterative deepening depth first search
# A comparison of these four needs to be done. Complete list of pathway and path cost of each
# algorithm has to be calculated so that it shows clearly that which algorithm is best out of all in
# ascending order.

# a) Breadth first search
# b) Uniform cost search

# In[3]:


import heapq

#representation of the romania map as a graph
romania_map = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Oradea': 151, 'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

#heuristics straight-line distance to Bucharest table for the informed strategies
heuristics = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
    'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
    'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193,
    'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
}

#breadth-first search algorithm
def bfs(graph, start, goal):
    visited = set()  # set to keep track of visited nodes.
    queue = []  # initialize a queue
    queue.append((start, [start]))  #enqueue the start node and the path to it

    while queue:
        (vertex, path) = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            if vertex == goal:
                return path  #return the path if goal is reached
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor])) #enqueue the node and path to it
    return None

#uniform cost search algorithm
def ucs(graph, start, goal):
    visited = set()
    queue = []
    heapq.heappush(queue, (0, start, [start]))  #priority queue

    while queue:
        (cost, vertex, path) = heapq.heappop(queue)
        if vertex not in visited:
            visited.add(vertex)
            if vertex == goal:
                return (cost, path)  #return the cost and path if goal is reached
            for neighbor, weight in graph[vertex].items():
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))
    return None

#test bfs
start_city = 'Arad'
goal_city = 'Bucharest'
bfs_path = bfs(romania_map, start_city, goal_city)
print(f"BFS path from {start_city} to {goal_city}: {bfs_path}")

# Test UCS
ucs_cost, ucs_path = ucs(romania_map, start_city, goal_city)
print(f"UCS path from {start_city} to {goal_city} with total cost {ucs_cost}: {ucs_path}")


# c) Greedy best firstsearch
# d) Iterative deepening depth first search

# In[5]:


romania_map = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Oradea': 151, 'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

#heuristics straight-line distance to bucharest table for the informed strategies
heuristics = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
    'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
    'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193,
    'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
}

#implementing greedy best first search for the romanian map
def greedy_best_first_search(graph, heuristics, start, goal):
    visited = set()  # set to keep track of visited nodes.
    queue = []  # initialize a priority queue
    heapq.heappush(queue, (heuristics[start], start, [start]))

    while queue:
        #pop the vertex with the lowest heuristic value
        _, current, path = heapq.heappop(queue)
        if current == goal:
            return path  # return the path if goal is reached

        visited.add(current)

        #go through all the neighbors of the current node
        for neighbor in graph[current]:
            if neighbor not in visited:
                # calculate heuristic for the neighbor
                priority = heuristics[neighbor]
                # add the neighbor to the queue with its heuristic value
                heapq.heappush(queue, (priority, neighbor, path + [neighbor]))
    return None

#implementing iterative deepening depth first search for the romanian map
def iddfs(graph, start, goal, max_depth):
    #recursive depth limited search
    def dls(current, goal, depth):
        if depth == 0:
            return None if current != goal else [current]
        if current == goal:
            return [current]
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                path = dls(neighbor, goal, depth - 1)
                if path is not None:
                    return [current] + path
        return None
    
    for depth in range(max_depth):
        visited = set([start])
        path = dls(start, goal, depth)
        if path is not None:
            return path
    return None

#example usage of greedy best first search
start_city = 'Arad'
goal_city = 'Bucharest'
gbfs_path = greedy_best_first_search(romania_map, heuristics, start_city, goal_city)
print(f"Greedy Best-First Search path from {start_city} to {goal_city}: {gbfs_path}")

#example usage of iterative deepening depth first search
max_depth = 20  # Example depth limit
iddfs_path = iddfs(romania_map, start_city, goal_city, max_depth)
print(f"Iterative Deepening Depth-First Search path from {start_city} to {goal_city}: {iddfs_path}")


# # Q7

# Q7: N-Queens problem: There is an n x n grid where the value of n is 4≤n≤8 (user shall be asked at run time
# for the value of n he wants to keep). Your task is to place n queens on this board. As per the rules of chess, a
# queen should have no other queen in its respective column, neither should it have any other queen in its row
# nor should it have any within its diagonal cells. You can consider this case as placing each queen individually
# per column such that it does not violate any of the constraints mentioned. It’s quite easy to find solution
# manually but your task is now to code it and find the correct positions for the queens.
# 
# This problem has to be solved through the concept of backtracking. So initially you will place the first
# queen randomly at any location within column 1. With respect to its location, now next n-1 queens’
# domain i.e. the places where they can be placed might shrink up.
# E.g. in this case 4 queens have to placed and Q1 is placed on (0,0) so x positions represent the illegal
# places now where other queens cannot be placed due to Q1 placement. This means for rest of the
# queens some positions have been considered as illegal.
# Further up, when we will move forward, there might be a point where domain gets empty for any
# particular queen, at that instance apply backtrack concept, which means that location of previous
# queen will have to get changed.
# Advise: Start building up your logic first on 4 queen problem so that you may exactly understand the
# flow then go for making a generalized code version of n queens’ placement.

# In[11]:


import random

def calculate_attacks(queens):
    attacks = 0
    for i in range(len(queens)):
        for j in range(i+1,len(queens)):
            #checks for same row or diagonal attacks
            if queens[i]==queens[j] or abs(queens[i]-queens[j])==j-i:
                attacks+=1
    return attacks

def generate_neighbors(state):
    neighbors = []
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i] != j:
                #move the queen to the new row in the same column
                neighbor = state.copy()
                neighbor[i] = j
                neighbors.append(neighbor)
    return neighbors

def hill_climbing(n):
    #initialize a random starting state
    current = list(range(n))
    random.shuffle(current)
    
    while True:
        neighbors = generate_neighbors(current)
        #select the neighbor with the least number of attacks
        next_state = min(neighbors, key=calculate_attacks)
        
        #if no neighbor has fewer attacks, we've reached a local maximum
        if calculate_attacks(next_state) >= calculate_attacks(current):
            break
        current = next_state
    
    return current

#ask the user for the size of the board
n = int(input("enter the value of n (4≤n≤8) "))
sol = hill_climbing(n)
print("one of the solution ")
print(sol)


# In[ ]:




