# Django for Professionals - Code Examples

This repository contains the code examples and project implementations from the book **"Django for Professionals"** by William S. Vincent. The book provides a comprehensive guide to building production-ready Django web applications with modern best practices.

## About

This repo follows along with the Django for Professionals book, implementing each chapter's examples and demonstrating professional Django development techniques including:

- Docker-based development workflow
- PostgreSQL database configuration
- Custom user models
- Advanced user authentication
- Environment-based configuration
- Static and media file handling
- Production deployment strategies

**Book Information:**

- Title: Django for Professionals
- Author: William S. Vincent
- Website: https://djangoforprofessionals.com/

## Repository Structure

This repository is organized by chapter, with each major example or project contained in its own directory following the book's progression.

## Prerequisites

- Python 3.10+
- Docker and Docker Compose
- Git
- Basic understanding of Django and Python

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/MinatoNami/django-for-professionals.git
cd django-for-professionals
```

### Docker-Based Development

The book emphasizes Docker for consistent development environments:

```bash
# Build the Docker image
docker-compose up -d --build

# Run migrations
docker-compose exec web python manage.py migrate

# Create a superuser
docker-compose exec web python manage.py createsuperuser

# Access the application
# Navigate to http://localhost:8000
```

### Local Development (Without Docker)

If you prefer to run without Docker:

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

## Key Topics Covered

Based on the book's curriculum, this repository demonstrates:

1. **Docker Setup** - Containerized development environment
2. **PostgreSQL** - Production-grade database configuration
3. **Custom User Model** - Best practice user authentication
4. **User Authentication** - Login, logout, signup flows
5. **Bootstrap Styling** - Professional UI/UX
6. **Password Management** - Reset and change functionality
7. **Email Configuration** - Production email setup
8. **Static Assets** - WhiteNoise and production static files
9. **Advanced User Registration** - Email confirmation workflows
10. **Environment Variables** - Secure configuration management
11. **Testing** - Comprehensive test coverage
12. **Performance** - Optimization and security hardening
13. **Deployment** - Production deployment strategies

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=postgres://user:password@db:5432/dbname
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Database

The project uses PostgreSQL by default (configured via Docker Compose). Update `docker-compose.yml` or your `.env` file to configure database credentials.

## Running Tests

```bash
# With Docker
docker-compose exec web python manage.py test

# Without Docker
python manage.py test
```

## Production Deployment

The book covers deployment to various platforms. Key production considerations:

- Set `DEBUG=False`
- Configure `ALLOWED_HOSTS` properly
- Use environment variables for secrets
- Set up proper database backups
- Configure email backend
- Use HTTPS/SSL certificates
- Run `collectstatic` for static files
- Use a production WSGI server (Gunicorn)

## Learning Resources

- **Book Website**: https://djangoforprofessionals.com/
- **Django Documentation**: https://docs.djangoproject.com/
- **Docker Documentation**: https://docs.docker.com/

## Notes for Learners

This repository is intended as a learning resource and reference implementation. Each commit and branch may correspond to different chapters or sections of the book. Feel free to:

- Explore the code
- Experiment with modifications
- Use as a template for your own projects
- Reference when following along with the book

## Support

For book-related questions and errata:

- Visit the official book website
- Check the Django for Professionals community resources

For issues with this repository:

- Open an issue on GitHub
- Provide details about your environment and the problem

## License

The code in this repository follows the examples from Django for Professionals. Please respect the book's copyright and use this code for educational purposes.

## Acknowledgments

- **William S. Vincent** - Author of Django for Professionals
- The Django community for excellent documentation and support

## Disclaimer

This repository contains code examples for educational purposes following the Django for Professionals book. Please purchase the book to support the author and get the full learning experience with detailed explanations, context, and best practices.

---

**Happy Learning!** 🚀

_This repository is maintained by [@MinatoNami](https://github.com/MinatoNami)_
