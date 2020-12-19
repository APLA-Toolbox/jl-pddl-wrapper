from .modules import loading_bar_handler

UI = False

if UI:
    loading_bar_handler(False)
import julia

_ = julia.Julia(compiled_modules=False)

if UI:
    loading_bar_handler(True)
    
from julia import PDDL


class AutomatedPlanning:
    def __init__(self, domain_path, problem_path):
        self.domain = PDDL.load_domain(domain_path)
        self.problem = PDDL.load_problem(problem_path)
        self.initial_state = PDDL.initialize(self.problem)
        self.current_state = self.initial_state

    def execute_action(self, action, state):
        return PDDL.execute(action, state)

    def satisfies(self, asserted_state, state, domain):
        return PDDL.satisfy(asserted_state, state, domain)[0]


if __name__ == "__main__":
    ap = AutomatedPlanning("..data/domain.pddl", "..data/problem.pddl")
