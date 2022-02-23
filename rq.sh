#!/bin/bash
command -v curl > /dev/null 2>&1 || {  echo >&2 "Требуется curl, но он не установлен. \n Установка.."; apt install curl -y; }
command -v python > /dev/null 2>&1 || {  echo >&2 "Требуется python, но он не установлен. \n Установка.."; apt install python -y; }
command -v pip > /dev/null 2>&1 || {  echo >&2 "Требуется pip, но он не установлен. \n Установка.."; curl https:bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py ; }
command -v toilet > /dev/null 2>&1 || {  echo >&2 "Требуется toilet, но он не установлен. \n Установка.."; apt install toilet -y; }
