import numpy as np
import re

def n_gram(w, corpus, n=5):
    n_gram_list = []
    idx = [i for (y, i) in zip(corpus, range(len(corpus))) if w == y]
    for i in idx:
        for j in range(n):
            n_gram_list.append(corpus[i-j:i-j+n])
    return n_gram_list

def EditDist(X, Y):
    if len(X) > len(Y): X, Y = Y, X

    dist = range(len(X) + 1)
    for i2, c2 in enumerate(Y):
        dist_ = [i2+1]
        for i1, c1 in enumerate(X):
            if c1 == c2:
                dist_.append(dist[i1])
            else:
                dist_.append(1 + min((dist[i1], dist[i1 + 1], dist_[-1])))
        dist = dist_
    return dist[-1]

def candidate_search(corpus, w_error, delta=3):
    dist_list = np.array([])
    uniq_cp = np.unique(corpus)
    
    for s in uniq_cp:
        dist = EditDist(w_error, s)
        dist_list = np.append(dist_list, dist)
    idx = np.where(dist_list<=delta)[0]
    return uniq_cp[idx]

def lcs(X, Y, m, n): 
  
    if m == 0 or n == 0: 
        return 0
    elif X[m-1] == Y[n-1]: 
        return 1 + lcs(X, Y, m-1, n-1)
    else: 
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))

def mclcs(X, Y, mod_type):
    if len(X) > len(Y): X, Y = Y, X
    length = 0

    if mod_type == 1:
        for i in range(len(X)):
            if X[i] == Y[i]: length += 1
            else: break
    elif mod_type == 0:
        for i in range(len(X)):
            if X[-i-1] == Y[-i-1]: length += 1
            else: break
    elif mod_type > 1 and mod_type <= len(X):
        for i in range(mod_type-1, len(X), 1):
            if X[i] == Y[i]: length += 1
            else: break
    else: print('subscript out of bound!')
    return length

def nlcs(X, Y):
    return 2*lcs(X, Y, len(X), len(Y))**2/(len(X)+len(Y))

def nmnlcs(X, Y, mod_type):
    return 2*mclcs(X, Y, mod_type)**2/(len(X)+len(Y))

def LED_score(w_error, w_correct, delta=3):

    score = max(1-EditDist(w_error, w_correct)/(delta+1), 0)
    return score

def SS_score(w_error, w_correct, a1=.25, a2=.25, a3=.25, a4=.25, N=3):
    L = min(len(w_error), len(w_correct))
    if L<=3: n=0
    else: n=N
    return a1*nlcs(w_error, w_correct) + a2*nmnlcs(w_error, w_correct, 1) + a3*nmnlcs(w_error, w_correct, n) + a4*nmnlcs(w_error, w_correct, 0)

def LP_score(w_cand, corpus):
    freq = corpus.count(w_cand)
    return freq

def ECP_score(gram_list, w_cand, truth_corpus, n):
    pos = np.arange(len(gram_list))%n
    truth = ' '.join(truth_corpus)
    freq = 0
    for i,j in zip(np.arange(len(gram_list)), pos):
        gram_list[i][j] = w_cand
        l = gram_list[i]
        s = ' '.join(l)
        freq += truth.count(s)
    return freq

def RCP_score(w_error, w_correct, tess_corpus, truth_corpus, n=5, delta=3):
    gram_list = n_gram(w_error, tess_corpus, n)
    cand_list = candidate_search(truth_corpus, w_error, delta)
    pos = np.arange(len(gram_list))%n

    truth = ' '.join(truth_corpus)
    cand_freq = []
    for c in cand_list:
        for i,j in zip(np.arange(len(gram_list)), pos):
            gram_list[i][j] = c
        freq = 0
        for i in range(len(gram_list)):
            l = gram_list[i]
            for k in range(n):
                if k == i%n: continue
                else: 
                    l[k] = '[a-z]*'
                    s = ' '.join(l)
                    freq += len(re.findall(s, truth))
        cand_freq.append(freq)
    
    for i,j in zip(np.arange(len(gram_list)), pos): 
        gram_list[i][j] = w_correct
    freq = 0
    for i in range(len(gram_list)):
        l = gram_list[i]
        for k in range(n):
            if k == i%n: continue
            else:
                l[k] = '[a-z]*'
                s = ' '.join(l)
                freq += len(re.findall(s, truth))
    if max(cand_freq)==0 :
        return 0
    else: return freq/max(cand_freq)
