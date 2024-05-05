import tkinter as tk
from tkinter import filedialog, scrolledtext
from graphviz import Digraph

class DFA:
    def __init__(self):
        # 状态和转移的定义
        self.states = {'start': 0, 'digit': 1, 'percent': 2}
        self.final_states = {'percent': 2}
        self.current_state = self.states['start']

    def reset(self):
        self.current_state = self.states['start']

    def transition(self, char):
        if self.current_state == self.states['start'] and char.isdigit():
            self.current_state = self.states['digit']
        elif self.current_state == self.states['digit'] and char == '%':
            self.current_state = self.states['percent']
        elif self.current_state == self.states['digit'] and char.isdigit():
            pass
        else:
            self.reset()

    def is_accepting(self):
        return self.current_state in self.final_states.values()

def visualize_dfa():
    dfa = Digraph()
    dfa.node('S', 'Start')
    dfa.node('D', 'Digit')
    dfa.node('P', 'Percent', shape='doublecircle')
    dfa.edges(['SD', 'DD', 'DP'])
    dfa.render('dfa_diagram', format='png', cleanup=True)

def find_numbers(text, dfa):
    dfa.reset()
    results = []
    buffer = ""
    for i, char in enumerate(text):
        dfa.transition(char)
        if dfa.current_state != dfa.states['start']:
            buffer += char
        if dfa.is_accepting():
            results.append((buffer, i - len(buffer) + 1, i))
            buffer = ""
            dfa.reset()
        elif dfa.current_state == dfa.states['start']:
            buffer = ""
    return results

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
        self.dfa = DFA()

    def analyze(self):
        text = self.text_input.get("1.0", tk.END)
        results = find_numbers(text, self.dfa)
        self.result_area.delete("1.0", tk.END)
        for res in results:
            self.result_area.insert(tk.END, f"Found '{res[0]}' from {res[1]} to {res[2]}\n")

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
