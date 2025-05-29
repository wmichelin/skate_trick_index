# Skate Trick Index

A Django web application for tracking and learning skateboard tricks. This platform helps skateboarders of all levels track their progress, learn new tricks, and organize their skateboarding journey.

## Features

- 📝 Comprehensive trick database with categories and difficulty levels
- 🎯 Progress tracking for individual users
- 📊 Filter tricks by category and difficulty
- 🎥 Support for trick images and video tutorials
- 📱 Responsive design for mobile and desktop
- 🔒 User authentication and progress tracking

## Tech Stack

- Python 3.11+
- Django 4.2+
- Bootstrap 5
- SQLite (development) / PostgreSQL (production ready)
- Crispy Forms for better form rendering

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/skate_trick_index.git
cd skate_trick_index
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit http://127.0.0.1:8000/ to see the application

## Project Structure

```
skate_trick_index/
├── skate_trick_index/          # Main application directory
│   ├── migrations/            # Database migrations
│   ├── templates/            # HTML templates
│   ├── models.py            # Database models
│   ├── views.py             # View logic
│   └── urls.py              # URL routing
├── media/                    # User-uploaded files
├── static/                   # Static files
├── manage.py                # Django management script
└── requirements.txt         # Project dependencies
```

## Models

- **TrickCategory**: Categories for organizing tricks (e.g., Flip Tricks, Grinds, Grabs)
- **SkateTrick**: Individual tricks with details like difficulty, description, and media
- **UserProgress**: Tracks user progress on individual tricks

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the skateboarding community for inspiration
- Django documentation for excellent framework documentation
- Bootstrap team for the responsive design framework

Project Link: [https://github.com/yourusername/skate_trick_index](https://github.com/yourusername/skate_trick_index) 