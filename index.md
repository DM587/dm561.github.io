---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
---


## General information

- [Official course description](http://natfak.sdu.dk/laeseplan/kursusbeskrivelse.php?kursuskode=DM865&lang=en)

- [BlackBoard](https://e-learn.sdu.dk/webapps/blackboard/execute/courseMain?course_id=_386519_1)

- Teachers: [Lene Monrad Favrholdt](http://www.imada.sdu.dk/~lenem/) and [Marco Chiarandini](http://www.imada.sdu.dk/~marco)


## Schedule

<a href="https://mitsdu.sdu.dk/skema/activity/15020201/f18">MitSDU</a>

<button onclick="myFunction('Demo1')" class="w3-btn w3-cell w3-left-align">Show alternative view <i class="fa fa-caret-down"></i></button>
<div id="Demo1" class="w3-container w3-hide">

<div class="w3-responsive">
<div w3-include-html="./assets/timetable.html"></div>
<script>
w3.includeHTML();
</script>
</div>

</div>



## Contents 

The overview will be continousuly updated during the course.

| Date         | Lectures  	                                                                                                                                      | Suggested reading                                                                                                  |   |   |
|--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+---+---|
| <!--L--> 1/2 | Introduction to the course <br> Introduction to approximation algorithms<br> Set Cover: IP formulation and LP relaxation<br> Set Cover: LP-rounding | [Pizza meeting slides][1]; [More details][2]<br> 1.1 [WS]<br> 1.2 [WS]<br> 1.3-1.4 [WS]; [Lecture notes][3]        |   |   |
| <!--L--> 2/2 | Exercises <br> Set Cover: Primal-Dual                                                                                                               | [Exercise sheet 1]({% post_url 2018-01-23-exercises %})<br> 1.4-1.5 [WS]; [Lecture notes][4]                       |   |   |
|--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+---+---|
| <!--L--> 5/2 | Exercises  <br> Set Cover: Greedy                                                                                                                   | [Exercise sheet 2]({% post_url 2018-01-23-exercises %}#sheet2) <br> 1.6 [WS]; [Lecture notes][5]                   |   |   |
| <!--L--> 6/2 | Exercises <br> Set Cover: Randomized LP-rounding                                                                                                    | [Exercise sheet 3]({% post_url 2018-01-23-exercises %}#sheet3) <br> 1.7 [WS]; [Lecture notes][6]                   |   |   |
| <!--L--> 9/2 | *This lecture will start at 8:45* <br> TSP: Insertion and Christofide's algorithm                                                                   | <br> 2.4 [WS]; [Lecture notes][7]                                                                                  |   |   |
|--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+---+---|
| 12/2         | Exercises                                                                                                                                           | [Exercise sheet 4]({% post_url 2018-01-23-exercises %}#sheet4); [Lecture notes][10]                                |   |   |
| 13/2         | TSP: Heuristics                                                                                                                                     | [No]; 1-4 [Be]; [Slides][8]                                                                                        |   |   |
| 16/2         | TSP: Heuristics                                                                                                                                     | [No]; 1-4 [Be] <br> [Exercise sheet 5]({% post_url 2018-01-23-exercises %}#sheet5)                                 |   |   |
|--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+---+---|
| 19/2         | TSP: More on construction heuristics. Local search                                                                                                  | 1-3 [Be]                                                                                                           |   |   |
| 20/2         | TSP: Local search                                                                                                                                   | [Exercise sheet 6]({% post_url 2018-01-23-exercises%}#sheet6) <br>4 [Be], ch 1, sc 2.1, 4.1 [MAK] <br> [Slides][9] |   |   |
| 23/2         | TSP: Efficiency issues in local search + Code review                                                                                                | [Exercise sheet 7]({% post_url 2018-01-23-exercises%}#sheet7)                                                      |   |   |
|--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+---+---|
| 27/2         | Local search theory                                                                                                                                 | ch 1, sc 2.1, 4.1 [MAK]; [Slides][11]                                                                              |   |   |
| 2/3          | Exercises on local search design                                                                                                                    | [Slides][12] <br> [Project 1st part][13]                                                                           |   |   |
|--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+---+---|
| 6/3          | Knapsack: Approximation algorithms <br> Introduction to Bin Packing                                                                                 | 3.1 [WS] <br> 3.3 [WS]; [Lecture notes][14]                                                                        |   |   |
| 9/3          | Exercises <br> Bin Packing: Approximation algorithms                                                                                                | [Exercise sheet 8]({% post_url 2018-01-23-exercises%}#sheet8) <br>  3.3 [WS]; [Lecture notes][15]                  |   |   |
|--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+---+---|
| 12/3         | Bin Packing: Dyn. prg. and running time for the APTAS <br> Working Environment                                                                      | 3.3 [WS]; [Lecture notes][18]  <br> [Slides][16]                                                                   |   |   |
| 13/3         | Experimental Analysis of Heuristics for Optimization                                                                                                | [Slides][17]                                                                                                       |   |   |
|--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+---+---|
| 19/3         | Experimental Analysis of Heuristics for Optimization: Visualization                                                                                 |                                                                                                                    |   |   |
| 20/3         | Experimental Analysis of Heuristics for Optimization: Testing <br> Midway course evaluation                                                         | [Slides][19]                                                                                                       |   |   |
|--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+---+---|
| 3/4          | Cancelled                                                                                                                                           |                                                                                                                    |   |   |
| 6/4          | SAT: Local Search                                                                                                                                   | [Slides][20]; [Exercise sheet 9]({% post_url 2018-01-23-exercises%}#sheet9)                                        |   |   |
|--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+---+---|
| 10/4         | Stochastic Local Search & Metaheuristics (local search based)                                                                                       | ch 7 [MAK]; [Slides][21]                                                                                           |   |   |
| 13/4         | Metaheuristics (construction heuristic based)                                                                                                       | [Slides][22]; [Project 2nd part][23]                                                                               |   |   |
|--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+---+---|
| 16/4         | Ant Colony Optimization                                                                                                                             | [Slides][24]                                                                                                       |   |   |
| 17/4         | Evolutionary Algorithms                                                                                                                             | [Slides][25]; [Slides][26]                                                                                         |   |   |
| 19/4         | Scheduling: Approximation algorithms                                                                                                                | 2.3 [WS]; [Lecture notes][27]                                                                                      |   |   |
|--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+---+---|
| 23/4         | Exercises<br>Scheduling: PTAS                                                                                                                       | [Exercise sheet 10]({% post_url 2018-01-23-exercises%}#sheet10) <br> 3.2 [WS]; [Lecture notes][28]                 |   |   |
| 24/4         | Scheduling: Classification                                                                                                                          | [Slides][29]; ch 1 [BK]; [Exercise sheet 11]({% post_url 2018-01-23-exercises%}#sheet11)                           |   |   |
|--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+---+---|
| 30/4         | Scheduling: Complexity, Single Machine Problems                                                                                                     | [Slides][30] [BK ch 1] [P chp 2,3]                                                                                 |   |   |
| 1/5          | Scheduling: Shop Problems                                                                                                                           | [Slides][31]                                                                                             |   |   |
|--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+---+---|
| 7/5          | Scheduling: Flow Shop                                                                                                                               | [Slides][32] [P sec 6.1]                                                                                         |   |   |
| 8/5          | Scheduling: Job Shop                                                                                                                                | [Slides][33] [P sec 7.1-7.3] [MAK sec 3.3]                                                                                                      |   |   |
| 9/5          | Scheduling: Resource Constrained Project Scheduling                                                                                                 |              [BK chp 3]                                                                                                      |   |   |
|--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+---+---|
| 14/5         | MAX SAT: Randomized algorithms and derandomization                                                                                                  | 5.1-5.3 [WS]                                                                                                       |   |   |
| 15/5         | MAX SAT: LP rounding                                                                                                                                |                                                                                                                    |   |   |
| 18/5         |                                                                                                                                                     |                                                                                                                    |   |   |
|--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+---+---|
| 22/5         |                                                                                                                                                     |                                                                                                                    |   |   |
|--------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+---+---|


## References 

- [WS] David P. Williamson and David
  B. Shmoys. [Design of Approximation Algorithms](http://www.designofapproxalgs.com/). Cambridge
  University Press. 2010.

- [MAK] W. Michiels, E. Aarts and J. Korst. [Theoretical Aspects of Local Search](http://dx.doi.org/10.1007/978-3-540-35854-1). Springer Berlin Heidelberg, 2007

- [Be]
  J.J. Bentley. [Fast Algorithms for Geometric Traveling Salesman Problems](http://dx.doi.org/10.1287/ijoc.4.4.387). ORSA
  Journal on Computing, 1992, vol. 4, issue 4, pp. 387-411 (Available in
  BlackBoard Course Materials)

- [No] Peter Norvig [The Traveling Salesperson Problem: Python notebook](http://nbviewer.jupyter.org/url/norvig.com/ipython/TSP.ipynb).

- [BK] P. Brucker, S. Knust. [Complex
  Scheduling](https://doi.org/10.1007/978-3-642-23929-8). Springer, 2012.

- [P] M. L. Pinedo. [Scheduling Theory, Algorithms, and Systems](https://doi.org/10.1007/978-3-319-26580-3). Springer 2016.  



[1]: {{ "/assets/dm865-presentation-handout.pdf" | absolute_url }}
[2]: {{ "/assets/dm865-organization-handout.pdf" | absolute_url }}
[3]: {{ "/assets/dm865-lec180201.pdf" | absolute_url }}
[4]: {{ "/assets/dm865-lec180202.pdf" | absolute_url }}
[5]: {{ "/assets/dm865-lec180205.pdf" | absolute_url }}
[6]: {{ "/assets/dm865-lec180206.pdf" | absolute_url }}
[7]: {{ "/assets/dm865-lec180209.pdf" | absolute_url }}
[8]: {{ "/assets/dm865-tsp-ch-handout.pdf" | absolute_url }}
[9]: {{ "/assets/dm865-tsp-ls-handout.pdf" | absolute_url }}
[10]: {{ "/assets/dm865-lec180212.pdf" | absolute_url }}
[11]: {{ "/assets/dm865-local_search-handout.pdf" | absolute_url }}
[12]: {{ "/assets/dm865-exercises-handout.pdf" | absolute_url }}
[13]: {{ "/assets/dm865-assignment-ls.pdf" | absolute_url }}
[14]: {{ "/assets/dm865-lec180306.pdf" | absolute_url }}
[15]: {{ "/assets/dm865-lec180309.pdf" | absolute_url }}
[16]: {{ "/assets/dm865-working-handout.pdf" | absolute_url }}
[17]: {{ "/assets/dm865-experimental-1-handout.pdf" | absolute_url }}
[18]: {{ "/assets/dm865-lec180312.pdf" | absolute_url }}
[19]: {{ "/assets/dm865-experimental-2-handout.pdf" | absolute_url }}
[20]: {{ "/assets/dm865-sat-handout.pdf" | absolute_url }}
[21]: {{ "/assets/dm865-metaheuristics-handout.pdf" | absolute_url }}
[22]: {{ "/assets/dm865-constr-meta-handout.pdf" | absolute_url }}
[23]: {{ "/assets/dm865-assignment-meta.pdf" | absolute_url }}
[24]: {{ "/assets/dm865-aco-handout.pdf" | absolute_url }}
[25]: {{ "/assets/dm865-evolutionary-handout.pdf" | absolute_url }}
[26]: {{ "/assets/dm865-vrp-handout.pdf" | absolute_url }}
[27]: {{ "/assets/dm865-lec180419.pdf" | absolute_url }}
[28]: {{ "/assets/dm865-lec180423.pdf" | absolute_url }}
[29]: {{ "/assets/dm865-scheduling-class-handout.pdf" | absolute_url }}
[30]: {{ "/assets/dm865-scheduling-complex-handout.pdf" | absolute_url }}
[31]: {{ "/assets/dm865-scheduling-single-handout.pdf" | absolute_url }}
[32]: {{ "/assets/dm865-scheduling-flow-handout.pdf" | absolute_url }}
[33]: {{ "/assets/dm865-scheduling-job-handout.pdf" | absolute_url }}

## Assessment and Grading

- Oral exam based on the theoretical part and the practical project
  assignment. Ordinary session: June 5th. Reexams: August 28th.


## Course Evaluation

- [Mid term evaluation]({% post_url 2018-03-20-midterm_eval %})
