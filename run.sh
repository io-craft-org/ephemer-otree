#!/bin/bash
# Script to start the oTree server on a PaaS.

source venv/bin/activate

: ${IP:=127.0.0.1}
: ${PORT:=8001}
otree prodserver "$IP:$PORT"
