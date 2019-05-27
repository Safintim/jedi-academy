from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, name, planet, age, pass_test=False, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            age=age,
            planet=planet,
            pass_test=pass_test
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, planet, age, password):
        user = self.create_user(
            email=email,
            name=name,
            age=age,
            planet=Planet(planet),
            pass_test=False,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Planet(models.Model):
    name = models.CharField(max_length=30, db_index=True,)

    def __str__(self):
        return self.name


class Candidate(AbstractBaseUser):
    name = models.CharField(max_length=150, unique=False)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    pass_test = models.BooleanField(default=False)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'age', 'planet']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Jedi(models.Model):
    name = models.CharField(max_length=150)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Padawan(models.Model):
    jedi_id = models.ForeignKey(Jedi, on_delete=models.CASCADE)
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'jedi: {self.jedi_id}, candidate: {self.candidate_id}'


class Test(models.Model):
    title = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.title


class ListQuestions(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    number = models.IntegerField()
    question = models.CharField(max_length=300, db_index=True)
    metadata = models.CharField(max_length=150, db_index=True, blank=True)

    def __str__(self):
        return self.question


class Answer(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    question = models.ForeignKey(ListQuestions, on_delete=models.CASCADE)
    text_answer = models.CharField(max_length=150)
    date_answer = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text_answer
