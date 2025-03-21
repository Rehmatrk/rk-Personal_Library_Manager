import streamlit as st
import json

# Apply Enhanced Styling
st.markdown("""
    <style>
    /* Sky Blue Background */
    .stApp {
        background: linear-gradient(to right, #87CEFA, #00BFFF); 
        color: #000000;
        font-family: 'Arial', sans-serif;
    }

    /* Sidebar Styling */
    .css-1d391kg {
        background: linear-gradient(to bottom, #f0f8ff, #b0e0e6) !important;
        color: #000000;
    }

    /* Title Styling */
    h1 {
        color: #ffffff;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5);
    }

    /* Subheader Styling */
    .stMarkdown h2 {
        color: #ffffff;
        font-weight: bold;
    }

    /* Styled Buttons */
    .stButton>button {
        background: linear-gradient(to right, #0066cc, #004080);
        color: white;
        border-radius: 12px;
        font-size: 18px;
        padding: 12px 24px;
        transition: 0.3s;
        font-weight: bold;
        border: none;
    }

    /* Input Field Styling */
    .stTextInput>div>div>input {
        background-color: #ffffff;
        color: #000000;
        font-weight: bold;
        padding: 10px;
        border-radius: 8px;
    }

    /* Hover Effect for Buttons */
    .stButton>button:hover {
        background: linear-gradient(to right, #004080, #00274d);
        transform: scale(1.05);
        box-shadow: 0px 4px 12px rgba(0, 91, 187, 0.8);
    }

    </style>
""", unsafe_allow_html=True)

# Load & Save Library Data
def load_library():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_library():
    with open("library.json", "w") as file:
        json.dump(library, file, indent=4)

# Initialize Library
library = load_library()

# Set Title
st.title("📚 Personal Library Manager")

# Sidebar Menu
menu = st.sidebar.radio("📌 Select an Option", 
                        ["🏠 View Library", "➕ Add Book", "❌ Remove Book", "🔍 Search Book", "💾 Save & Exit"])

# View Books
if menu == "🏠 View Library":
    st.subheader("📖 Your Library")
    if library:
        st.table(library)
    else:
        st.warning("⚠ No books in your library. Add some!")

# Add Book
elif menu == "➕ Add Book":
    st.subheader("📘 Add a New Book")
    title = st.text_input("📖 Book Title")
    author = st.text_input("🖊 Author")
    year = st.number_input("📅 Year", min_value=2023, max_value=2100, step=1)
    genre = st.text_input("🏷 Genre")
    read_status = st.checkbox("✅ Mark as Read")

    if st.button("Add Book"):
        library.append({"title": title, "author": author, "year": year, "genre": genre, "read": read_status})
        save_library()
        st.success("📚 Book Added Successfully!")
        st.rerun()

# Remove Book
elif menu == "❌ Remove Book":
    st.subheader("📕 Remove a Book")
    book_titles = [book["title"] for book in library]

    if book_titles:
        selected_book = st.selectbox("📌 Select a book to remove", book_titles)

        if st.button("Remove Book"):
            library = [book for book in library if book["title"] != selected_book]
            save_library()
            st.success("🗑 Book Removed!")
            st.rerun()
    else:
        st.warning("⚠ No books to remove!")

# Search Book
elif menu == "🔍 Search Book":
    st.subheader("🔎 Search for a Book")
    search_term = st.text_input("🔍 Enter title or author name")

    if st.button("Search"):
        results = [book for book in library if search_term.lower() in book["title"].lower() 
                   or search_term.lower() in book["author"].lower()]
        
        if results:
            st.table(results)
        else:
            st.warning("⚠ No books found!")

# Save & Exit
elif menu == "💾 Save & Exit":
    save_library()
    st.success("✅ Library Saved!")

   
            
