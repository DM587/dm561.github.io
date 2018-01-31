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

2.  Assume that you have an algorithm for finding a minimum
    cardinality vertex cover in a graph. 
    
    a) Explain how you can use the algorithm for finding a
       maximum cardinality independent set.

    b) Does this mean that you can use an approximation algorithm for
       unweighted Set Cover, like the ones in Sections 1.3 and 1.4,
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