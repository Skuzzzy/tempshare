#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, send_file, render_template, request, abort
import os
app = Flask(__name__)

@app.route('/')
def root():
    return 'hi (´・ω・`)'


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', ip=request.remote_addr, error=e.description), 404

@app.route('/tmp/<filename>')
def tmp(filename):
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tmp', filename)
    print path
    if os.path.isfile(path):
        return send_file(path), 200
    else:
        abort(404, 'File not found')


