import random

def generate_instagram_post(product_name, description, price=None):
    opening = random.choice([
        f"🚀 Introducing {product_name}!",
        f"✨ Meet your new favorite — {product_name}!",
        f"🔥 {product_name} is here and it's amazing!"
    ])
    
    body = f"💡 {description}"
    
    price_line = f"💰 Special Price: ₹{price}\n🛒 Order now before stock runs out!" if price else "🛒 Limited stock available — grab yours now!"
    
    tags = f"#{product_name.replace(' ', '')} #shopnow #trending #sale #deals"
    
    return f"{opening}\n\n{body}\n\n{price_line}\n\n{tags}"


def generate_whatsapp_message(product_name, description, price=None):
    msg = f"*🌟 {product_name}*\n\n"
    msg += f"_{description}_\n\n"
    if price:
        msg += f"💰 *Price: ₹{price}*\n\n"
    msg += "📦 Limited stock!\n📞 Reply *YES* to order now!"
    return msg