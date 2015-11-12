import random
from exercise.models import ExerciseCategory, Exercise
from workout.models import Set


def generate_series(n=None, series=30, set_target=10, ex_diff=2):
    """Method to take a target difficulty, and generate a suitable series of
    exercise sets. Returns a list of Set objects.
    """
    # If n (number of sets) is None:
    # Divide series by set_target, result is the number of sets (rounded).
    # Construct sets using exercises of difficulty ex_diff or ex_diff+1, to be
    # within 10% of set_target.
    # If set reps > 8, increase exercise difficulty by 1 and recalculate.
    # Choose each set exercise from a different category.
    if not n:
        n = int(round((series / set_target)))
    categories = random.sample([c for c in ExerciseCategory.objects.all()], n)
    sets = []
    for c in categories:
        exercises = list(Exercise.objects.filter(
            categories__in=[c],
            difficulty__in=[ex_diff-1, ex_diff, ex_diff+1]))
        # FIXME: handle if no Exercise objects are returned.
        exercise = random.choice(exercises)
        # Handle repeated/isometric exercises.
        if exercise.isometric:
            s = int(round((set_target * 3) / exercise.difficulty))
            new_set = Set.objects.get_or_create(exercise=exercise, seconds=s)[0]
        else:
            reps = int(round(set_target / exercise.difficulty))
            new_set = Set.objects.get_or_create(exercise=exercise, reps=reps)[0]
        sets.append(new_set)

    return sets
