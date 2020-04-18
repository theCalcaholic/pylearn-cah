# A Cards against Humanity clone written in Python (working title)

# Roadmap

1. Support multipick questions
    - **hint:** Another loop?
2. Make hand cards persist between rounds
3. Prevent cards from being repeatedly drawn
    - **hint:** Couldn't it work like a real card deck?
4. **Refactoring stop:** Let's think about how we can improve our existing code
    - readibility
    - code duplication
    - modularity
    - _Introducing:_ The Zen of Python
4. Implement simple web interface
    1. Your first 3rd party package: Flask
    2. demo web application (hello world)
    3. refactor existing code into a library (no code outside functions)
    4. Show game in browser
    5. Sending data back (introducing HTML forms)
5. Add multi user support
    1. Manage basic user ids
    2. Implement game rounds
    3. Use sessions
6. Improve the interface
    1. Make it pretty (introducing HTML and Styling - maybe bootstrap or similar?)
    2. Make it interactive (introducing _some_ Javascript)