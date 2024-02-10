import urllib
import streamlit as st
import pendulum as pdlm
from io import StringIO
from contextlib import contextmanager, redirect_stdout
import jingjue

@contextmanager
def st_capture(output_func):
    with StringIO() as stdout, redirect_stdout(stdout):
        old_write = stdout.write
        def new_write(string):
            ret = old_write(string)
            output_func(stdout.getvalue())
            return ret
        stdout.write = new_write
        yield
        
def get_file_content_as_string(path):
    url = 'https://raw.githubusercontent.com/kentang2017/kinqimen/master/' + path
    response = urllib.request.urlopen(url)
    return response.read().decode("utf-8")

def get_file_content_as_string1(path):
    url = 'https://raw.githubusercontent.com/kentang2017/kinliuren/master/' + path
    response = urllib.request.urlopen(url)
    return response.read().decode("utf-8")

st.set_page_config(layout="wide",page_title="堅荊訣占")
pan,links = st.tabs([' 排盤 ', ' 連結 ' ])

with links:
    st.header('連結')
    st.markdown(get_file_content_as_string1("update.md"))
    
with pan:
    st.header('排盤')
    output = st.empty()
    with st_capture(output.code):
        print("干卦︰"+jingjue.qigua()[0])
        print("")
        print("卦義︰"+jingjue.qigua()[1])
