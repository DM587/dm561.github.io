---
layout: default
mathjax: true
title:  asg1
date:   2018-11-11 09:33:19 +0100
categories: assignments
---

### Assignment 1: Vector and Matrix 

**Submission Deadline: Monday, November 16 2020, at noon**


In this assignment you are asked to implement your own Vector and Matrix
types in Python and to compare them with Numpy array type implementations.


In your git repository you will find the following spec files that you
will need to edit `vec.py` and `mat.py`. In addition, you will find the
file `banchmark.py` that will use your implementations to carry out the
comparison with NumPy.

The files `vec-sparse.py` and `mat-sparse.py` are for an optional part
of the assignment. For implementing the methods in these files you
will get help by the instructors in the first exercise class of week
46.

Your job is to implement the appropriate methods for the classes `Vec`
and `Mat` such that the functions in the doctest examples and those in
`benchmark.py`, that use the operators with objects from the `Vec` and
`Mat` classes, work correctly.  To facilitate your task the procedures
that you have to finish implementing have been moved out of the class
where they are called. Hence you should make no changes to the class
definition.  Your code for a procedure can include calls to other
procedures that you have implemented.

The table below resumes the functions that are used for the different operators:

| operation                       |syntax	|function|
|----------|:-------------:|------:|
|vector addition				 |u+v		|`__add__`
|vector negation				 |	 -v		|`__neg__`
|vector subtraction				 |u-v		|
|scalar-vector multiplication	 |alpha*v	|`__rmult__`
|division of a vector by a scalar| v/alpha	|`__truediv__`
|dot-product					 |	 u*v	|`__mult__`	
|getting value of an entry		 |v[d]		|`__getitem__`
|setting value of an entry		 |v[d] = .	|`__setitem__`
|testing vector equality		 |	 u == v	|`__eq__`
|pretty-printing a vector		 |print(v)	|`__str__`
|copying a vector                | v.copy() |`copy`






You can test if your modules pass all their `doctests` from a console,
by typing
```bash
python3 -m doctest vec.py
```
or
```bash
python3 vec.py
```
To benchmark your implementations against those from Numpy you can call:
```bash
python3 benchmark.py
```
You can vary the size of the matrices to observe the growing rate of
computation time but you should otherwise not edit file `benchmark.py`. 

Your code will be tested and graded on a different test set than the one
in the docstring of the files provided.


*Assertions*: For most of the procedures to be written, the first
statement after the docstring is an assertion. Executing an assertion
verifies that the condition is true, and raises an error if not. The
assertions are there to detect errors in the use of the procedures. Take
a look at the assertions to make sure you understand them. You can take
them out, but you do so at your own risk.





#### Sparse Vectors and Matrices (Optional)

This part will be discussed in class probably in the second exercise
session of week 46. It is associated with the files `vec_sparse.py`
and `mat_sparse.py`.

A vector (matrix) most of whose values are zeros is called a *sparse
vector (matrix)*.

*Sparse representation*:
To represent sparse vectors and matrices in Euclidean spaces, it might be useful to regard
them as functions from a domain $D$ to a co-domain $\mathbb{R}$. For
example the vector
$
[3.14159, 2.718281828, −1.0, 2.0]
$
can be represented as the function:

$$
\begin{array}{lcl}
0 &\mapsto & 3.14159\\
1 &\mapsto & 2.718281828\\
2 &\mapsto & -1.0\\
3 &\mapsto & 2.0
\end{array}
$$

For a matrix the domain $D$ is made by the product of a domain $R$ for
the rows and a domain $C$ for the columns. For example, the identity
matrix of size $3\times 3$ can be seen as the function that maps the
pairs $(r,c)\in R\times C$ where $R=C=\\{1,2,3\\}$.

$$
\begin{array}{lcl}
(0,0) &\mapsto & 1\\
(1,1) &\mapsto & 1\\
(2,2) &\mapsto & 1
\end{array}
$$

All other elements of the domain $R\times C$ are mapped to zero and do
not need to be explicitly stated.

Functions like these can be represented in Python by dictionaries, where
the keys are elements from the set $D$ or tuples from the set $R\times
C$ and values are the corresponding values from $\mathbb{R}$.

Sparse vectors and matrices are implemented in Python in the module
`scipy`, which contains the [numerical code for operations on
arrays](https://www.scipy.org/scipylib/faq.html#what-is-the-difference-between-numpy-and-scipy). Here
you find a [short introduction to sparse matrices in
`scipy`](https://imada.sdu.dk/~marco/DM559/Resources/Ipython/Sparse.html).

Your task is to implement in `vec_sparse.py` and `mat_sparse.py` methods
that can cope with sparse representations, For example, `getitem(v, k)`
should return a value for every domain element even if `k` is not a key
of `v.f`.

However, your methods do not need to make any effort to retain sparsity
when adding two vectors. That is, for two instances `u` and `v` of
`Vec`, it is okay if every element of `u.D` is represented explicitly in
the dictionary of the instance `u+v`.  Several other procedures need to
be written with the sparsity convention in mind. For example, two
vectors can be equal even if their `.f` fields are not equal: one vector’s
`.f` field can contain a key-value pair in which the value is zero, and
the other vector’s `.f` field can omit this particular key. For this
reason, the `equal(u, v)` procedure needs to be written with care.











