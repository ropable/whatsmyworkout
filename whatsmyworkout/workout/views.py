from django.views.generic import TemplateView


class WorkoutPage(TemplateView):
    """Page to return a random workout, and accept requests for a harder/easier one.
    May also serve as an API endpoint.
    """
    template_name = 'workout/workout.html'
