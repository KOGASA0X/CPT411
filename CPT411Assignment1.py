import tkinter as tk
from tkinter import filedialog, scrolledtext
from automata.fa.dfa import DFA
import pygraphviz as pgv

states = {
    'start', 'q1', 'number', 'percent', 'ordinal-st', 'ordinal-nd', 'ordinal-rd', 'ordinal-th', 
    'accept-1', 'accept', 
    'J', 'Ja', 'Jan', 'Janu', 'Janua', 'Januar',
    'Ju', 'Jun', 'Jul', 
    'F', 'Fe', 'Feb', 'Febr', 'Febru', 'Februa', 
    'M', 'Ma', 'Mar', 'Marc', 
    'A', 'Ap', 'Apr', 'Apri', 'Au', 'Aug', 'Augu', 'Augus', 
    'S', 'Se', 'Sep', 'Sept', 'Septe', 'Septem', 'Septemb', 'Septembe',  
    'O', 'Oc', 'Oct', 'Octo', 'Octob', 'Octobe',  
    'N', 'No', 'Nov', 'Nove', 'Novem', 'Novemb', 'Novembe', 
    'D', 'De', 'Dec', 'Dece', 'Decem', 'Decemb', 'Decembe', 
    'ye', 'yea',
    'date_year2', 'date_year3', 'date_year4', 'date_year_end'
}
input_symbols = {
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'r', 'd', 't', 'h', 's', ' ', '%',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
}
transitions={
    'start': {' ': 'q1'},
    'q1': {'0': 'number', '1': 'number', '2': 'number', '3': 'number', '4': 'number', '5': 'number',
            '6': 'number', '7': 'number', '8': 'number', '9': 'number'},
    'number': {
        '0': 'number', '1': 'number', '2': 'number', '3': 'number', '4': 'number', '5': 'number',
        '6': 'number', '7': 'number', '8': 'number', '9': 'number', 
        '%': 'percent',
        's': 'ordinal-st','n': 'ordinal-nd','r': 'ordinal-rd','t': 'ordinal-th',

        ' ': 'accept'
    },
    'percent': {' ': 'accept-1'},

    'ordinal-st': {'t': 'accept-1'},
    'ordinal-nd': {'d': 'accept-1'},
    'ordinal-rd': {'d': 'accept-1'},
    'ordinal-th': {'h': 'accept-1'},

    

    'accept-1': {' ': 'accept'},

    'accept': {'J': 'J', 'F': 'F', 'M': 'M', 'A': 'A', 'S': 'S', 'O': 'O', 'N': 'N', 'D': 'D',
            '1': 'date_year2', '2': 'date_year2', '3': 'date_year2', '4': 'date_year2', '5': 'date_year2', '6': 'date_year2',
            '7': 'date_year2', '8': 'date_year2', '9': 'date_year2', '0': 'date_year2',
            'y': 'ye'},

    'J': {'a': 'Ja', 'u': 'Ju'},
    'Ja': {'n': 'Jan'},
    'Jan': {'u': 'Janu'},
    'Janu': {'a': 'Janua'},
    'Janua': {'r': 'Januar'},
    'Januar': {'y': 'accept-1'},
    'Ju': {'n': 'Jun', 'l': 'Jul'},
    'Jun': {'e': 'accept-1'},

    'Jul': {'y': 'accept-1'},

    'F': {'e': 'Fe'},
    'Fe': {'b': 'Feb'},
    'Feb': {'r': 'Febr'},
    'Febr': {'u': 'Febru'},
    'Febru': {'a': 'Februa'},
    'Februa': {'r': 'accept-1'},

    'M': {'a': 'Ma'},
    'Ma': {'r': 'Mar'},
    'Mar': {'c': 'Marc'},
    'Marc': {'h': 'accept-1'},

    'A': {'p': 'Ap', 'u': 'Au'},
    'Ap': {'r': 'Apr'},
    'Apr': {'i': 'Apri'},
    'Apri': {'l': 'accept-1'},

    'Au': {'g': 'Aug'},
    'Aug': {'u': 'Augu'},
    'Augu': {'s': 'Augus'},
    'Augus': {'t': 'accept-1'},

    'S': {'e': 'Se'},
    'Se': {'p': 'Sep'},
    'Sep': {'t': 'Sept'},
    'Sept': {'e': 'Septe'},
    'Septe': {'m': 'Septem'},
    'Septem': {'b': 'Septemb'},
    'Septemb': {'e': 'Septembe'},
    'Septembe': {'r': 'accept-1'},

    'O': {'c': 'Oc'},
    'Oc': {'t': 'Oct'},
    'Oct': {'o': 'Octo'},
    'Octo': {'b': 'Octob'},
    'Octob': {'e': 'Octobe'},
    'Octobe': {'r': 'accept-1'},

    'N': {'o': 'No'},
    'No': {'v': 'Nov'},
    'Nov': {'e': 'Nove'},
    'Nove': {'m': 'Novem'},
    'Novem': {'b': 'Novemb'},
    'Novemb': {'e': 'Novembe'},
    'Novembe': {'r': 'accept-1'},

    'D': {'e': 'De'},
    'De': {'c': 'Dec'},
    'Dec': {'e': 'Dece'},
    'Dece': {'m': 'Decem'},
    'Decem': {'b': 'Decemb'},
    'Decemb': {'e': 'Decembe'},
    'Decembe': {'r': 'accept-1'},

    'ye': {'a': 'yea'},
    'yea': {'r': 'accept-1'},

    'date_year2':{
        '1': 'date_year3','2': 'date_year3','3': 'date_year3','4': 'date_year3','5': 'date_year3','6': 'date_year3','7': 'date_year3','8': 'date_year3','9': 'date_year3','0': 'date_year3'
    },
    'date_year3':{
        '1': 'date_year4','2': 'date_year4','3': 'date_year4','4': 'date_year4','5': 'date_year4','6': 'date_year4','7': 'date_year4','8': 'date_year4','9': 'date_year4','0': 'date_year4'
    },
    'date_year4':{
        '1': 'date_year_end','2': 'date_year_end','3': 'date_year_end','4': 'date_year_end','5': 'date_year_end','6': 'date_year_end','7': 'date_year_end','8': 'date_year_end','9': 'date_year_end','0': 'date_year_end'
    },
    'date_year_end':{
        ' ': 'accept'
    }
}
allow_partial=True
initial_state='start'
final_states={'accept'}

for key in transitions.keys():
    print(key)

dfa = DFA(states=states, input_symbols=input_symbols, transitions=transitions, initial_state=initial_state, final_states=final_states, allow_partial=allow_partial)


def visualize_dfa():
    graph = dfa.show_diagram()
    graph.draw('dfa_graph.png')
    

def find_numbers(article, dfa):
    current_state = dfa.initial_state
    matched_strings = []
    current_string = ''

    for char in article:
        try:
            next_state = dfa.transitions[current_state][char]
            current_state = next_state
            current_string += char

            if next_state in dfa.final_states:
                matched_strings.append(current_string)
                current_string = ''
        except KeyError:
            current_state = dfa.initial_state
            current_string = ''

    return matched_strings


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
        article = self.text_input.get("1.0", tk.END)
        matched_strings = find_numbers(article, self.dfa)
        result = '\n'.join(matched_strings)
        self.result_area.delete("1.0", tk.END)
        self.result_area.insert(tk.END, result)




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
