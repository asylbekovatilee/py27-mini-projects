from utils import get_products, update_products

def create():
    title = input("введите название: ")
    price = float(input("введите цену: "))# prinimaen dannye

    new_product = {"title":title, "price":price}#sobiraem slovar

    products = get_products()#polychaem spisok staryh pproductov
    products.append(new_product)# dobavlyaem v spisok novye dannye
    update_products(products)# perezapisyvaem fail s novymy dannymy

def read():
    products = get_products()# polychaem spisok productov
    print(products)
    for product in products:
        print(f"""
    ============================================================
    название: {product['title']}  )
    цена: {product['price']}
    =============================================
    """)