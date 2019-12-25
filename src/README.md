# Compiling your own sheep game

The *lists* directory contains two files: *lifecards.txt* and *wishes.txt*. Edit those files to add / remove life events and wishes. To generate the packs of cards with your new content, run:

    python3 life_card_maker.py

and 
    python3 wish_card_maker.py

This will create separate images for each card in the game, saved in the *img* directory.


# Making print-ready cards

You can concatenate all cards, ready to be printed, by running:

    python3 life_cards_paste.py

and

    python3 wish_cards_paste.py

The resulting files will be found in the *printing* directory.
    

### Credit

The AnnabelScript font was made by Jose Alberto Reyes Galvez and is freely available [here](https://www.1001freefonts.com/annabel-script.font).

The Raleway Regular font was made by Matt McInerney and is freely available [here](https://www.1001freefonts.com/raleway.font).
