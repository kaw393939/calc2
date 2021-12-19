"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.pylint_controller import PylintController
from app.controllers.glossary_controller import GlossaryController
from app.controllers.python_home_controller import PythonHomeController
from app.controllers.solid_principles_controller import SolidPrinciplesController
from app.controllers.testing_controller import TestingController
from app.controllers.oops_concepts_controller import OopsConceptsController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/pylint", methods=['GET'])
def pylint_get():
    return PylintController.get()

@app.route("/glossary", methods=['GET'])
def glossary_get():
    return GlossaryController.get()

@app.route("/testing", methods=['GET'])
def testing_get():
    return TestingController.get()

@app.route("/oopsConcepts", methods=['GET'])
def oops_concepts_get():
    return OopsConceptsController.get()

@app.route("/solidprinciples", methods=['GET'])
def solid_principles_get():
    return SolidPrinciplesController.get()

@app.route("/pythonHome", methods=['GET'])
def python_home_get():
    return PythonHomeController.get()


if __name__ == '__main__':
    app.run(use_debugger=False, use_reloader=False, passthrough_errors=True)
    