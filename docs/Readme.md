# Pydantic Arguments Validator
Let's say we have an application that converts a given amount of currency into another currency. The constraints are as follows: 
- The ``amount`` must be a float type greater than 0
- Our backend only supports a selected set of world currencies, so ``from_currency`` and ``to_currency`` must be within a predefined range.

The demo shows how to check constraints on function arguments manually or with the Pydantic ``@validate_arguments`` decorator, leaving the body of the function uncluterred.
For details and usage of ``@validate_arguments`` see https://pydantic-docs.helpmanual.io/usage/validation_decorator/