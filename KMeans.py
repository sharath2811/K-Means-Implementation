#Instructions for running the script below



#from matplotlib import*
#import matplotlib.pyplot as plt
import random
import numpy as np
import operator as op

def classify_points(X, mu):
    clusters  = {}
    for x in X:
        bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]])) \
                    for i in enumerate(mu)], key=lambda t:t[1])[0]
        try:
            clusters[bestmukey].append(x)
        except KeyError:
            clusters[bestmukey] = [x]
    return clusters
    
 
def calc_centroid(mu, clusters):
    newmu = []
    keys = sorted(clusters.keys())
    for k in keys:
        newmu.append(np.mean(clusters[k], axis = 0))
    return newmu
    
 
def converged(mu, oldmu,a):
	subs=list(map(op.sub, mu, oldmu))
	abs_subs=sum(np.absolute(subs))
	#print("The difference is: " + str(abs_subs))
	if abs_subs<0.001:
		return True
	else:
		return False
    
    
 
def kmeans(X,K):
    num_iter=0
    oldmu = random.sample(X, K)
    mu = random.sample(X, K)
    while not converged(mu, oldmu, num_iter):
            num_iter +=1
            oldmu = mu
            # Assign all points in X to clusters
            clusters = classify_points(X, mu)
            # Reevaluate centers
            mu = calc_centroid(oldmu, clusters)
    print("The total number of iterations necessary for convergence: " + str(num_iter))
    print("The total number of data instances is: " + str(len(X)))
    print("The final means of each cluster are: " + str(mu))
    print("The size of each cluster is: " + str(len(clusters)))
    #print("The final clusters are: " + str(clusters))
    return

#load your input data here    
X= np.loadtxt("iris.txt", delimiter=',')
#call your KMeans function below with the dataset and number of clusters as parameters
kmeans(X,4) 
