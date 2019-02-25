import json
import psycopg2
import time

conn = psycopg2.connect(host="localhost",database="testdb", user="david", password="1234")

cursor = conn.cursor()

with open('/home/david/Stažené/json_ratings.json') as f:
    json_file = json.load(f)

ratings = {}

#print(json_file['ratings'][0])

for _, element in enumerate(json_file['ratings']):
    key = element['country']
    value = element['all_ratings']

    ratings[key] = {key: value[key] for key in value.keys() if key not in 'average'}

    #ratings[element['country']] = element['all_ratings']

#print(ratings.items())

for key, value in ratings.items():
    query = "INSERT INTO ratings (country, one_stats_ratings, five_stats_ratings, ratings_count, two_stats_ratings, four_stats_ratings, three_stats_ratings, created_at, updated_at, date) VALUES ( s%, %d, %d, %d, %d, %d, %f, %f, %f);"
    data = (key, [value[key] for key in value.keys()], time.time(), time.time(), time.time())

    cursor.execute(query, data)
    conn.commit()