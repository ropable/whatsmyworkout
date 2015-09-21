from allauth.account.models import EmailAddress
from datetime import datetime
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from exercise.models import Exercise


class UserManager(BaseUserManager):
    """A custom Manager for the WorkoutUser model.
    """
    use_in_migrations = True

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        """Creates and saves a WorkoutUser with the given email and password.
        """
        if not email:
            raise ValueError('The email must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email, is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


@python_2_unicode_compatible
class WorkoutUser(AbstractBaseUser, PermissionsMixin):
    """Custom authentication model for the whatsmyworkout project.
    Password and email are required. Other fields are optional.
    """
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=64, blank=True)
    last_name = models.CharField(_('last name'), max_length=64, blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into the admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    series_target = models.PositiveIntegerField(
        default=30,
        help_text='Represents the target difficult for a workout series')
    set_target = models.PositiveIntegerField(
        default=10,
        help_text='Represents the target difficulty of a single set')
    exercise_target = models.PositiveIntegerField(
        default=2,
        help_text='Represents the typical difficulty of exercise assigned')
    # TODO: save user timezone

    objects = UserManager()
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('workout user')
        verbose_name_plural = _('workout users')

    def __str__(self):
        return self.email

    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Sends an email to this WorkoutUser.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_workout(self):
        from workout.utils import generate_series
        series = generate_series(
            self.series_target, self.set_target, self.exercise_target)

        workout = Workout(
            user=self, repeats=3, target_difficulty=self.workout_target,
            generated=datetime.now())
        workout.save()

        for s in series:
            workout.sets.add(s)

        return workout


@python_2_unicode_compatible
class Set(models.Model):
    """A single exercise set, records reps.
    Set difficulty is exercise difficult * reps or (seconds/6).
    # TODO: clean method: reps or seconds, not both.
    # TODO: seconds can only be set for an isometric exercise.
    """
    exercise = models.ForeignKey(Exercise)
    reps = models.PositiveIntegerField(
        null=True, blank=True, help_text='Reps for repeating movements')
    seconds = models.PositiveIntegerField(
        null=True, blank=True, help_text='Seconds to hold isometric movement')

    class Meta:
        unique_together = (('exercise', 'reps'), ('exercise', 'seconds'))

    def __str__(self):
        if self.reps:
            return '{} x {}'.format(self.exercise, self.reps)
        else:
            return '{} x {}s'.format(self.exercise, self.seconds)


@python_2_unicode_compatible
class Workout(models.Model):
    """A collection of exercise sets, delivered to a WorkoutUser.
    Target difficulty is sum of all set difficulties, times repeats.
    Has a target and calculated difficulty. Should record any feedback by the
    user.
    """
    FEEDBACK_CHOICES = (
        (0, _('Easy')),
        (1, _('Okay')),
        (2, _('Hard')),
    )
    user = models.ForeignKey(WorkoutUser)
    sets = models.ManyToManyField(Set)
    repeats = models.PositiveIntegerField()
    target_difficulty = models.PositiveIntegerField()
    generated = models.DateTimeField()
    delivered = models.DateTimeField(null=True)
    feedback = models.PositiveSmallIntegerField(
        null=True, choices=FEEDBACK_CHOICES)

    def __str__(self):
        return '{} ({})'.format(self.user, self.target_difficulty)
