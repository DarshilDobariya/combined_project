import webbrowser
import streamlit as st
import subprocess
import os

def main():
    st.title('Streamlit App with Django Redirect')

    django_app_url = "http://localhost:8000"

    # Create a button
    if st.button("Run Django App"):
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Define the path to the manage.py file in your Django project
        manage_py_path = os.path.join(script_dir, "django_chatbot", "manage.py")
        print(manage_py_path)
        
        # Define the command to run your Django app
        django_command = f"python {manage_py_path} runserver"
        
        # Run the Django app using subprocess
        subprocess.Popen(django_command, shell=True)
        webbrowser.open_new_tab(django_app_url)

if __name__ == '__main__':
    main()
