---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
mathjax: true
---



## General information

- [Official course description](https://odinlister.sdu.dk/fagbesk/internkode/DM561/)

- [ItsLearning](https://sdu.itslearning.com/main.aspx?CourseID=13197)

- Teachers:
  [David Kyed](https://imada.sdu.dk/~dkyed),
  [Daniel Merkle](https://imada.sdu.dk/~daniel) and [Marco Chiarandini](https://imada.sdu.dk/~marco)

- Teacher assistants: 
H1: [Anders Sund-Jensen](mailto:ansun20@student.sdu.dk) (H1); [Casper Asbjørn Eriksen](mailto:casbjorn@imada.sdu.dk) (H2)


## Schedule

- <a href="https://mitsdu.sdu.dk/skema/activity/N330024101/e22">MitSDU</a>

- <a href="https://vis.aida.imada.sdu.dk/public/e22udgave3/DM561">Alternative view</a>

- Semester overview: <button onclick="myFunction('h1')" class="w3-btn w3-cell
w3-left-align"> section H1 <i class="fa fa-caret-down"></i></button>
<button onclick="myFunction('h2')" class="w3-btn w3-cell
w3-left-align"> section H2 <i class="fa fa-caret-down"></i></button>

<div id="h1" class="w3-container w3-hide">
<div class="w3-responsive">
<div w3-include-html="./assets/dm561_h1.html"></div>
<script>
w3.includeHTML();
</script>
</div>
</div>

<div id="h2" class="w3-container w3-hide">
<div class="w3-responsive">
<div w3-include-html="./assets/dm561_h2.html"></div>
<script>
w3.includeHTML();
</script>
</div>
</div>





## Contents

### Introductory Classes

<table>
<thead>
<tr>
<th width="5%">Week</th>
<th width="7%">Date</th>
<th width="7%">Teacher</th>
<th width="36%">Topics and Slides</th>
<th width="55%">Suggested reading</th>
</tr>
</thead>
{% for lecture in site.data.lectures %}
{% assign date_format = site.minima.date_format | default: "%b %-d" %}
<tbody>
<tr>
<td>{{ lecture.week }}</td>
<td>{{ lecture.date | date: date_format }}</td>
<td>
{{ lecture.teacher }}
</td>
<td>
{% if lecture.turl %}
<a class="post-link" href="{{ lecture.turl | absolute_url }}">{{ lecture.topics | escape }}</a>
{% else %}
{{ lecture.topics | escape }}
{% endif %}
</td>
<td>{{ lecture.sug_reading }}</td>
</tr>
</tbody>
{% endfor %}
</table>



### Exercises and Assignments



| Week | Sheet                      | Topic  	           | Solutions     | Assignments        |
|------+----------------------------+---------------------------+---------------+--------------------|
|   43 | [colab1][40]; [sheet1][31] | Python, Part 1            | [sheet1][83]  | [asg0][50]         |
|------+----------------------------+---------------------------+---------------+--------------------|
|   44 | [sheet2][32]               | Python, Part 2            |               | [asg1][51]         |
|      | [sheet3][33]               | Python, Part 3 - plotting | [sheet3][833] |                    |
|------+----------------------------+---------------------------+---------------+--------------------|
|   45 | [sheet4][34]               | Least Squares             | [sheet4][84]  | [asg2][52]         |
|------+----------------------------+---------------------------+---------------+--------------------|
|   46 |             | Page Rank                 |               |                    |
|      |                            |                           |               | [asg_pagerank][55] |
|------+----------------------------+---------------------------+---------------+--------------------|
|   47 |                            |                           |               |                    |
|      |                            |                           |               |                    |
|------+----------------------------+---------------------------+---------------+--------------------|
|   48 |                            |                           |               |                    |
|      |                            |                           |               |                    |
|------+----------------------------+---------------------------+---------------+--------------------|
|   49 |                            |                           |               |                    |
|      |                            |                           |               |                    |
|------+----------------------------+---------------------------+---------------+--------------------|
|   50 |                            |                           |               |                    |
|------+----------------------------+---------------------------+---------------+--------------------|


<!--
|------+----------------------------+--------------------------------+---------------+-------------|
|   43 | [colab1][40]; [sheet1][31] | Python, Part 1                 | [sheet1][83]  | [asg0][50]  |
|------+----------------------------+--------------------------------+---------------+-------------|
|   44 | [sheet2][32]               | Python, Part 2                 |               | [asg1][51]  |
|      | [sheet3][33]               | Python, Part 3 - plotting      | [sheet3][833] |             |
|------+----------------------------+--------------------------------+---------------+-------------|
|   45 | [sheet4][34]               | Least Squares                  | [sheet4][84]  | [asg2][52]  |
|------+----------------------------+--------------------------------+---------------+-------------|
|   46 | [sheet5][35]               | Graph Theory                   | [sheet5][85]  |             |
|      |                            |                                |               | [asg3][53]  |
|------+----------------------------+--------------------------------+---------------+-------------|
|   47 | [sheet6][36]               | From Random Polygon to Ellipse | [sheet6][86]  |             |
|      |                            |                                |               | [asg4][54]  |
|------+----------------------------+--------------------------------+---------------+-------------|
|   48 | [sheet7][37]               | Page Rank                      | [sheet7][87]  |             |
|      |                            |                                |               | [asg5][55]  |
|------+----------------------------+--------------------------------+---------------+-------------|
|   49 | [sheet8][38]               | Eigenfaces / PCA               |               |             |
|      |                            |                                |               | [asg6][56]  |
|------+----------------------------+--------------------------------+---------------+-------------|
|   50 | [sheet9][39]               | Linear Programming               |               |             |
|------+----------------------------+--------------------------------+---------------+-------------|

-->


<!--

| Week | Sheet                      | Topic  	                | Solutions     | Assignments |
|------+----------------------------+--------------------------------+---------------+-------------|
|   44 | [colab1][40]; [sheet1][31] | Python, Part 1                 | [sheet1][83]  | [asg0][50]  |
|------+----------------------------+--------------------------------+---------------+-------------|
|   45 | [sheet2][32]               | Python, Part 2                 |               | [asg1][51]  |
|------+----------------------------+--------------------------------+---------------+-------------|
|   46 | [sheet3][33]               | Python, Part 3 - plotting      | [sheet3][833]  |             |
|      | [sheet4][34]               | Least Squares                  | [sheet4][84]  | [asg2][52]  |
|------+----------------------------+--------------------------------+---------------+-------------|
|   47 | [sheet5][35]               | Graph Theory                   | [sheet5][85]  |             |
|      |                            |                                |               | [asg3][53]  |
|------+----------------------------+--------------------------------+---------------+-------------|
|   48 | [sheet6][36]               | From Random Polygon to Ellipse | [sheet6][86]  |             |
|      |                            |                                |               | [asg4][54]  |
|------+----------------------------+--------------------------------+---------------+-------------|
|   49 | [sheet7][37]               | Page Rank                      | [sheet7][87]  | [asg5][55]  |
|      |                            |                                |               |             |
|------+----------------------------+--------------------------------+---------------+-------------|
|   50 | [sheet8][38]               | Eigenfaces / PCA               |  [sheet8][88]       |             |
|      |                            |                                |               | [asg6][56]  |
|------+----------------------------+--------------------------------+---------------+-------------|

-->


<!--


| Week | Type | Sheet        | Topic  	                | Solutions     | Assignments |
|------+------+--------------+--------------------------------+---------------+-------------|
|   44 | L    | [colab1][40] [sheet1][31] | Python                         |               | [asg0][50]  |
|------+------+--------------+--------------------------------+---------------+-------------|
|   45 | L    |              |                                |               |  |
|------+------+--------------+--------------------------------+---------------+-------------|
|   46 | L    | [sheet2][32] | Python                         |               |             |
|      | L    | [sheet3][33] | Python - plotting              |               | [asg2][52]  |
|------+------+--------------+--------------------------------+---------------+-------------|
|   47 | L    | 
|      | L    |              |                                |               | [asg3][53]  |
|------+------+--------------+--------------------------------+---------------+-------------|
|   48 | L    | [sheet5][35] | Graph Theory                   |               |             |
|      | L    |              |                                |               | [asg4][54]  |
|------+------+--------------+--------------------------------+---------------+-------------|
|   49 | L    | [sheet6][36] | From Random Polygon to Ellipse |               |             |
|      | L    |              |                                |               |
|------+------+--------------+--------------------------------+---------------+-------------|
|   50 | L    |
|      | L    |              |                                |               | [asg6][56]        |
|------+------+--------------+--------------------------------+---------------+-------------|
|   51 | L    | [sheet8][38] | Eigenfaces                     |               |             |
|------+------+--------------+--------------------------------+---------------+-------------|


-->









## References

#### Recommended book:

- [HJ1] [Python Essentials][1]. Jeffrey Humpherys and Tyler J. Jarvis,
  managing editors

- [HJ2]
  [Data Science Essentials](https://github.com/Foundations-of-Applied-Mathematics/Labs/raw/master/docs/DataScienceEssentials.pdf). Jeffrey
  Humpherys and Tyler J. Jarvis, managing editors

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
  T. Akenine-Möller. 2017. for $x$ in $(-1, 1)$


- [MC] [Lecture Notes on Linear Regression][13] by Marco Chiarandini.


- [NS]
  [`numpy` API reference](https://docs.scipy.org/doc/numpy/reference/) and
  its submodule
  [linalg](https://docs.scipy.org/doc/numpy/reference/routines.linalg.html);
  and [`scipy` API reference](https://docs.scipy.org/doc/scipy/reference/)
  and its submodule
  [linalg](https://docs.scipy.org/doc/scipy/reference/linalg.html).
  (`scipy` is a superset of `numpy`.)

- [Wi] Introduction to Graph Theory, Robin J. Wilson, 5th edition, 2010.

- [BP] Brin, Sergey; Page, Lawrence. [The anatomy of a large-scale
  hypertextual Web search
  engine](https://doi.org/10.1016/S0169-7552(98)00110-X). Computer
  Networks and ISDN Systems. Volume 30, Issues 1–7, April 1998, Pages
  107-117

- [PBMW] Page, Lawrence; Brin, Sergey; Motwani, Rajeev and Winograd,
  Terry, [The PageRank citation ranking: Bringing order to the
  Web](http://dbpubs.stanford.edu:8090/pub/showDoc.Fulltext?lang=en&doc=1999-66&format=pdf). 1999

- [LM] Amy N. Langville; Carl D. Meyer. [A Survey of Eigenvector Methods
  for Web Information
  Retrieval](https://epubs.siam.org/doi/pdf/10.1137/S0036144503424786). SIAM
  REVIEW, Society for Industrial and Applied Mathematics, Vol. 47,
  No. 1, pp. 135–161







[1]: {{ "/assets/PythonEssentials.pdf" | absolute_url }}

[10]: {{ "https://www.cs.cornell.edu/cv/ResearchPDF/EllipsePoly.pdf" |absolute_url }}
[11]: {{"https://www.pathlms.com/siam/courses/8265/sections/12047" |absolute_url}}
[12]: {{ "assets/ullmann.pdf" | absolute_url }}
[13]: {{ "assets/linreg-notes.pdf" | absolute_url }}
[14]: {{ "/assets/dm561-lec3.pdf" | absolute_url }}
[15]: {{ "/assets/dm561-linreg.pdf" | absolute_url }}
[18]: {{ "/assets/sheet5.html" | absolute_url }}
[19]: {{ "/assets/sheet6.html" | absolute_url }}
[21]: {{ "https://arxiv.org/abs/1404.1100" | absolute_url}}
[22]: {{ "https://github.com/Foundations-of-Applied-Mathematics/Labs/raw/master/docs/Volume1.pdf" | absolute_url }}
[23]: {{ "http://setosa.io/ev/principal-component-analysis/" | absolute_url }}
[24]: {{ "https://sebastianraschka.com/Articles/2015_pca_in_3_steps.html" | absolute_url }}
[25]: {{ "https://www.learnopencv.com/eigenface-using-opencv-c-python/" | absolute_url }}
[26]: {{ "https://github.com/Foundations-of-Applied-Mathematics/Labs/raw/master/docs/Volume1.pdf" | absolute_url }}


<!-- External solutions -->

[83]: {{ "/solutions/sheet1_sols.html" | absolute_url }}
[833]: {{ "/solutions/sheet3_sols.html" | absolute_url }}
[85]: {{ "https://roras18.github.io/dm561-TA-2020/sheet5_sol.pdf" }}
[86]: {{ "https://roras18.github.io/dm561-TA-2020/sheet6_sol.pdf" }}
[88]: {{ "https://roras18.github.io/dm561-TA-2020/sheet8_sol.pdf" }}

<!-- Internal solutions --> 

[84]: {{ "/solutions/sheet_4.html" | absolute_url }}
[87]: {{ "/solutions/pagerank.html" | absolute_url }}


<!-- Sheets -->

{% capture page_link %}{% post_url 2020-10-28-sheet1 %}{% endcapture %}
[31]: {{ page_link | absolute_url }}
[31]: {{ "exercises/sheet1.html" | absolut_url }}

[32]: {{ site.baseurl }}{% post_url 2020-11-05-sheet2 %}
[32]: {{ "exercises/sheet2.html" | absolut_url }}

[33]: {{ site.baseurl }}{% post_url 2021-11-03-sheet3 %}
[33]: {{ "exercises/sheet3.html" | absolut_url }}

[34]: {{ site.baseurl }}{% post_url 2021-11-10-sheet4 %}
[34]: {{ "exercises/sheet4.html" | absolut_url }}


[35]: {{ "/assets/ex-week46-2021.pdf" | absolute_url }}
[36]: {{ "/assets/ex-week47-2021.pdf" | absolute_url }}
{% capture page_link %}{% post_url 2022-11-15-sheet5 %}{% endcapture %}
[37]: {{ page_link | absolute_url }}
[34]: {{ "exercises/sheet5.html" | absolute_url }}

[38]: {{ "/assets/ex-week49-2021.pdf" | absolute_url }}
[39]: {{ site.baseurl }}{% post_url 2021-12-14-sheet9 %}

[40]: {{ "https://colab.research.google.com/github/DM561/dm561.github.io/blob/master/assets/Python_in_a_Nutshell.ipynb" | absolute_url }}


<!-- Assignments -->

[50]: {{ "/assignments/asg0.html" | absolute_url }}
[51]: {{ "/assignments/asg1.html" | absolute_url }}
[52]: {{ "/assets/asg_linreg.pdf" | absolute_url }}
[53]: {{ "/assignments/asg3.html" | absolute_url }}
[54]: {{ "/assignments/asg4.html" | absolute_url }}
[55]: {{ "/assignments/asg_pagerank.html" | absolute_url }}
[56]: {{ "/assignments/asg6.html" | absolute_url }}
