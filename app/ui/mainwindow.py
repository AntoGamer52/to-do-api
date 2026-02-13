import sys
from PyQt6.QtWidgets import (
    QApplication, QTreeView, QWidget,
    QHBoxLayout, QVBoxLayout, QPushButton,
    QCheckBox, QLabel, QMainWindow
)
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt


# =========================
# Widget personalizado por fila
# =========================
class RowWidget(QWidget):
    def __init__(self, text, item, model):
        super().__init__()

        self.item = item
        self.model = model

        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 0, 5, 0)

        # Checkbox
        self.checkbox = QCheckBox()
        self.checkbox.stateChanged.connect(self.update_check_state)

        # Texto
        self.label = QLabel(text)

        # Botón +
        self.btn_add = QPushButton("+")
        self.btn_add.setFixedWidth(25)
        self.btn_add.clicked.connect(self.add_child)

        # Botón -
        self.btn_remove = QPushButton("-")
        self.btn_remove.setFixedWidth(25)
        self.btn_remove.clicked.connect(self.remove_self)
        self.btn_remove.hide()  # Se muestra solo en hover

        layout.addWidget(self.checkbox)
        layout.addWidget(self.label)
        layout.addWidget(self.btn_add)
        layout.addStretch()
        layout.addWidget(self.btn_remove)

    # Mostrar botón "-" en hover
    def enterEvent(self, event):
        self.btn_remove.show()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.btn_remove.hide()
        super().leaveEvent(event)

    # Sincronizar checkbox con el modelo
    def update_check_state(self, state):
        self.item.setCheckState(
            Qt.CheckState.Checked if state else Qt.CheckState.Unchecked
        )

    # Añadir hijo
    def add_child(self):
        new_item = QStandardItem()
        self.item.appendRow(new_item)

        index = self.model.indexFromItem(new_item)

        widget = RowWidget("Nuevo Item", new_item, self.model)
        tree.setIndexWidget(index, widget)

        tree.expand(self.model.indexFromItem(self.item))

    # Eliminar item
    def remove_self(self):
        parent = self.item.parent()

        if parent:
            parent.removeRow(self.item.row())
        else:
            self.model.removeRow(self.item.row())


# =========================
# Ventana principal
# =========================
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tree Todo Test")
        self.resize(500, 400)

        global tree
        tree = QTreeView()
        tree.setIndentation(20)
        tree.setHeaderHidden(True)

        self.model = QStandardItemModel()
        tree.setModel(self.model)

        self.setCentralWidget(tree)

        self.load_initial_data()

    def load_initial_data(self):
        # Crear estructura inicial de prueba

        categoria = QStandardItem()
        self.model.appendRow(categoria)

        tarea = QStandardItem()
        categoria.appendRow(tarea)

        subtarea = QStandardItem()
        tarea.appendRow(subtarea)

        # Asignar widgets visuales
        self.add_widget_to_item(categoria, "Categoría 1")
        self.add_widget_to_item(tarea, "Tarea 1")
        self.add_widget_to_item(subtarea, "Subtarea 1")

        tree.expandAll()

    def add_widget_to_item(self, item, text):
        index = self.model.indexFromItem(item)
        widget = RowWidget(text, item, self.model)
        tree.setIndexWidget(index, widget)


# =========================
# Ejecutar app
# =========================
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())