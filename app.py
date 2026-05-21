from flask import Flask, render_template, jsonify, request, session
from play_content import PLAY_INFO, CHARACTERS, NAV_TEXT, ALL_ACTS

app = Flask(__name__)
app.secret_key = 'ghost-castle-secret-key-2024'

# 缓存数据，避免每次请求重新导入
CACHED_DATA = {
    'play_info': PLAY_INFO,
    'characters': CHARACTERS,
    'nav_text': NAV_TEXT,
    'all_acts': ALL_ACTS,
    'act_count': len(ALL_ACTS)
}

@app.route('/')
def home():
    lang = session.get('lang', 'zh')
    play_info = CACHED_DATA['play_info'][lang]
    return render_template('home.html',
                         play_info=play_info,
                         nav_text=CACHED_DATA['nav_text'][lang],
                         acts=CACHED_DATA['all_acts'],
                         lang=lang)

@app.route('/characters')
def characters():
    lang = session.get('lang', 'zh')
    play_info = CACHED_DATA['play_info'][lang]
    return render_template('characters.html',
                         play_info=play_info,
                         nav_text=CACHED_DATA['nav_text'][lang],
                         characters=CACHED_DATA['characters'][lang],
                         lang=lang)

@app.route('/act/<int:act_num>')
def act(act_num):
    lang = session.get('lang', 'zh')
    if 1 <= act_num <= CACHED_DATA['act_count']:
        act_data = CACHED_DATA['all_acts'][act_num - 1]
        play_info = CACHED_DATA['play_info'][lang]
        return render_template('act.html',
                             play_info=play_info,
                             nav_text=CACHED_DATA['nav_text'][lang],
                             act=act_data,
                             act_num=act_num,
                             total_acts=CACHED_DATA['act_count'],
                             lang=lang)
    return "Act not found", 404

@app.route('/api/set-language', methods=['POST'])
def set_language():
    try:
        data = request.get_json(force=True)
        lang = data.get('lang', 'zh')
        if lang in ['zh', 'en']:
            session['lang'] = lang
            return jsonify({'success': True, 'lang': lang})
        return jsonify({'success': False}), 400
    except Exception:
        return jsonify({'success': False}), 400

@app.route('/api/get-language')
def get_language():
    lang = session.get('lang', 'zh')
    return jsonify({'lang': lang})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5001)
