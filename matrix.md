# Matrices

# Introduction

Matrices among many other things, allow us to solve simultaneous equations.

$$
    3a + 4b = 26\\
    -3a + b = -1
$$

Here's the matrix representation:

$$
\begin{equation*}

\begin{bmatrix}
3 & 4  \\
-3  & 1  \\
\end{bmatrix}
\begin{bmatrix}
{a}  \\
{b}  \\
\end{bmatrix}
=
\begin{bmatrix}
26  \\
-1  \\
\end{bmatrix}

\end{equation*}
$$

Consider the matrix product with the natural basis vectors.

$$
\begin{equation*}
\begin{align*}
\begin{bmatrix}
3 & 4  \\
-3  & 1  \\
\end{bmatrix}
\begin{bmatrix}
{1}  \\
{0}  \\
\end{bmatrix}
=
\begin{bmatrix}
3  \\
-3  \\
\end{bmatrix}\\
\\
\begin{bmatrix}
3 & 4  \\
-3  & 1  \\
\end{bmatrix}
\begin{bmatrix}
{0}  \\
{1}  \\
\end{bmatrix}
=
\begin{bmatrix}
4  \\
1  \\
\end{bmatrix}
\end{align*}
\end{equation*}
$$

![basis vectors](img/basis.svg "basis vectors")
The key idea is that the matrix transforms the input vector space. Think of the matrix as a function that takes input vectors and produces output vectors.
The simultaneous equation problem is to find the input vector that solves the equations.

$$
\begin{equation*}
\begin{gather*}
x_1
\begin{bmatrix}
3  \\
-3  \\
\end{bmatrix}
+ x_2
\begin{bmatrix}
4 \\
1  \\
\end{bmatrix}
=
\begin{bmatrix}
26  \\
-1  \\
\end{bmatrix}

\\
\bm{x}_b =
 \begin{bmatrix}
x_1  \\
x_2  \\
\end{bmatrix}
=
 \begin{bmatrix}
2  \\
5 \\
\end{bmatrix}
\end{gather*}
\end{equation*}
$$
