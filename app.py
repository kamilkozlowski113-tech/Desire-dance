from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Prowizoryczna baza danych w pamięci (na start; docelowo można podpiąć SQLite/PostgreSQL)
profiles = [
    {"id": 1, "name": "Kasia", "age": 32, "style": "Bachata", "day": "Czwartek", "level": "Początkujący", "role": "Follower", "phone": "+48 123 456 789"},
    {"id": 2, "name": "Michał", "age": 35, "style": "Bachata", "day": "Czwartek", "level": "Początkujący", "role": "Leader", "phone": "+48 987 654 321"}
]

@app.route('/')
def index():
    # Pobieranie filtrów z formularza
    selected_style = request.args.get('style', '')
    selected_day = request.args.get('day', '')
    
    filtered_profiles = profiles
    if selected_style:
        filtered_profiles = [p for p in filtered_profiles if p['style'] == selected_style]
    if selected_day:
        filtered_profiles = [p for p in filtered_profiles if p['day'] == selected_day]
        
    return render_template('index.html', profiles=filtered_profiles, selected_style=selected_style, selected_day=selected_day)

@app.route('/add', methods=['POST'])
def add_profile():
    new_profile = {
        "id": len(profiles) + 1,
        "name": request.form.get('name'),
        "age": int(request.form.get('age', 0)),
        "style": request.form.get('style'),
        "day": request.form.get('day'),
        "level": request.form.get('level'),
        "role": request.form.get('role'),
        "phone": request.form.get('phone')
    }
    profiles.append(new_profile)
    return redirect(url_for('index'))

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 10000))
  app.run(host='0.0.0.0', port=port)