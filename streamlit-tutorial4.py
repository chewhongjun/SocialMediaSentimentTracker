#Base Imports
import streamlit as st
import time
import asyncio

#EDA Imports
import pandas as pd



TIME_LIMIT = 60

class File:
    def __init__(self, data, header,indexcol):
        self.data = data
        self.header = header
        self.indexcol = indexcol


def dataReader():
    """Reading User File Via Drag & Drop"""

    if(st.checkbox("Upload Dataset")):
        File.data = st.file_uploader("Upload a Dataset", type = ["csv", "txt"])
        if File.data is not None:
            dataframe = pd.read_csv(File.data)
            if st.button("Set Header"):
                File.indexcol = list(dataframe)
                index_column = st.selectbox("Index Column",File.indexcol)
                dataframe = dataframe.set_index(index_column)
                st.write(index_column)
            st.dataframe(dataframe.head())
            if st.checkbox("Show Dataframe"):
                st.dataframe(dataframe.head())
                st.write(dataframe.iloc[0])

        return 1
    return None
    


def main():
    df = dataReader()
    if  df is not None and not st.checkbox("Data Visualisation"):
            pass




if __name__ == "__main__":
    main()