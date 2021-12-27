#!/usr/bin/python
## bellman ford and floyd warshall algorithms

import getopt, sys
import argparse
import numpy as np


def initialize_single_source(G,s):
    d = [ np.inf for i in range(G.shape[0])]
    p = [ None for i in range(G.shape[0])]
    d[s]=0
    return d,p

def relax(u,v,w,d,p):
    if d[v] > d[u]+w:
        d[v]= d[u]+w
        p[v]=u
def bellman_ford(G,s,d,p):
    E=np.transpose(G.nonzero())# edges
    for i in range(G.shape[0]-1):
        for e in E:
            w=G[tuple(e)]
            relax(e[0],e[1],w,d,p)
    for e in E:
        w=G[tuple(e)]
        u=e[0]
        v=e[1]
        if d[v]>d[u]+w:
            return False
    return True

def floyd_warshall(G):
    d=G.copy()
    size=G.shape[0]
    size_r=range(size)
    for k in size_r:
        for i in size_r:
            for j in size_r:
                if d[i,j]>d[i,k]+d[k,j]:
                    d[i,j]=d[i,k]+d[k,j]
    return d

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    args = parser.parse_args()

    HELP_STRING = """O arquivo de entrada deve ter o seguinte formato:
V
u1 v1 w1
u1 v3 w2
u2 v3 w3
u2 v5 w4
...
onde a primeira linha é a quantidade de vértices e cada linha posterior descreve uma aresta com seu peso, sendo u e v os vértices e w o peso.
As variaveis são definidas como:
V ∊ ℕ
u,v ∊ [0,V]
w ∊ ℝ"""
    if args.input == None:
        parser.print_help()
        print(HELP_STRING)
        sys.exit(1)

    fin = open(args.input,'r')

    E=list()
    NUM_V=int(fin.readline())
    for line in fin:
            u,v,w = line.split()
            u,v,w = int(u),int(v),float(w)
            E.append([u,v,w])

    G = np.array([[0 if i == j else np.inf for i in range(NUM_V)] for j in range(NUM_V)])
    for u,v,w in E:
        G[u,v]=w
    print("Matriz de adjacência:")
    print(G)
    print("Número de vértices:",NUM_V)
    ### FLOYD WARSHALL
    print("Matriz de distância:")
    print(floyd_warshall(G))
    
    
    ### BELLMAN
#     for s in range(NUM_V):
        #d,p=initialize_single_source(G,s)# distances and parents
        #work=bellman_ford(G,s,d,p)
#         if not work:
#             print("Ciclo negativo encontrado no grafo.")
#             break
#         print("-==Vértice "+str(s)+"==-")
#         print("Distâncias:"+str(d),"Pais de cada vértice:"+str(p),sep='\n')

    fin.close()
