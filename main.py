import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QFileDialog, QMessageBox
import new_main_window_620_480 #mainwindow4_640_480
from new_main_window_620_480 import *
# from mainwindow4_640_480 import *


class StartWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = new_main_window_620_480.Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.loadimage.clicked.connect(self.add_file)  # загрузка изобр-я
        self.ui.space_for_display_images.mousePressEvent = self.handleMousePressEvent
        # block for table
        self.ui.add_row.clicked.connect(self.addRow)
        self.ui.delete_row.clicked.connect(self.removeRow)
        self.ui.export_table.clicked.connect(self.export_table)  # add button to export_table method
        # block for paint the crosses
        self.cross_position = None
        self.pixmap = QPixmap('white.jpg')
        self.crosses = []
        self.setMouseTracking(True)
        self.ui.space_for_display_images.setPixmap(self.pixmap)
        self.ui.space_for_display_images.setScaledContents(True)

    def handleMousePressEvent(self, event):
        # Получаем глобальные координаты клика
        global_pos = event.globalPosition()
        x_global = global_pos.x()
        y_global = global_pos.y()

        coord = self.ui.space_for_display_images
        x = coord.mapFromGlobal(QPoint(x_global, y_global)).x()
        y = coord.mapFromGlobal(QPoint(x_global, y_global)).y()

        print(f"Clicked coordinates within space_for_display_images: ({x}, {y})")
        # Добавляем строку в таблицу
        row_position = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_position)

        # Добавляем ячейки с координатами в таблицу
        item = QTableWidgetItem(f"{x}")
        self.ui.tableWidget.setItem(row_position, 0, item)
        item = QTableWidgetItem(f"{y}")
        self.ui.tableWidget.setItem(row_position, 1, item)
        # block for paint the crosses
        self.cross_position = self.mapFromGlobal(QCursor.pos())
        self.update()
        if self.cross_position is not None:
            self.crosses.append(self.cross_position)  # Сохраняем позицию крестика
            self.cross_position = None
            self.update()
        painter = QPainter(self.pixmap)

        painter.drawLine(x - 5, y, x + 5, y)
        painter.drawLine(x, y - 5, x, y + 5)

        self.ui.space_for_display_images.setPixmap(self.pixmap)

    @QtCore.Slot()
    def add_file(self):
        fname, filetype = QFileDialog.getOpenFileName(
            self,
            "Open file",
            ".",
            "All (*);;Images (*.png *.jpg *.tif)"
        )
        if fname:
            with open(fname) as f:
                self.pixmap = QPixmap(fname)
                self.ui.space_for_display_images.setPixmap(self.pixmap)
                self.ui.space_for_display_images.setScaledContents(False)
                # Добавляем путь к файлу в listWidget
                item = QListWidgetItem(fname)
                self.ui.listWidget.addItem(item)

    def addRow(self):
        row_count = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_count)

    def removeRow(self):
        selection = self.ui.tableWidget.selectedItems()
        if selection:
            self.ui.tableWidget.removeRow(selection[0].row())

    def export_table(self):
        # Получаем данные из таблицы
        data = [[str(self.ui.tableWidget.item(row, col).text()) for col in range(self.ui.tableWidget.columnCount())] for
                row in range(self.ui.tableWidget.rowCount())]

        # Создаем файл для записи данных
        file_name, _ = QFileDialog.getSaveFileName(self, "Export Table", "", "Text files (*.txt)")
        if file_name:
            # Открываем файл для записи
            with open(file_name, 'w', encoding='utf-8') as file:
                # Записываем данные в файл, разделяя их запятыми
                file.write('\n'.join([' '.join(row) for row in data]))

            # Показываем сообщение об успешном экспорте
            msg = QMessageBox.information(self, "Export Successful",
                                          "The table has been successfully exported to a text file.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = StartWindow()
    sys.exit(app.exec())
