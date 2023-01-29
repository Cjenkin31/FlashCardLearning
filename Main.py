from WindowSwitch import *
from repickler import RePickle
def main():
    RePickle()
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setStyleSheet("QPushButton { margin: 10ex; }")
    controller = Controller()
    controller.show_main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()