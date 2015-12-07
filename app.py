import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from sqlalchemy.dialects.postgresql import JSON

DEFAULT_CONN = "postgresql://mserver:mserver@db/mserver"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_MSERVER', DEFAULT_CONN)
db = SQLAlchemy(app)

#print(db.metadata)
#print(db)

class MetadataModel(db.Model):
        __tablename__ = 'metadata'

        id = db.Column(db.Integer, primary_key=True)
        data = db.Column(JSON)

        def __init__(data):
                self.data = data

        def __repr__(self):
                return '<id {}>'.format(self.id)

@app.route('/api/storage/<ecosystem>/<name>', methods=['GET', 'POST'])
def get_metadata(ecosystem, name):
        if request.method == 'GET':
                return 'GET /api/storage {"%s": "%s"}' % (ecosystem, name)
        elif request.method = 'POST':
                return 'POST /api/storage {"%s": "%s"}: %s' % (ecosystem, name, str(request.form['payload']))
        else:
                return 'UNKNOWN METHOD'

if __name__ == '__main__':
        app.debug = True
        app.run()
