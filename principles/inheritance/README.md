# Head First: Design Patterns

# Chapter 1

## Inheritance

Creating Base/Super Classes from which Sub-Classes can inherit shared traits and attributes. Implementation Driven, because all Sub-Classes inherit, all traits of the Super Class.

Using Duck Simulations as the example:
The Super Class is Duck.
Mallard, Red-Head and Rubber Ducks inherit from Duck.

The Duck Super Class defines how Ducks:
    1.Fly
    2.Swim
    3.Quack
    4.Display

This means All 3 Sub-Classes have implemented each and everyone of those Duck Traits by virtue of inheriting from the Super Class.

Considerations:
Should a Sub-Class be implementing each and everyone of the Super Class Traits? Consider Rubber Duck flying.
Could overriding any Super Class Traits become unmanageable? Consider Rubber Duck implementing (Overriding) the flying/quacking traits.
