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

The transpose $ \bm{A}^T$ is described as:

$$
    a^T_{ij} = a{ji}
$$

Here's a concrete example:

$$
\begin{align*}
\bm{A} =
\begin{bmatrix}
4 &1 \\
0 & 9
\end{bmatrix}
\\
\bm{A^T} =
\begin{bmatrix}
4 &0 \\
1 & 9
\end{bmatrix}
\end{align*}
$$

When you have a transfer matrix that consists of basis column vectors that are orthogonal, and of unit length. The vectors are called _orthonormal_. The Matrix is called an _Orthognoal Maxtrix_

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

## Gram-Schmidt process

A process to convert a linearly independent matrix to one that consist of orthonormal column vectors.

$$
\bm{V} =
\begin{bmatrix}
\begin{bmatrix}
    \ \\
    \vec{v_1}\\
    \ \\
\end{bmatrix}
\begin{bmatrix}
    \ \\
    \vec{v_2} \\
    \ \\
\end{bmatrix}
...
\begin{bmatrix}
    \ \\
    \vec{a_n} \\
    \ \\
\end{bmatrix}
\end{bmatrix}
$$

The new $ \bm{v_1}^`$ is just normalized to have unit length.

$$
    \vec{e_1} = { \vec{v_1} \over | \vec{v_1} | }
$$

To calculate e2, subtract the vector projection of v2 onto e1. The result is orthogonal to e1.Then normalize to unit length.

$$
    \vec{w_2} =  \vec{v_2}  -   ( \vec{v_2} \cdot \vec{e_1} ) \vec{e_1} \\
    \vec{e_2} = {  \vec{w_2}  \over |\vec{w_2}| }
$$

For V3, subtract v3 projected onto e1 and v3 projected on to e2. What remains is orthogonal to both e1 and e2. Normalize to unit length

$$
    \vec{w_3} =  \vec{v_3}  -   ( \vec{v_3} \cdot \vec{e_1} ) \vec{e_1}
 -   ( \vec{v_3} \cdot \vec{e_2} ) \vec{e_2}
    \\
    \vec{e_3} = {  \vec{w_3}  \over |\vec{w_3}| }
$$

# Reflecting a plane in a different coordinate system.

## The motivation behind Gram-Schmidt and basis transformations

Reflecting a plane that is defined in the standard $e_x e_y e_z $ system is easy. However, reflecting a plane that is defined by two vectors e.g. $ \begin{bmatrix}  3&1\\ -1&2  \end{bmatrix}$ is much harder. This is where finding a orthogonal matrix makes things easy.

For a motivation example, if we have a matrix B with the first two column vectors defining a plane. And we want to reflect a different vector V about that plane.

$$
\bm{B} =  \begin{bmatrix}
    1& 2&3 \\
    1&0&3 \\
    1&1&-1 \\
\end{bmatrix}
$$

$$
\vec{v} = \begin{bmatrix} 2 \\ 3 \\ 5  \end{bmatrix}
$$

Using Gram-Schmidt process on the column vectors of B, the result is:

$$
\bm{E_b} =  \begin{bmatrix}
{  1 \over \sqrt(3)}  \begin{bmatrix}  1 \\ 1\\ 1  \end{bmatrix} &
{  1 \over \sqrt(2)}  \begin{bmatrix}  1 \\ -1\\ 0  \end{bmatrix} &
{  1 \over \sqrt(6)}  \begin{bmatrix}  1 \\ -1\\ -2  \end{bmatrix}
 \end{bmatrix}
$$

A reflection about the plane defined by the first two columns is this following matrix defined not in the normal basis, but B basis

$$
\bm{T_{b}} = \begin{bmatrix} 1&0&0 \\ 0&1&0 \\ 0&0&-1\end{bmatrix}
$$

Transforming a vector from normal coordinate to a new basis is:

$$
 \bm{E_b}^{-1} \  \vec{v}
$$

And remember for orthogonal matrices composed of orthonormal vectors, the matrix inverse is equal to it's transpose. This can make calculations easier.

$$
 \bm{E_b}^{-1}  = \bm{E_b}^{T}
$$

The calculation for the reflected vector v prime:

$$
\vec{v}^` = \bm{E_b} \ \bm{T_{b}} \  \bm{E_b^T} \ \vec{v}
$$
