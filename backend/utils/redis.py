from typing import Any



def create_queued_entry(request_id: str):
    data = {
       'status': 'QUEUED',
       'result': {},
    }


def complete(request_id: str, result: Any):
    _update_entry(
        request_id=request_id,
        result=result,
        status='COMPLETE',
    )

def error(request_id: str, result: Any):
    _update_entry(
        request_id=request_id,
        result=result,
        status='COMPLETE'
    )



def _update_entry(request_id: str, status: str, result: dict):
    if not isinstance(result, dict):
        result = {'data': result}
    # update redis entry
