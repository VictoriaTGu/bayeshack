from flask import Flask
from flask import request
from rq import Queue
from worker import conn
import json
import sys
import traceback
from Queue import Queue as FifoQueue
from utils import ask_question
from utils import sendTextMessage

app = Flask(__name__)
q = Queue(connection=conn)
question_queue = FifoQueue()

QUESTIONS = [
    ('intro', 'Hi, to start I will need a few details'),
    ('city','What city do you live in?'),
    ('job','What do you do for a living?'),
    ('experience','How many years of experience do you have in that job?'),
    ('education','Education? ("Less Than High School", "High School" , "Some College", "College", "Advanced")'),
    ('gender','What gender do you identify as?'),
]
CURRENT_ATTRIBUTE='intro'
USER_PROFILE = {}
SENDER_ID=1020675814687539

@app.route("/")
def ind():
    return "Hello World!"

@app.route('/webhook', methods=['GET', 'POST'])
def validate():
    try:
        if request.method == 'GET':
            if request.args.get('hub.verify_token') == 'verify_me':
                return request.args.get('hub.challenge')
        else:
            messaging_events = json.loads(request.data.decode("utf-8"))
            messages = messaging_events['entry'][0]['messaging']
            sys.stderr.write(str(messaging_events) + '\n')
            for event in messages:
                if (event.get('message') and event['message']['text']):
                    text = event['message']['text']
                    sendTextMessage(SENDER_ID, text + ' received, Thank you!')
                    # Handle a text message from this sender
                    store_attribute(text)
                    sys.stderr.write('store_attribute ' + text + '\n')
                    ask_next_question()
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        app.logger.error(traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2))
        return 'Error, wrong validation token'

def store_attribute(text):
    USER_PROFILE[CURRENT_ATTRIBUTE] = text
    sys.stderr.write(str(USER_PROFILE) + '\n')

def ask_next_question():
    sys.stderr.write('ask next question\n')
    if question_queue.empty():
        sys.stderr.write('question queue empty\n')
        return
    global question_queue
    attribute, question = question_queue.get()
    global CURRENT_ATTRIBUTE
    CURRENT_ATTRIBUTE=attribute
    sys.stderr.write('enqueue ' + attribute + ' ' + question)
    q.enqueue(
        ask_question,
        attribute,
        question,
        SENDER_ID,
        USER_PROFILE
    )

def fill_queue(queue):
    for attribute, question in reversed(QUESTIONS):
        queue.put((attribute,question))
    sys.stderr.write(str(queue.qsize()) + '\n')
    return queue


def main():
    global question_queue
    # question_queue = fill_queue()
    # attribute, question = question_queue.get()
    for attribute, question in QUESTIONS:
        ask_question(
            attribute,
            question,
            SENDER_ID,
            USER_PROFILE
        )
    app.run(debug=True)


if __name__ == "__main__":
    main()
