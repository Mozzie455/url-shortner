from flask import Flask, request, redirect
import random

app = Flask(__name__)

next_url_path = 0
url_mapping = {}

letters = 'abcdefghijklmnopqrstuvwxyz'
shortened_length = 8

@app.post('/shorten')
def create_new_short_url():
    long_url = request.json['url']
    short_url = ''
    
    for i in range(shortened_length):
        short_url += random.choice(letters)
    
    if short_url not in url_mapping:
        url_mapping[short_url] = long_url
        return short_url
    else:
        return 'Oh no!'


@app.get('/s/</id>')
def redirect_to_url(id):
    long_url = url_mapping.get(f'/s/{id}')

    if long_url:
        return redirect(long_url)
    else:
        return f'Not Found'

if __name__ == '__main__':
    app.run(debug=True)