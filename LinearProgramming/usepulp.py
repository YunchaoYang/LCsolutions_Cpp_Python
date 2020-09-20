
# Import PuLP modeler functions
from pulp import *

# A new LP problem
prob = LpProblem("test1", LpMinimize)

# Variables
DM_0 = LpVariable("DM_0", 0, None)
DM_1 = LpVariable("DM_1", 0, None)
DM_2 = LpVariable("DM_2", 0, 2.772)
DM_3 = LpVariable("DM_3", 0, None)
DM_4 = LpVariable("DM_4", 0, None)
DM_5 = LpVariable("DM_5", 0, None)


# Objective
prob += 64.139941691  * DM_0 + \
	26.6666666667 * DM_1 + \
	8.88888888889 * DM_2 + \
	50.6329113924 * DM_3 + \
	56.1111111111 * DM_4 + \
	25.2525252525 * DM_5 , "obj"

prob += 	            DM_2                      <= 2.772, "c0" 
prob += 	                   DM_3 + DM_4 + DM_5 <= 11.088, "c1"
prob += 		                DM_3 + DM_4 + DM_5 >= 3.696,  "c2"
prob += DM_0 + DM_1 + DM_2 + DM_3 + DM_4 + DM_5 >= 18.48,  "c3"
prob += DM_0 + DM_1 + DM_2 + DM_3 + DM_4 + DM_5 <= 20.328, "c4"
prob += 9.24 *DM_0 + 6    *DM_1 + 4.5   *DM_2 + 10  *DM_3 + 10   *DM_4 >= 163.6911, "c5"
prob += 9.24 *DM_0 + 6    *DM_1 + 4.5   *DM_2 + 10  *DM_3 + 10   *DM_4 <= 218.2548, "c6"
prob += 0.09 *DM_0 + 0.13 *DM_1 + 0.006 *DM_2 + 0.2 *DM_3 + 0.16 *DM_4 >= 2.2257,   "c7"
prob += 0.09 *DM_0 + 0.13 *DM_1 + 0.006 *DM_2 + 0.2 *DM_3 + 0.16 *DM_4 <= 2.9676,   "c8"
prob += 3    *DM_0 + 3.6  *DM_1 + 6     *DM_2 + 2.7 *DM_3 + 8    *DM_4 + 280* DM_5 >= 93.342, "c9"
prob += 3    *DM_0 + 2.9  *DM_1 + 3     *DM_2 + 5.7 *DM_3 + 7    *DM_4 + 190* DM_5 >= 59.73,  "c10"


status = prob.solve()

print("Status:", LpStatus[prob.status])

for v in prob.variables():
	print(v.name, "=", v.varValue)

# Print the value of the objective
print("objective=", value(prob.objective))

for constraint in prob.constraints:
    constraint_sum = 0
    for var, coefficient in prob.constraints[constraint].items():
        constraint_sum += var.varValue * coefficient
    print(prob.constraints[constraint].name, constraint_sum)