import random
import itertools
def gen_edges(n=8):
    edges=list(itertools.combinations(range(n),2))
    i=len(edges)
    for j in itertools.combinations(edges,i):
        for _ in range(1,100000):
            colored={x:None for x in j}
            not_colored=list(j)
            for k in range(100):
                if len(not_colored)==0:
                    if k>n:
                        print("example of more than d+1")
                        print(colored)
                    if k > 2*(n-1)-1:
                        print("example of more than 2d-1")
                        print(colored)
                    break
                random.shuffle(not_colored)
                exists=False
                newly_colored=[]
                for edge in not_colored:
                    for key in colored.keys():
                        if key[0] in edge or key[1] in edge:
                            if colored[key]==k:
                                exists=True
                                break
                    if not exists:
                        colored[edge]=k
                        newly_colored.append(edge)
                    exists = False
                for edge in newly_colored:
                    not_colored.remove(edge)


if __name__ == "__main__":
    gen_edges()