import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

graph = []
diamet=[200,500,700,900]


matplotlib.rcParams["toolbar"]="None"
cf = pylab.gcf()
cf.set_facecolor('w')
ax = pylab.gca()


nodes = int(raw_input("Enter the count of nodes: "))

for i in xrange(1,nodes+1):
    graph.append(i)


def draw(graph):
    xy = []
    k=0
    a=np.random.randint(len(diamet),size=nodes)
    print a
    for i in xrange(len(graph)):
        x = np.random.random()
        y = np.random.random()
        xy.append([x, y])
        node_collection = ax.scatter(x, y, s=diamet[a[k]], c='y', marker='o', zorder=2)
        k+=1

    graph1=list(graph)
    xy1=list(xy)
    pos = []
    start=[-0.1,-0.1]
    mini=xy1[0]
    k=0
    start=[-0.1,-0.1]
    while xy1:
        dist=100
        for i in xy1:
           ''' k+=1
            if k>=2:
                if diamet'''
            x=i[0]
            y=i[1]
            rast=np.sqrt((x-start[0])**2+(y-start[0])**2)
            if rast<dist:
                dist=rast
                k=i
        plt.plot([start[0], k[0]], [start[1], k[1]], 'k-', zorder=1)
        start=k
        xy1.remove(k)
        
    
    
    for i in graph:
            t = ax.text(xy[i-1][0]-0.007, xy[i-1][1]-0.01, i, zorder=3)

    x1, x2 = -0.1, 1.3
    y1, y2 = -0.1, 1.3
    plt.xlim([x1, x2])
    plt.axis([x1, x2, y1, y2])
    #plt.axis("off")
    cf.canvas.set_window_title("Graph vizualization")
    plt.show()


draw(graph)
