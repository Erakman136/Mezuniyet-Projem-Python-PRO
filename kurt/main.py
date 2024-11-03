from flask import Flask, render_template, request, jsonify, redirect, url_for
import random

app = Flask(__name__)

seviyeler = {
    "kolay": ["dairy", "mouse", "computer", "hello", "mask"],
    "orta": ["programming", "algorithm", "developer"],
    "zor": ["neural network", "machine learning", "artificial intelligence"]
}

# Anket seçenekleri ve sonuçları
poll_data = {
    'question': 'En sevdiğiniz programlama dili nedir?',
    'fields': ['Python', 'JavaScript', 'Java', 'C#', 'C++'],
    'votes': [0, 0, 0, 0, 0]
}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        button_python = request.form.get('button_python')
        button_discord = request.form.get('button_discord')
        button_html = request.form.get('button_html')
        button_db = request.form.get('button_db')
        button_kurt = request.form.get('button_kurt')
        button_extra = request.form.get('button_extra')
        button_new_project = request.form.get('button_new_project')
        button_mleh = request.form.get('button_mleh')
        button_dene = request.form.get('button_dene')

        email = request.form.get('email')
        text = request.form.get('text')

        if email and text:
            with open('form.txt', 'a') as f:
                f.write(f'Email: {email}\nComment: {text}\n\n')

        return render_template('ana.html',
                               button_python=button_python,
                               button_discord=button_discord,
                               button_html=button_html,
                               button_db=button_db,
                               button_kurt=button_kurt,
                               button_extra=button_extra,
                               button_new_project=button_new_project,
                               button_mleh=button_mleh,
                               button_dene = button_dene)
    else:
        return render_template('ana.html')

@app.route('/kronometre')
def kronometre():
    return render_template('kronometre.html')


@app.route('/sendfeedback', methods=['POST'])
def feedback():
    email = request.form.get("email")
    mesaj = request.form.get("text")
    with open("form.txt", "a", encoding="utf-8") as file:
        file.write(f"email = {email}\n")
        file.write(f"mesaj = {mesaj}\n")
    return render_template('feedback.html')


@app.route('/hesap')
def hesap():
    return render_template('hesap.html')

# Oyun rotası
@app.route('/pronunciation_game', methods=['GET', 'POST'])
def pronunciation_game():
    if request.method == 'POST':
        level = request.form.get('level')
        if level in seviyeler:
            selected_words = random.sample(seviyeler[level], 3)  # 3 kelime seçiyoruz
            return jsonify({'words': selected_words})
        return jsonify({'error': 'Geçersiz seviye'})
    else:
        return render_template('pronunciation_game.html')

# Anket rotası
@app.route('/anket')
def index():
    return render_template('deneme.html', data=poll_data)

@app.route('/vote', methods=['POST'])
def vote():
    selected_option = request.form.get('language')
    if selected_option is not None:
        poll_data['votes'][int(selected_option)] += 1
    return redirect(url_for('results'))

@app.route('/results')
def results():
    # `fields` ve `votes` listelerini birleştirerek `field_votes` oluştur
    field_votes = list(zip(poll_data['fields'], poll_data['votes']))
    return render_template('results.html', field_votes=field_votes)

if __name__ == '__main__':
    app.run(debug=True)
