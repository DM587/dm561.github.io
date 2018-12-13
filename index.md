---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
---



## General information

- Official course description:
  [DM561](https://odinlister.sdu.dk/fagbesk/internkode/DM561/), [DM562](https://odinlister.sdu.dk/fagbesk/internkode/DM562/)

- BlackBoard: [DM561](https://e-learn.sdu.dk/webapps/blackboard/execute/courseMain?course_id=_390707_1), [DM562](https://e-learn.sdu.dk/webapps/blackboard/execute/courseMain?course_id=_390712_1)


- Teachers: [Christian Kudahl](https://imada.sdu.dk/~kudahl/), [Daniel Merkle](https://imada.sdu.dk/~daniel) and [Marco Chiarandini](https://imada.sdu.dk/~marco)


- Teachers: [Jonas Herskind Sejr](http://findresearcher.sdu.dk:8080/portal/en/person/sejr), Hans Kristian Anders Møller

<!-- hmoel15@student.sdu.dk -->

## Schedule

<a href="https://mitsdu.sdu.dk/skema/activity/N330024101/e18">MitSDU</a>


<button onclick="myFunction('h1')" class="w3-btn w3-cell
w3-left-align">Schedule for DM561, section H1 <i class="fa fa-caret-down"></i></button>
<div id="h1" class="w3-container w3-hide">

<div class="w3-responsive">

<!--
<iframe src="https://calendar.google.com/calendar/embed?showTitle=0&amp;showPrint=0&amp;showCalendars=0&amp;showTz=0&amp;height=600&amp;wkst=1&amp;bgcolor=%23FFFFFF&amp;src=egkljh81e5gn1qa11drhvli5g1quqn6e%40import.calendar.google.com&amp;color=%23853104&amp;src=i1sgtn4cueuhfc0o5u0aao73ikbrkuol%40import.calendar.google.com&amp;color=%23853104&amp;src=e_2_en%23weeknum%40group.v.calendar.google.com&amp;color=%23B1365F&amp;ctz=Europe%2FCopenhagen" style="border-width:0" width="960" height="600" frameborder="0" scrolling="no"></iframe>
-->

<div w3-include-html="./assets/dm561_h1.html"></div> 
<script>
w3.includeHTML();
</script>
</div>
</div>



<button onclick="myFunction('h2')" class="w3-btn w3-cell
w3-left-align">Schedule for DM561, section H2 <i class="fa fa-caret-down"></i></button>
<div id="h2" class="w3-container w3-hide">

<div class="w3-responsive">

<div w3-include-html="./assets/dm561_h2.html"></div> 
<script>
w3.includeHTML();
</script>
</div>
</div>





<button onclick="myFunction('dm562h2')" class="w3-btn w3-cell
w3-left-align">Schedule for DM562, section H1 <i class="fa fa-caret-down"></i></button>
<div id="dm562h2" class="w3-container w3-hide">

<div class="w3-responsive">

<div w3-include-html="./assets/dm562_h1.html"></div> 
<script>
w3.includeHTML();
</script>
</div>
</div>





## Contents

### Introductory Classes


| Week |  Date | Teacher        | Topics and Slides  	                                      | Suggested reading                                                             |
|------+-------+----------------+------------------------------------------------------------------+-------------------------------------------------------------------------------|
|   45 | 05.11 | Marco & Daniel | [Intro to Python - Part 1][2]                                    | App A, B and ch 1-3 of [HJ1]; [DB]                                            |
|      | 07.11 | Marco & Daniel | [Intro to Python - Part 2][4];                                   | ch 4-6 of [HJ1]                                                               |
|------+-------+----------------+------------------------------------------------------------------+-------------------------------------------------------------------------------|
|   46 | 14.11 | Daniel         | [Graph Isomorphism and Molecules][5], [script][6]                | [Additional slides on Ullmann algorithm][12]                                  |
|------+-------+----------------+------------------------------------------------------------------+-------------------------------------------------------------------------------|
|   47 | 21.11 | Daniel         | [From Random Polygon to Ellipse][9]                              | [Article (pp 1-5,17)][10]; [Video (optional)][11]                             |
|------+-------+----------------+------------------------------------------------------------------+-------------------------------------------------------------------------------|
|   48 | 28.11 | Marco          | [Intro to Python - Part 3][14]; [Least Squares Data Fitting][15] | Sc. 6.3-6.5 of [AR]; [Lecture Notes][13]                                      |
|------+-------+----------------+------------------------------------------------------------------+-------------------------------------------------------------------------------|
|   49 | 05.12 | Marco          | [Page Rank][16]                                                  | Sc. 4.12, 9.2-9.3, 10.5 of [AR]; [Article](https://doi.org/10.1016/S0169-7552(98)00110-X) |
|------+-------+----------------+------------------------------------------------------------------+-------------------------------------------------------------------------------|
|   50 | 12.12 | Daniel         | [Eigenfaces][20]                                                       | [Article][21]; [Chapter 7 (Facial Recognition)][26]; [Visual Intro][23]; [PCA Tutorial][24]; [Eigenfaces (OpenCV based)][25]                                                                              |
|------+-------+----------------+------------------------------------------------------------------+-------------------------------------------------------------------------------|



### Exercises and Assignments

|                       Week | Type | Exercises  	                             | Solutions    | Assignment                                                      |
|----------------------------+------+---------------------------------------------+--------------+-----------------------------------------------------------------|
|                         45 | L    | [sheet1]( {% post_url 2018-11-04-sheet1 %}) |              | [asg0]({% post_url 2018-11-01-asg0 %}); [FAQ][3]                |
|----------------------------+------+---------------------------------------------+--------------+-----------------------------------------------------------------|
|                         46 | L    | [sheet2][7]                                 |              | [asg1]({% post_url 2018-11-11-asg1 %})                          |
|----------------------------+------+---------------------------------------------+--------------+-----------------------------------------------------------------|
| 47: H1: 22, H2: 20, H1: 21 | E    | [sheet3]( {% post_url 2018-11-16-sheet3 %}) |              |                                                                 |
| 47: H1: 23, H2: 27, H1: 22 | L    | [sheet4][8]                                 |              | [asg2]({% post_url 2018-11-21-asg2 %})                          |
|----------------------------+------+---------------------------------------------+--------------+-----------------------------------------------------------------|
|                         48 | L    | [sheet5]( {% post_url 2018-11-26-sheet5 %}) | [sheet5][18] | [asg3]({% post_url 2018-11-28-asg3 %})                          |
|----------------------------+------+---------------------------------------------+--------------+-----------------------------------------------------------------|
|                         49 | E    | sheet5                                      |              |                                                                 |
|                            | L    | [sheet6]( {% post_url 2018-12-04-sheet6 %}) |  [sheet6][19]             | [asg4][17] (Reload the page! Last update: Saturday 8 at 14:05.) |
|----------------------------+------+---------------------------------------------+--------------+-----------------------------------------------------------------|
|                         50 | L    |                                             |              |                                                                 |
|----------------------------+------+---------------------------------------------+--------------+-----------------------------------------------------------------|
|                         51 | L    |                                             |              |                                                                 |
|----------------------------+------+---------------------------------------------+--------------+-----------------------------------------------------------------|



## References 

#### Recommended book:

- [HJ1] [Python Essentials][1]. Jeffrey Humpherys and Tyler J. Jarvis, managing editors

<!--
- [HJ2] [Labs for Foundations of Applied Mathematics. Volume 1. Mathematical Analysis](2)
  Jeffrey Humpherys and Tyler J. Jarvis, managing editors
-->

  
#### Other References:

- [DB] David Beazley. [Python Tutorial Video](https://www.youtube.com/watch?v=lyDLAutA88s)

- [HJ] Jeffrey Humpherys and Tyler
  J. Jarvis. [Foundations of Applied Mathematics. Volume 1. Mathematical Analysis](http://bookstore.siam.org/ot152/). 2017. Society
  for Industrial and Applied Mathematics.

- [AR] Howard Anton and Chris Rorres. [Elementary Linear Algebra With
  Supplemental Applications](http://eu.wiley.com/WileyCDA/WileyTitle/productCd-1118677455.html). Edition
  International Student Version. 11th Edition. 2014. Wiley


- [PK] Philip N. Klein. [Coding the Matrix: Linear Algebra through
  Applications to Computer
  Science](https://www.amazon.com/dp/0615880991/). 1st Edition.
  Newtonian Press; 1 edition, September 3, 2013

 

- [AH] Martin Anthony and Michele Harvey, [Linear Algebra, Concepts and Methods](http://www.cambridge.org/us/academic/subjects/mathematics/algebra/linear-algebra-concepts-and-methods). 2012. Cambridge


- [Le] Steven J. Leon, [Linear Algebra with
  Applications](http://wps.aw.com/leon_linearalg_9/), Prentice Hall
  (2010).


- [FSV] [Computing with Python: An introduction to Python for science and engineering](http://www.pearson.ch/1471/9780273786436/Computing-with-Python-An-introduction-to.aspx)
  Claus Führer, Jan Erik Solem, Olivier Verdier



- [SAA] [Immersive linear algebra](http://immersivemath.com/ila/index.html) by J. Ström, K. Åström, and
  T. Akenine-Möller. 2017.




[1]: {{ "/assets/PythonEssentials.pdf" | absolute_url }}
[2]: {{ "/assets/dm561-lec1.pdf" | absolute_url }}
[4]: {{ "/assets/dm561-lec2.pdf" | absolute_url }}
[3]: {{ "/assets/faq.txt" | absolute_url }}
[5]: {{ "/assets/DM561-DM562-Graphs-small.pdf" | absolute_url }}
[6]: {{ "/assets/graph-permutation.py" | absolute_url }}
[7]: {{ "assets/ex-week46.pdf" | absolute_url }}
[8]: {{ "assets/ex-week47.pdf" | absolute_url }}
[9]: {{ "/assets/DM561-DM562-RandomPolygon.pdf" | absolute_url }}
[10]: {{ "https://www.cs.cornell.edu/cv/ResearchPDF/EllipsePoly.pdf" |absolute_url }}
[11]: {{"https://www.pathlms.com/siam/courses/8265/sections/12047" |absolute_url}}
[12]: {{ "assets/ullmann.pdf" | absolute_url }}
[13]: {{ "assets/linreg-notes.pdf" | absolute_url }}
[14]: {{ "/assets/dm561-lec3.pdf" | absolute_url }}
[15]: {{ "/assets/dm561-linreg.pdf" | absolute_url }}
[16]: {{ "/assets/dm561-pagerank.pdf" | absolute_url }}
[17]: {{ "/assets/asg4.pdf" | absolute_url }}
[18]: {{ "/assets/sheet5.html" | absolute_url }}
[19]: {{ "/assets/sheet6.html" | absolute_url }}
[20]: {{ "/assets/DM561-DM562-PCA-Eigenfaces.pdf" | absolute_url }}
[21]: {{ "https://arxiv.org/abs/1404.1100" | absolute_url}}
[22]: {{ "https://github.com/Foundations-of-Applied-Mathematics/Labs/raw/master/docs/Volume1.pdf" | absolute_url }}
[23]: {{ "http://setosa.io/ev/principal-component-analysis/" | absolute_url }}
[24]: {{ "https://sebastianraschka.com/Articles/2015_pca_in_3_steps.html" | absolute_url }}
[25]: {{ "https://www.learnopencv.com/eigenface-using-opencv-c-python/" | absolute_url }}
[26]: {{ "https://github.com/Foundations-of-Applied-Mathematics/Labs/raw/master/docs/Volume1.pdf" | absolute_url }}