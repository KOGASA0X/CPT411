import tkinter as tk
from tkinter import filedialog, scrolledtext
from automata.fa.dfa import DFA
import pygraphviz as pgv

dfa = DFA(
    states={'q0', 'q1'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q1', '1': 'q0'}
    },
    initial_state='q0',
    final_states={'q0'}
)


def visualize_dfa():
    graph = dfa.show_diagram()
    graph.draw('dfa_graph.png')
    

def find_numbers(text, dfa):
    return False

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Data Finder")
        self.text_input = scrolledtext.ScrolledText(root, height=10)
        self.text_input.pack(padx=10, pady=10)
        self.result_area = scrolledtext.ScrolledText(root, height=10)
        self.result_area.pack(padx=10, pady=10)
        tk.Button(root, text="Analyze", command=self.analyze).pack(pady=10)
        tk.Button(root, text="Load File", command=self.load_file).pack(pady=10)
        tk.Button(root, text="Visualize DFA", command=visualize_dfa).pack(pady=10)
        self.dfa = dfa

    def analyze(self):
        return False

    def load_file(self):
        file_path = filedialog.askopenfilename()
        with open(file_path, 'r') as file:
            content = file.read()
            self.text_input.delete("1.0", tk.END)
            self.text_input.insert(tk.END, content)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
