# Recipe Finder 🍴

**Recipe Finder** is a web application that allows users to generate creative recipes by entering a list of ingredients. It utilizes AI to craft personalized recipes and provides a user-friendly interface for a seamless experience.

---

## 📂 Project Structure

Recipe-Finder/
├── Frontend/
│   ├── index.html        # Main HTML file for the UI
│   ├── style.css         # CSS for styling the frontend
│   └── script.js         # JavaScript for handling user interaction
├── Backend/
│   └── main.py           # FastAPI backend for recipe generation
└── requirements.txt      # Python dependencies


---

## 🌟 Features

- *Interactive Frontend*: A clean and intuitive UI for entering ingredients.
- *AI-Powered Recipe Generation*: Generates creative and unique recipes based on user-provided ingredients.
- *Responsive Design*: Optimized for both mobile and desktop devices.
- *Backend-Frontend Integration*: Connected via REST API for smooth functionality.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Node.js (optional, for frontend testing)
- A valid API key for Google Generative AI (configured in .env)

### Installation

1. Clone the repository:
   bash
   git clone https://github.com/Shreyaax/Recipe-Finder.git
   cd Recipe-Finder
   

2. Navigate to the Backend directory and install dependencies:
   bash
   pip install -r requirements.txt
   

3. Create a .env file in the Backend directory and add your API key:
   
   API_KEY=your-google-generative-ai-api-key
   

4. Run the backend server:
   bash
   uvicorn Backend.main:app --reload
   

5. Open the index.html file in your browser to test the frontend.

---

## 🛠 Usage

1. Open the web app in your browser.
2. Enter ingredients in the input box provided.
3. Click *Find Recipe* to generate a recipe.
4. View your personalized recipe below the input area and try it out in your kitchen!

---

## 🎨 Technologies Used

### Frontend
- *HTML5*: For the structural layout of the app.
- *CSS3*: For styling and enhancing the UI.
- *JavaScript*: For interactivity and dynamic features.

### Backend
- *FastAPI*: For building the REST API.
- *Google Generative AI*: For generating recipes from user inputs.
- *Python-dotenv*: For managing environment variables securely.

---

## 🐞 Debugging & Logs

- Check backend logs to troubleshoot API requests and responses.
- Use browser developer tools (e.g., Chrome DevTools) to debug frontend issues.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and share it.

---

## 🤝 Contributions

We welcome contributions! Here’s how you can help:

1. Fork the repository.
2. Create a new branch (feature/your-feature).
3. Commit your changes with clear descriptions.
4. Push your branch to the repository.
5. Submit a pull request for review.

---

## 💌 Acknowledgments

- Special thanks to food lovers and creators who inspired this project.
- Built with ❤ by *Shreyaax*.

---

## ✨ Future Enhancements

- Add support for generating multiple recipe suggestions.
- Enhance UI with animations, transitions, and themes.
- Integrate a database for saving and sharing user-generated recipes.
- Add user authentication for personalized recipe history.
