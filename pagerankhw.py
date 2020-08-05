"""
Created on 7/30/20

@author: jordanshomefolder
"""
import random
import numpy as np
from scipy import sparse
import pagerankeq as pr


#a
def pr_matrix(linelst, alpha):
    count = 0
    idx = []
    for i in linelst:
        if i[0] == 'a':
            i = i.strip()
            count += 1
            newlst = []
            for y in i:
                if y != " " and y != "a" and y!= 'e':
                    newlst.append(int(y))
            idx.append(newlst[1:])
    arr = []
    for i in idx:
        arrrow = [0]*len(idx)
        for j in range(len(i)):
            arrrow[i[j]] = 1/len(i)
        arr.append(arrrow)
    arrmatrix = (np.array(arr)).transpose()
    onesmatrix = np.array([[1] * len(arr)] * len(arr))
    add = onesmatrix * (1 - alpha) / len(arr)
    m = np.array(arrmatrix * alpha + add)
    return m



def pr_order(linelst, alpha):
    order = []
    matrix = pr_matrix(linelst, alpha)
    nodes = pr.ranking(matrix, steps=100)
    for i in range(len(matrix)):
        order.append((linelst[i][-1], nodes[i]))
    finorder = sorted(order, key=lambda order: order[1], reverse = True)
    final = [finorder[i][0] for i in range(len(finorder))]
    return final    

#b done

#c
def sparse(file):
    adj,n,name=pr.read_graph_file(file)
    r = []
    c = []
    data = []
    
    for key,value in adj.items():
        for i in range(len(value)):
            r.append(value[i])
            c.append(key)
            data.append(1/len(value))
    n = max(max(r),max(c)) +1
    return pr.sparse_example1(r,c,data,n)


def top5(file, alpha, linelst2):
    sparsed = sparse(file)
    ranks = pr.ranking_sparse(sparsed, alpha, steps=100)
    order = []
    print(linelst2[0])
    
    for i in range(len(sparsed)):
        f = linelst2[i].index('h')
        order.append((linelst2[i][f:], ranks[i]))
    finorder = sorted(order, key=lambda order: order[1], reverse = True)
    final = [finorder[i][0] for i in range(len(finorder))]
    return final[:5]
# top url: 'http://search.ucdavis.edu/'


if __name__ == '__main__':
    fname = open('newtxt.txt')
    Lines = fname.readlines()
    linelst = []
    for line in Lines:
        line = line.strip()
        linelst.append(line)
    alpha = .9
    file = 'newtxt.txt'
    file2 = 'california.txt'
    fname2 = open(file2)
    Lines2 = fname2.readlines()
    linelst2 = []
    for line in Lines2:
        line = line.strip()
        linelst2.append(line)
    print(top5(file2,alpha,linelst2))