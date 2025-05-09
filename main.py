from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt
from gui import Ui_MainWindow
from logic import VoteCounter
import sys

class VoteApp(QMainWindow):
    """
    Main application class for the voting GUI.
    Handles navigation, input validation, styling, and voting logic.
    """
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.setup_welcome_screen()
        self.setup_voting_screen()
        self.setup_result_screen()

        self.votes = VoteCounter()

        self.start_button.clicked.connect(self.show_voting_screen)
        self.ui.voteButton.clicked.connect(self.vote)
        self.ui.resultButton.clicked.connect(self.show_results_screen)

        self.show_welcome_screen()

    def setup_welcome_screen(self) -> None:
        """Create and style the welcome screen."""
        self.welcome_screen = QWidget()
        welcome_layout = QVBoxLayout()
        welcome_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        welcome_label = QLabel("Welcome to the Voting App!")
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label.setStyleSheet("font-size: 28px; font-weight: bold; margin-bottom: 20px; color: white;")

        self.start_button = QPushButton("Start Voting")
        self.start_button.setStyleSheet("padding: 12px; font-size: 18px; background-color: #5c6bc0; color: white; border-radius: 8px;")

        welcome_layout.addWidget(welcome_label)
        welcome_layout.addWidget(self.start_button)
        self.welcome_screen.setLayout(welcome_layout)
        self.welcome_screen.setStyleSheet("background-color: #2c2f33;")
        self.stack.addWidget(self.welcome_screen)

    def setup_voting_screen(self) -> None:
        """Setup and style the voting interface."""
        self.ui = Ui_MainWindow()
        self.main_window = QMainWindow()
        self.ui.setupUi(self.main_window)
        self.main_window.setStyleSheet("background-color: #1e1f22;")

        self.ui.johnRadio.setStyleSheet("font-size: 18px; padding: 10px; color: white;")
        self.ui.janeRadio.setStyleSheet("font-size: 18px; padding: 10px; color: white;")
        self.ui.voteButton.setStyleSheet("font-size: 16px; padding: 10px 20px; background-color: #43a047; color: white; border-radius: 8px;")
        self.ui.resultButton.setStyleSheet("font-size: 16px; padding: 10px 20px; background-color: #1e88e5; color: white; border-radius: 8px;")
        self.ui.statusLabel.setStyleSheet("font-size: 14px; margin-top: 10px; color: #eeeeee;")
        self.ui.resultLabel.setStyleSheet("font-size: 14px; margin-top: 10px; color: #eeeeee;")

        self.stack.addWidget(self.main_window)

    def setup_result_screen(self) -> None:
        """Setup and style the results display screen."""
        self.result_screen = QMainWindow()
        self.result_screen.setWindowTitle("Results")
        self.result_screen.setGeometry(100, 100, 400, 200)
        self.result_label = self.ui.resultLabel
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_label.setStyleSheet("font-size: 22px; font-weight: bold; color: white; background-color: #2c2f33;")
        self.result_screen.setCentralWidget(self.result_label)
        self.stack.addWidget(self.result_screen)

    def show_welcome_screen(self) -> None:
        """Display the welcome screen."""
        self.setWindowTitle("Welcome")
        self.stack.setCurrentWidget(self.welcome_screen)

    def show_voting_screen(self) -> None:
        """Display the voting screen."""
        self.setWindowTitle("Vote Now")
        self.stack.setCurrentWidget(self.main_window)

    def vote(self) -> None:
        """Register a vote based on selected radio button and user ID."""
        user_id = self.ui.userIdInput.text().strip()

        if not user_id:
            self.ui.statusLabel.setStyleSheet("color: red;")
            self.ui.statusLabel.setText("Please enter your Voting ID.")
            return

        if self.votes.has_voted(user_id):
            self.ui.statusLabel.setStyleSheet("color: red;")
            self.ui.statusLabel.setText("This user has already voted.")
            return

        candidate = None
        if self.ui.johnRadio.isChecked():
            candidate = "John"
        elif self.ui.janeRadio.isChecked():
            candidate = "Jane"

        if candidate:
            result = self.votes.add_vote(user_id, candidate)
            if result == "success":
                self.ui.statusLabel.setStyleSheet("color: lightgreen;")
                self.ui.statusLabel.setText(f"You voted for {candidate}!")
            else:
                self.ui.statusLabel.setStyleSheet("color: red;")
                self.ui.statusLabel.setText("Voting error.")
        else:
            self.ui.statusLabel.setStyleSheet("color: red;")
            self.ui.statusLabel.setText("Please select a candidate.")

    def show_results_screen(self) -> None:
        """Display the vote counts."""
        try:
            result = self.votes.get_results()
            self.result_label.setText(f"John: {result['John']} | Jane: {result['Jane']}")
            self.stack.setCurrentWidget(self.result_screen)
        except Exception as e:
            print("Error loading results:", e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VoteApp()
    window.show()
    sys.exit(app.exec())
