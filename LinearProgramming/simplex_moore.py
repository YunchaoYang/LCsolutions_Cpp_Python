# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 23:35:10 2020

@author: 320100598
"""



"""
Read-me:
Call functions in this order:
    problem = gen_matrix(v,c)
    constrain(problem, string)
    obj(problem, string)
    maxz(problem)
gen_matrix() produces a matrix to be given constraints and an objective function to maximize or minimize.
    It takes var (variable number) and cons (constraint number) as parameters.
    gen_matrix(2,3) will create a 4x7 matrix by design.
constrain() constrains the problem. It takes the problem as the first argument and a string as the second. The string should be
    entered in the form of 1,2,G,10 meaning 1(x1) + 2(x2) >= 10.
    Use 'L' for <= instead of 'G'
Use obj() only after entering all constraints, in the form of 1,2,0 meaning 1(x1) +2(x2) +0
    The final term is always reserved for a constant and 0 cannot be omitted.
Use maxz() to solve a maximization LP problem. Use minz() to solve a minimization problem.
Disclosure -- pivot() function, subcomponent of maxz() and minz(), has a couple bugs. So far, these have only occurred when
    minz() has been called.
"""

import numpy as np

# generates an empty matrix with adequate size for variables and constraints.
def gen_matrix(var,cons):
    tab = np.zeros((cons+1, var+cons+2))
    return tab

# checks the furthest right column for negative values ABOVE the last row. 
# If negative values exist, another pivot is required.
def next_round_r(table):
    final_column = table[:-1,-1]
    m = min(final_column)
    print("final column", final_column);
#    m = min(table[:-1,-1])
    print("min right colume = ", m)

    if m>= 0:
        return False
    else:
        return True

# checks that the bottom row, excluding the final column, for negative values. 
# If negative values exist, another pivot is required.
def next_round(table):
    lr = len(table[:,0])
    m = min(table[lr-1,:-1])
    print("negative bottom row = ",m)
    if m>=0:
        return False
    else:
        return True

# Similar to next_round_r function, but returns row index of negative element in furthest right column
def find_neg_r(table):
    # lc = number of columns, lr = number of rows
    lc = len(table[0,:])
    # search every row (excluding last row) in final column for min value
    m = min(table[:-1,lc-1])
    if m<=0:
        # n = row index of m location
        n = np.where(table[:-1,lc-1] == m)[0][0]
    else:
        n = None
    return n

#returns column index of negative element in bottom row
def find_neg(table):
    lr = len(table[:,0])
    m = min(table[lr-1,:-1])
    print(table[lr-1,:-1])
    if m<=0:
        # n = row index for m
        n = np.where(table[lr-1,:-1] == m)[0][0]
    else:
        n = None
    return n

# locates pivot element in tableu to remove the negative element from the furthest right column.
def loc_piv_r(table):
        total = []
        # r = row index of negative entry
        r = find_neg_r(table)
        # finds all elements in row, r, excluding final column
        row = table[r,:-1]
        # finds minimum value in row (excluding the last column)
        m = min(row)
        # c = column index for minimum entry in row
        c = np.where(row == m)[0][0]
        # all elements in column
        col = table[:-1,c]
        # need to go through this column to find smallest positive ratio
        print('r', r)
        for i, b in zip(col,table[:-1,-1]):
            # i cannot equal 0 and b/i must be positive.
            if i**2>0 and b/i>0:
                total.append(b/i)
            else:
                # placeholder for elements that did not satisfy the above requirements. Otherwise, our index number would be faulty.
                total.append(0)
        element = max(total)
        for t in total:
            if t > 0 and t < element:
                element = t
            else:
                continue
        
        print(total)
        index = total.index(element)
        print('pivot at', index,c);
        return [index,c]
# similar process, returns a specific array element to be pivoted on.
def loc_piv(table):
    if next_round(table):
        total = []
        n = find_neg(table)
        for i,b in zip(table[:-1,n],table[:-1,-1]):
            if i**2>0 and b/i>0:
                total.append(b/i)
            else:
                # placeholder for elements that did not satisfy the above requirements. Otherwise, our index number would be faulty.
                total.append(0)
        element = max(total)
        for t in total:
            if t > 0 and t < element:
                element = t
            else:
                continue
        
        index = total.index(element)
        print('pivot at, ',index,n)
        return [index,n]

# Takes string input and returns a list of numbers to be arranged in tableu
def convert(eq):
    eq = eq.split(',')
    if 'G' in eq:
        g = eq.index('G')
        del eq[g]
        eq = [float(i)*-1 for i in eq]
        return eq
    if 'L' in eq:
        l = eq.index('L')
        del eq[l]
        eq = [float(i) for i in eq]
        return eq

# The final row of the tablue in a minimum problem is the opposite of a maximization problem so elements are multiplied by (-1)
def convert_min(table):
    table[-1,:-2] = [-1*i for i in table[-1,:-2]]
    table[-1,-1] = -1*table[-1,-1]
    return table

# generates x1,x2,...xn for the varying number of variables.
def gen_var(table):
    lc = len(table[0,:])
    lr = len(table[:,0])
    var = lc - lr -1
    v = []
    for i in range(var):
        v.append('x'+str(i+1))
    return v

# pivots the tableau such that negative elements are purged from the last row and last column
def pivot(row,col,table):
    # number of rows
    lr = len(table[:,0])
    # number of columns
    lc = len(table[0,:])
    t = np.zeros((lr,lc)) # initial table 
    pr = table[row,:] # pivot row 
    print("pivot row",row) 
    print(pr)
    if table[row,col]**2>0: #new
        e = 1/table[row,col] # make this entry table[row,col]  one
        r = pr*e # mulitply this row 
        print('mulitply row =, ', r);
        for i in range(len(table[:,col])): # multiply and subtract other rows
            k = table[i,:]   # original row i value
            c = table[i,col] # data in row i and the colume col
            if list(k) == list(pr):
                continue
            else:
                t[i,:] = list(k-r*c)  # multiply and subtract other rows
                print(t);
        t[row,:] = list(r) # put pivot row back
        return t
    else:
        print('Cannot pivot on this element.')

# checks if there is room in the matrix to add another constraint
def add_cons(table):
    lr = len(table[:,0])
    # want to know IF at least 2 rows of all zero elements exist
    empty = []
    # iterate through each row
    for i in range(lr):
        total = 0
        for j in table[i,:]:
            # use squared value so (-x) and (+x) don't cancel each other out
            total += j**2
        if total == 0:
            # append zero to list ONLY if all elements in a row are zero
            empty.append(total)
    # There are at least 2 rows with all zero elements if the following is true
    if len(empty)>1:
        return True
    else:
        return False

# adds a constraint to the matrix
def constrain(table,eq):
    if add_cons(table) == True:
        lc = len(table[0,:])
        lr = len(table[:,0])
        var = lc - lr -1
        # set up counter to iterate through the total length of rows
        j = 0
        while j < lr:
            # Iterate by row
            row_check = table[j,:]
            # total will be sum of entries in row
            total = 0
            # Find first row with all 0 entries
            for i in row_check:
                total += float(i**2)
            if total == 0:
                # We've found the first row with all zero entries
                row = row_check
                break
            j +=1

        eq = convert(eq)
        i = 0
        # iterate through all terms in the constraint function, excluding the last
        while i<len(eq)-1:
            # assign row values according to the equation
            row[i] = eq[i]
            i +=1
        #row[len(eq)-1] = 1
        row[-1] = eq[-1]

        # add slack variable according to location in tableau.
        row[var+j] = 1
    else:
        print('Cannot add another constraint.')

# checks to determine if an objective function can be added to the matrix
def add_obj(table):
    lr = len(table[:,0])
    # want to know IF exactly one row of all zero elements exist
    empty = []
    # iterate through each row
    for i in range(lr):
        total = 0
        for j in table[i,:]:
            # use squared value so (-x) and (+x) don't cancel each other out
            total += j**2
        if total == 0:
            # append zero to list ONLY if all elements in a row are zero
            empty.append(total)
    # There is exactly one row with all zero elements if the following is true
    if len(empty)==1:
        return True
    else:
        return False

# adds the onjective functio nto the matrix.
def obj(table,eq):
    if add_obj(table)==True:
        eq = [float(i) for i in eq.split(',')]
        print("eq= ",eq)
        lr = len(table[:,0])
        row = table[lr-1,:]
        i = 0
    # iterate through all terms in the constraint function, excluding the last
        while i<len(eq)-1:
            # assign row values according to the equation
            row[i] = eq[i]*-1
            i +=1
        row[-2] = 1
        row[-1] = eq[-1]
    else:
        print('You must finish adding constraints before the objective function can be added.')

# solves maximization problem for optimal solution, returns dictionary w/ keys x1,x2...xn and max.
def maxz(table, output='summary'):
    while next_round_r(table)==True:
        table = pivot(loc_piv_r(table)[0],loc_piv_r(table)[1],table)
        print("After pivot")
        # print(table)
    while next_round(table)==True:
        table = pivot(loc_piv(table)[0],loc_piv(table)[1],table)

    lc = len(table[0,:])
    lr = len(table[:,0])
    var = lc - lr -1
    i = 0
    val = {}
    for i in range(var):
        col = table[:,i]
        s = sum(col)
        m = max(col)
        if float(s) == float(m):
            loc = np.where(col == m)[0][0]
            val[gen_var(table)[i]] = table[loc,-1]
        else:
            val[gen_var(table)[i]] = 0
    val['max'] = table[-1,-1]
    for k,v in val.items():
        val[k] = round(v,6)
    if output == 'table':
        return table
    else:
        return val

# solves minimization problems for optimal solution, returns dictionary w/ keys x1,x2...xn and min.
def minz(table, output='summary'):
    table = convert_min(table)
    print(table[-1]);
    print("-------")
    while next_round_r(table)==True:        
        table = pivot(loc_piv_r(table)[0],loc_piv_r(table)[1],table)
    print("--------------------------------------")

    while next_round(table)==True:
        table = pivot(loc_piv(table)[0],loc_piv(table)[1],table)
    lc = len(table[0,:]) # column number
    lr = len(table[:,0]) # row number
    var = lc - lr -1     # variable number 
    i = 0
    val = {}
    for i in range(var): # 
        col = table[:,i] # find column = i
        s = sum(col) 
        m = max(col)
        if float(s) == float(m):
            print("col =", col)            
            loc = np.where(col == m)[0][0] # find row number of 
            print('loc=',loc)
            val[gen_var(table)[i]] = table[loc,-1] # map from vi-> value;
        else:
            val[gen_var(table)[i]] = 0
    val['min'] = table[-1,-1]*-1
    print(val)
    for k,v in val.items():
        val[k] = round(v,6)
    if output == 'table':
        return table
    else:
        return val

if __name__ == "__main__":
    number_of_variables = 6
    number_of_constraints = 10
    m = gen_matrix(number_of_variables,number_of_constraints)
    constrain(m, '0,0,1,0,0,0,L,2.772')
    constrain(m, '0,0,0,1,1,1,L,11.088')
    constrain(m, '0,0,0,1,1,1,G,3.696')
    constrain(m, '1,1,1,1,1,1,G,18.48')
    constrain(m, '1,1,1,1,1,1,L,20.328')
    constrain(m, '9.24,6,4.5,10.0,10.0,0,G,163.6911')
    constrain(m, '9.24,6,4.5,10.0,10.0,0,L,218.2548')
    constrain(m, '0.09,0.13,0.006,0.2,0.16,0,G,2.2257')
    constrain(m, '0.09,0.13,0.006,0.2,0.16,0,L,2.9676')
    constrain(m, '3,3.6,6,2.7,8,280,G,93.342')
    #constrain(m, '3,2.9,3,5.7,7,190,G,59.73')
    obj(m,'64.139941691,26.6666666667,8.88888888889,50.6329113924,56.1111111111,25.2525252525,0')
    m0 = np.array(m[:,:number_of_variables])
    
    print(m)
    print('-----------------------------')
    val = minz(m)
    print(val)
    x=list(val.values())
    x=np.array(x[:number_of_variables]).reshape((number_of_variables,-1))
    c = np.dot(m0,x)    



    
    
    
    # number_of_variables = 2
    # number_of_constraints = 2
    # m = gen_matrix(number_of_variables,number_of_constraints)
    # constrain(m,'2,-1,G,10')
    # constrain(m,'1,1,L,20')
    # obj(m,'5,10,0')
    # print(m)
    # print('-----------------------------')
    # val = maxz(m, output='summary')
    # print(maxz(m))

    # number_of_variables = 2
    # number_of_constraints = 4
    # m = gen_matrix(number_of_variables,number_of_constraints)
    # constrain(m,'2,5,G,30')
    # constrain(m,'-3,5,G,5')
    # constrain(m,'8,3,L,85')
    # constrain(m,'-9,7,L,42')
    # obj(m,'2,7,0')
    # print(m)
    # print('-----------------------------')
    # val = minz(m)
    # print(val)