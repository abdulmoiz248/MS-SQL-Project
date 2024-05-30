import string
import pyodbc
from faker import Faker
import random

# Connection details
Driver = 'SQL Server'
server = 'DESKTOP-EQ55Q8H'
database = 'tempfinalfinal'

# Connection string
connection = f"DRIVER={{{Driver}}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"

try:
    # Establishing connection
    conn = pyodbc.connect(connection)
    cursor = conn.cursor()

    fake = Faker('en_US')
    pakistan_cities = [
        "Karachi", "Lahore", "Faisalabad", "Rawalpindi", "Multan", "Gujranwala", "Islamabad", "Hyderabad",
        "Peshawar", "Quetta", "Sargodha", "Sialkot", "Bahawalpur", "Sukkur", "Larkana", "Sheikhupura",
        "Rahim Yar Khan", "Jhang", "Dera Ghazi Khan", "Gujrat", "Sahiwal", "Wah Cantonment", "Mardan",
        "Kasur", "Okara", "Mingora", "Nawabshah", "Chiniot", "Kotri", "Kāmoke", "Hafizabad", "Sadiqabad",
        "Mirpur Khas", "Burewala", "Kohat", "Khanewal", "Dera Ismail Khan", "Turbat", "Muzaffargarh",
        "Abbotabad", "Mandi Bahauddin", "Shikarpur", "Jacobabad", "Jhelum", "Khanpur", "Khairpur", "Khuzdar",
        "Pakpattan", "Hub", "Daska", "Gojra", "Dadu", "Muridke", "Bahawalnagar", "Samundri", "Tando Allahyar"
    ]
    men = [
        "Aamir", "Abbas", "Abdul", "Abdullah", "Abid", "Abrar", "Adam", "Adil", "Adnan", "Afzal",
        "Ahmad", "Ahmed", "Ahsan", "Ajmal", "Akbar", "Akhtar", "Alauddin", "Ali", "Amir", "Ammar",
        "Amjad", "Anas", "Anees", "Anwar", "Arif", "Arslan", "Asad", "Asghar", "Ashfaq", "Ashraf",
        "Asif", "Ata", "Atif", "Awais", "Ayan", "Azeem", "Azhar", "Aziz", "Babar", "Bashir",
        "Bilal", "Burhan", "Danish", "Dawood", "Ehsan", "Ejaz", "Emad", "Faheem", "Faisal", "Faraz",
        "Farhan", "Farrukh", "Fawad", "Feroz", "Furqan", "Ghaffar", "Ghalib", "Ghaus", "Ghulam", "Habib",
        "Haider", "Hamid", "Hamza", "Hanif", "Haroon", "Hashim", "Hasnain", "Hassan", "Hussain", "Ibrahim",
        "Idris", "Iftikhar", "Imad", "Imran", "Inam", "Iqbal", "Irshad", "Irtaza", "Ishtiaq", "Ishaq",
        "Ismail", "Jabbar", "Jafar", "Jamal", "Jawad", "Junaid", "Kabir", "Kaleem", "Kamran", "Kashif",
        "Kazim", "Khalid", "Khizar", "Khurshid", "Latif", "Luay", "Luqman", "Mansoor", "Masood", "Mateen",
        "Mehmood", "Miftah", "Mikael", "Mirza", "Moazzam", "Moeen", "Mohammad", "Mohammed", "Moin", "Momin",
        "Mubashir", "Mudasir", "Mufti", "Muhammad", "Mukhtar", "Munir", "Murtaza", "Mushtaq", "Mustafa", "Nabeel",
        "Nadeem", "Naeem", "Najeeb", "Najib", "Naseem", "Nasir", "Nawaz", "Nazar", "Nazim", "Nisar",
        "Noman", "Numan", "Nusrat", "Omar", "Osama", "Parvez", "Qadeer", "Qadir", "Qasim", "Rafi",
        "Rafiq", "Rahim", "Raheel", "Rameez", "Rashid", "Rauf", "Rayyan", "Rehan", "Riaz", "Rizwan",
        "Saad", "Saeed", "Safi", "Sajid", "Sajjad", "Salman", "Sami", "Saqib", "Sarfaraz", "Shabbir",
        "Shadab", "Shafi", "Shafqat", "Shahid", "Shakeel", "Shakil", "Shamim", "Shan", "Sharif", "Shehzad",
        "Sheraz", "Shibli", "Shoaib", "Sikandar", "Sohail", "Sultan", "Talha", "Tariq", "Tayyab", "Tufail",
        "Umair", "Umar", "Usama", "Usman", "Waqas", "Wasim", "Yahya", "Yasir", "Yousaf", "Yusuf",
        "Zafar", "Zahid", "Zain", "Zaheer", "Zakir", "Zubair", "Zulfiqar", "Abdulaziz", "Abdulbaqi", "Abdulbari",
        "Abdulfattah", "Abdulkadir", "Abdulkareem", "Abdullah", "Abdulmohsen", "Abdulrahman", "Abdulrahim",
        "Abdulrashid", "Abdurahman", "Abdussalam",
        "Abid", "Abu", "Adel", "Adham", "Adil", "Adnan", "Afif", "Ahmad", "Aiman", "Ajmal",
        "Akeem", "Alaa", "Ali", "Ameen", "Amjad", "Amro", "Anas", "Anees", "Aqeel", "Arafat",
        "Areeb", "Arfan", "Arif", "Arkan", "Arman", "Arshad", "Asad", "Ashfaq", "Ashraf", "Asif",
        "Aslam", "Ata", "Atif", "Ayman", "Ayyub", "Ayaz", "Azam", "Azeem", "Azfar", "Azhar",
        "Aziz", "Badar", "Baha", "Baqir", "Bashir", "Bilal", "Burhan", "Dawood", "Dhiya", "Dilawar",
        "Ehsan", "Elahi", "Elias", "Emad", "Emran", "Essa", "Eyman", "Fadi", "Fadil", "Fahad",
        "Fahim", "Faizan", "Fakhruddin", "Faraz", "Fareed", "Farhan", "Farrukh", "Fawad", "Fawzi", "Fayez",
        "Feroz", "Fuad", "Furqan", "Ghaith", "Ghazi", "Ghulam", "Habib", "Hafeez", "Hafiz", "Haider",
        "Hameed", "Hamid", "Hamza", "Hanif", "Harith", "Haroon", "Haseeb", "Hashim", "Hassan", "Hatem",
        "Hussain", "Hussam", "Ibrahim", "Idris", "Iftikhar", "Ihsan", "Ikram", "Imad", "Imran", "Irfan",
        "Irtaza", "Isam", "Ishtiaq", "Ismail", "Jabbar", "Jafar", "Jamal", "Jawad", "Jibril", "Junaid",
        "Kabeer", "Kamal", "Kamran", "Karam", "Kashif", "Khaled", "Khalid", "Khaleel", "Khayyam", "Khurram",
        "Latif", "Luqman", "Majeed", "Mansoor", "Marwan", "Masood", "Mateen", "Mehdi", "Mehmood", "Moin",
        "Moiz", "Mohammad", "Mohammed", "Momin", "Mudassar", "Mueen", "Mujahid", "Mukhtar", "Munir", "Murtaza",
        "Mustafa", "Nabeel", "Nadeem", "Naeem", "Najeeb", "Najib", "Naseem", "Nasir", "Nawaz", "Nazir",
        "Nisar", "Noman", "Numan", "Nusrat", "Omar", "Osama", "Parvez", "Qadir", "Qasim", "Qays",
        "Rafi", "Rafiq", "Raheel", "Rahim", "Raouf", "Rashid", "Rauf", "Rayyan", "Rehan", "Riaz",
        "Rizwan", "Saad", "Saeed", "Safi", "Sajid", "Sajjad", "Salman", "Sami", "Saqib", "Sarfaraz",
        "Shabbir", "Shadab", "Shafi", "Shafqat", "Shahid", "Shakeel", "Shakil", "Shamim", "Shan", "Sharif",
        "Shehzad", "Sheraz", "Shibli", "Shoaib", "Sikandar", "Sohail", "Sultan", "Talha", "Tariq", "Tayyab",
        "Tufail", "Umair", "Umar", "Usama", "Usman", "Waqas", "Wasim", "Yahya", "Yasir", "Yousaf",
        "Yusuf", "Zafar", "Zahid", "Zain", "Zaheer", "Zakir", "Zubair", "Zulfiqar"
    ]

    women = [
        "Aaliyah", "Aasma", "Abeer", "Abida", "Adeela", "Aeesha", "Afifa", "Afnan", "Afsana", "Ayesha",
        "Ahlam", "Aisha", "Aleena", "Aliya", "Amal", "Amara", "Ambreen", "Amina", "Aminah", "Amna",
        "Anam", "Anisa", "Anusha", "Arfa", "Arisha", "Arwa", "Asifa", "Asma", "Ayesha", "Aziza",
        "Badia", "Basma", "Batool", "Bibi", "Bilqis", "Bushra", "Dania", "Daniah", "Dilshad", "Duaa",
        "Durrah", "Emaan", "Eman", "Erum", "Esma", "Farah", "Fareeha", "Farida", "Fatema", "Fatemah",
        "Fatima", "Fatimah", "Fauzia", "Fawzia", "Fiza", "Fouzia", "Ghazala", "Gul", "Gulzar", "Habiba",
        "Hafsa", "Hafsah", "Haifa", "Haleema", "Hanan", "Hania", "Haniya", "Hanin", "Haseena", "Hawa",
        "Heba", "Hina", "Hira", "Huda", "Humaira", "Husna", "Ibtisam", "Iffat", "Ihsan", "Ikram",
        "Ilham", "Inaya", "Iqra", "Irsa", "Irum", "Isha", "Jameela", "Jamila", "Javeria", "Jihan",
        "Juwairiyah", "Khadija", "Khadijah", "Khalida", "Kiran", "Kulsoom", "Kulthum", "Laila", "Laiba", "Lina",
        "Lubna", "Luqma", "Maheen", "Mahira", "Mahnoor", "Maira", "Malaika", "Maliha", "Marwa", "Maryam",
        "Meher", "Mehreen", "Mina", "Mishal", "Mishkat", "Mona", "Mubeena", "Mumtaz", "Munira", "Munni",
        "Nabila", "Nadia", "Nadine", "Nafisa", "Naila", "Naima", "Najat", "Najma", "Nargis", "Nashwa",
        "Nasreen", "Nazia", "Nelofer", "Nida", "Nigar", "Nihal", "Nimra", "Noreen", "Nuha", "Nusrat",
        "Nuzhat", "Omaima", "Parveen", "Qamar", "Quratulain", "Rabia", "Rafia", "Rafiah", "Rafia", "Raja",
        "Ramla", "Rania", "Raniyah", "Rashida", "Razia", "Reema", "Rida", "Rimsha", "Rina", "Roma",
        "Rosa", "Rubab", "Rubeena", "Rubina", "Ruhina", "Rukhsana", "Ruqayyah", "Saadia", "Saba", "Sabeen",
        "Sabina", "Sabira", "Sabreen", "Sadaf", "Sadia", "Safa", "Safiya", "Sahar", "Sahira", "Saima",
        "Saira", "Sakina", "Salma", "Sameena", "Samia", "Samina", "Sana", "Sanam", "Sania", "Sara",
        "Sariyah", "Saba", "Shabana", "Shaista", "Shakira", "Shama", "Shamim", "Shanaz", "Shazia", "Sheema",
        "Shehla", "Shereen", "Shifa", "Shireen", "Shirin", "Sobia", "Sohaila", "Sonia", "Soraya", "Sumaiya",
        "Sumaya", "Sundus", "Suraiya", "Suriya", "Tabassum", "Tahira", "Taiba", "Tala", "Tamanna", "Tania",
        "Tasneem", "Uzma", "Wafa", "Wajiha", "Warda", "Wasila", "Yasmin", "Yasmine", "Yusra", "Zainab",
        "Zakia", "Zainab", "Zainab", "Zakia", "Zakiyah", "Zamzam", "Zara", "Zehra", "Zeinab", "Zohra",
        "Zoya", "Zubeida", "Zulekha", "Zunaira", "Aafreen", "Aala", "Aalya", "Aaminah", "Aatika", "Aatiya",
        "Aayat", "Abeer", "Adeeba", "Adeelah", "Adiba", "Adila", "Afifah", "Afra", "Afsar", "Afyah",
        "Ahana", "Ahmara", "Aida", "Ailah", "Aiman", "Aini", "Aira", "Akifah", "Aksa", "Alaya",
        "Aleemah", "Alina", "Alishba", "Almas", "Almaas", "Alvina", "Ambar", "Ameena", "Amirah", "Amra",
        "Amreen", "Ana", "Anan", "Anayah", "Andleeb", "Aniqa", "Anjum", "Ansha", "Anwaar", "Aqsa",
        "Arfa", "Arisha", "Arub", "Arwa", "Asbah", "Ashra", "Asiyah", "Atika", "Atiya", "Azhar",
        "Azizah", "Badriya", "Bahar", "Balqis", "Barkah", "Bashira", "Basimah", "Batool", "Benazir", "Bibiana",
        "Bishara", "Bisma", "Bushra", "Daisha", "Dalia", "Dania", "Daniah", "Danya", "Deeba", "Delara",
        "Dilara", "Durra", "Eesha", "Eilia", "Eliza", "Emira", "Emra", "Erum", "Eshaal", "Eshal",
        "Ezza", "Fadia", "Fadilah", "Faheema", "Faiqa", "Faiqah", "Faiza", "Faizah", "Falak", "Fara",
        "Fareena", "Farha", "Farhana", "Farida", "Fariha", "Fariya", "Fauzia", "Fawzia", "Ferhana", "Fiza",
        "Fouzia", "Gehan", "Ghadah", "Ghazala", "Ghazal", "Ghina", "Gul", "Gulalai", "Gulbano", "Habeeba",
        "Hafsa", "Hajrah", "Hajira", "Hala", "Haleema", "Hamida", "Hanaa", "Hanifa", "Hani", "Hania",
        "Haniyah", "Haniya", "Hannah", "Hasna", "Hawra"
    ]
    product_categories = [
    "Electronics", "Clothing", "Home & Kitchen", "Books", "Toys & Games",
    "Beauty & Personal Care", "Sports & Outdoors", "Automotive", "Health & Wellness",
    "Grocery & Gourmet Food", "Office Products", "Pet Supplies", "Tools & Home Improvement",
    "Musical Instruments", "Furniture", "Jewelry", "Shoes", "Watches",
    "Baby", "Outdoor Recreation", "Luggage & Travel", "Fitness & Exercise",
    "Home Decor", "Crafts & Hobbies", "Party Supplies"
    ]

    category_products = {
        "Electronics": [
            "Blender", "Microwave", "Refrigerator", "Washing Machine", "Vacuum Cleaner",
            "Television", "Computer", "Laptop", "Tablet", "Smartphone",
            "Speaker", "Headphones", "Camera", "Drone", "Projector",
            "Gaming Console", "Virtual Reality Headset", "Smartwatch", "Fitness Tracker",
            "Smart Home Hub", "Wireless Earbuds", "Portable Charger", "Gaming Mouse", "Keyboard"
        ],
        "Clothing": [
            "Shirt", "Pants", "Dress", "Skirt", "Jacket",
            "Sweater", "Shoes", "Boots", "Sandals", "Hat",
            "Underwear", "Socks", "Jewelry", "Scarf", "Sunglasses",
            "Swimwear", "Activewear", "Sleepwear", "Cosplay Costume",
            "Pajamas", "Leggings", "T-Shirt", "Dress Pants", "Formal Dress"
        ],
        "Home & Kitchen": [
            "Pots and Pans", "Dishes", "Flatware", "Utensils", "Cutlery Sets",
            "Coffee Maker", "Toaster", "Blender", "Food Processor", "Microwave",
            "Stove", "Oven", "Refrigerator", "Freezer", "Dishwasher",
            "Vacuum Cleaner", "Iron", "Ironing Board", "Trash Can", "Storage Containers",
            "Mixing Bowls", "Measuring Cups", "Knives", "Cutting Board", "Can Opener"
        ],
        "Books": [
            "The Lord of the Rings", "Jane Eyre", "Animal Farm", "Brave New World", "The Iliad",
            "Crime and Punishment", "Wuthering Heights", "Great Expectations", "The Divine Comedy",
            "A Tale of Two Cities",
            "Les Misérables", "The Brothers Karamazov", "Catch-22", "The Grapes of Wrath", "Slaughterhouse-Five",
            "The Adventures of Huckleberry Finn", "The Count of Monte Cristo", "Gone with the Wind", "Don Quixote",
            "The Scarlet Letter",
            "One Hundred Years of Solitude", "The Picture of Dorian Gray", "Dracula", "Madame Bovary", "Frankenstein",
            "The Metamorphosis", "Sense and Sensibility", "Anna Karenina", "A Clockwork Orange", "Heart of Darkness",
            "The Stranger", "Ulysses", "East of Eden", "A Farewell to Arms", "Rebecca",
            "Lord of the Flies", "The Shining", "The Road", "The Old Man and the Sea", "Lolita",
            "Beloved", "Middlemarch", "The Wind in the Willows", "The Call of the Wild", "Dune",
            "The Sun Also Rises", "Of Mice and Men", "The Name of the Rose", "The Secret Garden", "The Handmaid's Tale",
            "The Alchemist", "The Book Thief", "Life of Pi", "The Girl with the Dragon Tattoo", "Memoirs of a Geisha",
            "The Time Traveler's Wife", "The Help", "Water for Elephants", "The Hunger Games", "The Fault in Our Stars",
            "Twilight", "Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets",
            "Harry Potter and the Prisoner of Azkaban", "Harry Potter and the Goblet of Fire",
            "Harry Potter and the Order of the Phoenix", "Harry Potter and the Half-Blood Prince",
            "Harry Potter and the Deathly Hallows", "The Maze Runner", "Divergent",
            "The Giver", "Ender's Game", "Ready Player One", "The Chronicles of Narnia",
            "The Hitchhiker's Guide to the Galaxy",
            "The Martian", "A Game of Thrones", "American Gods", "The Road to Serfdom",
            "Sapiens: A Brief History of Humankind",
            "Educated", "Becoming", "Steve Jobs", "The Wright Brothers", "Unbroken",
            "Into the Wild", "Quiet: The Power of Introverts in a World That Can't Stop Talking",
            "Thinking, Fast and Slow", "Outliers: The Story of Success", "Grit: The Power of Passion and Perseverance"
        ],
        "Toys & Games": [
            "Action Figure", "Doll", "Board Game", "Card Game", "Puzzle",
            "Building Set", "Stuffed Animal", "Remote Control Car", "Art Set", "Musical Instrument (Toy)",
            "Sports Equipment (Toy)", "Dress-Up Clothes (Toy)", "Slime Kit", "Science Kit", "Legos",
            "Play Kitchen", "Play Tent", "Building Blocks", "Educational Toy", "Board Game (Classic)"
        ],
        "Beauty & Personal Care": [
            "Shampoo", "Conditioner", "Soap", "Lotion", "Body Wash",
            "Makeup", "Skincare", "Haircare", "Fragrance", "Shaving Supplies",
            "Nail Care", "Dental Care", "Bath Products", "Men's Grooming", "Cosmetics",
            "Makeup Brushes", "Hair Styling Tools", "Sunblock", "Deodorant", "Moisturizer"
        ],
        "Sports & Outdoors": [
            "Basketball", "Baseball", "Football", "Soccer Ball", "Tennis Racket",
            "Golf Club", "Bicycle", "Camping Tent", "Sleeping Bag", "Hiking Boots",
            "Fishing Rod", "Kayak", "Swimsuit", "Sunscreen", "Water Bottle",
            "Yoga Mat", "Fitness Tracker (watch)", "Sports Apparel", "Camping Stove", "Tent Lamp"
        ],
        "Automotive": [
            "Car Battery", "Engine Oil", "Tires", "Windshield Wipers", "Floor Mats",
            "Car Seat", "Headlights", "Tail Lights", "Car Wash Kit", "Jump Starter",
            "GPS Navigation", "Dash Cam", "Car Vacuum Cleaner", "Air Freshener", "Car Cover",
            "Windshield Washer Fluid", "Brake Pads", "Antifreeze", "Oil Filter", "Car Wax"
        ],
        "Health & Wellness": [
            "Vitamins", "Pain Relief Medication", "Allergy Medication", "Cold & Flu Medication", "First-Aid Kit",
            "Paper Towels", "Toilet Paper", "Trash Bags", "Cleaning Supplies", "Laundry Detergent",
            "Dish Soap", "Sponges", "Air Purifier", "Humidifier", "Thermometer"
        ],
        "Musical Instruments": [
            "Guitar", "Piano", "Violin", "Drums", "Flute",
            "Trumpet", "Saxophone", "Clarinet", "Keyboard", "Microphone",
            "Amplifier", "Speaker", "Music Stand", "Metronome", "Tuner"
        ],
        "Furniture": [
            "Sofa", "Bed", "Dining Table", "Coffee Table", "Desk",
            "Chair", "Wardrobe", "Bookshelf", "Cabinet", "Dresser",
            "Nightstand", "Futon", "TV Stand", "Ottoman", "Bean Bag Chair"
        ],
        "Jewelry": [
            "Necklace", "Earrings", "Bracelet", "Ring", "Pendant",
            "Anklet", "Brooch", "Charm", "Cufflinks", "Watch",
            "Body Jewelry", "Jewelry Box", "Jewelry Cleaner", "Jewelry Display", "Pearls"
        ],
        "Shoes": [
            "Sneakers", "Boots", "Sandals", "Heels", "Flats",
            "Loafers", "Oxfords", "Espadrilles", "Slippers", "Athletic Shoes",
            "Hiking Boots", "Dress Shoes", "Work Boots", "Platform Shoes", "Wedge Sandals"
        ],
        "Watches": [
            "Analog Watch", "Digital Watch", "Smartwatch", "Sports Watch", "Dress Watch",
            "Chronograph Watch", "Automatic Watch", "Mechanical Watch", "Skeleton Watch", "Pocket Watch",
            "Fitness Tracker (watch)", "Dive Watch", "Pilot Watch", "Field Watch", "Racing Watch"
        ],
        "Baby": [
            "Diapers", "Baby Wipes", "Baby Food", "Baby Bottles", "Pacifiers",
            "Baby Clothes", "Baby Shoes", "Baby Blankets", "Baby Carrier", "Baby Monitor",
            "Stroller", "Car Seat", "High Chair", "Baby Toys", "Baby Books"
        ],
        "Outdoor Recreation": [
            "Camping Tent", "Sleeping Bag", "Hiking Backpack", "Backpack", "Sleeping Pad",
            "Camp Stove", "Lantern", "Flashlight", "Camp Chair", "Cooler",
            "Hammock", "Outdoor Table", "Folding Chair", "Portable Grill", "Water Purifier"
        ],
        "Luggage & Travel": [
            "Suitcase", "Carry-On Bag", "Duffel Bag", "Backpack", "Weekender Bag",
            "Garment Bag", "Laptop Bag", "Tote Bag", "Travel Organizer", "Packing Cubes",
            "Travel Pillow", "Travel Adapter", "Luggage Scale", "Passport Holder", "Luggage Tag"
        ],
        "Fitness & Exercise": [
            "Dumbbells", "Kettlebell", "Resistance Bands", "Yoga Mat", "Exercise Ball",
            "Jump Rope", "Foam Roller", "Exercise Bike", "Treadmill", "Elliptical Machine",
            "Rowing Machine", "Weight Bench", "Pull-Up Bar", "Punching Bag", "Boxing Gloves"
        ],
        "Home Decor": [
            "Wall Art", "Picture Frame", "Vase", "Candle Holder", "Sculpture",
            "Mirrors", "Rug", "Throw Blanket", "Throw Pillow", "Curtains",
            "Clock", "Decorative Tray", "Decorative Bowls", "Artificial Plants", "Lamp"
        ],
        "Crafts & Hobbies": [
            "Painting Supplies", "Sketchbook", "Drawing Pencils", "Watercolor Paints", "Acrylic Paints",
            "Oil Paints", "Canvas", "Easel", "Sculpting Clay", "Pottery Wheel",
            "Knitting Needles", "Yarn", "Cross Stitch Kit", "Model Kit", "Jigsaw Puzzle"
        ],
        "Party Supplies": [
            "Balloons", "Party Hats", "Party Decorations", "Streamers", "Confetti",
            "Tableware", "Disposable Cups", "Plates", "Napkins", "Cutlery",
            "Tablecloth", "Party Favors", "Pinata", "Cake Toppers", "Party Games"
        ],
        "Grocery & Gourmet Food": [
            "Bread", "Milk", "Eggs", "Cheese", "Butter",
            "Fresh Fruits", "Fresh Vegetables", "Meat", "Poultry", "Seafood",
            "Cereal", "Snacks", "Beverages", "Canned Goods", "Condiments",
            "Pasta", "Rice", "Beans", "Baking Ingredients", "Frozen Foods"
        ],
        "Office Products": [
            "Pens", "Pencils", "Notebooks", "Binders", "File Folders",
            "Stapler", "Staples", "Scissors", "Tape", "Glue",
            "Desk Organizer", "Calendar", "Whiteboard", "Markers", "Highlighters",
            "Printer Paper", "Ink Cartridges", "Desk Chair", "Desk Lamp", "Shredder"
        ],
        "Pet Supplies": [
            "Dog Food", "Cat Food", "Dog Treats", "Cat Treats", "Dog Toy pack",
            "Cat Toys pack", "Pet Bed", "Pet Crate", "Leash", "Collar",
            "Pet Carrier", "Pet Brush", "Pet Shampoo", "Litter Box", "Fish Tank",
            "Bird Cage", "Hamster Wheel", "Rabbit Hutch", "Reptile Terrarium"
        ],
        "Tools & Home Improvement": [
            "Hammer", "Screwdriver Set", "Wrench Set", "Pliers", "Tape Measure",
            "Level", "Utility Knife", "Flashlight", "Toolbox", "Power Drill",
            "Circular Saw", "Sander", "Paintbrush Set", "Roller", "Drop Cloth",
            "Screws", "Nails", "Paint", "Caulk", "Wood Glue"
        ]
    }
    descriptions = [
        "Unleash the Power Of:",
        "Effortless Elegance:",
        "Innovation at Your Fingertips:",
        "Crafted for Performance:",
        "The Future is Here:",
        "Simplify Your Life:",
        "Experience the Difference:",
        "Built to Last:",
        "Your Gateway to:",
        "Level Up Your:",
        "Incredibly versatile ",
        "Luxuriously soft ",
        "Remarkably powerful ",
        "Seamlessly integrates with ",
        "Unbelievably comfortable ",
        "Ultra-portable and convenient ",
        "Stylish and functional ",
        "The perfect  ",
        "Elevate your everyday life with  ",
        "Discover the joy of  ",
        "Make a statement with ",
        "Take control of your ",
        "Live a more fulfilling life with ",
        "Memories made easy with ",
        "Get yours today!",
        "Upgrade your experience now with ",
        "Don't miss out, order now! :",
        "Limited time offer to get ",
        "Purchase here to learn more about :"
    ]


    def total_products():
        total_products = 0
        for category, products in category_products.items():
            total_products += len(products)
        return total_products

    def insert_reg_user(name, email, password, phone_number,gender,country,city,postalcode,address):
        cursor.execute( "INSERT INTO registered_users(name, email, password,  phone_number,gender,country,city,postal_code,street_address) VALUES (  ?, ?, ?, ?,?,?,?,?,?)", (name, email, password,  phone_number,gender,country,city,postalcode,address))
        conn.commit()




    def insert_nonreg_user(cookie,name):
        cursor.execute("INSERT INTO non_registered_users(name,cookie) VALUES (?,?)", (name, cookie))
        conn.commit()

    def insert_prodcut_Category(name):
        cursor.execute( "INSERT INTO product_categories(category_name) VALUES (?)", (name))
        conn.commit()


    def insert_pre_booking(user_id, product_id,date):
        cursor.execute("exec prebookingpro  @user_id =?,  @product_id =?, @date=?",
                       ( user_id, product_id,date))
        conn.commit()

    def insert_retailers(retailer_name,phone ):
        cursor.execute(
            "INSERT INTO retailers (name, phone) VALUES (?, ?)",
            ( retailer_name,phone))
        conn.commit()


    def insert_customer_support_ticket( user_id, issue,status):
        cursor.execute("INSERT INTO customer_support_tickets ( user_id, issue,status) VALUES (?, ?, ?)",
                       ( user_id, issue,status))
        conn.commit()


    def insert_reviews(user_id, product_id, rating, review_text):
        cursor.execute("exec insertreviews  @product_id =?,@user_id =?, @rating =?,@review=?", (user_id, product_id, rating, review_text))
        conn.commit()


    def insert_products(name,catid,description,price,rating):
        cursor.execute("insert into products values (?,?,?,?,?)",name,catid,description,price,rating)
        conn.commit()

    def insert_coupon (discount,start,end,limit):
        cursor.execute("insert into coupons values (?,?,?,?)",discount,start,end,limit)
        conn.commit()

    def insert_shipping_method(method ,fees):
        cursor.execute("insert into shipping values (?,?)",method ,fees)
        conn.commit()

    def insert_rb_fill_inv(p_id,r_id,quantity,discount,date):
      cursor.execute("exec add_retailerbill_fill_inventory @product_id =?, @retailer_id =?, @quantity =?, @discount= ?,@date=?",p_id,r_id,quantity,discount,date)
      conn.commit()

    def insert_order(userid,date,time,shippingid,couponid,paymentmethod):
       cursor.execute("exec add_order   @user_id =?,   @date =? ,   @time = ? , @shipping_id =?, @coupon_id =?, @payment_method=?",userid,date,time,shippingid,couponid,paymentmethod)
       conn.commit()

    def insert_order_items(orderid,productid,quantity):
        cursor.execute("exec add_order_items @order_id =?, @product_id =?, @quantity=?",orderid,productid,quantity)
        conn.commit()

    def insert_payment(orderid,date,time):
        cursor.execute("exec add_payments  @order_id =?,  @date=? ,   @time=? ",orderid,date,time)
        conn.commit()

    def insert_cart(userid,cookie,total):
        cursor.execute("insert into cart(user_id ,cookie,total ) values (?,?,?)",userid,cookie,total)
        conn.commit()

    def insert_cart_items(cartid,productid,quantity):
        cursor.execute("exec add_cart_items @cart_id=?, @product_id=?,@quantity=?",cartid,productid,quantity)
        conn.commit()

    def insert_refunds(userid,productid,orderid,quantity,reason,date):
        cursor.execute("exec refunds    @user_id =?,    @product_id =?, @order_id =?,@quantity =?, @reason =?,	@date=?",userid,productid,orderid,quantity,reason,date)
        conn.commit()

    def pakistaninumbergen():
        mobile_code = random.choice(['300', '301', '302', '303', '304', '305', '306', '307', '308', '309',
                                     '311', '312', '313', '314', '315', '316', '317', '318', '319',
                                     '321', '322', '323', '324', '331', '332', '333', '334', '335',
                                     '336', '337', '338', '339'])
        country_code = '+92'
        number = ''.join([str(random.randint(0, 9)) for _ in range(7)])
        return f"{country_code} {mobile_code} {number}"

    def add_1000_users():
     i= 0
     while i<500:
      name=random.choice(men)
      father=random.choice(men)
      fullname=name+" "+father
      email=name+father+str(i)+"@gmail.com"
      insert_reg_user(fullname,email,fake.password(),pakistaninumbergen(),'M','Pakistan',random.choice(pakistan_cities),fake.postalcode(),str(random.randint(0, 1000)) +' '+ random.choice(string.ascii_uppercase)+ ' Block')
      i=i+1
      print("Added reg male users=",i)

     i=0

     while i<100:
      try:
       insert_nonreg_user(random.randint(0, 100000)+i, fake.name())
      except Exception as e:
          continue
      i=i+1
      print("Added cookie users=",i)

     i=0
     while i<500:
      name = random.choice(women)
      father = random.choice(men)
      fullname = name + " " + father
      email = name + father + str(i) + "@gmail.com"
      insert_reg_user(fullname, email, fake.password(),pakistaninumbergen(), 'F', 'Pakistan',random.choice(pakistan_cities), fake.postalcode(), str(random.randint(0, 1000)) + ' ' + random.choice(string.ascii_uppercase) + ' Block')
      i = i + 1
      print("Added reg female users=", i)

    def add_products_and_Cats():
     alt=1;
     for name in product_categories:
       insert_prodcut_Category(name)
       print("Added ",name)

       for products in category_products[name]:
           insert_products(products,alt,random.choice(descriptions)+products, random.randint(500 // 5, 10000 // 5) * 5,5)
       alt=alt+1

    def add_100_retailers():
     i=0
     while i<100:
      insert_retailers(random.choice(men)+ " "+random.choice(men),pakistaninumbergen())
      i=i+1
      print("Added retailer no= ",i)

    def fill_inventory_for_1_year(year):
     month=1;
     while month<=12:
      days=0
      if month in (1, 3, 5, 7, 8, 10, 12):
         days=31
      elif month==2 :
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
         days=29
        else:
         days=28
      else:
         days=30
      for day in range(1,days+1):
       insert_rb_fill_inv(random.randint(1,total_products()),random.randint(1,100),random.randint(10,100),random.randint(5,15),str(year) + "-" + str(month) + "-" + str(day))
      print('Added for month=',month)
      month=month+1

    #add_1000_users()
    #add_products_and_Cats()
    #add_100_retailers()
    #fill_inventory_for_1_year(2023)
    insert_pre_booking(1,185,"2023-11-30")
    insert_pre_booking(1, 14, "2023-11-30")

    cursor.close()
    conn.close()

except pyodbc.Error as ex:
    sqlstate = ex.args[1]
    print(f"Error connecting to the database: {sqlstate}")
