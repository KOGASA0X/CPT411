
from typing import Optional
from automata.fa.dfa import DFA

states = {
    'start', 'is_number', 'number', 'percent', 'ordinal-st', 'ordinal-nd', 'ordinal-rd', 'ordinal-th', 
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
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'r', 'd', 't', 'h', 's', ' ', '%','(',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '.', ','
}
transitions={
    'start': {' ': 'is_number', '(': 'is_number'},
    'is_number': {
        '0': 'number', '1': 'number', '2': 'number', '3': 'number', '4': 'number', '5': 'number',
        '6': 'number', '7': 'number', '8': 'number', '9': 'number'},
    'number': {
        '0': 'number', '1': 'number', '2': 'number', '3': 'number', '4': 'number', '5': 'number',
        '6': 'number', '7': 'number', '8': 'number', '9': 'number', ',': 'number',
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
        '.': 'accept',
        ',': 'accept'
    }
}
allow_partial=True
initial_state='start'
final_states={'accept'}

# for key in transitions.keys():
#     print(key)

def crazy_mode():
    transitions_trap={
        'start': {' ': 'number'},
    }
    return

dfa = DFA(states=states, input_symbols=input_symbols, transitions=transitions, initial_state=initial_state, final_states=final_states, allow_partial=allow_partial)


def visualize_dfa(text: Optional[str] = None):
    graph = dfa.show_diagram(text)
    graph.draw('dfa_graph.png')

def remove_newlines(article):
    return article.replace('\n', '')
    

def find_numbers(article, dfa):
    article = remove_newlines(article)
    current_state = dfa.initial_state
    matched_strings = []
    unmatched_strings = []
    current_string = ''
    temp_string = ''

    for char in article:
        try:
            next_state = dfa.transitions[current_state][char]
            current_state = next_state
            current_string += char

            if next_state in dfa.final_states:
                temp_string = temp_string + current_string
                current_string = ''
        except KeyError:
            current_state = dfa.initial_state
            current_string = ''
            if temp_string != '':
                matched_strings.append(temp_string)
                temp_string = ''

    return matched_strings

from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPixmap,QPainter
from PyQt5.QtCore import QRectF

class ImageViewer(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setScene(QGraphicsScene(self))
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setOptimizationFlags(QGraphicsView.DontAdjustForAntialiasing | QGraphicsView.DontSavePainterState)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

    def set_image(self, file_path):
        self.scene().clear()
        pixmap = QPixmap(file_path)
        self.scene().addPixmap(pixmap)
        self.setSceneRect(QRectF(pixmap.rect()))

    def wheelEvent(self, event):
        factor = pow(1.00125, event.angleDelta().y())
        self.scale(factor, factor)

from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QFileDialog, QVBoxLayout, QWidget, QHBoxLayout,QListWidget
from PyQt5.QtGui import QPixmap

class App(QMainWindow):
    def __init__(self):
        self.dfa=dfa

        super().__init__()
        self.setWindowTitle("Number Data Finder")

        self.text_input = QTextEdit(self)
        self.result_area = QListWidget(self)
        self.result_area.itemDoubleClicked.connect(self.visualize_text)
        self.analyze_button = QPushButton("Analyze", self)
        self.analyze_button.clicked.connect(self.analyze)
        self.load_file_button = QPushButton("Load File", self)
        self.load_file_button.clicked.connect(self.load_file)
        self.visualize_button = QPushButton("Visualize DFA", self)
        self.visualize_button.clicked.connect(self.visualize_all)
        self.ImageViewer = ImageViewer(self)

        self.ImageViewer.setMinimumSize(600, 600)

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.text_input)
        left_layout.addWidget(self.result_area)
        left_layout.addWidget(self.analyze_button)
        left_layout.addWidget(self.load_file_button)
        left_layout.addWidget(self.visualize_button)
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addWidget(self.ImageViewer)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def analyze(self):
        article = self.text_input.toPlainText()
        matched_strings = find_numbers(article, self.dfa)
        result = '\n'.join(matched_strings)
        self.result_area.clear()
        self.result_area.addItems(matched_strings)
    
    def visualize_text(self,item):
        visualize_dfa(item.text())
        self.update_image('dfa_graph.png')

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self)
        with open(file_path, 'r') as file:
            content = file.read()
            self.text_input.clear()
            self.text_input.insertPlainText(content)

    def visualize_all(self):
        visualize_dfa()
        self.update_image('dfa_graph.png')
        pass

    def update_image(self, image_path):
        self.ImageViewer.set_image(image_path)

if __name__ == "__main__":
    app = QApplication([])
    window = App()
    window.show()
    app.exec_()

