from django.db import models

class Books(models.Model):
    GENRE = (
        ('Фантастика', 'Фантастика'),
        ('Детектив', 'Детектив'),
        ('Роман', 'Роман'),
    )
    image = models.ImageField(upload_to='books/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=10, choices=GENRE)
    mail = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    wikipedia_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Reviews(models.Model):
    GRADE = (
        ('⭐','⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),

    )

    choice_book = models.ForeignKey(Books, on_delete=models.CASCADE,
                                    related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True,blank=True)
    grade = models.CharField(max_length=10, choices=GRADE, default='⭐')

    def __str__(self):
        return f'{self.choice_book.title} - {self.grade}'
