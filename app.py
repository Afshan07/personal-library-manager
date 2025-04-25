import streamlit as st

# Page settings
st.set_page_config(page_title="📚 Personal Library Manager")

st.title("📚 Personal Library Manager")
st.subheader("Manage your books easily!")

# Session state for storing books
if "books" not in st.session_state:
    st.session_state.books = []

# Add a book
with st.form("add_book"):
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    submitted = st.form_submit_button("Add Book")
    if submitted and title and author:
        st.session_state.books.append({"title": title, "author": author})
        st.success(f"Added: {title} by {author}")

# Show books
st.markdown("### 📖 Your Books")
if st.session_state.books:
    for idx, book in enumerate(st.session_state.books):
        st.write(f"{idx+1}. **{book['title']}** by *{book['author']}*")
        if st.button(f"Delete Book {idx+1}", key=idx):
            st.session_state.books.pop(idx)
            st.experimental_rerun()
else:
    st.info("No books added yet!")

# Footer
st.markdown("---")
st.caption("Made with 💜 by Afshan Iftikhar")
