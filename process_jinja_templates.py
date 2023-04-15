import os
import re
import jinja2


def process_jinja_template(input_file, output_file):
    with open(input_file, "r") as f:
        template_str = f.read()

    template = jinja2.Template(template_str)
    rendered_content = template.render()

    # Ensure YAML file ends with a newline character
    if not rendered_content.endswith('\n'):
        rendered_content += '\n'

    with open(output_file, "w") as f:
        f.write(rendered_content)


pattern = re.compile(r".*\.j2(?:.*)?\.ya?ml$")

for root, _, files in os.walk("."):
    for file in files:
        if pattern.match(file):
            input_file = os.path.join(root, file)
            output_file = os.path.join(root, file.replace(".j2", ""))
            process_jinja_template(input_file, output_file)
