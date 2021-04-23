===
Rock paper scissors game
===
The django rock paper scissors game is a simple game of rock paper scissors to play against the computer.
The player selects his/her choice and the computer selects its choice, then the winner is selected.

Quick Start
-----------

1. Add "game" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'game',
    ]

2. Include the game URLconf in your project urls.py like this::

    path('game/', include('game.urls')),

3. Run ``python manage.py migrate`` to create the game models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create rocks papers and scissors (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/game/ to play the game.
