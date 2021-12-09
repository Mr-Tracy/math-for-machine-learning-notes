# Matrices as objects that map one vector on to another (week 4)

Einstein summation convention
for square matrix multiplication
$ \bm{A}\bm{B} = \bm{C} $

$$
A =
\begin{bmatrix}
a_{11} & \ a_{12}  & . & . & \ a_{1,n}\\
a_{21} & \ a_{22}  & . & . & \ a_{2,n}\\
. & .  & . & . & \ .\\
a_{n1} & \ a_{n2}  & . & . & \ a_{n,n}\\
\end{bmatrix}
$$

$$
C_{rc} = \sum_{j} \bm{a_{rj}} \  \bm{b_{jc}}
$$

It's clear that the number of A rows should match B columns for non-square matrices.

### Einstein summation convention

A notation convention, you can drop the summation. Here are the rules:

1. Omit summation signs
2. If a suffix appears only once, it can take any value
3. A suffix cannot appear more than twice

# Matrix transforms from one basis to another

Consider two sets of 2d basis vectors. The first being the natural basis that we are familiar with call this n. The other basis being e.

$$
\bm{n_x} =
\begin{bmatrix}
1 \\
0
\end{bmatrix}
\bm{n_y} =
\begin{bmatrix}
0 \\
1
\end{bmatrix}
$$

Now the e basis vectors written according to n's frame:

$$
\bm{e_{xn}} =
\begin{bmatrix}
3 \\
1
\end{bmatrix}
\bm{e_{yn}} =
\begin{bmatrix}
1 \\
1
\end{bmatrix}
$$

According to e's frame they are just:

$$
\bm{e_{x}} =
\begin{bmatrix}
1 \\
0
\end{bmatrix}
\bm{e_{y}} =
\begin{bmatrix}
0 \\
1
\end{bmatrix}
$$

To convert a vector in E's frame to one n's frame use a matrix multiplication of the E basis vectors written in terms of n.

$$
\begin{equation*}
\begin{bmatrix}
3 & 1\\
1 & 1\\
\end{bmatrix}
\begin{bmatrix}
x_e \\
y_e
\end{bmatrix}
=
\begin{bmatrix}
x_n \\
y_n
\end{bmatrix}
\end{equation*}
$$

A concrete example is:

$$
\begin{equation*}
\begin{bmatrix}
3 & 1\\
1 & 1\\
\end{bmatrix}_n
\begin{bmatrix}
3/2 \\
1/2
\end{bmatrix}_e
=
\begin{bmatrix}
5 \\
2
\end{bmatrix}_n
\end{equation*}
$$

To change a vector from n to E. Use a matrix of n's basis vectors according to E's frame. The transfer matrix is the inverse of E->N matrix.

$$
\begin{equation*}
\begin{bmatrix}
\ 1/2 & -1/2\\
-1/2  & \  3/2\\
\end{bmatrix}_{e}
\begin{bmatrix}
5 \\
2
\end{bmatrix}_n
=
\begin{bmatrix}
3/2 \\
1/2
\end{bmatrix}_e
\end{equation*}
$$

# Orthogonal Matrices

## Matrix Transpose

The transpose $ \vec{A}^T$ is described as:

$$
    a^T_{ij} = a{ji}
$$

Here's a concrete example:

$$
\begin{align*}
\vec{A} =
\begin{bmatrix}
4 &1 \\
0 & 9
\end{bmatrix}
\\
\vec{A^T} =
\begin{bmatrix}
4 &0 \\
1 & 9
\end{bmatrix}
\end{align*}
$$

When you have a transfer matrix that consists of basis column vectors that are orthogonal, and of unit length.

### The vectors are called _orthonormal_

### The Matrix is called an _Orthognoal Maxtrix_

$$
\bm{A} =
\begin{bmatrix}
\begin{bmatrix}
    \ \\
    \vec{a_1}\\
    \ \\
\end{bmatrix}
\begin{bmatrix}
    \ \\
    \vec{a_2} \\
    \ \\
\end{bmatrix}
\begin{bmatrix}
    \ \\
    \vec{a_3} \\
    \ \\
\end{bmatrix}
\end{bmatrix}
$$

Then $ \bm{A^T} \bm{A}= \bm{I}$

This means that the transpose is the inverse $ \bm{A^T} = \bm{A^{-1}}$

Note: Orthogonal means that all column vectors have zero dot products.$
\vec{a_i} \cdot \vec{a_j} = 0 $
