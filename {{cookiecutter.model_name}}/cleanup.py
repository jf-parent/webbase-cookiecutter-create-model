import shutil

shutil.move("{{cookiecutter.model_name}}.py", "..")
shutil.rmtree("../{{cookiecutter.model_name}}")
