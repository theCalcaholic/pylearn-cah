# A Cards against Humanity clone written in Python (working title)

# Roadmap

1. [M] Support multipick questions
    - **hint:** Another loop?
    - **hint:** `"".replace("old", "new", max_amount)`
2. [S] Make hand cards persist between rounds
    - **hint:** `answers_sample.remove('A sea of troubles')` (lists allow removal by value)
3. [S + M] Prevent cards from being repeatedly drawn
    - **hint:** Couldn't it work like a real card deck?
    - **hint:** `from random import shuffle`
4. **Refactoring stop:** Let's think about how we can improve our existing code <-- you are here
    - readibility
    - code duplication
    - modularity
    - _Introducing:_ The Zen of Python
5. Game state
    - Implement central game state (introducing classes/objects)
    - discuss programming paradigms (imperative, functional, object oriented)
5. Implement simple web interface
    1. Your first 3rd party package: Flask
    2. demo web application (hello world)
    3. refactor existing code into a library (no code outside functions)
    4. Show game in browser
    5. Sending data back (introducing HTML forms)
6. Add multi user support
    1. Manage basic user ids
    2. Implement game rounds
    3. Use sessions
7. Improve the interface
    1. Make it pretty (introducing HTML and Styling - maybe bootstrap or similar?)
    2. Make it interactive (introducing _some_ Javascript)