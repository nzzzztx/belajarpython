from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.f6od9yz.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

list_produk = [
    {
        '#' : '1',
        'item' : 'CPU',
        'quantity': '12',
    },
    
    {
        '#' : '2',
        'item' : 'Keyboard',
        'quantity': '13',
    },

    {
        '#' : '3',
        'item' : 'Monitor',
        'quantity': '13',
    },

    {
        '#' : '4',
        'item' : 'Hardisk',
        'quantity': '15',
    },

    {
        '#' : '5',
        'item' : 'Printer',
        'quantity': '2',
    },
]

db.produks.insert_many(list_produk)