# importing required packages:
import streamlit as st
import radon.raw as rr
import radon.metrics as rm
import radon.complexity as rc
import pandas as pd
import graphviz
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import altair as alt
import plotly_express as px

from utility import getKeywordsCount
from parser import createAstTree
from parse import make_ast
from lexical import lexical_analysis
from syntax import syntax_analysis
from semantic import semantic_analysis

def creatDataframe(dict):
    return pd.DataFrame(list(dict.items()), columns=["Keywords", "Counts"])

def plotData(docx):
    wrdCloud = WordCloud().generate(docx)
    fig = plt.figure()
    plt.imshow(wrdCloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot(fig)

def main():
    st.markdown("""
        <style>
            .title {
                font-size: 60px;
                font-weight: bold;
                text-align: center;
                text-shadow: 2px 2px 10px rgba(255, 87, 51, 0.7);
            }
            .subtitle {
                font-size: 30px;
                font-weight: 500;
                text-align: center;
                margin-top: -10px;
            }
        </style>
        <h1 style='color: #8ea26f;' class="title">PyCheckMate</h1>
        <h3 style='color:skyblue;'class="subtitle">Static Code Analyzer for Python</h3>
    """, unsafe_allow_html=True)

    with st.form(key="myForm"):
        sourceCode = st.text_area("Enter Your Source Code...")
        btn = st.form_submit_button(label="Analyze Code")

    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "Code Analysis", "Keywords", "Identifiers", "AST", "Lexical Analysis", "Syntax Analysis", "Semantic Analysis"
    ])

    if btn:
        res = getKeywordsCount(sourceCode)

        with tab1:
            st.subheader("Code Analysis")
            with st.expander("Source Code"):
                st.code(sourceCode)
                analysis = rr.analyze(sourceCode)
            with st.expander("Analysis: "):
                st.write(analysis)
                mainIdx = rm.mi_visit(sourceCode, True)
                ccIdx = rc.cc_visit(sourceCode)
                halTdx = rm.h_visit(sourceCode)
                col1, col2 = st.columns(2)
                col1.metric(label="Maintainability Index", value=mainIdx)
                col2.metric(label="Cyclomatic Complexity", value=f"{ccIdx}")
            with st.expander("Halstead Metrics: "):
                st.write(halTdx[0])

        with tab2:
            st.subheader("Keywords")
            df = creatDataframe(res["Keywords"])
            chart1 = alt.Chart(df).mark_bar().encode(x="Keywords", y="Counts", color="Keywords")
            st.altair_chart(chart1, use_container_width=True)
            t1, t2, t3 = st.tabs(["Code Cloud", "Word Frequency", "Pie Chart"])
            with t1:
                plotData(sourceCode)
            with t2:
                st.dataframe(df)
            with t3:
                chart2 = px.pie(values=res["Keywords"].values(), names=res["Keywords"].keys())
                st.plotly_chart(chart2)

        with tab3:
            st.subheader("Identifiers")
            df = creatDataframe(res["Identifiers"])
            chart2 = alt.Chart(df).mark_bar().encode(x="Keywords", y="Counts", color="Keywords")
            st.altair_chart(chart2, use_container_width=True)
            plotData(sourceCode)

        with tab4:
            st.subheader("AST Tree")
            ast_visualization = createAstTree(sourceCode)
            st.graphviz_chart(ast_visualization.source)
            with st.expander("AST: "):
                ast_representation = createAstTree(sourceCode)
                st.code(ast_representation, language="text")

        with tab5:
            st.subheader("Lexical Analysis")
            tokens = lexical_analysis(sourceCode)
            st.code("\n".join(tokens), language="text")

        with tab6:
            st.subheader("Syntax Analysis")
            ast_tree = syntax_analysis(sourceCode)
            st.json(ast_tree)

        with tab7:
            st.subheader("Semantic Analysis")
            semantic_result = semantic_analysis(sourceCode)
            st.code(semantic_result)

if __name__ == '__main__':
    main()

#Example
#a =  2*3+4
#print("ans: ", a)