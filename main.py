from tkinter import *
import requests
import json

pycrypto = Tk()
pycrypto.title("My crypto portfolio")
pycrypto.iconbitmap('fav.ico')


def font_color(amount):
    if amount >= 0:
        return "green"
    else:
        return "red"


def my_portfolio():
    api_request = requests.get(
        "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=10&convert=USD&CMC_PRO_API_KEY=bb496eb4-b857-467c-86de-efeb2f89f79f")

    api = json.loads(api_request.content)

    # Now I would be adding my own coin that I've invested
    # coins = ["BTC", "ADA", "SOL"] Instead of list let's store it in a dictionary like json file
    # coin name, amount no. of coins bought, price at which bought

    print("<------------>")
    print("<------------>")

    coins = [
        {
            "symbol": "BTC",
            "amount_owned": 2,
            "price_per_coin": 19100.59
        },
        {
            "symbol": "ADA",
            "amount_owned": 15,
            "price_per_coin": 0.99
        },
        {
            "symbol": "SOL",
            "amount_owned": 6,
            "price_per_coin": 31.46
        }
    ]

    total_pl = 0
    coin_row = 1  # bc 0th row will always be heading
    total_current_value = 0

    # whenever I am hitting the run button I am sending a request so these req are counted in database and the daashboard
    # I want info only of my portfolio
    for i in range(0, 10):  # remember 5 is not included
        for coin in coins:
            # if the current coin is equal to my coin in list
            if api["data"][i]["symbol"] == coin["symbol"]:
                total_paid = coin["amount_owned"] * coin["price_per_coin"]
                current_value = coin["amount_owned"] * \
                    api["data"][i]["quote"]["USD"]["price"]
                pl_percoin = api["data"][i]["quote"]["USD"]["price"] - \
                    coin["price_per_coin"]
                total_pl_coin = pl_percoin * coin["amount_owned"]

                total_pl = total_pl + total_pl_coin
                total_current_value = total_current_value + current_value

                # print(api["data"][i]["name"] + " - " + api["data"][i]["symbol"])
                # print("Price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
                # print("Number of Coin: ", coin["amount_owned"])
                # print("Total Amount Paid: ", "${0:.2f}".format(total_paid))
                # print("Current Value: ", "${0:.2f}".format(current_value))
                # print("P/L Per coin: ", "${0:.2f}".format(pl_percoin))
                # print("Total P/L with coin: ","${0:.2f}".format(total_pl_coin))
                # print("------------")

                name = Label(
                    pycrypto, text=api["data"][i]["symbol"], bg="#DDDDDD", fg="black", font="Segoe 12", padx="5", pady="5", borderwidth=2, relief="groove")
                name.grid(row=coin_row, column=0, sticky=N+S+E+W)

                price = Label(pycrypto, text="${0:.2f}".format(
                    api["data"][i]["quote"]["USD"]["price"]), bg="#DDDDDD", fg="black", font="Segoe 12", padx="5", pady="5", borderwidth=2, relief="groove")
                price.grid(row=coin_row, column=1, sticky=N+S+E+W)

                no_coins = Label(
                    pycrypto, text=coin["amount_owned"], bg="#DDDDDD", fg="black", font="Segoe 12", padx="5", pady="5", borderwidth=2, relief="groove")
                no_coins.grid(row=coin_row, column=2, sticky=N+S+E+W)

                amount_paid = Label(pycrypto, text="${0:.2f}".format(
                    total_paid), bg="#DDDDDD", fg="black", font="Segoe 12", padx="5", pady="5", borderwidth=2, relief="groove")
                amount_paid.grid(row=coin_row, column=3,  sticky=N+S+E+W)

                current_val = Label(pycrypto, text="${0:.2f}".format(current_value), bg="#DDDDDD", fg=font_color(float(
                    "{0:.2f}".format(current_value))), font="Segoe 12", padx="5", pady="5", borderwidth=2, relief="groove")
                current_val.grid(row=coin_row, column=4, sticky=N+S+E+W)

                pl_coin = Label(pycrypto, text="${0:.2f}".format(
                    pl_percoin), bg="#DDDDDD", fg=font_color(float("{0:.2f}".format(pl_percoin))), font="Segoe 12", padx="5", pady="5", borderwidth=2, relief="groove")
                pl_coin.grid(row=coin_row, column=5, sticky=N+S+E+W)

                totalpl = Label(pycrypto, text="${0:.2f}".format(
                    total_pl_coin), bg="#DDDDDD", fg=font_color(float(
                        "{0:.2f}".format(total_pl_coin))), font="Segoe 12", padx="5", pady="5", borderwidth=2, relief="groove")
                totalpl.grid(row=coin_row, column=6, sticky=N+S+E+W)

                coin_row = coin_row + 1

    # print("Total P/L for Portfolio: ", "${0:.2f}".format(total_pl))
    totalcv = Label(pycrypto, text="${0:.2f}".format(
        total_current_value), bg="#DDDDDD", fg="black", font="Segoe 12", padx="5", pady="5", borderwidth=2, relief="groove")
    totalcv.grid(row=coin_row, column=4, sticky=N+S+E+W)

    totalpl = Label(pycrypto, text="${0:.2f}".format(
        total_pl), bg="#DDDDDD", fg=font_color(float("{0:.2f}".format(total_pl))), font="Segoe 12", padx="5", pady="5", borderwidth=2, relief="groove")
    totalpl.grid(row=coin_row, column=6, sticky=N+S+E+W)


name = Label(pycrypto, text="Coin Name", bg="#30475E", fg="#DDDDDD",
             font="Segoe 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
name.grid(row=0, column=0, sticky=N+S+E+W)

price = Label(pycrypto, text="Price", bg="#30475E", fg="#DDDDDD",
              font="Segoe 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
price.grid(row=0, column=1, sticky=N+S+E+W)

no_coin = Label(pycrypto, text="Coin Owned", bg="#30475E", fg="#DDDDDD",
                font="Segoe 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
no_coin.grid(row=0, column=2, sticky=N+S+E+W)

amount_paid = Label(pycrypto, text="Total amount paid", bg="#30475E", fg="#DDDDDD",
                    font="Segoe 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
amount_paid.grid(row=0, column=3, sticky=N+S+E+W)

current_val = Label(pycrypto, text="Current Value", bg="#30475E", fg="#DDDDDD",
                    font="Segoe 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
current_val.grid(row=0, column=4, sticky=N+S+E+W)

pl_coin = Label(pycrypto, text="P/L Per coin", bg="#30475E", fg="#DDDDDD",
                font="Segoe 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
pl_coin.grid(row=0, column=5, sticky=N+S+E+W)

totalpl = Label(pycrypto, text="Total P/L", bg="#30475E", fg="#DDDDDD",
                font="Segoe 12 bold", padx="5", pady="5", borderwidth=2, relief="groove")
totalpl.grid(row=0, column=6, sticky=N+S+E+W)

# Calling the api function to retrieve the coins
my_portfolio()

pycrypto.mainloop()

print("Program completed")
