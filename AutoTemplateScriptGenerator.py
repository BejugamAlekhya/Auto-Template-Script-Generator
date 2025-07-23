import streamlit as st
import subprocess

st.title("Auto Template Script Generator")

st.markdown("""
Use the buttons below to run specific automation tasks related to test script and data generation:
""")
st.markdown("""
- **Generate All**: Generates the both Test script and Excel data.
- **Test data generator**: Generates the Excel data only.
- **Test script generator**: Generates the test scripts only.
""")

# Define paths to your .bat files
bat_file_1 = r"C:\code\infor\m3-ia-testscripts\m3-ia-testscripts-2.0\Run_GenerateAllData.bat"
bat_file_2 = r"C:\code\infor\m3-ia-testscripts\m3-ia-testscripts-2.0\Run_TestDataGenerator.bat"
bat_file_3 = r"C:\code\infor\m3-ia-testscripts\m3-ia-testscripts-2.0\Run_TestScriptGenerator.bat"

# Use columns to align buttons side by side
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Generate All"):
        try:
            subprocess.Popen(f'start cmd /c "{bat_file_1}"', shell=True)
            st.success("✅ Generate All script executed.")
        except Exception as e:
            st.error(f"❌ Error running Generate All script: {e}")

with col2:
    if st.button("Test data generator"):
        try:
            subprocess.Popen(f'start cmd /c "{bat_file_2}"', shell=True)
            st.success("✅ Test data generator script executed.")
        except Exception as e:
            st.error(f"❌ Error running Test data generator script: {e}")

with col3:
    if st.button("Test script generator"):
        try:
            subprocess.Popen(f'start cmd /c "{bat_file_3}"', shell=True)
            st.success("✅ Test script generator executed.")
        except Exception as e:
            st.error(f"❌ Error running Test script generator: {e}")
