import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt

class GammaLauncher(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("🔆 Calibração de Gama 🔆")
        self.setGeometry(300, 200, 400, 150)
        self.setStyleSheet("background-color: #202020; color: white;")

        layout = QVBoxLayout()

        # Botão para abrir dccw
        self.dccw_btn = QPushButton("Abrir Calibração de Cores")
        self.dccw_btn.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px;")
        self.dccw_btn.clicked.connect(self.open_dccw)
        layout.addWidget(self.dccw_btn)

        self.setLayout(layout)

    def open_dccw(self):
        """Abre o assistente de calibração de cores do Windows"""
        subprocess.run(["dccw"])

    def closeEvent(self, event):
        """Evita erro ao fechar a janela"""
        print("Aplicação encerrada corretamente.")
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GammaLauncher()
    window.show()
    sys.exit(app.exec())