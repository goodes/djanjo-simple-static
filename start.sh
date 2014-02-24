#!/usr/bin/env bash
./pyve/bin/gunicorn --pythonpath staticsite staticsite.wsgi:application
