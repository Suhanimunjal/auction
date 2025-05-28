# auction
Blind Auction Game – Description
This is a fun and dramatic text-based auction game where multiple bidders can place secret bids, and the highest bidder wins in the end. The auction includes some nice ASCII art and a suspenseful winner reveal.

How It Works:
Banner Display
A cool ASCII-art auction banner is printed at the start to make the game feel fancy.

Bidding Loop:
The user is asked to enter their name.
They then place a bid (a number).
The screen clears (using os.system('clear') or cls) to hide previous bidders' info.
This continues until the user says no (n) when asked to add another bidder.

Winner Reveal:
The program simulates a “winner calculation” by printing dots with a short delay (time.sleep).
It then finds the highest bid using max(d, key=d.get) and displays the winner with trophy emojis 🏆🥇.

