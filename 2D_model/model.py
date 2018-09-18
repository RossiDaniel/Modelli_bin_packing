from __future__ import print_function
from ortools.linear_solver import pywraplp

def model2D(packages,cargo):
    solver = pywraplp.Solver('Model2D', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    # importo dimensioni dei pacchi e del camion
    M=1000
    n=len(packages)

    w =[packages[i].getW() for i in range(n)]
    d =[packages[i].getD() for i in range(n)]

    W =cargo.getW()
    D =solver.IntVar(0,solver.infinity(),"D")

    # definisco le variabili
    l =[[solver.BoolVar("l%d%d" % (i,j)) for i in range(n)] for j in range(n)]
    b =[[solver.BoolVar("b%d%d" % (i,j)) for i in range(n)] for j in range(n)]

    x =[solver.IntVar(0,solver.infinity(),"x%d" % i) for i in range(n)]
    y =[solver.IntVar(0,solver.infinity(),"y%d" % i) for i in range(n)]

    # definisco i constraints
    for i in range(n):
        for j in range(n):
            if(i < j):
                solver.Add(l[i][j] + l[j][i] + b[i][j] + b[j][i] >= 1)
            if(i != j):
                solver.Add(x[i] - x[j] + M * l[i][j] <= M - w[i])
                solver.Add(y[i] - y[j] + M * b[i][j] <= M - d[i])

        solver.Add(x[i] <= W - w[i])
        solver.Add(y[i] + d[i]<= D)

    #funzione obiettivo
    objective = solver.Objective()
    objective.SetCoefficient(D,1)
    objective.SetMinimization()

    #soluzione
    print(solver.Solve())
    print("larghezza camion: ",W)
    print("lunghezza migliore: ",D.solution_value())
    print ("larghezze: ",w)
    print ("lungo:     ",d)
    for i in range(n):
        print("oggetto n: ",i," coordinate:",x[i].solution_value()," ",y[i].solution_value())
