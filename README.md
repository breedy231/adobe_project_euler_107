# Brendan Reed - Project Euler Problem #107

## Process Description

To go about solving this problem, I first identified that I was looking at a problem that would require a minimum spanning tree. I then went back to when I first learned about them in my Algorithms class at Northeastern University and referenced my class notes on this topic. From there I went onto the Python homepage to see if there was an established pattern for representing a network graph and used that pattern to inform my main data structure. Combining these two pieces and a bit of coffee, I went about writing up my program to handle 4 tasks in its execution:

    * Reading from the provided network.txt file and creating a 2D matrix
    * Calculating the total weight of the network before applying Prim's algorithm
    * Creating a network graph from the 2D matrix to be used in creating the Minimum Spanning Tree
    * Applying Prim's Algorithm to the graph to create a Minimum Spanning Tree

In the process of debugging I used print statements to ensure my matrix & graph were being constructed correctly, along with the Python docs to ensure I was using built-ins correctly.

## Sample Run

As the project spec requested the use of Docker, ensure it's installed prior to running the code block on the command line

To setup the Docker container, run the following command:

```shell
docker build -t project_euler_107 .
```

Sample output of the run:

```shell
docker run project_euler_107
Old network weight: 261832
New network weight: 259679
Execution time: 0.003490017999865813 seconds
```

## Refrences

* Class notes from my previous Algorithms class, found on my professor's [course website](https://shelat.ccis.neu.edu/16f-4800/). Specifically notes on Prim's Algorithm and Minimum Spanning Trees
* [Python 3.6 Documentation](https://docs.python.org/3.6/index.html)
* [Python Patterns - Implementing Graphs](https://www.python.org/doc/essays/graphs/)
* [Docker Documentation](https://docs.docker.com/)

## Time Spent

Around 3-4 hours (between taking the Christmas decorations down)
