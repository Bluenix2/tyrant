import os
from typing import Optional

LEMON_NOUNS = [
    "lemonade",
    "limon",
    "citron",
    "citrus",
    "sourfruit",
    "lime",
    "melon",
    "kiwi",
    "fruit",
    "yellowfruit",
    "lemonfish"
]

LEMON_VERBS = [
    "demonic",
    "pleasant",
    "citrusy",
    "sour",
    "yellow",
    "round",
    "aromatic",
    "juicy",
    "acidic",
    "fresh",
    "sweet",
    "bitter",
    "pale",
    "plain",
]

LEMON_FACTS = [
    "Lemons are native to Asia.",
    "Lemons are a hybrid between a sour orange and a citron.",
    "Lemons are rich in vitamin C.",
    "Lemons trees can produce up to 600lbs of lemons every year.",
    "Lemon trees produce fruit all year round.",
    "Lemon zest, grated rinds, is often used in baking.",
    "Lemon tree leaves can be used to make tea.",
    "The high acidity of lemons make them good cleaning aids.",
    "California and Arizona produces most of the United States’ lemon crop.",
    "The most common types of lemons are the Meyer, Eureka, and Lisbon lemons.",
    "The name is said to have derived from an Asian word for “sour fruit”.",
    "Lemons are technically berries.",
    "Historians believe that lemons have been around since first century A.D.",
    "It is believed that they cultivated from the Mediterranean.",
    "There are three common lemons which are Bearss, Eureka and Lisbon.",
    "Lemon trees can produce up to 600 pounds in a year and can grow up to 20 feet tall.",
    "California and Arizona produce 95% of the entire lemon crop.",
    "Today, the British Navy requires all ships to carry enough lemons so that every sailor can have an ounce of juice a day.",
    "An average lemon contains eight seeds.",
    "An average lemon holds three tablespoons of juice.",
    "The juice of a lemon contains 5% of citric acid.",
    "There are roughly fifteen calories in each lemon.",
    "Sprinkling the juice on other fruits can prevent them turning brown.",
    "Lemon juice and hot water is good for a sore throat as it is anti-bacterial.",
    "Lemons used to be so rare that kings used to present them to each other as gifts.",
    "During the California Gold Rush in 1849, miners were willing to pay huge amounts of money for a single lemon.",
    "During the Renaissance, ladies used the juice of a lemon to redden their lips.",
    "For natural highlights in your hair, apply lemon juice daily, for a week.",
    "Wealthy Victorians grew lemons trees in their homes as a sign of prestige and to be a fragrant.",
    "In February and March, Menton in the French Riviera celebrates an annual lemon festival.",
    "Lemon oil is used in unsealed rosewood fingerboards of stringed instruments.",
    "The lemon shark is named for its yellowish skin.",
    "Lemons are high in vitamin C.",
    "Lemons can prevent scurvy.",
    "To power a flashlight bulb, you need 500 wired lemons to conduct electricity.",
    "The heaviest lemon was 11 pounds, 9.7 ounces in 2003.",
    "Lemon was a common unisex name in the 1900’s.",
]


class Bot:
    """Constants relating to the bot itself."""
    token: Optional[str] = os.environ.get("LEMON_DISCORD_TOKEN")
    prefix: str = "!"


class Channels:
    """Channel IDs that are relevant for this community."""
    mc_rules: int = 721496293024989265
    mc_chat: int = 721396164489904189


class Roles:
    """Roles relevant to this bot."""
    average_lemon: int = 718181055902908516
    lemon_allies: int = 718216622929739926


class Users:
    """Users relevant to this bot."""
    owner_lemon: int = 353290053377589258
