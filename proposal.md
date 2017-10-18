### *Name

**Possible names:**

DigiFridge (aka Digital Fridge)

Fridgital (Organizer?)

Fridge Friend / Fridge Buddy / Fridge Saver (with superhero cape)

---

### *Product Overview

*What is your MVP web app going to do?
How does a user interact with it on a high level?*

The app will allow users to add all the groceries they buy to a "digital fridge" which will then track the expiration dates and alert them when food items get close to spoiling so they can be used. The aim is to reduce food waste and make shopping more efficient by eliminating buying duplicate/unnecessary items.

---

### *Specific Functionality

Ideally I would like to implement this as a one-page app, with each feature occurring in a pop-up/overlay box on top which carries out its functionality and saves data, then can be closed to return to the "original" screen. The page should not need to be refreshed (other than first logging in/opening fridge).

#### Greeting page (not logged in)

[(View Image)](proposalimages/00WelcomePage.png)

Shows closed fridge and login box on front, empty notice board and empty shopping bag to right side.

(MVP: Login will allow user to access fridge just by typing their name -- no security; local copy only.
Proper launch may integrate password-protected and stored/outside-accessible accounts.)

Left sidebar has intro text stating purpose/functionality, how to use, tips.

#### Main Page (logged in)

[(View Image)](proposalimages/00LoggedIn.png)

Upon successful login, animation of fridge door swinging open reveals shelves with icons of different categories of food items **(1)**.

To the side there is a notice board with options to make shopping list **(2)**, view tossed items **(3)**, and view all items in fridge in list form **(4)**.

Below is a grocery bag icon which can be clicked to add new items to fridge **(5)**.

To the side of the fridge door is an icon to close fridge (equivalent to logging out and saving).

**(1) Fridge View**

[(View Image)](proposalimages/01ItemView.png)

User can click category icons in fridge to activate a pop-up/overlay window displaying which sub-items they have in each (i.e. Dairy >> Cheese). (Apart from the list of provided categories, there will also be an "unknown/other" category at the end, so the user isn't limited and can have pretty much any item conceivable in their fridge.)

Clicking an item pops out a side menu with details of individual items: Purchased-date, expiration-date, used/tossed buttons (optional: calories, recipe suggestions).

- Expiration: Tracks current system date and displays countdown of how many days left until item expires. (Flavor: Have display change from green >> yellow >> orange >> red as it gets closer to expiration.)

- Used/tossed buttons: If "used" is clicked, item is simply deleted from current fridge.

- If "tossed" is clicked, item is added to "tossed list" along with the date it was tossed.

Click the X in the top menu bar to close and return to main fridge view.

**(2) Shopping List**

[(View Image)](proposalimages/02ShoppingList.png)

When shopping list is clicked on the notice board, it pops up and displays a list of the main fridge categories, with blank lines in between for adding items. (Categories are listed in order even if empty, to make it easy to compare with fridge list(4).)

Functionally, it acts as a to-do list:

- Type in an empty line to add a new item.

- Click an item to ~~cross it out~~.

- Click "new list" to erase all contents and start a new list.

Click the X in the top menu bar to save/close and return to main fridge view.

(With this style, the user can technically add any item under any category, but...it's up to them how chaotic/organized they want their life to be.)

**(3) Tossed Items**

[(View Image)](proposalimages/03TossedList.png)

Clicking tossed items pops up an overlay displaying all items tossed within the last month and the date they were tossed, allowing user to track what they're buying too much of/not using. This item also tracks system time, and items older than one month fall off automatically.

Click the X in the top menu bar to close and return to main fridge view.

**(4) Fridge List**

[(View Image)](proposalimages/04FridgeList.png)

Clicking the arrow on the right side of the screen will expand a sidebar which contains all the items currently in the fridge in condensed list form without details (i.e. only category, name, quantity: meat >> pork chops >> 2). This is meant to be used side-by-side with the shopping list to make sure no duplicate/unnecessary items are being added to the shopping list.

**(5) Add Items**

[(View Image)](proposalimages/05AddItem.png)

The grocery bag icon can be clicked to bring up the "add items" overlay. This brings up a list of the main fridge categories. Clicking one of those pops out an input form with fields for item name, quantity, date purchased, expiration date, calories, recipes.

- Date purchased autopopulates with today's date.

- Expiration date autopopulates from outside database of suggested expiration dates for certain foods.
(API?)

- Calories autopopulates from outside database of nutrition facts. (API?)

- Recipes: either user lists what recipe they will use the item in, OR it gets a list of suggested recipes from API

All fields are user-editable and not all need to be filled in. (But, of course, leaving fields blank makes your fridge not as useful.)

---

### *Data Model

*What are the persistent "nouns" you need to save across pages in your project MVP?
What do they represent?*

"Fridge" = the main database that items are stored in. Equivalent to a user account.

"Category" = food subcategories that items can be listed under.

"Item" = user-input of individual food items to be stored in database.

These could all be implemented as python classes and the specific info put into a big ol' dictionary.

---

### *Technical Components

*What are the "moving parts" of your MVP?
What are the things like "modules" you're going to write?
How do they talk to each other?*

Each "page" (or pop-up window) has specific functionality and could be considered a module on its own. They should ideally be implemented in order of importance:

Main page fridge view(0). Contents database attached. (Will be populated with "dummy" items for testing.)

Item detail view (1). This includes ability to delete items from database or move them to "tossed items" list.

Add item (5).

View tossed items (3).

Shopping list (2).

Sidebar list view of fridge (4). (Same content as (0).)

---

### *Schedule

*Write out the order in which you will tackle your technical components of your MVP.*

*What are the easy parts?
What are the hard parts?
Can you guess how long you'll take for each?*

**Most important/difficult (because I have no idea how):** *(1-2 weeks)*

~~A database to store individual fridge instances (i.e. user accounts).~~ (Moved to Further Work.)

A database to store each fridge's individual items, with attached details, and ability to add and delete items.

Database (or at this level maybe just a list/array) to store "tossed" deleted items to display on the tossed list screen.

Find and implement APIs for expiration dates, calories, suggested recipes.

**Somewhat easier:** *(1 week)*

Lots of Javascript interactivity on the main page: clicking icons to pop up new windows in the page, form inputs and so on, saving that input to the database, X to close rather than going back/refreshing the page.

Entire page layout/design, making it responsive and appealing.

Have food icons change (color? or move?) to draw attention and indicate that an item inside is close to expiring.

**Most easy/superfluous:** *(any time left over)*

Creating cute CSS/vector pictures for my food icons.



---

### *Further Work

*Here you should outline other features you'd like to implement if you get "done" early.
Order them by importance towards your high-level goal and what order you'll work on them later.*

- Add multiple-user accessibility, i.e. instead of setting up one fridge in one browser/instance, have the ability to create user accounts, log in/out, save multiple instances of fridge collections.

- Once the framework is in place, it would be easy to expand this to a "Pantry Buddy" which categorizes dry goods: things with far-out (or no) expiration dates, with similar functionality of having a list of these items available when making a shopping list to avoid buying duplicates. Also a "Cleaning Buddy" to organize chemicals and cleaning supplies. (If I were monetizing this I could charge for each "extension"! ...Even though the all do basically the same thing.)

- Same model with some tweaks could be used to make a "Closet Organizer" (sort clothing items by frequency worn, clean/dirty, tag items to wear soon, put items in "donation box" etc...)
