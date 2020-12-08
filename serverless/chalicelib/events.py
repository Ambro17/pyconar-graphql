from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
import json
import logging
import boto3

logger = logging.getLogger(__name__)


class Event:
    """Represents a domain event. Serializable as JSON""" 

    @abstractmethod
    def to_dict(self) -> dict:
        ...

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


@dataclass
class TestEvent(Event):
    message: str

    def to_dict(self) -> dict:
        return {
            'type': self.__class__.__name__,
            'message': self.message,
        }


class MessageBus(ABC):
    """Abstraction reponsible of sending messages for async treatment"""

    @abstractmethod
    def send(self, event: Event):
        ...


class SQSBus(MessageBus):
    """Send messages to aws SQS for async treatment"""

    def __init__(self, queue: str):
        self.client = boto3.client('sqs')
        # run first `aws sqs create-queue --queue-name some-name`
        self.queue = queue

    def send(self, event: Event):
        self.client.send_message(
            QueueUrl=self.queue,
            MessageBody=event.to_json()
        )


class NullBus(MessageBus):
    """Send messages nowhere"""

    def __init__(self, *args, **kwargs):
        pass

    def send(self, event: Event):
        pass