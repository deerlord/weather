from dataclasses import dataclass
from functools import wraps
from backend.utils import redis


@dataclass
class Task():
    
    request_id: str

    def __post_init__(self):
        redis.create_queued_entry(request_id=self.request_id)

    def __call__(self, func):
        @wraps
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                redis.complete(request_id=request_id, result=result)
            except Exception as error:
                message = f'{error}'
                logging.error(message)
                redis.error(request_id=request_id, result=result)
                raise error
            return result
        return wrapper
