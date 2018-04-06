---
layout: default
mathjax: true
title:  "Sheet 1"
date:   2018-01-10 09:33:19 +0100
categories: exercises sheet1
---

#### Sheet 1: Exercises for Friday, February 2


1. a) Write down an LP-formulation of the unweighted Vertex Cover problem.

   b) Write down the dual of the LP from a).

   c) Which combinatorial problem does the dual correspond to?


#### Sheet 2: <a name="sheet2"></a> Exercises for Monday, February 5

1.  Although the unweighted Vertex Cover problem is NP-hard for general graphs,
    there are graph classes that allow for efficient algorithms.  
    Design an algorithm that finds a minimum cardinality vertex cover
    of a tree in linear time.

2.  a) Assume that you have an algorithm for finding a minimum
       cardinality vertex cover in a graph.   
       Explain how you can use the algorithm for finding a
       maximum cardinality independent set.

    b) Does this mean that you can use an approximation algorithm for
       unweighted Vertex Cover, like the ones in Sections 1.3 and 1.4,
       for approximating a maximum cardinality independent set? 
       <br>
      (Hint: What approximation factor could you obtain?)


#### Sheet 3: <a name="sheet3"></a> Exercises for Tuesday, February 6

1.  Consider the primal-dual algorithm for the unweighted Vertex Cover
    problem.
    
    a) What does the algorithm do?

    b) Write down the same algorithm without explicitly using the
       LP-formulation of the problem.
    
    c) Give an example showing that the algorithm has an approximation
       factor of at least 2.

2. Recall that, for Vertex Cover, the algorithms of Sections 1.3 and
   1.4 are 2-approximation algorithms.
   <br>
   Give an example showing that the greedy algorithm of Section 1.6 is
   not a 2-approximation algorithm, even for unweighted Vertex Cover.

3. Give an instance of the Set Cover problem proving that the
   approximation ratio of the greedy algorithm is at least $H_n$
   (i.e., the lower bound of $H_n$ is tight).  
   Hint: What does the upper bound of $H_g$ tell us about such an
   example?
   (Recall that $g$ is the size of the largest set in the instance.)


#### Sheet 4: <a name="sheet4"></a> Exercises for Monday, February 12

1.  Let $G$ be a complete undirected graph with non-negative edge
    weights.

    a) Let $W$ denote the maximum weight of any edge in $G$.  
       For each edge $e$, add $W$ to the weight of $e$.  
       Let $G'$ denote the resulting weighted graph.

       Prove that the weights of $G'$ are metric, i.e., prove that
       they satisfy the triangle inequality.

    b) Argue that a TSP tour in $G$ is optimal, if and only if the
       corresponding tour in $G'$ is optimal.

    c) Why doesn't this contradict Theorem 2.9?

2. Describe an algorithm for finding an Euler tour in a graph where
   all vertices have even degree.
   
   
   
#### Sheet 5: <a name="sheet5"></a> Exercises for Friday, February 16
   
   
Read the Python tutorial [No]. You find some starting code from that
page [here](https://github.com/DM865/TSP).

Following the procedure for Benchmarking described there implement and
compare as many TSP heuristics as you can. You find a list below, in
bold the heuristics implemented in [No]. For a description of these
heuristics see [Be].

- Heuristics that Grow Fragments
	+ **Nearest neighborhood heuristic**
	+ Double-Ended Nearest Neighbor heuristic
	+ **Multiple Fragment heuristic (aka, greedy heuristic)**
- Heuristics that Grow Tours
	+ Nearest Addition
	+ Farthest Addition
	+ Random Addition
	+ Clarke-Wright savings heuristic
	+ Nearest Insertion
	+ Farthest Insertion
	+ Random Insertion
- Heuristics based on Trees
	+ **Minimum spanning tree heuristic**
	+ Christofides' heuristics
	+ Fast recursive partitioning heuristic



#### Sheet 6: <a name="sheet6"></a> Exercises for Tuesday, February 20.


1. In a 3-opt local search algorithm for the TSP how many possible ways
   are there to add three new edges once three edges have been removed
   in order to re-obtain an Hamiltonian tour? Justify your answer.

2. Consider the traveling salesmane define on an incomplete graph. How
   could we encode the problem such that we can approach it with the
   construction heuristics and local search algorithms implemented for
   the complete version of the problem? 

2. Consider the asymmetric TSP. How can we encode this problem into a
   symmetric TSP, such that we can approach it with the construction
   heuristics and local search algorithms implemented for the symmetric
   version of the problem?



#### Sheet 7: <a name="sheet7"></a> Exercises for Friday, February 23.


Design a 3 exchange iterative improvement procedure for the TSP.  The
procedure must return a local optimum in the 3 exchange neighborhood.
Implement the procedure in the framework made
[available in git](https://github.com/DM865/TSP).

A template to be completed is available in the file `three_opt.py`. You must
only edit this file, you are not allowed to change the other files.
When executed, your program will read the instance USA, construct a
canonical tour and call your iterative improvement procedure. The
benchmarking called from the main file will take care of assessing the
quality of your solution.

Describe your algorithm in pseudocode in a one-page document edited with
Latex. Use the Latex package
[algorithm2e](https://ctan.org/pkg/algorithm2e?lang=en).

Submit only the file `three_opt.py` and the PDF result of your Latex
pseudocode at this [portal](http://valkyrien.imada.sdu.dk/DOApp/). Keep your
files anonymous! (The portal is likely to become available only during
the night before Friday. Hence, you might have to submit during the
class of Friday.)

You are encouraged to work in pairs at this assignment, in which case it is
enough that only one submits.

Remember: start out with simple and even inefficient code without
optimizing for efficiency. Only later, when your initial implementation
is working and doing what you expect, start looking at efficiency
improvements of your code (and consider the quality of the solutions as
well).



#### Sheet 8: <a name="sheet8"></a> Exercises for Friday, March 9.

2. Algorithm 3.1 is similar to the dynamic programming algorithm
   described in class, but may be more time and space efficient.  
   Explain Algorithm 3.1.  

1. Solve Exercise 3.1.  
   Hint: For proving the appoximation ratio it may be helpful to first
   consider the algorithm that chooses between the sets {$1,2,\ldots,k$} and
   {$k+1$}.

2. Solve Exercise 3.6


#### Sheet 9: <a name="sheet9"></a> Exercises for Tuesday, April 9.

Encode the $k$-coloring problem as a SAT problem.
