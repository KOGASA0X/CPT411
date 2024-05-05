import tkinter as tk
from graphviz import Digraph

# 定义DFA类
class DFA:
    def __init__(self):
        self.states = ['q0', 'q1', 'q2']  # 例子中的状态
        self.final_states = ['q2']        # 接受状态
        self.transitions = {
            ('q0', '1'): 'q1',
            ('q1', '0'): 'q2',
            ('q2', '1'): 'q2',  # 循环在q2状态
            ('q2', '0'): 'q2'
        }
        self.current_state = 'q0'

    def transition(self, input_char):
        if (self.current_state, input_char) in self.transitions:
            self.current_state = self.transitions[(self.current_state, input_char)]
        else:
            self.current_state = None  # 陷阱状态

    def is_accepting(self):
        return self.current_state in self.final_states

    def reset(self):
        self.current_state = 'q0'

    def create_graph(self):
        dot = Digraph()
        for state in self.states:
            if state in self.final_states:
                dot.node(state, state, shape='doublecircle')
            else:
                dot.node(state, state)
        
        for (src, char), dst in self.transitions.items():
            dot.edge(src, dst, label=char)
        
        dot.render('dfa', view=True)

# 设置GUI
def run_dfa():
    dfa.reset()
    input_string = entry.get()
    for char in input_string:
        dfa.transition(char)
    result.set("Accepted" if dfa.is_accepting() else "Rejected")
    dfa.create_graph()

app = tk.Tk()
app.title("DFA Simulator")

dfa = DFA()
entry = tk.Entry(app)
entry.pack()

result = tk.StringVar()
tk.Label(app, textvariable=result).pack()

tk.Button(app, text="Run DFA", command=run_dfa).pack()

app.mainloop()
