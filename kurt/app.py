from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Anket seçenekleri ve sonuçları
poll_data = {
    'question': 'En sevdiğiniz programlama dili nedir?',
    'fields': ['Python', 'JavaScript', 'Java', 'C#', 'C++'],
    'votes': [0, 0, 0, 0, 0]
}

@app.route('/deneme')
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
