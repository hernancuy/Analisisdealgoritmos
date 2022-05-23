import sys
import random
from collections import defaultdict
import time


def main():
    filename = sys.argv[1]
    algo = sys.argv[2]

    G = load_graph(filename)
    if algo == "1":
        cover = algorithm1(G)
    elif algo == "2":
        cover = algorithm2(G)
    elif algo == "3":
        cover = algorithm3(G)  
    elif algo == "4":
        cover = algorithm3(G) 
    else:
        print("Incorrect arguments")
        exit()

    print(cover)
    print("El tamaño del conjunto de vertices es", len(cover)) 



def output_cover(cover):
    with open("vertexCoverResultado.txt", "w") as fout:
        for v in cover:
            fout.write(str(v)+"\n")

def algorithm4(adj_list):
    cover = []
    while len(adj_list.values()) > 0:
        x = random.choice(list(adj_list.keys()))
        if len(adj_list[x])>0:
            y = random.choice(tuple(adj_list[x]))
            cover.append(x)
            cover.append(y)
            for item in adj_list:
                adj_list[item].discard(x)
            adj_list.pop(x)
        else:
            adj_list.pop(x)   
    return set(cover)

def algorithm3(adj_list):
    cover = []
    while len(adj_list.values()) > 0:
        x = random.choice(list(adj_list.keys()))
        if len(adj_list[x])>0:
            y = random.choice(tuple(adj_list[x]))
            if len(adj_list[x])>len(adj_list[y]):
                cover.append(x)
                for item in adj_list:
                    adj_list[item].discard(x)
                adj_list.pop(x)
            elif len(adj_list[x])<=len(adj_list[y]):
                cover.append(y)
                for item in adj_list:
                    adj_list[item].discard(y)
                adj_list.pop(y)
        else:
            adj_list.pop(x)
    return set(cover)

def algorithm2(adj_list):
    cover = []
    while len(adj_list.values()) > 0:
        sort = sorted(adj_list, key=lambda k: len(adj_list[k]), reverse=True)
        x = sort[0]
        if len(adj_list[x])>0:
            cover.append(x)
            for item in adj_list:
                adj_list[item].discard(x)
            adj_list.pop(x)
        else:
            adj_list.pop(x) 
    return set(cover)

def algorithm1(adj_list):
    cover = []
    while len(adj_list.values()) > 0:
        x = random.choice(list(adj_list.keys()))
        if len(adj_list[x])>0:
            y = tuple(adj_list[x])
            cover.append(x)
            cover.append(y[0])
            for item in adj_list:
                adj_list[item].discard(x)
            adj_list.pop(x)
        else:
            adj_list.pop(x)   
    return set(cover)
    

def load_graph(filename):
    adj_list = defaultdict(set)
    with open(filename, "r") as fin:
        for line in fin:
            u, v = [int(v) for v in line.strip().split()]
            adj_list[u].add(v)
            adj_list[v].add(u)
    return adj_list


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Tiempo de ejecucion --- %s segundos ---" % (time.time() - start_time))
