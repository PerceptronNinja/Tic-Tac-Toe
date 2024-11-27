# Tic-Tac-Toe Web Application

A simple and interactive Tic-Tac-Toe game built using **Python (Flask)** for the backend and **HTML/CSS** for the frontend. This web-based game allows two players to compete in a game of Tic-Tac-Toe with a clean, user-friendly interface.

### **Features**
- **Landing Page**: Players can input their names and start the game.
- **Game Board**: A 3x3 grid where players take turns (X and O) to mark their spots.
- **Score Tracking**: Tracks the score for Player 1 and Player 2.
- **Turn Indicator**: Shows whose turn it is (Player 1 or Player 2).
- **Match Result**: Displays the winner or "Match Draw" message at the end of each game.
- **Game Options**:
  - **Play Again**: Starts a new round of the current game while keeping the scores.
  - **New Game**: Resets the game completely and takes players back to the landing page.

### **Technologies Used**
- **Python** (Flask framework) for backend logic and routing.
- **HTML5** for the webpage structure.
- **CSS3** for styling the user interface.
- **JavaScript** (optional, for enhanced interactivity).

---

## **Installation Guide**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/tic-tac-toe.git
   cd tic-tac-toe
   ```

2. **Install Python dependencies**:
   You need to have Python installed. If you haven't installed it yet, download and install from [here](https://www.python.org/downloads/).

   Install required packages using pip:
   ```bash
   pip install Flask
   ```

3. **Run the Flask application**:
   ```bash
   python app.py
   ```

4. **Access the game**:
   Open your web browser and navigate to `http://127.0.0.1:5000/` to start playing the game.

---

## **How to Play**

1. Enter **Player 1** and **Player 2** names on the landing page and click **Start Game**.
2. Players take turns to click on the 3x3 grid to place their symbol (X or O).
3. The game will notify if a player wins or if the game ends in a draw.
4. After the game ends:
   - Click **Play Again** to start a new round.
   - Click **New Game** to reset everything and go back to the landing page.

---

## **Game Rules**
- The board consists of 9 cells, arranged in a 3x3 grid.
- Player 1 is represented by **X** and Player 2 by **O**.
- Players take turns placing their marks on the board.
- The game ends when one player has three of their marks in a row (horizontally, vertically, or diagonally) or when all cells are filled with no winner (draw).
- The score is displayed at the bottom of the page.

---

## **Project Structure**
```
tic-tac-toe/
│
├── app.py               
├── templates/           
│   ├── index.html       
│   ├── game.html        
│   └── result.html      
├── static/              
│   └── style.css        
├── README.md            
└── requirements.txt     
```

---

## **Contributing**

1. Fork the repository.
2. Clone the forked repository to your local machine.
3. Create a new branch.
4. Implement your changes or new features.
5. Commit your changes.
6. Push the changes to your forked repository.
7. Submit a Pull Request.

---

## **Screenshots**
<img width="793" alt="Screenshot 2024-11-27 at 7 57 23 PM" src="https://github.com/user-attachments/assets/048fc8cf-b2bc-4df4-949f-3b76c3fc11d4">
<img width="689" alt="Screenshot 2024-11-27 at 7 58 18 PM" src="https://github.com/user-attachments/assets/7d2dd5b9-3706-46fe-9a86-65cdfcd03b9e">



---

## **License**

This project is open-source and available under the [MIT License](LICENSE).

---

### **Acknowledgments**
- [Flask Documentation](https://flask.palletsprojects.com/) for building the web application.
- [W3Schools](https://www.w3schools.com/) for providing resources on HTML/CSS.
