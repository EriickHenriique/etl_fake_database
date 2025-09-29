from faker import Faker
import random


fake = Faker('pt_BR')


# Criando Formas de Pagamentos Ficticias para Randomizar um Resultado
def payments_types() -> str:
    payment_types = [
        "Cartão de Crédito",
        "Cartão de Débito",
        "Dinheiro",
        "Boleto",
        "PIX",
        "Transferência Bancária"
    ]
    return fake.random_element(elements=payment_types)

#Criação de Produtos
def generate_product_record_focused() -> list:
    products = [
        # Eletrônicos
        ("Eletrônicos", "Smartphone Android Pro X", 1899.90, "Samsung"),
        ("Eletrônicos", "Notebook Gamer G15", 5499.00, "Dell"),
        ("Eletrônicos", "Smart TV QLED 65'", 4299.00, "LG"),
        ("Eletrônicos", "Fone Bluetooth Cancel. Ruído", 799.00, "Sony"),
        ("Eletrônicos", "Câmera Mirrorless Alpha Z", 8500.00, "Canon"),
        
        # Acessórios de Informática
        ("Acessórios", "Mouse Gamer Óptico", 249.00, "Logitech"),
        ("Acessórios", "Teclado Mecânico RGB TKL", 499.00, "Redragon"),
        ("Acessórios", "Monitor Curvo Ultrawide 34'", 2999.00, "AOC"),
        ("Acessórios", "Webcam Full HD com Microfone", 189.00, "Diversos"),
        ("Acessórios", "HD Externo 2TB USB 3.0", 350.00, "Seagate"),
        
        # Casa e Cozinha
        ("Casa", "Cafeteira Expresso Automática", 2150.00, "Nespresso"),
        ("Casa", "Air Fryer Digital 5L", 499.00, "Mondial"),
        ("Casa", "Robô Aspirador Inteligente", 1350.00, "iRobot"),
        ("Casa", "Conjunto de Panelas Antiaderente", 389.00, "Tramontina"),
        
        # Moda e Vestuário
        ("Moda", "Tênis Esportivo Performance", 529.90, "Nike"),
        ("Moda", "Relógio Smartwatch G8", 999.00, "Xiaomi"),
        ("Moda", "Mochila Executiva Impermeável", 179.90, "Samsonite"),
        
        # Mídia, Saúde e Beleza
        ("Mídia", "Ebook Reader Tela Tinta Eletrônica", 699.00, "Kindle"),
        ("Saúde", "Escova de Dente Elétrica Sônica", 350.00, "Oral-B"),
        ("Saúde", "Kit de Vitaminas e Suplementos", 120.00, "Growth"),
    ]
    
    # Desempacota a tupla do produto
    category, name_template, fixed_price, brand = fake.random_element(elements=products)
    return [category, name_template, fixed_price, brand]


#Criação do Database
def database_random(param: int): 
    result = []
    for i in range(param):
        products = generate_product_record_focused()
        result.append({
            "date_purchase": fake.date_between(start_date="-5y", end_date="-1d"),
            "client_name": fake.first_name(),
            "client_lastname": fake.last_name(),
            "state": fake.administrative_unit(),
            "birthday_client": fake.date_of_birth(minimum_age=18, maximum_age=70),
            "job": fake.job(),
            "payment_type": payments_types(),
            "price" : random.randint(1, 1000),
            "store" : random.randint(1, 12),
            "category": products[0],
            "product": products[1],
            "brand": products[3],
            "price": products[2]
        }) 
    return result




print(database_random(10))



