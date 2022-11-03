


from flask import Flask, request,jsonify
app = Flask(__name__)
movies = [
    {
        'name':'action',
        'details':[
            {
                'name': 'Batman',
                'imdb': 8.3,
                'date': 2015
            },
            {
                'name': 'Godzilla',
                'imbd': 8.5,
                'date': 2014
            }
        ]  
    },
    {
        'name': 'anime',
        'details':[
            {
                'name': 'Haikyuu',
                'imbd': 8.8,
                'date': 2014
            },
            {
                'name': 'Free',
                'imbd': 8.2,
                'date': 2019
            }
        ]
        
    }
    ]

@app.route('/')
def home():
    return "Hello to Api"


@app.route('/movie', methods=['POST'])
def create_movie():
    request_data = request.get_json()
    new_movie = {
        'name': request_data['name'],
        'details': []
    }
    movies.append(new_movie)
    return jsonify(new_movie)


@app.route('/movie/<string:name>')
def get_movie_name(name):
    for movie in movies:
        if(movie['name'] == name):
            return jsonify(movie)
    return jsonify({'message': 'movie not found'})


@app.route('/movie')
def get_all_movie_name():
    return jsonify({'movies': movies})


@app.route('/movie/<string:name>/detail', methods=['POST'])
def create_movie_detail(name):
    request_data = request.get_json()
    for movie in movies:
        if(movie['name'] == name):
            new_detail = {
                'name': request_data['name'],
                'imbd': request_data['imbd'],
                'date': request_data['date']
            }
            movie['details'].append(new_detail)
            return jsonify(new_detail)
    return jsonify({'message':'movie not found'})


@app.route('/movie/<string:name>/detail')
def get_movie_detail(name):
    for movie in movies:
        if(movie['name'] == name):
            return jsonify(movie['details'])
    return jsonify({'message': 'movie not found'})

@app.route('/movie/<string:name>', methods=["DELETE"])
def delete(name):
        for movie in movies:
            if (movie['name'] == name):
                movies.remove(movie)
        return jsonify({'mesage': 'movie is deleted'})      
app.run(port=5000)
    
