# Template Pattern

## Definition

The Template Method Pattern defines the skeleton of an algorithm in a method, deferring some steps to subclasses. Template Method lets sub-classes redefine certain steps of an algorithm without changing the algorithm’s structure.

### Beverage Template

    ```python
    from abc import ABC, abstractmethod


    class Beverage(ABC):
        """Abstract class representing a beverage."""

        def prepare_recipe(self):
            """Template method defining the overall beverage preparation steps."""
            self.boil_water()
            self.brew()
            self.pour_in_cup()
            self.add_condiments()
            self.stir()

        def boil_water(self):
            """Boils water for the beverage."""
            print("Boiling water...")

        def pour_in_cup(self):
            """Pours the beverage into a cup."""
            print("Pouring beverage into cup...")

        def stir(self):
            """Stirring the beverage."""
            print("Stirring water...")

        @abstractmethod
        def add_condiments(self):
            """Adding condiments (specific to some subclasses)."""
            print("Adding Sugar...")

        @abstractmethod
        def brew(self):
            """Abstract method for brewing the beverage (specific to each subclass)."""
            pass

    ```

### Beverages

    ```python
    class Coffee(Beverage):
        """Concrete class for coffee."""

        def brew(self):
            """Brews coffee grounds."""
            print("Brewing coffee grounds...")

        def add_condiments(self):
            """Optionally adds milk and sugar."""
            print("Adding milk and sugar...")


    class Tea(Beverage):
        """Concrete class for tea."""

        def brew(self):
            """Steeps tea leaves."""
            print("Steeping tea leaves...")

        def add_condiments(self):
            """Optionally adds lemon or honey."""
            print("Adding lemon or honey...")


    # Prepare and drink coffee
    coffee = Coffee()
    coffee.prepare_recipe()

    # Prepare and drink tea
    tea = Tea()
    tea.prepare_recipe()

    ```

## Benefits

- Code Reusability: The base class defines the overall algorithm structure, reducing code duplication across subclasses.
- Flexible Customization: Subclasses can override specific steps to tailor the algorithm to their needs.
- Improved Maintainability: Modifications to the algorithm's structure can be made in the base class, affecting all subclasses.
- Easier Testing: The base class provides a clear framework for testing, making it easier to verify the correct execution of the algorithm.
- Consistent Behavior (Enforced Algorithm Structure): The base class ensures that all subclasses follow the same algorithmic steps, promoting consistency.
- Prevented Errors: The template method enforces the order of operations, reducing the risk of errors caused by incorrect sequencing.
- Extensibility: Subclasses can be created to implement specific variations of the algorithm, making it adaptable to different scenarios. Easy Addition of New Subclasses: New subclasses can be added without affecting the existing algorithm structure.

## Use Case

The Template Method pattern is particularly useful in scenarios where you have a core algorithm or process that remains consistent across different implementations, but specific steps within that algorithm may vary. Here are some common use cases:

1. Data Access Frameworks: Provide a template for database operations like connecting, querying, and closing connections. Subclasses can implement specific database-related tasks.
2. Web Frameworks: Define a template for handling HTTP requests, including parsing requests, processing, and generating responses. Subclasses can customize request handling and response generation.
3. Report Generation: Define a template for generating reports, including steps like header, body, and footer. Subclasses can customize the content of each section.
4. Document Formatting: Provide a template for formatting documents, such as applying styles, adding images, and creating tables. Subclasses can implement specific formatting rules.
5. AI Algorithms: Define a template for AI decision-making processes, such as path-finding, enemy behavior, and player interaction. Subclasses can implement specific AI strategies.
6. Game Engine: Provide a template for game loops, rendering, and input handling. Subclasses can customize game logic and graphics.
7. Test Case Execution: Define a template for executing test cases, including setup, execution, and teardown. Subclasses can implement specific test scenarios.
8. Test Report Generation: Provide a template for generating test reports, including summary, detailed results, and charts. Subclasses can customize the report format and content.
9. Trade Execution: Define a template for executing trades, including order placement, execution, and confirmation. Subclasses can implement specific trading strategies.
10. Risk Assessment: Provide a template for assessing risk, including data collection, analysis, and reporting. Subclasses can implement specific risk models.

## Summary

The Template Method pattern promotes code reuse and maintainability by defining a common algorithm structure.
It allows for flexibility and customization by enabling subclasses to override specific steps. It's particularly useful when you have a core algorithm with variations in implementation details. By understanding the core principles and use cases of the Template Method pattern, you can effectively apply it to your software designs to create more robust and adaptable systems.
