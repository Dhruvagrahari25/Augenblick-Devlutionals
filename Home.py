# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import plotly.graph_objects as go
# from PIL import Image
# import librosa
# import librosa.display
# import matplotlib.pyplot as plt
# from io import BytesIO
# import base64
# import time

# # Configure page settings
# st.set_page_config(
#     page_title="Industrial Anomaly Detection System",
#     page_icon="🔍",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )



# def file_upload_section():
#     st.markdown('<h2 class="sub-header">Upload Your Sensor Data</h2>', unsafe_allow_html=True)
#     st.write("Upload one file at a time (.csv, .xlsx, .jpg, .png, .wav, .mp3)")
    
#     uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "jpg", "png", "wav", "mp3"])
    
#     if uploaded_file is not None:
#         # Display a spinning loader
#         with st.spinner('Processing your file...'):
#             time.sleep(2)  # Simulate processing time
            
#             # Get file extension
#             file_extension = uploaded_file.name.split('.')[-1].lower()
            
#             # Process based on file type
#             if file_extension in ['csv', 'xlsx']:
#                 process_tabular_data(uploaded_file, file_extension)
#             # (Other types like image/audio would call their respective functions)
#             else:
#                 st.markdown('<p class="error-message">Invalid file type. Please upload a CSV, Excel, image, or audio file.</p>', unsafe_allow_html=True)
#                 st.markdown("""
#                 <div style="animation: shake 0.5s ease-in-out; text-align: center;">
#                     <img src="https://cdn.dribbble.com/users/251873/screenshots/9288094/media/a1c2f89747ce6589b2d7b8190c2341bc.gif" width="200">
#                     <h3>Please try again with a valid file</h3>
#                 </div>
#                 """, unsafe_allow_html=True)
#     else:
#         display_placeholder_visualizations()

# def process_tabular_data(file, extension):
#     try:
#         # Read the file data into bytes and wrap it in a BytesIO object
#         file_data = file.read()
#         bytes_data = BytesIO(file_data)
        
#         if extension == 'csv':
#             df = pd.read_csv(bytes_data)
#         else:
#             df = pd.read_excel(bytes_data)
        
#         st.success("File uploaded successfully!")
        
#         # Display basic info about the dataset
#         st.subheader("Data Summary")
#         st.write(f"Number of records: {len(df)}")
#         st.write(f"Number of features: {len(df.columns)}")
#         st.write(f"Data Shape: {df.shape}")  # Debug info
        
#         # Display a preview of the data
#         st.subheader("Data Preview")
#         st.dataframe(df.head())
        
#         # Create a 3D plot if there are at least 3 numerical columns
#         numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
#         if len(numeric_cols) >= 3:
#             x_col, y_col, z_col = numeric_cols[:3]
#             fig = go.Figure(data=[go.Scatter3d(
#                 x=df[x_col],
#                 y=df[y_col],
#                 z=df[z_col],
#                 mode='markers',
#                 marker=dict(
#                     size=5,
#                     color=df.index,
#                     colorscale='Viridis',
#                     opacity=0.8
#                 )
#             )])
#             fig.update_layout(
#                 title="3D Visualization of Sensor Data",
#                 scene=dict(
#                     xaxis_title=x_col,
#                     yaxis_title=y_col,
#                     zaxis_title=z_col
#                 ),
#                 height=700
#             )
#             st.plotly_chart(fig, use_column_width=True)
#         else:
#             st.warning("Not enough numerical columns for 3D visualization")
    
#     except Exception as e:
#         st.error(f"Error processing file: {str(e)}")


# def display_placeholder_visualizations():
#     st.info("Upload a file to see visualizations here.")

# # Main app execution
# def main():
#     file_upload_section()
# if __name__ == '__main__':
#     main()




























import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import librosa
import librosa.display
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import time

# Configure page settings
st.set_page_config(
    page_title="Industrial Anomaly Detection System",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

def file_upload_section():
    st.markdown('<h2 class="sub-header">Upload Your Sensor Data</h2>', unsafe_allow_html=True)
    st.write("Upload one file at a time (.csv, .xlsx, .jpg, .png, .wav, .mp3)")
    
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "jpg", "png", "wav", "mp3"])
    
    if uploaded_file is not None:
        with st.spinner('Processing your file...'):
            time.sleep(2)  # Simulate processing time
            file_extension = uploaded_file.name.split('.')[-1].lower()
            
            if file_extension in ['csv', 'xlsx']:
                process_tabular_data(uploaded_file, file_extension)
            else:
                st.error("Invalid file type. Please upload a CSV, Excel, image, or audio file.")
    else:
        display_placeholder_visualizations()

def process_tabular_data(file, extension):
    try:
        file_data = file.read()
        bytes_data = BytesIO(file_data)
        
        if extension == 'csv':
            df = pd.read_csv(bytes_data)
        else:
            df = pd.read_excel(bytes_data)
        
        st.success("File uploaded successfully!")
        
        st.subheader("Data Summary")
        st.write(f"Number of records: {len(df)}")
        st.write(f"Number of features: {len(df.columns)}")
        st.write(f"Data Shape: {df.shape}")
        
        st.subheader("Data Preview")
        st.dataframe(df.head())
        
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        if len(numeric_cols) >= 3:
            x_col, y_col, z_col = numeric_cols[:3]
            fig = go.Figure(data=[go.Scatter3d(
                x=df[x_col],
                y=df[y_col],
                z=df[z_col],
                mode='markers',
                marker=dict(
                    size=5,
                    color=df.index,
                    colorscale='Viridis',
                    opacity=0.8
                )
            )])
            fig.update_layout(
                title="3D Visualization of Sensor Data",
                scene=dict(
                    xaxis_title=x_col,
                    yaxis_title=y_col,
                    zaxis_title=z_col
                ),
                height=700
            )
            st.plotly_chart(fig, use_column_width=True)
        else:
            st.warning("Not enough numerical columns for 3D visualization")
        
        display_time_series_plots(df)
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")

def display_time_series_plots(df):
    st.subheader("Time Series Plots")
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    if not numeric_cols:
        st.warning("No numerical columns available for time series visualization.")
        return
    
    for col in numeric_cols:
        fig = px.line(df, x=df.index, y=col, title=f"Time Series Plot of {col}")
        fig.update_layout(xaxis_title="Index", yaxis_title=col)
        st.plotly_chart(fig, use_container_width=True)

def display_placeholder_visualizations():
    st.info("Upload a file to see visualizations here.")

def main():
    file_upload_section()

if __name__ == '__main__':
    main()
