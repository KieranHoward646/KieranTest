# Ghost Castle 幽灵城堡

A Shakespearean tragedy website with bilingual support (Chinese & English).

## Features

- 📖 Five-act tragedy play
- 🌍 Bilingual support (中文 & English)
- 📱 Responsive design
- 🎨 Dark theme with elegant styling

## Tech Stack

- Backend: Flask (Python)
- Frontend: HTML5 + CSS3
- Deployment: Render

## Local Development

1. Clone or download the project
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Visit `http://localhost:5001`

## Deploy to Render

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed deployment instructions.

## Project Structure

```
new_made/
├── app.py              # Flask application
├── play_content.py     # Play data (bilingual)
├── requirements.txt    # Python dependencies
├── Procfile           # Render deployment config
├── static/
│   └── style.css      # Styling
└── templates/
    ├── base.html      # Base template
    ├── home.html      # Homepage
    ├── act.html       # Act pages
    └── characters.html # Characters page
```
