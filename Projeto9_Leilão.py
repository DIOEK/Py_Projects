from replit import clear
VARIAVEL_DE_MANUTENCAO_DE_CICLO = True
print("This is a secret auction, please place your bets everyone.")
auction_documents = {}
while VARIAVEL_DE_MANUTENCAO_DE_CICLO:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    guest_documents = {
        f"{name}" : bid
    }
    auction_documents.update(guest_documents)
    yes_or_no = input("Are there any other bidders? Type 'yes' or 'no': ")
    VARIAVEL_DE_MANUTENCAO_DE_CICLO = yes_or_no.lower()
    if VARIAVEL_DE_MANUTENCAO_DE_CICLO == 'yes':
       clear()
    if VARIAVEL_DE_MANUTENCAO_DE_CICLO == "no": #make an elif afterwords
        VARIAVEL_DE_MANUTENCAO_DE_CICLO = False
print(auction_documents)
highest_bid = 0
for key in auction_documents:
    print(key)
    print(auction_documents[key])
    if auction_documents[key] > highest_bid:
        winner = key
print(f"The winner is {key}!")


