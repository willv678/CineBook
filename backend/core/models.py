from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=100)
    # You can add more fields here if needed, like date_of_birth, etc.

    def __str__(self):
        return self.name

class Movie(models.Model):
    CATEGORY_CHOICES = [
        ('ACTION', 'Action'),
        ('COMEDY', 'Comedy'),
        ('DRAMA', 'Drama'),
        ('HORROR', 'Horror'),
        ('SCIFI', 'Sci-Fi'),
        ('THRILLER', 'Thriller'),
        ('ROMANCE', 'Romance'),
        ('DOCUMENTARY', 'Documentary'),
        ('ANIMATION', 'Animation'),
        ('FANTASY', 'Fantasy'),
        ('MYSTERY', 'Mystery'),
        ('ADVENTURE', 'Adventure'),
        ('CRIME', 'Crime'),
        ('BIOGRAPHY', 'Biography'),
        ('HISTORY', 'History'),
        ('MUSICAL', 'Musical'),
        ('WAR', 'War'),
        ('WESTERN', 'Western'),
        ('SPORTS', 'Sports'),
        ('FAMILY', 'Family'),
        ('OTHER', 'Other'),
    ]

    RATING_CHOICES = [
        ('G', 'G'),
        ('PG', 'PG'),
        ('PG-13', 'PG-13'),
        ('R', 'R'),
        ('NC-17', 'NC-17'),
        ('UNRATED', 'Unrated'),
        ('NOT_RATED', 'Not Rated'),
    ]

    title = models.CharField(max_length=200)
    synopsis = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='ACTION')
    director = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    cast = models.ManyToManyField(Actor) # Use a Many-to-Many field for a list of actors
    trailer_url = models.URLField(max_length=200, blank=True)
    trailer_pic_link = models.URLField(max_length=200, blank=True)
    rating = models.CharField(max_length=10, choices=RATING_CHOICES, default='G')
    is_running = models.BooleanField(default=False)
    is_coming_soon = models.BooleanField(default=False)
    poster_image_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='showtimes')
    date = models.DateField()
    time = models.TimeField()
    # You can add hall and seat information later.

    def __str__(self):
        return f"{self.movie.title} on {self.date} at {self.time}"