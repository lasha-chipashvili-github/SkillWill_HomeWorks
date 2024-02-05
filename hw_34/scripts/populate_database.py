import json

from recipe.models import Recipe

# python3 manage.py runscript populate_database
def run():

    file = "/home/hattori/Desktop/sweeft/skillwill/skillwill_api1/scripts/mock_data.json"
    mock_data = open(file)
    data = json.load(mock_data)['data']
    for recipe in data:
        Recipe.objects.create(**recipe)


