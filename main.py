from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    draft_variable = 'I want to listen to this music forever!'
    musical_sets = [{'time': '11.07.23',
                     'head': 'TRANSATLANTIC',
                     'body': 'Feminism',
                     'file': 'audio/amorsatyr.mp3'
                     },
                    {'time': '12.07.23',
                     'head': 'TRANS',
                     'body': 'Fusion',
                     'file': 'audio/laparole.mp3',
                     },
                    {'time': '13.07.23',
                     'head': 'TRANSMOTION',
                     'body': 'Fem',
                     'file': 'audio/money.mp3',
                     },
                    {'time': '14.07.23',
                     'head': 'TEHNO',
                     'body': 'Freejazz',
                     'file': 'audio/umamami.mp3',
                     }]
    return render_template('index.html', dv=draft_variable, musical_sets=musical_sets)


if __name__ == '__main__':
    app.run()
