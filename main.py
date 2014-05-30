import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

graph = []
diamet=[200,400,700,1000]


matplotlib.rcParams["toolbar"]="None"
cf = pylab.gcf()
cf.set_facecolor('w')
ax = pylab.gca()

diam={}

nodes = int(raw_input("Enter the count of nodes: "))

for i in xrange(1,nodes+1):
    graph.append(i)


def draw(graph):
    xy = []
    k=0
    a1=np.random.randint(len(diamet),size=nodes)
    a=[]
    for i in a1:
        a.append(i)
    
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
    flag=1
    i=-1
    l1=[]
    while xy1:
        dist=100
        l=-1
        le=len(xy1)-1
        while i < le:
            l+=1
            i+=1
            while i in l1:
                i+=1
            if i > le:
                break
            x=xy1[i][0]
            y=xy1[i][1]
            rast=np.sqrt((x-start[0])**2+(y-start[0])**2)
            if rast<dist:
                dist=rast
                k=[xy1[i][0],xy1[i][1]]
                m=i
                d=a[i]
        if start!=[-0.1,-0.1] or flag!=1:
            if d1 in a:
                if d==d1:
                    plt.plot([start[0], k[0]], [start[1], k[1]], 'k-', zorder=1)
                    start=k
                    d1=d
                    a[m]=10
                    a.remove(10)
                    xy1.remove(k)
                    i=-1
                    l1=[]
                else:
                    l1.append(m)
                    i=-1
            else:
                plt.plot([start[0], k[0]], [start[1], k[1]], 'k-', zorder=1)
                start=k
                d1=d
                a[m]=10
                a.remove(10)
                xy1.remove(k)
                i=-1
                l1=[]
        else:
            plt.plot([start[0], k[0]], [start[1], k[1]], 'k-', zorder=1)
            start=k
            d1=d
            a[m]=10
            a.remove(10)
            xy1.remove(k)
            flag=0
            i=-1
            l1=[]

    
    
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
