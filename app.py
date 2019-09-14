import sys
from flask import Flask, request, make_response, jsonify, render_template
from utils import dialogflow
import question_modules
from pprint import pprint

class Answers:
    def __init__(self):
        self._answers = {}

    def init(self, session, location):
        self._answers[session] = {'answers': [], 'questions': question_modules.get_questions(location)}

    def get_len_answers(self, session):
        return len(self._answers[session]['answers'])

    def get_question(self, session):
        return self._answers[session]['questions'][self.get_len_answers(session)]['question']

    def get_answers_to_questions(self, session):
        return self._answers[session]['questions'][self.get_len_answers(session)]['answers']

    def get_aswers_from_user(self, session):
        return self._answers[session]['answers'][self.get_len_answers(session)]

    def set_answer(self, session, answer):
        self._answers[session]['answers'].append(answer)
        print(self._answers)

    def get_session_data(self, session):
        return self._answers[session]

app = Flask(__name__, static_url_path='/static')
answers = Answers()

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
            r = ' OK 🙂'
        else:
            r = ' Wrong 😭'

        text.append(question['answers'][answer] + r + question['answers'][question['correct']])
        text.append(question['value'])

    return dialogflow.response_quick_replies('\r\n'.join(text), ['Hrát znovu'])

def handle_answer_a(session, location):
    answers.set_answer(session, 0)

    if answers.get_len_answers(session) != 3:
        return next_question(session)

    else:
        return evaluate(session)

def handle_answer_b(session, location):
    answers.set_answer(session, 1)

    if answers.get_len_answers(session) != 3:
        return next_question(session)

    else:
        return evaluate(session)

def handle_answer_c(session, location):
    answers.set_answer(session, 2)

    if answers.get_len_answers(session) != 3:
        return next_question(session)

    else:
        return evaluate(session)

def handle_answer_d(session, location):
    answers.set_answer(session, 3)

    if answers.get_len_answers(session) <= 3:
        return next_question(session)

    else:
        return evaluate(session)


def start_quiz(session, location):
    answers.init(session, location)
    question = answers.get_question(session)
    answers_to_questions = answers.get_answers_to_questions(session)

    print(question, answers_to_questions)

    return dialogflow.response_quick_replies(question + '\r\n' + ('\r\n'.join(answers_to_questions)), ['A', 'B', 'C', 'D'])

def got_location(session, location):
    return dialogflow.response_quick_replies('Lokace nastavena na %s' % location, ['Začít hrát'])

def error_handler(session, location=None):
    if location:
        return dialogflow.response_message('Nerozumím, co po mě chceš nebo jsi zadal špatně město. Město zadávej v 1. pádě')

    else:
        return dialogflow.response_message('Nejdřív mi zadej polohu (v 1. pádě)')

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
        'D': handle_answer_d
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
        #pprint(question_modules.get_questions('Opava')[0])
    except Exception as e:
        print('Exited with error:', e)
        sys.exit()
