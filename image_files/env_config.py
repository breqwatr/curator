#!/usr/bin/env python3
"""Apply environment variables to rsyslog config files"""

import json
import os
from jinja2 import Template

def apply_template(jinja2_file, output_file, replacements):
    """Replace the replacements values in jinja2_file, write to output_file"""
    with open(jinja2_file, "r") as j2_file:
        j2_text = j2_file.read()
    template = Template(j2_text)
    replaced_text = template.render(**replacements)
    with open(output_file, "w+") as write_file:
        write_file.write(replaced_text)

# actions.yml
apply_template(
    jinja2_file="action.yml.j2",
    output_file="action.yml",
    replacements={
        "number_of_days": os.environ["RETENTION_PERIOD"],
    },
)

# CONFIG.yml
apply_template(
    jinja2_file="CONFIG.yml.j2",
    output_file="CONFIG.yml",
    replacements={
        "host": os.environ["ELASTICSEARCH_IP"],
        "port": os.environ["ELASTICSEARCH_PORT"],
        "user": os.environ["ELASTICSEARCH_USER"],
        "pass": os.environ["ELASTICSEARCH_PASS"],
    },
)
