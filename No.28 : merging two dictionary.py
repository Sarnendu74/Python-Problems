#sales report of mobile shop
store = {
    "Phones": 10000,
    "Headphones": 2000,
    "Charger" : 1500,
}

#sales report of toy shop

toy = {
    "Yellow" : 5000,
    "Green" : 3333,
    "Red" : 1866
}

#merging two dictionary

merge_two_report = store.copy()
merge_two_report.update(toy)
print(sorted(merge_two_report.items(),reverse=True))
