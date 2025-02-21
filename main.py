import sys
import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTableWidgetItem,
                             QDialog, QMessageBox)


class CoffeeEditDialog(QDialog):
    def __init__(self, parent=None, coffee_id=None):
        super().__init__(parent)
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.coffee_id = coffee_id
        self.con = sqlite3.connect("coffee.sqlite")
        self.cursor = self.con.cursor()

        if self.coffee_id is not None:
            self.setWindowTitle("Редактировать запись о кофе")
            self.load_coffee_data()
        else:
            self.setWindowTitle("Добавить новую запись о кофе")
        self.saveButton.clicked.connect(self.accept)

    def load_coffee_data(self):
        query = "SELECT * FROM table1 WHERE ID = ?"
        result = self.cursor.execute(query, (self.coffee_id,)).fetchone()
        if result:
            self.lineEditSort.setText(str(result[1]))
            self.lineEditDegree.setText(str(result[2]))
            self.lineEditState.setText(str(result[3]))
            self.lineEditTaste.setText(str(result[4]))
            self.lineEditPrice.setText(str(result[5]))
            self.lineEditVolume.setText(str(result[6]))

    def accept(self):
        sort = self.lineEditSort.text()
        degree = self.lineEditDegree.text()
        state = self.lineEditState.text()
        taste = self.lineEditTaste.text()
        price = self.lineEditPrice.text()
        volume = self.lineEditVolume.text()

        if not all([sort, degree, state, taste, price, volume]):
            QMessageBox.critical(self, "Ошибка", "Пожалуйста, заполните все поля.")
            return

        try:
            price = float(price)
            volume = float(volume)
        except ValueError:
            QMessageBox.critical(self, "Ошибка", "Некорректный формат цены или объема.")
            return

        if self.coffee_id is not None:
            # Режим редактирования
            query = """UPDATE table1 SET
                       name = ?, roasting = ?, type = ?, description = ?, cost = ?, volume = ?
                       WHERE ID = ?"""
            try:
                self.cursor.execute(query, (sort, degree, state, taste, price, volume, self.coffee_id))
                self.con.commit()
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Ошибка", f"Ошибка при редактировании: {e}")
                self.con.rollback()
                return
        else:
            # Режим добавления
            query = """INSERT INTO table1 (name, roasting, type, description, cost, volume)
                       VALUES (?, ?, ?, ?, ?, ?)"""
            try:
                self.cursor.execute(query, (sort, degree, state, taste, price, volume))
                self.con.commit()
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Ошибка", f"Ошибка при добавлении: {e}")
                self.con.rollback()
                return
        QDialog.accept(self)

    def closeEvent(self, event):
        QDialog.reject(self)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.pushButton.clicked.connect(self.update_result)
        self.addButton.clicked.connect(self.add_coffee)
        self.editButton.clicked.connect(self.edit_coffee)
        self.modified = {}
        self.titles = None
        self.update_result()

    def update_result(self):
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM table1").fetchall()
        if not result:
            self.statusBar().showMessage('Ничего не нашлось')
            self.tableWidget.setRowCount(0)  # clear the table
            return
        else:
            self.statusBar().showMessage('Результаты найдены')
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        self.tableWidget.setHorizontalHeaderLabels(self.titles)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}

    def add_coffee(self):
        dialog = CoffeeEditDialog(self)
        if dialog.exec():
            self.update_result()

    def edit_coffee(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите строку для редактирования.")
            return

        coffee_id = int(self.tableWidget.item(selected_row, 0).text())

        dialog = CoffeeEditDialog(self, coffee_id=coffee_id)
        if dialog.exec():
            self.update_result()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
