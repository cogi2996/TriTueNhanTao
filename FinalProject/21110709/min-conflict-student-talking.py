import random
import math
import matplotlib.pyplot as plt
import timeit

class Student_Conflict:
    def __init__(self, m):
        self.m = m
        self.variables = list(range(m))

    def goal_test(self, state):
        for i in range(len(state)-1):
            if( state[i]!=-1):  
                for j in range(i+1, len(state)):     
                    if (state[j]!=-1):
                        if ((state[i] == state[j] ) or (abs(state[i] - state[j]) == abs(i-j)==1)):
                            return False
        return True

    def num_conflict(self, state, var, value):
        conflict = 0
        for i in range(len(state)):
            if(state[var]>=0 and state[i]>=0 ):
                if (i != var and (state[i] == value  or (abs(state[i] - value) ==  abs(i-var)==1))):
                            
                    conflict += 1
        return conflict
    
class Problem_solver:
    def __init__(self):
        pass

    def train(self, csp, current_state):
        pass

    def solve(self):
        pass

class MinConflictsSolver(Problem_solver):
    def __init__(self, max_steps=1000):
        self.max_steps = max_steps
        self.count_steps = 0

    def train(self, csp, current_state):
        self.csp = csp
        self.current_state = current_state

    def solve(self):
        self.count_steps = 0
        for step in range(self.max_steps):
            if self.csp.goal_test(self.current_state):
                return self.current_state
                
            conflicted_vars = [var for var in self.csp.variables if self.csp.num_conflict(self.current_state, var, self.current_state[var]) > 0]
            var = random.choice(conflicted_vars)
            min_conflict = float('inf')
            min_value = None
            for value in self.csp.variables:
                conflict = self.csp.num_conflict(self.current_state, var, value)
                if conflict < min_conflict:
                    min_conflict = conflict
                    min_value = value
            self.current_state[var] = min_value
            self.count_steps += 1
        self.count_steps = 0
        return None

def draw_board(n, m , positions, name_student):#n:so hoc sinh noi chuyen ,m: kich thuoc lop hoc
    
    fig, ax = plt.subplots(figsize=(m, m))
    ax.set_xlim(0, m)
    ax.set_ylim(0, m)
    ax.set_xticks([i+0.5 for i in range(m)])
    ax.set_yticks([i+0.5 for i in range(m)])
    ax.set_yticklabels(range(0, m))
    ax.set_xticklabels(range(0, m))
    ax.set_title('Seat', loc='center', pad=20,fontsize=20)
    ax.tick_params(axis='both', which='both', length=0)

    for i in range(m):
        for j in range(m):
                square = plt.Rectangle((i, j), 1, 1, linewidth=0.75, edgecolor='black', facecolor='none')
                ax.add_patch(square)
    used_name=[]
    i=0
    while (i<m):
        if(positions[i]>=0):
            rand_name =random.randint(0,n-1)
            if rand_name not in used_name:
                used_name.append(rand_name)
                ax.text(positions[i]+0.5, i+0.5 , name_student[rand_name], fontsize=20, ha='center', va='center', color='red')
                i+=1
        else:
            i+=1
        
    plt.show()

if __name__ == '__main__':
    n = 10
    student_order = [(i+1) for i in range(n)]
    conf_student = Student_Conflict(n)
    # Khoi tao ban dau
    initial_state=[-1]*n
    i=0
    rand_int=[]
    while (i<n):
        rand_seat=random.randint(0,n-1)
        if rand_seat not in rand_int:
            rand_int.append(rand_seat)
            initial_state[rand_seat] = random.randint(0, n-1)
            i+=1
    print('Khởi tạo : ')
    print(initial_state)
    #draw_board(n, m, initial_seat, student_order )

    solver = MinConflictsSolver(max_steps=1000)
    solver.train(conf_student, initial_state)
    start = timeit.default_timer()
    solution = solver.solve()
    stop = timeit.default_timer()

    if solution is not None:
        print("Đã tìm thấy giải pháp:")
        print(solution)
        print('Step to solve: ', solver.count_steps)
        # print('Time to solve: ', stop - start)
        draw_board(n, n, solution, student_order)
    else:
        print("Không tìm thấy giải pháp ")
    