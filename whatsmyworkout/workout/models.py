from allauth.account.models import EmailAddress
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
    workout_target = models.PositiveIntegerField(default=135)
    set_target = models.PositiveIntegerField(default=15)
    exercise_target = models.PositiveIntegerField(default=3)
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

    def generate_workout(self):
        """Method to take a user's target workout difficulty, and generate a
        suitable series of exercises for the user.
        """
        # TODO: stub
        # Divide workout_target by 5, then divide this by exercise_target.
        # This is the number of exercises in the workout (min 2).
        # Fill exercises: core, arm/legs, arm/legs/core, repeat.
        # Divide exercise_target by 5. This is the target exercise difficulty.
        # Select from exercises +/-1 from that number.
        # For each exercise, divide exercise_target by its difficult and round off.
        # This is the number of reps for that exercise.
        pass


@python_2_unicode_compatible
class Workout(models.Model):
    """A collection of exercise activities, delivered to a WorkoutUser.
    Has a target and calculated difficulty. Should record any feedback by the
    user.
    """
    FEEDBACK_CHOICES = (
        (0, _('Easy')),
        (1, _('Okay')),
        (2, _('Hard')),
    )
    user = models.ForeignKey(WorkoutUser)
    sets = models.PositiveIntegerField()
    target_difficulty = models.PositiveIntegerField()
    generated = models.DateTimeField()
    delivered = models.DateTimeField(null=True)
    feedback = models.PositiveSmallIntegerField(
        null=True, choices=FEEDBACK_CHOICES)

    def __str__(self):
        return '{}:{}'.format(self.user, self.target_difficulty)


@python_2_unicode_compatible
class Activity(models.Model):
    """A single activity, part of a single Workout.
    Acts as a link field between Workout and Exercise, records reps.
    """
    workout = models.ForeignKey(Workout)
    exercise = models.ForeignKey(Exercise)
    reps = models.PositiveIntegerField()

    def __str__(self):
        return '{} x {}'.format(self.exercise, self.reps)
