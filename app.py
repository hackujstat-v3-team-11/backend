import sys
from flask import Flask, request, make_response, jsonify, render_template
from utils import dialogflow
import question_modules


COMMANDS = ['Nastavit lokaci na Prahu', 'Začít hrát', 'Nastav počet otázek na 8']

class Answers:
    def __init__(self):
        self._answers = {}

    def init(self, session, location):
        self._answers[session] = {'answers': [], 'questions': question_modules.get_questions(location, count=3)}

    def get_len_answers(self, session):
        return len(self._answers[session]['answers'])

    def get_len_question(self, session):
        return len(self._answers[session]['questions'])

    def get_question(self, session):
        return self._answers[session]['questions'][self.get_len_answers(session)]['question']

    def get_answers_to_questions(self, session):
        return self._answers[session]['questions'][self.get_len_answers(session)]['answers']

    def get_aswers_from_user(self, session):
        return self._answers[session]['answers'][self.get_len_answers(session)]

    def set_answer(self, session, answer):
        self._answers[session]['answers'].append(answer)

    def get_session_data(self, session):
        return self._answers[session]

app = Flask(__name__, static_url_path='/static')
answers = Answers()

def get_emoji_by_score(points, max_score):
    result = points / max_score

    if 0 <= result <= 0.1:
        return '🤮'

    elif 0.1 < result <= 0.2:
        return '😩'

    elif 0.2 < result <= 0.3:
        return '😨'

    elif 0.3 < result <= 0.4:
        return '😳'

    elif 0.4 < result <= 0.5:
        return '😐'

    elif 0.5 < result <= 0.6:
        return '😋'

    elif 0.6 < result <= 0.7:
        return '😉'

    elif 0.7 < result <= 0.8:
        return '😎'

    elif 0.8 < result <= 0.9:
        return '😍'

    else:
        return '🤩'

def next_question(session):
    question = answers.get_question(session)
    answers_to_questions = answers.get_answers_to_questions(session)

    return dialogflow.response_quick_replies(question + '\r\n' + ('\r\n'.join(answers_to_questions)), ['A', 'B', 'C', 'D'])

lut = ['A', 'B', 'C', 'D']
def evaluate(session):
    s = answers.get_session_data(session)
    score = 0
    text = []
    for index, answer in enumerate(s['answers']):
        question = s['questions'][index]
        text.append(question['question'])
        if question['correct'] == answer:
            score+=1
            text.append('✔ ' + question['answers'][answer])
        else:
            if answer > question['correct']:
                text.append('📖 ' + question['answers'][question['correct']])
            text.append('❌ ' + question['answers'][answer])
            if answer < question['correct']:
                text.append('📖 ' + question['answers'][question['correct']])

        text.append(question['value'])
        text.append('')
    text.append('Skóre {0}/{1} => {2}'.format(score, answers.get_len_question(session),
                get_emoji_by_score(score, answers.get_len_question(session))))

    return dialogflow.response_quick_replies('\r\n'.join(text), ['Hrát znovu'])

def handle_answer_a(session, location):
    answers.set_answer(session, 0)

    if answers.get_len_answers(session) != answers.get_len_question(session):
        return next_question(session)

    else:
        return evaluate(session)

def handle_answer_b(session, location):
    answers.set_answer(session, 1)

    if answers.get_len_answers(session) != answers.get_len_question(session):
        return next_question(session)

    else:
        return evaluate(session)

def handle_answer_c(session, location):
    answers.set_answer(session, 2)

    if answers.get_len_answers(session) != answers.get_len_question(session):
        return next_question(session)

    else:
        return evaluate(session)

def handle_answer_d(session, location):
    answers.set_answer(session, 3)

    if answers.get_len_answers(session) != answers.get_len_question(session):
        return next_question(session)

    else:
        return evaluate(session)


def start_quiz(session, location):
    answers.init(session, location)
    question = answers.get_question(session)
    answers_to_questions = answers.get_answers_to_questions(session)

    return dialogflow.response_quick_replies(question + '\r\n' + ('\r\n'.join(answers_to_questions)), ['A', 'B', 'C', 'D'])

def got_location(session, location):
    return dialogflow.response_quick_replies('Lokace nastavena na %s' % location, ['Začít hrát'])

def error_handler(session, location=None):
    if location:
        return dialogflow.response_message('Nerozumím, co po mě chceš nebo jsi zadal špatně město. Město zadávej v 1. pádě')

    else:
        return dialogflow.response_message('Nejdřív mi zadej polohu (v 1. pádě)')

def pomoc_handler(session, location):
    return dialogflow.response_quick_replies('Tady máš příkazy, jaké na mě můžeš použít', COMMANDS)

def demo(session, location):
    return dialogflow.response_quick_replies('Demo', ['Nápověda 1', 'Nápověda 2'])

def results():
    req = request.get_json(force=True)
    session = req['session'].split('/')[4]

    callbacs = {
        'Start quiz': start_quiz,
        'Give location': got_location,
        'Default Fallback Intent': error_handler,
        'cau': demo,
        'A': handle_answer_a,
        'B': handle_answer_b,
        'C': handle_answer_c,
        'D': handle_answer_d,
        'Pomoc': pomoc_handler
    }

    action = req['queryResult']['intent']['displayName']

    try:
        location = req['queryResult']['outputContexts'][0]['parameters']['mesto']

    except Exception:
        location = None

    return callbacs.get(action)(session, location)

@app.route('/dialogflow', methods=['POST'])
def webhook():
    return make_response(jsonify(results()))

@app.route('/', methods=['GET'])
def root():
    return 'Use it on Facebook Messenger'

if __name__ == '__main__':
    try:
        app.run('localhost', 80)
    except Exception as e:
        print('Exited with error:', e)
        sys.exit()
