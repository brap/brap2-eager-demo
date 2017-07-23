from brap.container import Container

from brap.compilers.edge_node_compiler import EdgeNodeCompiler
from brap.compilers.circular_dependency_compiler import CircularDependencyCompiler
from brap.compilers.eager_dependency_injection_compiler import EagerDependencyInjectionCompiler

from demo.parameters import parameter_container
from demo.runner import Runner
from demo.credit_card import CreditCard
from demo.fight import Fight

container = Container()
container.merge(parameter_container)

container.set(
    'blade_runner',
    Runner,
    lambda c: c('blade_runner_name', 'blade_runner_occupation')
)

container.set(
    'logan_runner',
    Runner,
    lambda c: c('runner_name', 'runner_occupation')
)

container.set(
    'credit_card',
    CreditCard,
    lambda c: c('ccn', 'cv2_code', 'expiry')
)

container.set(
    'fight',
    Fight,
    lambda c: c('credit_card')
    [
        ('add_combatant', lambda c: c('blade_runner')),
        ('add_combatant', lambda c: c('logan_runner'))
    ]
)

container.use_compiler(EdgeNodeCompiler())  # Finds unregistered edge nodes
container.use_compiler(CircularDependencyCompiler())  # Finds circular dependencies
container.use_compiler(EagerDependencyInjectionCompiler())  # Injects actual instances/parameters together, and fully.

app = container.get('fight')
