from tkinter import *
import requests
import json
import sqlite3

pycrypto = Tk()
pycrypto.title("My crypto portfolio")
pycrypto.iconbitmap('fav.ico')

# adding database
con = sqlite3.connect('coin.db')
cursorObj = con.cursor()

cursorObj.execute(
    "CREATE TABLE IF NOT EXISTS coins(id INTEGER PRIMARY KEY, symbol TEXT, amount INTEGER, price REAL)")
con.commit()


def font_color(amount):
    if amount >= 0:
        return "green"
    else:
        return "red"


def my_portfolio():
    api_request = requests.get(
        "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=10&convert=USD&CMC_PRO_API_KEY=bb496eb4-b857-467c-86de-efeb2f89f79f")

    api = json.loads(api_request.content)

    # Taking data from the DB
    cursorObj.execute("SELECT * FROM coins")
    coins = cursorObj.fetchall()

    total_pl = 0
    coin_row = 1  # bc 0th row will always be heading
    total_current_value = 0

    # I want info only of my portfolio
    for i in range(0, 10):  # remember 5 is not included
        for coin in coins:
            # if the current coin is equal to my coin in list
            if api["data"][i]["symbol"] == coin[1]:
                total_paid = coin[2] * coin[3]
                current_value = coin[2] * \
                    api["data"][i]["quote"]["USD"]["price"]
                pl_percoin = api["data"][i]["quote"]["USD"]["price"] - \
                    coin[3]
                total_pl_coin = pl_percoin * coin[2]

                total_pl = total_pl + total_pl_coin
                total_current_value = total_current_value + current_value

                # print(api["data"][i]["name"] + " - " + api["data"][i]["symbol"])
                # print("Price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
                # print("Number of Coin: ", coin[2])
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
                    pycrypto, text=coin[2], bg="#DDDDDD", fg="black", font="Segoe 12", padx="5", pady="5", borderwidth=2, relief="groove")
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

    # Once all the loop is printed and the data is printed I will be clear the api so that
    # when I click update new data is printed

    api = ""

    update = Button(pycrypto, text="Update", bg="#DDDDDD", fg="black", command=my_portfolio,
                    font="Segoe 12", padx="5", pady="5", borderwidth=2, relief="groove")
    update.grid(row=coin_row+1, column=6, sticky=N+S+E+W)


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

# closing database
cursorObj.close()
con.close()
