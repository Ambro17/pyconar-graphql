from chalice import Chalice
from serverless.chalicelib.events import TestEvent, NullBus, SQSBus


def create_app(name='test', queue_name=None):
    app = Chalice(app_name=name)

    bus = SQSBus(queue_name) if queue_name else NullBus(queue_name)
    app.bus = bus

    return app

app = create_app(name='demo')
app.debug = True


@app.route('/')
def index():
    app.log.error("Not an error")
    app.bus.send(TestEvent(message='TestEvent #1'))
    return {'hello': 'world'}


@app.on_sqs_message(queue='my-queue', batch_size=1)
def handle_sqs_message(event):
    for record in event:
        app.log.debug("Received message with contents: %s", record.body)
