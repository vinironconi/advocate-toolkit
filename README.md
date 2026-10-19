# Essential Oil Advocate Toolkit
#### Video Demo:


#### Description:
This is a toolkit that uses data to get the important information of products in different currencies. It's a program i built for advocates in Paraguay and Brazil to help them close a deal. I noticed it took quite a lot of time to look up the prices, pv and essential information about a product, changing currencies without knowing the exchange rate, etc... So I built this program to help me and all on my team to focus our time on more important things.
- Pv(point value): It's a number all products have that is used to reach certain rewards and to receive commissions.


## Features
- **Order Builder**: The program has a feature to save a product and its quantity, so that users can see, after all the calculations, how many products it saved, their prices and pv from the products.
- **Search**: The search feature is where the user only wants the information about a product so this search mechanism only gives out important information about a product
- **Two Currencies**: doTERRA does not have official Guaranis prices yet, so the function works as a way to facilitate the user to the prices in guarani as well as reais. The program has a feature that first asks the user for their currency, and if later changed all the prices updates to the new currency.
- **Pv Goal**: Most advocates have a pv goal they need to achieve, so instead of just showing the pv from a program it also calculates the pvs in the order and shows the user how many pv remaining(if any) they need to achieve their goal
- **Input Validation**: Most of the program was made using input validation, this was made to facilitate the users input and to reduce the amount of possible bugs on the program.


## How to run
- What you need first: Python 3 installed
- Get the code: Download it from GitHub or clone it from GitHub
- Install the libraries:
```bash
pip install -r requirements.txt
```
- Start the program:
```bash
python project.py
```
You should see the program asking you which currencies you desire!
- Test the program:
```bash
pytest test_project.py
```
You should see that all the tests have passed.


## Files
- **project.py**: this is the main file needed to run the program, and all the required code is here
    - **main**: This is where you call all the other functions and it goes into an infinite loop until the user exits the program.
    - **get_currency**: This function lets the user select and then later change the current currency used in the program. There are only two valid currencies and the user must choose one or the other.
    - **load_products**: All of the products from the csv file get loaded here.
    - **search_products**: This is a function to return the products during a search in the program. It does not matter if the search is uppercase or lowercase and a blank search returns an empty list.
    - **calculate_total**: This is a function to return the total cost of an order, that uses two price types, members and regular.
    - **to_guaranis**: A function to change the price from reais to guaranis, using a fixed exchange rate. It also rounds the number to the nearest 1000.
    - **calculate_pv**: Function to calculate the total pv times the quantity of the product in an order.
    - **pv_remaining**: The remaining pv that needs to be reached to beat the pv goal is calculated here.
    - **add_to_order**: Adding the products in a saved order is in this code. If there are multiple matches when searching, the program asks the user to be more specific.
    - **show_products**: This is the function where the products from the dict are shown, with their current cost based on the currency chosen. If there are no products a message will show that no products were found.
    - **show_order**: This is the function to show the saved order to the user.
- **test_project.py**: Was used to test the calculation and most important features. It tested the pv_remaining function if changes in the pv still worked properly. The search_products was also tested and returned the products as required. All the calculating functions were tested and they all gave the results as expected. For example almost if a user searches in all caps it still finds the product, or if the pv goal has been reached the number returned is 0, meaning they reached their goal.
- **requirements.txt**: Is the required installs that i used in the code.
- **products.csv**: Is the data the program uses. It has a SKU to identify the product. It also has the name, size and category of each product. The two prices a product has, member prices for discount, and retail prices, and a pv to each product.


## Design Choices
- Why a CSV file? There are hundreds of products on the website, and to hardcode them into the code would take a long time to test and the project would honestly just not work.
- Why does all the math only use Reais instead of guaranis? doTERRA's website has only prices in reais, so I make all the calculations before I change the currency to guaranis.
- Why round the guaranis to the nearest 1.000? This is so that the product doesn't give broken prices(Ex: 123.750)
- Why does adding to order ask the user to be more specific? There are lots of products that use the same flower, lavender has the oil and a body splash for example, so the user needs to give precise input so the program can add the correct product.
- Why are print functions separate from calculating functions? This was made precisely for testing


## Future Improvements
This project will be made into a web version, with Flask, so that people can use it on other devices and not only in the terminal.


## Disclaimer
- This program is not affiliated or endorsed by doTERRA.


## AI Use
- Claude was used to create the starting skeleton, explained concepts and reviewed the code. All the functions were either created entirely by me or were modified by me.
