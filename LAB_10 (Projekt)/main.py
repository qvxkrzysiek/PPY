from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import category_encoders as ce
import tkinter as tk
from tkinter import ttk
import pandas as pd
import seaborn as sns
import numpy as np
import pickle
import random


class Classifier:
    def __init__(self):
        self.Y_pred = None
        self.Y_test = None
        self.Y_train = None
        self.X_test = None
        self.X_train = None
        self.model = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=0)
        self.X = pd.DataFrame
        self.Y = None
        self.load_data()

    def load_data(self):
        path = "/Users/qvxkrzysiek/Desktop/car.csv"
        data = pd.read_csv(path, header=None)
        data.columns = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
        self.X = data.drop('class', axis=1)
        self.Y = data['class']
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.X, self.Y, test_size=0.33, random_state=random.randint(0, 100))

    def train_model(self):
        encoder = ce.OrdinalEncoder(cols=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety'])
        self.X_train = encoder.fit_transform(self.X_train)
        self.X_test = encoder.transform(self.X_test)
        self.model.fit(self.X_train, self.Y_train)
        self.Y_pred = self.model.predict(self.X_test)
        return accuracy_score(self.Y_test, self.Y_pred)

    def show_model_matrix(self):
        fig = plt.figure(figsize=(4, 4))
        classes = np.unique(self.Y)
        ax = fig.add_subplot(111)
        sns.heatmap(confusion_matrix(self.Y_test, self.Y_pred), annot=True, fmt='d', cmap='Reds', xticklabels=classes, yticklabels=classes, ax=ax)
        ax.set_xlabel('Predicted')
        ax.set_ylabel('Real')
        ax.set_title('Confusion Matrix')
        return fig

    def show_model_table(self):
        x = []
        for row, i in enumerate(self.Y_test):
            x.append([i, self.Y_pred[row]])
        return x, ["Real", "Predicted"]

    def import_model(self):
        with open('model.pkl', 'rb') as f:
            self.model = pickle.load(f)
        f.close()

    def export_model(self):
        with open('model.pkl', 'wb') as f:
            pickle.dump(self.model, f)
        f.close()


class GUI:

    def __init__(self, in_model):
        self.model = in_model
        self.root = tk.Tk()
        self.label = ttk.Label(text="")
        self.root.title("Random Forest Classifier")
        self.menu()

    def menu(self):
        menu = tk.Frame(self.root)
        menu.pack(pady=20)
        menu.pack(padx=20)

        style = ttk.Style()
        style.configure('Custom.TButton', padding=10, relief="flat", background="#3d85c6", foreground="black", font=('Arial', 12))

        self.label = ttk.Label(menu, text="Hello", foreground="black", font=('Arial', 12))
        self.label.pack(side=tk.TOP, pady=10)

        train_button = ttk.Button(menu, text="Train", command=self.train, style='Custom.TButton')
        train_button.pack(side=tk.TOP, pady=10)
        matrix_button = ttk.Button(menu, text="Show matrix", command=self.show_matrix, style='Custom.TButton')
        matrix_button.pack(side=tk.TOP, pady=10)
        table_button = ttk.Button(menu, text="Show table", command=self.show_table, style='Custom.TButton')
        table_button.pack(side=tk.TOP, pady=10)
        import_button = ttk.Button(menu, text="Import data", command=self.load, style='Custom.TButton')
        import_button.pack(side=tk.TOP, pady=10)
        export_button = ttk.Button(menu, text="Export data", command=self.save, style='Custom.TButton')
        export_button.pack(side=tk.TOP, pady=10)

    def train(self):
        self.label.configure(text=f"Accuracy: {100 * self.model.train_model() :.2f}%", foreground="black", font=('Arial', 12))

    def show_matrix(self):
        fig_window = tk.Toplevel(self.root)
        fig_window.title("Confusion Matrix")
        canvas = FigureCanvasTkAgg(self.model.show_model_matrix(), master=fig_window)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def show_table(self):
        x, y = self.model.show_model_table()
        fig_window = tk.Toplevel(self.root)
        fig_window.title("Table")

        table = ttk.Treeview(fig_window)
        table['columns'] = y

        table.column("#0", width=1)
        table.column(y[0], width=150)
        table.column(y[1], width=200)

        scrollbar_y = ttk.Scrollbar(fig_window, orient="vertical", command=table.yview)
        scrollbar_y.pack(side='right', fill='y')
        table.configure(yscroll=scrollbar_y.set)

        for column in y:
            table.heading(column, text=column)
        for row in x:
            table.insert('', tk.END, values=row)

        table.pack()

    def load(self):
        self.model.import_model()

    def save(self):
        self.model.export_model()

    def start(self):
        self.root.mainloop()


GUI(Classifier()).start()
