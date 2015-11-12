from django.http import JsonResponse
from django.views.generic import View, TemplateView
from workout.utils import generate_series


class WorkoutPage(TemplateView):
    """View to render a generated workout.
    """
    template_name = 'workout/workout.html'


class WorkoutJson(View):
    """Basic view to accept a GET request and return a workout as JSON.
    """
    http_method_names = [u'get', u'options']

    def get(self, request, *args, **kwargs):
        """Handles GET requests, returns a JSON response.
        """
        data = request.GET.dict()
        if data.get('preset', None) == 'easy':
            print('EASY')
            data['sets'] = 3
            data['exercise_difficulty'] = 2
        elif data.get('preset', None) == 'medium':
            print('MEDIUM')
            data['sets'] = 4
            data['exercise_difficulty'] = 4
        elif data.get('preset', None) == 'advanced':
            print('ADVANCED')
            data['sets'] = 5
            data['exercise_difficulty'] = 6
        else:
            print('CUSTOM')
            data['preset'] = 'custom'
            if 'sets' not in data:
                data['sets'] = 3

        series = generate_series(
            n=data['sets'], ex_diff=data['exercise_difficulty'])
        print(series)

        return JsonResponse(data)
