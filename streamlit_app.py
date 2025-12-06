import streamlit as st

from auth import validate_login
from query import insert_query, fetch_queries, close_query, delete_query



def do_login():
    st.title("Client Query Management System")

    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        role = validate_login(username, password)

        if role:
            st.success(f"Logged in as {role}")
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.session_state["role"] = role.lower()  # support / client
            st.rerun()

        else:
            st.error("Invalid username or password")


def sidebar_menu():
    """Show sidebar with user info + logout."""
    with st.sidebar:
        st.write(f"👤 **User:** {st.session_state.get('username')}")
        st.write(f"🔑 **Role:** {st.session_state.get('role').capitalize()}")

        if st.button("Logout"):
            st.session_state.clear()
            st.rerun()



# Client UI 

def client_view():
    st.header("Client Portal")

    st.subheader("Create a New Query")

    with st.form("create_query_form"):
        mail_id = st.text_input("Email")
        mobile_number = st.text_input("Mobile Number")
        query_heading = st.text_input("Query Heading")
        query_description = st.text_area("Query Description")

        submitted = st.form_submit_button("Submit Query")

        if submitted:
            if not (mail_id and mobile_number and query_heading and query_description):
                st.error("All fields are required.")
            else:
                try:
                    insert_query(
                        mail_id=mail_id,
                        mobile_number=mobile_number,
                        query_heading=query_heading,
                        query_description=query_description,
                    )
                    st.success("Query submitted successfully!")
                except Exception as e:
                    st.error(f"Error while inserting query: {e}")

    st.markdown("---")
    st.subheader("All Queries (for demo)")

    try:
        queries = fetch_queries()
        if queries:
            st.dataframe(queries)
        else:
            st.info("No queries found yet.")
    except Exception as e:
        st.error(f"Error fetching queries: {e}")


#  Support UI

def support_view():
    st.header("Support Dashboard")

    # Filter by status
    status_filter = st.selectbox("Filter by Status", ["All", "Open", "Closed"])

    if status_filter == "All":
        status_value = None
    else:
        status_value = status_filter

    try:
        queries = fetch_queries(status=status_value)
    except Exception as e:
        st.error(f"Error fetching queries: {e}")
        return

    if not queries:
        st.info("No queries found.")
        return

    st.subheader("Queries")

    # Show each query with a close button
    for q in queries:
        with st.expander(f"#{q['query_id']} - {q['query_heading']} [{q['status']}]"):
            st.write(f"**Mail ID:** {q['mail_id']}")
            st.write(f"**Mobile:** {q['mobile_number']}")
            st.write(f"**Description:** {q['query_description']}")
            st.write(f"**Created:** {q['query_created_time']}")
            st.write(f"**Closed:** {q['query_closed_time']}")

            if q["status"].lower() != "closed":
                if st.button(
                    f"Close Query #{q['query_id']}",
                    key=f"close_{q['query_id']}",
                ):
                    try:
                        close_query(q["query_id"])
                        st.success(f"Query {q['query_id']} closed.")
                        st.rerun()

                    except Exception as e:
                        st.error(f"Error closing query: {e}")


#  Main App 

def main():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        do_login()
    else:
        sidebar_menu()
        role = st.session_state.get("role")

        if role == "client":
            client_view()
        elif role == "support":
            support_view()
        else:
            st.error(f"Unknown role: {role}")


if __name__ == "__main__":
    main()
