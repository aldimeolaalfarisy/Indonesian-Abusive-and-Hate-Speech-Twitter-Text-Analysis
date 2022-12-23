import pandas as pd
import re
import sqlite3
from flask import Flask, jsonify, request
from flasgger import Swagger, LazyString, LazyJSONEncoder, swag_from
from ast import Delete, In
from os import remove
from tkinter import S

app = Flask(__name__)

app.json_encoder = LazyJSONEncoder
swagger_template = dict(
    info = {
        'title': LazyString(lambda: 'API Documentation for Text Processing'),
        'version': LazyString(lambda: '1.0.0'),
        'description': LazyString(lambda: 'API Documentation for Text Processing'),
    },
    host = LazyString(lambda: request.host)
)

swagger_config = {
    'headers': [],
    'specs': [
        {
            'endpoint': 'docs',
            'route': '/docs.json',
        }
    ],
    'static_url_path': '/flasgger_static',
    'swagger_ui': True,
    'specs_route':'/docs/'
}

swagger = Swagger(app, template=swagger_template, config=swagger_config)

def lowercase(s):
    return s.lower()

def remove_punctutation(s):
    s = re.sub('[^0-9a-zA-Z]+', ' ', s)
    s = re.sub(r':', '', s)
    s = re.sub('\n',' ',s)
    s = re.sub('rt',' ', s)
    s = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))',' ', s)
    s = re.sub('  +', ' ', s)
    s = re.sub(r'pic.twitter.com.[\w]+', '', s)
    s = re.sub('user',' ', s)
    s = re.sub('gue','saya', s)
    s = re.sub(r'‚Ä¶', '', s)
    return s

db = sqlite3.connect('C:/Users/ASUS/Documents/Gold Challenge/database.db', check_same_thread = False)
q_kamusalay = 'SELECT * FROM kamusalay'
t_kamusalay = pd.read_sql_query(q_kamusalay, db)
q_abusive = 'SELECT * FROM abusive'
t_abusive = pd.read_sql_query(q_abusive, db)

alay_dict = dict(zip(t_kamusalay['alay'], t_kamusalay['normal']))
def alay_to_normal(s):
    for word in alay_dict:
        return ' '.join([alay_dict[word] if word in alay_dict else word for word in s.split(' ')])

l_abusive = t_abusive['ABUSIVE'].str.lower().tolist()
def normalize_abusive(s):
    list_word = s.split()
    return ' '.join([s for s in list_word if s not in l_abusive])

def text_cleansing(s):
    s = lowercase(s)
    s = remove_punctutation(s)
    s = alay_to_normal(s)
    s = normalize_abusive(s)
    return s

@swag_from("docs/input_data.yml", methods=['POST'])
@app.route('/input_data', methods=['POST'])
def test ():
    input_txt = str(request.form["input_data"])
    output_txt = text_cleansing(input_txt)

    db.execute('create table if not exists input_data (input_text varchar(255), output_text varchar(255))')
    query_txt = 'insert into input_data (input_text , output_text) values (?,?)'
    val = (input_txt,output_txt)
    db.execute(query_txt,val)
    db.commit()

    return_txt = { "input" :input_txt, "output" : output_txt}
    return jsonify (return_txt)

@swag_from("docs/upload_data.yml", methods=['POST'])
@app.route('/upload_data', methods=['POST'])
def upload_file():
    file = request.files["upload_data"]
    df_csv = (pd.read_csv(file, encoding="latin-1"))

    df_csv['new_tweet'] = df_csv['Tweet'].apply(text_cleansing)
    df_csv.to_sql("clean_tweet", con=db, index=False, if_exists='append')
    db.close()

    cleansing_tweet = df_csv.new_tweet.to_list()

    return_file = {
        'output': cleansing_tweet}
    return jsonify(return_file)


if __name__ == '__main__':
	app.run()