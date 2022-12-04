import streamlit as st
import numpy as np
import sqlite3

class Query:
    def __init__(self,cas_number):
        self.__casno = cas_number

    def CasnumberQuery(self):
        result_list_0=[]
        row=0
        cas_query_0 = '''SELECT ori_sn,casno,cnname,enname,remark,legid FROM CNOTHERS WHERE casno='CAS_X';'''
        cas_query_1=cas_query_0.replace('CAS_X',str(self.__casno))
        result_0 = chemicals.execute(cas_query_1)
        for chem in result_0:#解包到列表中
            result_list_0.append(chem[5])
        result_set_0=set(result_list_0)#转换列表为集合&#xff08;可去重&#xff09;
        print("result_set_0---", result_set_0)
        if len(result_set_0)==0:#如果列表为空&#xff0c;意味着未检索到结果
            print("None -----------")
            return None
        else:
            print('Run Els-------')
            # leg_query = '''SELECT legid, leg_cn,leg_en,pub_date FROM CNLAWS WHERE legid = 'LEG_X';'''
            leg_query = '''SELECT cnname,enname,remark, legid FROM CNOTHERS WHERE legid = 'LEG_X';'''
            leg_arr=np.empty((len(result_set_0)+1,3),object) #为储存查询结果&#xff0c;预制了一个空数组
            leg_arr[0,:] =(['Item','Status','Date']) #标题列
            for leg_id in result_set_0:#将数据库检索结果写入数组
                leg_query_1 = leg_query.replace('LEG_X',leg_id)
                leg_result_1 = chemicals.execute(leg_query_1).fetchone()
                # leg_result_1 = ["11","11","11"]
                row+=1
                print(leg_arr)
                leg_arr[row,:]=([leg_result_1[0],leg_result_1[1],leg_result_1[2]])
            return leg_arr#返回数组

def findillegalchar(casnum):
    '''
    检验查询输入字符&#xff0c;防止注入攻击
    '''
    safetynum= ['0','1','2','3','4','5','6','7','8','9','-','R']
    for char in casnum:
        if char not in safetynum:
            return char

st.title('EM Bag Service Status Tracking')
warehouse=sqlite3.connect(r'/Users/fengyangguo/Downloads/EMSearch.db')
chemicals = warehouse.cursor()
whichcasno = st.text_input('Enter CAS number', value = '', max_chars = None, key = None, type = 'default', help = 'CAS号形如1336-21-6')
if whichcasno!='':
    if findillegalchar(whichcasno):
        st.write(whichcasno,'包含非法字符:',findillegalchar(whichcasno))
    else:
        st.write(whichcasno,'Service Staus is following:')
        query_test = Query(whichcasno)
        df_result_0 = query_test.CasnumberQuery()
        if df_result_0 is not None:
            st.dataframe(data = df_result_0)
        else:
            st.write('oops!未检索到关联法规数据')
