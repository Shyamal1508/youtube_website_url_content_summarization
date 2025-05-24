import streamlit as st
import validators,streamlit as st
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate


from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader
st.set_page_config(page_title="Langchain:summarize yt or website")
st.title("Langchain:summarize text from youtube or website")

st.subheader("Summarize URL:")


with st.sidebar:
    groq_api_key=st.text_input("enter your groq api key",value="",type="password")
generic_url=st.text_input("URL",label_visibility="collapsed")

llm=ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)

prompt_template = """
                       provide me a summary of the following content in 300 words 
                      Content:{text}
                    """
prompt=PromptTemplate(template=prompt_template, input_variables=["text"])


if st.button("Summarize the content from youtube or website"):
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("please provide the information")
    elif not validators.url(generic_url):
        st.error("please enter a valid url.It can be a yt video or website url")
    else:
        try:
            with st.spinner("waiting...."):
                if "youtube.com" in generic_url:
                   loader=YoutubeLoader.from_youtube_url(generic_url,add_video_info=True)
                else:
                   loader=UnstructuredURLLoader(urls=[generic_url],ssl_verify=False,headers={"User-Agent":"Mozilla/5.0(Macintosh;Intel Mac OS X 10_15_7) AppleWebKit/537.36(KHTML,like Gecko) Chrome/91.0.4472.114 Safari/537.36"})
                data=loader.load()
                st.write(data)
                chain=load_summarize_chain(llm,chain_type="stuff",prompt=prompt)
                output_summary=chain.run(data)
                st.success(output_summary)

            
        except Exception as e:

            st.exception(f"Exception:{e}")

        
   

        

   
