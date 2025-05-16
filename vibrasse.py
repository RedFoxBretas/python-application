import sys
import ctypes
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QSlider, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class GammaApp(QWidget):
    def __init__(self):
        super().__init__()

        # Janela moderna
        self.setWindowTitle("Ajuste de Gama")
        self.setGeometry(300, 200, 400, 250)
        self.setStyleSheet("background-color: #202020; color: white; font-size: 14px;")

        layout = QVBoxLayout()

        # Título
        self.title_label = QLabel("🔆 Ajuste de Gama 🔆")
        self.title_label.setFont(QFont("Arial", 14, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title_label)

        # Slider para ajuste de gama
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(50)
        self.slider.setMaximum(200)
        self.slider.setValue(100)
        self.slider.setStyleSheet("QSlider { height: 20px; }")
        layout.addWidget(self.slider)

        # Botão "Aplicar"
        self.apply_btn = QPushButton("Aplicar Gama")
        self.apply_btn.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px;")
        self.apply_btn.clicked.connect(self.apply_gamma)
        layout.addWidget(self.apply_btn)

        # Botão de Restaurar
        self.restore_btn = QPushButton("Restaurar Padrão")
        self.restore_btn.setStyleSheet("background-color: #FF3D00; color: white; padding: 10px; border-radius: 5px;")
        self.restore_btn.clicked.connect(self.restore_gamma)
        layout.addWidget(self.restore_btn)

        self.setLayout(layout)

    def apply_gamma(self):
        """Aplica o gama no sistema."""
        value = self.slider.value() / 100.0
        self.set_gamma(value)

    def set_gamma(self, gamma_value):
        """Define o gama do sistema Windows."""
        gammaRamp = np.array([i * gamma_value for i in range(256)], dtype=np.uint16)
        gammaRamp = np.stack([gammaRamp] * 3, axis=1)
        gammaRamp = gammaRamp.flatten()

        hdc = ctypes.windll.user32.GetDC(0)
        success = ctypes.windll.gdi32.SetDeviceGammaRamp(hdc, gammaRamp.ctypes.data_as(ctypes.POINTER(ctypes.c_short)))

        if success:
            print(f"Gama ajustado para {gamma_value:.2f}")
        else:
            print("Erro ao definir gama. O sistema pode não permitir essa alteração.")

    def restore_gamma(self):
        """Restaura o gama para o padrão (1.0)."""
        self.slider.setValue(100)
        self.apply_gamma()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GammaApp()
    window.show()
    sys.exit(app.exec_())