import streamlit as st



def main():
    st.set_page_config(page_title="Chat with multiple PDFs",
                       page_icon=":books:")

    st.header("Chat with multiple PDFs")
    st.text_input("Ask a question about your documents:")

    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload your PdFs here and click on the button "
                         "'Process'")
        st.button("Process")












if __name__ == '__main__':
    main()