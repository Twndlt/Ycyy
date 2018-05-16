# -*- coding: utf-8 -*-
"""
@Created by Seven on 2018-05-10
import os
from flask import (Flask,request....)
"""
from contextlib import contextmanager


@contextmanager
def success_ok():
    pass


def deleted(model, id=None):
    delte = model.query.get_or_404(int(id))
    if delte:
        delte.deleted = 1
        delte.session.add()
        delte.session.commit()
        return True
    return False
