---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
---



## General information

- Official course description:
  [DM561](https://odinlister.sdu.dk/fagbesk/internkode/DM561/), [DM562](https://odinlister.sdu.dk/fagbesk/internkode/DM562/)

- BlackBoard: [DM561](https://e-learn.sdu.dk/webapps/blackboard/execute/courseMain?course_id=_410238_1), [DM562](https://e-learn.sdu.dk/webapps/blackboard/execute/courseMain?course_id=_410243_1)

- Teachers:
  [Wojciech Szymanski](https://portal.findresearcher.sdu.dk/da/persons/szymanski)
  (DM561),
  [Luís Cruz-Filipe](https://portal.findresearcher.sdu.dk/da/persons/lcf)
  (DM562), 
  [Daniel Merkle](https://imada.sdu.dk/~daniel) and [Marco Chiarandini](https://imada.sdu.dk/~marco)


- Teachers: Rasmus Bo Adeltoft (DM561), Johannes Lauritsen (DM561),
  [Nicklas Sindlev Andersen](https://imada.sdu.dk/~sindlev/)

<!-- hmoel15@student.sdu.dk -->

## Schedule

MitSDU: <a
href="https://mitsdu.sdu.dk/skema/activity/N330024101/e19">DM561</a>, <a href="https://mitsdu.sdu.dk/skema/activity/N330025101/e19">DM562</a>


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


<table>
<thead>
<tr>
<th width="5%">Week</th>
<th width="7%">Type</th>
<th width="20%">Sheet</th>
<th width="20%">Solutions</th>
<th width="30%">Assignments</th>
</tr>
</thead>
{% assign origin = '2019-10-01' | date: "%s" %}
{% assign end = '2019-12-01' | date: "%s" %}
{% for post in site.posts reversed %}
  {% capture date %}{{post.date | date: "%s" }}{% endcapture %}
  {% if date > origin and date < end %}
<tbody>
<tr>
{% assign date_format = site.minima.date_format | default: "%b %-d" %}
<td>{{ post.week }}</td>
<td>{{ post.type }}</td>
<td><a class="post-link" href="{{ post.url | absolute_url }}">{{ post.title | escape }}</a></td>
<td>
{% if post.sol_url %} 
<a class="post-link" href="{{ post.sol_url | absolute_url }}">solutions</a>
{% endif %}
</td>
</tr>
</tbody>
{% endif %}
{% endfor %}
</table>







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

[3]: {{ "/assets/faq.txt" | absolute_url }}


[7]: {{ "assets/ex-week46.pdf" | absolute_url }}
[8]: {{ "assets/ex-week47.pdf" | absolute_url }}
[10]: {{ "https://www.cs.cornell.edu/cv/ResearchPDF/EllipsePoly.pdf" |absolute_url }}
[11]: {{"https://www.pathlms.com/siam/courses/8265/sections/12047" |absolute_url}}
[12]: {{ "assets/ullmann.pdf" | absolute_url }}
[13]: {{ "assets/linreg-notes.pdf" | absolute_url }}
[14]: {{ "/assets/dm561-lec3.pdf" | absolute_url }}
[15]: {{ "/assets/dm561-linreg.pdf" | absolute_url }}

[17]: {{ "/assets/asg4.pdf" | absolute_url }}
[18]: {{ "/assets/sheet5.html" | absolute_url }}
[19]: {{ "/assets/sheet6.html" | absolute_url }}

[21]: {{ "https://arxiv.org/abs/1404.1100" | absolute_url}}
[22]: {{ "https://github.com/Foundations-of-Applied-Mathematics/Labs/raw/master/docs/Volume1.pdf" | absolute_url }}
[23]: {{ "http://setosa.io/ev/principal-component-analysis/" | absolute_url }}
[24]: {{ "https://sebastianraschka.com/Articles/2015_pca_in_3_steps.html" | absolute_url }}
[25]: {{ "https://www.learnopencv.com/eigenface-using-opencv-c-python/" | absolute_url }}
[26]: {{ "https://github.com/Foundations-of-Applied-Mathematics/Labs/raw/master/docs/Volume1.pdf" | absolute_url }}
[27]: {{ "/assets/asg5.pdf" | absolute_url }}
[28]: {{ "/assets/ex-week51.pdf" | absolute_url }}
[29]: {{ "/assets/reexam.pdf" | absolute_url }}
