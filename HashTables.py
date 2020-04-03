
def remove_duplicate(L):
    h={}
    for e in L:
        if e not in h:
            h[e]=e
    return h.keys()




def check_anagram(S1, S2):
    h={}
    for e in S1:
        if e not in h:
            h[e]=1

        else:
            h[e]+=1

    for e in S2:
        if e in h:
            h[e]-=1
        else:
            return False

    return True




def find_symmetric_pairs(L):
    h = {}
    result_list = []
    for e in L:
        if e[1] in h and h[e[1]] == e[0]:
            result_list.append(e)
        else:
            h[e[0]] = e[1]

    return result_list


def sum_2_k(A, K):
    h = {}
    B=[]
    
    for e in A:
        h[e]=e

    for e in h.keys():
        for i in h.keys():
            if i==K-e:
                B.append((e,i))
                    
    for e in B:
        for i in B:
            if e[0] == i[1] and i[0] == e[1]:
                B.remove(e)
                
    return B




