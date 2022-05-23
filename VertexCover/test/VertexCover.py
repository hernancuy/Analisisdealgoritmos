import sys
import random
import collections


def main():
    filename = sys.argv[1]
    algo = sys.argv[2]

    G = load_graph(filename)
    if algo == "greedy-vertex":
        cover = greedy_vertex(G)
    elif algo == "greedy-edge":
        cover = greedy_edge(G)
    else:
        print("Incorrect arguments")
        exit()

    #output_cover(cover)


def output_cover(cover):
    with open("approxOutput.txt", "w") as fout:
        for v in cover:
            fout.write(str(v)+"\n")


def greedy_edge(adj_list):
   #Prueba
   return

def greedy_vertex(adj_list):
    cover = []
    for key, value in range(0, len(adj_list)):
            random.choice([adj_list.keys()])
            adj_list[key].remove(value)
            adj_list[value].remove(key)
    return cover

def load_graph(filename):
    adj_list = collections.defaultdict(set)
    with open(filename, "r") as fin:
        for line in fin:
            u, v = [int(v) for v in line.strip().split()]
            adj_list[u].add(v)
            adj_list[v].add(u)
    return adj_list


if __name__ == "__main__":
    main()