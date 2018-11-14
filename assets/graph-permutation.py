import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

# Note, there is several 
B=np.array([[ 0,  1,  1,  0,  0],
            [ 1,  0,  1,  1,  0],
            [ 1,  1,  0,  1,  0],
            [ 0,  1,  1,  0,  1],
            [ 0,  0,  0,  1,  0]])

P=np.array([[ 1,  0,  0,  0,  0],
            [ 0,  0,  0,  1,  0],
            [ 0,  1,  0,  0,  0],
            [ 0,  0,  0,  0,  1],
            [ 0,  0,  1,  0,  0]])

# 1->1                     0->0                 [[ 1,  0,  0,  0,  0],
# 4->2                     3->1                  [ 0,  0,  0,  1,  0],
# 2->3                     1->2                  [ 0,  1,  0,  0,  0],
# 5->4                     4->3                  [ 0,  0,  0,  0,  1],
# 3->5                     2->4                  [ 0,  0,  1,  0,  0]]


# for drawing the graph, only
G = nx.from_numpy_matrix(np.array(B))
plt.figure()
plt.subplot(211)

# the annoying of zero- and one- indexing let's us rename the depicted labels 
mathLabels = {0: 1, 1:2, 2:3, 3:4, 4:5}
nx.draw(G, with_labels=True, labels=mathLabels)

# As taught in the lecture P*(P*A)^T
A = np.matmul(P,np.transpose(np.matmul(P,B)))

# Since python 3.5 the following also works (note the stronger binding of
# the transpose operator
A = P@(P@B).T

# More clever (see Appendix C or the numpy documentation)
# define how rows should be permuted 
# r = np.array([0, 3, 1, 4, 2])
# A = (B[np.array(r),:].T)[np.array(r),:]

H = nx.from_numpy_matrix(A)
plt.subplot(212)
nx.draw(H, with_labels=True, labels=mathLabels)
plt.show()

