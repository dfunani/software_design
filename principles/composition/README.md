# Head First: Design Patterns

# Chapter 2

## Interfaces

Abstract Classes that serve as a blueprint for implementing a Type, Trait or Behaviour.

Continuing from Chapter 1's Duck Simulations:
Using purely inheritance results in sub-classes gaining invalid traits. But we can extract and encapsulate certain non-shared and ever changing traits into stand alone classes. One design consideration is making those extracted traits into Interfaces. Which would define behaviours that are expected of the interface.

Interfaces:
1. FlyBehaviour
2. QuackBehaviour

So Both interfaces hold traits that must be implemented in order to implement the interface.

One correction is to implement the interfaces at runtime using an implementation class or function.

Interfaces - Must Be Implemented by overriding all methods.
Abstract Classes - Must be extended and all methods can be overridden but don't have to be.

We create dynamic traits for the duck objects by referencing the Behaviour Implementations, encapsulating the Required Behaviours.

Each Duck will instantiate it's desired Interface by referencing the respective Concrete interface implementation.

## Composition

That brings us to the next point, **COMPOSITION**, where classes are combined to create composite class.