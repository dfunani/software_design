# State Machine Pattern

## Definition

The State Machine Pattern allows an object to alter its behavior when its internal state changes. The object will appear to change its class.

### States - A, B and C

```python
class State(ABC):
    @abstractmethod
    def handle_transition_a(self, context):
        pass

    @abstractmethod
    def handle_transition_b(self, context):
        pass

    @abstractmethod
    def handle_transition_c(self, context):
        pass

    @abstractmethod
    def get_state_name(self):
        pass

class StateA(State):
    def handle_transition_a(self, context):
        print("Already in State A")

    def handle_transition_b(self, context):
        context.set_state(StateB())
        print("Transitioned from State A to State B")

    def handle_transition_c(self, context):
        context.set_state(StateC())
        print("Transitioned from State A to State C")

    def get_state_name(self):
        return "State A"

class StateB(State):
    def handle_transition_a(self, context):
        context.set_state(StateA())
        print("Transitioned from State B to State A")

    def handle_transition_b(self, context):
        print("Already in State B")

    def handle_transition_c(self, context):
        context.set_state(StateC())
        print("Transitioned from State B to State C")

    def get_state_name(self):
        return "State B"

class StateC(State):
    def handle_transition_a(self, context):
        context.set_state(StateA())
        print("Transitioned from State C to State A")

    def handle_transition_b(self, context):
        print("Invalid Transition from State C to State B") #example of a state transition rule.

    def handle_transition_c(self, context):
        print("Already in State C")

    def get_state_name(self):
        return "State C"
```

### Transitions

```python
from abc import ABC, abstractmethod
from enum import Enum

class StateMachineContext:
    def __init__(self):
        self._current_state = StateA()

    def set_state(self, state: State):
        self._current_state = state

    def transition_to_a(self):
        self._current_state.handle_transition_a(self)

    def transition_to_b(self):
        self._current_state.handle_transition_b(self)

    def transition_to_c(self):
        self._current_state.handle_transition_c(self)

    def get_current_state_name(self):
        return self._current_state.get_state_name()

# Example Usage
context = StateMachineContext()

print(f"Current State: {context.get_current_state_name()}")

context.transition_to_b()
print(f"Current State: {context.get_current_state_name()}")

context.transition_to_c()
print(f"Current State: {context.get_current_state_name()}")

context.transition_to_b()#invalid transition

context.transition_to_a()
print(f"Current State: {context.get_current_state_name()}")
```

## Use Case

1. Approval Workflow: Document moves through Draft, Submitted, Approved, Rejected states.
2. Network Connection: Transitions between Disconnected, Connecting, Connected states.
3. Video Player: Manages states like Stopped, Playing, Paused.

## Summary

The State Machine pattern lets an object change its behavior based on its internal state. It's like a flowchart, where each state dictates valid actions and transitions to other states. It helps manage complex processes with clear, organized steps.