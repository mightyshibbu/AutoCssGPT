# AutoCSS-GPT 🎨✨

AutoCSS-GPT is a Django web application that generates CSS and HTML code from user prompts, empowering developers and designers to create stunning designs quickly and efficiently. 🚀

---

## Features 🌟

- **Interactive UI**: Enter your prompt and instantly generate code.
- **Output Configurations**: Choose your desired format: CSS, SCSS, or LESS.
- **Responsive Design**: Works seamlessly across all screen sizes.
- **Spinner Feedback**: Displays a loading spinner while generating code.
- **Typewriter Effect**: Engaging placeholder animation for user input.

---

## Installation 🛠️

Follow these steps to set up the project locally:

### Prerequisites 📋
- Python 3.8+
- Django 4.0+
- Node.js (optional, for frontend bundling if required)

### Steps 🚶‍♂️

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/autocss-gpt.git
   cd autocss-gpt
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Open the application in your browser**:
   Visit `http://127.0.0.1:8000/` 🌐

---

## Usage 📖

1. Enter your design prompt in the input box.
2. Choose the output type (CSS, SCSS, or LESS) from the configuration panel.
3. Click the "Submit" button to generate the code.
4. View the generated code in the output section.
5. Copy and paste the generated code into your project. ✂️

---

## Project Structure 🏗️

```plaintext
├── autocss_gpt/
│   ├── settings.py      # Django settings
│   ├── urls.py          # URL routing
│   ├── models.py        # Database models
│   ├── views.py         # Request handling
├── templates/
│   └── index.html       # Main HTML template
├── static/
│   ├── css/             # Static CSS files
│   ├── js/              # Static JavaScript files
└── manage.py            # Django management script
```

---

## Contributing 🤝

Contributions are welcome! 🎉 To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## Acknowledgments 🙌

- [OpenAI](https://openai.com) for inspiring the AI-driven approach.
- [Django](https://www.djangoproject.com/) for being an awesome web framework.
- You, for using AutoCSS-GPT! ❤️

---

## Screenshots 📸

### Home Page 🏠


---

## Contact 📬

- pranav8tripathi@gmail.com

For any questions or feedback, feel free to reach out:
- **Email**: your-email@example.com
- **GitHub**: [@your-username](https://github.com/your-username)

Enjoy coding with AutoCSS-GPT! 🎉
