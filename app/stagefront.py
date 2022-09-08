import requests
import urllib3
import pandas as pd
import warnings
import streamlit as st
import altair as alt
from st_aggrid import AgGrid

urllib3.disable_warnings()
warnings.filterwarnings('ignore')

cookies = {
    '__RequestVerificationToken': 'zdhBRcbzP2gCA5DUuolrWb4yP6DFQyEHjNzEOsFLpkA2TXR28smtt9K0pG782iZOPfq5Eta_ZoYy7jRpZDvPo85QdKJUWORj4-iuZhZ-uy41',
    '_lr_uf_-4olzxu': 'd1628cfb-394a-44dd-8cb7-5c814eb9c41a',
    'ASP.NET_SessionId': 'aswpylnpeyxxbdph45zpzfpf',
    '_lr_tabs_-4olzxu%2Fconsignment-portal-beta': '{%22sessionID%22:0%2C%22recordingID%22:%225-f058e182-86f0-4cc2-a4be-e329ee102a5a%22%2C%22lastActivity%22:1662665285934}',
    '_lr_hb_-4olzxu%2Fconsignment-portal-beta': '{%22heartbeat%22:1662665285935}',
    '.AspNet.ApplicationCookie': 'N21CEDE9YxEh7iVAzSG6-VXYSFpMFpHdm6d8Oi93uasfMZ6OznYn5ak4R8kMwnVVtMTHLWPHXi6QpnBQ08QPiVp0Kg0_AoDo7Mr3NNZTSiPOXNnTkzp1nS11akH-lBmw5QvXNM775ZnB8a46Qoswsbitg8Bh0Ss62vJXvM_LtbEAgUT_myObZQqDuhQySZNqWJkKcsVTXg9_w_nLJl_1aTce1UZDS-BeEraA6PyHpdh2ntRzV_-UgMR2jOMqUMj6ndspfGjKnXRX8CBI5a748sEZykjhdm3l-MBLTK81VDmmiNVcQCVn-PF1Y8ZGiMaDD5sGKbxRI_Fp9ziFM_W8lxFfANJNtuPbhl44BG9qAIgcmMVPwSJ0ge_M1qzsL8DSXiXTAEZCUn9d-BIgj31f531FfkEPKttCNesxYDomGYAx9WML9btLxs-PcZq7HOe7jWgwCDFOijIna2oaKmerMtVgOLK6qdQNT7cHpUGLPMbzsERiHWwzYl1FNodR94L7tF6YdbsVQodo9zulg-h9MeSbB1u18I_77_Yivu-IN3ZfZqGLODvDyxM_JFZr8Rx_YBXcNRP-sgJHc2aFmy7BO9aIi1RlmVbxcI85xwB-s36H-EmLAD9cjloVA2moPE1HBpTqdaJi8dwtV4271xUYWVR7s7yxEE3onenp9qnGK9WFqacrYFBb-I9Rlk-VJ0jFaempYa1H11D85cppnsZsX8FXw-1LR2gQkxrgayboBTeADOrLBNW-re052IhHd0wRgtW8WrOkBwRHM-SqywMb4sp1K7AL8koYt03iha_U1kWytnDSAM7VO2y1O9JOBBxUXEAOHpsBTmP1LqFVUjgeP891YgWSRsLkyi1PByTNLpIqMkeBKD2FNrjpnHRo2wKy5N7VSPf2ZKVcbyc5zAe3HrFmlWbJuv8U0sihysWRlrDgXx6yVy8ZaoRv8OceWsSU6ag5sRdwwvfTqa4Rb1k1mCz8Qm-AsuDHB7PKkK2Cp2CfMT8tN88rr60PRy6QVCXTAMtCeHcwMV1_tESGoTJTyXkU47sjN5vUlNKZLxBrktldE9rwBgFIzGskWH0XZJQMzx5WhLC7cJHJbxENqcfKxzqASevPhYqHq561yUZOlX0',
}

headers = {
    'authority': 'portal.stagefront.com',
    'accept': 'application/json; charset=utf-8',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': '__RequestVerificationToken=zdhBRcbzP2gCA5DUuolrWb4yP6DFQyEHjNzEOsFLpkA2TXR28smtt9K0pG782iZOPfq5Eta_ZoYy7jRpZDvPo85QdKJUWORj4-iuZhZ-uy41; _lr_uf_-4olzxu=d1628cfb-394a-44dd-8cb7-5c814eb9c41a; ASP.NET_SessionId=aswpylnpeyxxbdph45zpzfpf; _lr_tabs_-4olzxu%2Fconsignment-portal-beta={%22sessionID%22:0%2C%22recordingID%22:%225-f058e182-86f0-4cc2-a4be-e329ee102a5a%22%2C%22lastActivity%22:1662665285934}; _lr_hb_-4olzxu%2Fconsignment-portal-beta={%22heartbeat%22:1662665285935}; .AspNet.ApplicationCookie=N21CEDE9YxEh7iVAzSG6-VXYSFpMFpHdm6d8Oi93uasfMZ6OznYn5ak4R8kMwnVVtMTHLWPHXi6QpnBQ08QPiVp0Kg0_AoDo7Mr3NNZTSiPOXNnTkzp1nS11akH-lBmw5QvXNM775ZnB8a46Qoswsbitg8Bh0Ss62vJXvM_LtbEAgUT_myObZQqDuhQySZNqWJkKcsVTXg9_w_nLJl_1aTce1UZDS-BeEraA6PyHpdh2ntRzV_-UgMR2jOMqUMj6ndspfGjKnXRX8CBI5a748sEZykjhdm3l-MBLTK81VDmmiNVcQCVn-PF1Y8ZGiMaDD5sGKbxRI_Fp9ziFM_W8lxFfANJNtuPbhl44BG9qAIgcmMVPwSJ0ge_M1qzsL8DSXiXTAEZCUn9d-BIgj31f531FfkEPKttCNesxYDomGYAx9WML9btLxs-PcZq7HOe7jWgwCDFOijIna2oaKmerMtVgOLK6qdQNT7cHpUGLPMbzsERiHWwzYl1FNodR94L7tF6YdbsVQodo9zulg-h9MeSbB1u18I_77_Yivu-IN3ZfZqGLODvDyxM_JFZr8Rx_YBXcNRP-sgJHc2aFmy7BO9aIi1RlmVbxcI85xwB-s36H-EmLAD9cjloVA2moPE1HBpTqdaJi8dwtV4271xUYWVR7s7yxEE3onenp9qnGK9WFqacrYFBb-I9Rlk-VJ0jFaempYa1H11D85cppnsZsX8FXw-1LR2gQkxrgayboBTeADOrLBNW-re052IhHd0wRgtW8WrOkBwRHM-SqywMb4sp1K7AL8koYt03iha_U1kWytnDSAM7VO2y1O9JOBBxUXEAOHpsBTmP1LqFVUjgeP891YgWSRsLkyi1PByTNLpIqMkeBKD2FNrjpnHRo2wKy5N7VSPf2ZKVcbyc5zAe3HrFmlWbJuv8U0sihysWRlrDgXx6yVy8ZaoRv8OceWsSU6ag5sRdwwvfTqa4Rb1k1mCz8Qm-AsuDHB7PKkK2Cp2CfMT8tN88rr60PRy6QVCXTAMtCeHcwMV1_tESGoTJTyXkU47sjN5vUlNKZLxBrktldE9rwBgFIzGskWH0XZJQMzx5WhLC7cJHJbxENqcfKxzqASevPhYqHq561yUZOlX0',
    'portal-version': '4.22',
    'referer': 'https://portal.stagefront.com/Pricing',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

st.set_page_config(
    page_title = "TexTickets Sales Data",
    layout ="wide")
st.sidebar.image("https://i.imgur.com/YiHfDnR.png", width = 150)
st.title(" Seatgeek Sales Dashboard")

with st.sidebar.form(key = 'my_form'):
    sg_url = st.text_input(label= 'SeatGeek URL')
    sg_id = sg_url[-7:]
    submit_button = st.form_submit_button(label = 'Submit')

if submit_button:
    url_temp = 'https://portal.stagefront.com/api/Marketplace/SeatGeek/Event/{}/Sales'
    url = url_temp.format(sg_id)

    response = requests.get(url, cookies=cookies, headers=headers, verify = False)
    data = response.json()
    event = data['Event']
    sales = data['Sales']

    #Event Information

    event_df = pd.json_normalize(event)
    event_df2 = event_df['datetime_utc'].str.split("T", 1, expand = True)

    Artist = event_df["Name"].values[0] + "  -  " +  event_df["Venue.Name"].values[0]
    Venue_City = event_df["Venue.City"].values[0]
    Venue_State = event_df["Venue.State"].values[0]
    Event_Datetime = event_df2[0].values[0]

    st.header(Artist)
    st.write(Venue_City, ",", Venue_State)
    st.write(Event_Datetime)


    #Sales Information
    sales_df = pd.json_normalize(sales)

    sales_df2 = sales_df[['putc', 'bp', 'q' ,'s', 'r']]

    df = sales_df2['putc'].str.split("-",2, expand=True)

    df2 = df[2].str.split("T", 1, expand = True)


    sales_df2['Year'] = df[0]
    sales_df2['Month'] = df[1]
    sales_df2['Day'] = df2[0]
    sales_df2['Time'] = df2[1]
    sales_df2.drop(columns = ["putc"], inplace = True)

    df_rename = sales_df2.rename(columns = {'bp':'Price', 'q' : 'Qty', 's' : 'Sec', 'r' : 'Row'})

    final_df = df_rename[['Year', 'Month', 'Day', 'Time', 'Price', 'Qty', 'Sec', 'Row']]
    final_df = final_df.sort_values(by=['Year', 'Month','Day', 'Time'])


    final_df['date_string'] = final_df['Year'].astype(str) + "-" + final_df['Month'].astype(str)+ "-" +  final_df['Day'].astype(str)    

    ##volume chart
    v_scale = [0, max(final_df['Qty']) + 5]
    volume_chart = alt.Chart(final_df).mark_bar().encode(
    x = alt.X('date_string', axis = alt.Axis(labelOverlap = True, labelSeparation = 10), title = 'Date'),
    y =alt.Y('Qty', scale =alt.Scale(domain = v_scale)),
        tooltip = ['date_string', 'Qty'],).interactive().properties(width = 500)


    ##price chart
    x_scale = [min(final_df['Price']) - 20, max(final_df['Price']) + 20]
    price_chart = alt.Chart(final_df).mark_line().encode(
    x = alt.X('date_string', axis = alt.Axis(labelOverlap = True, labelSeparation = 10), scale=alt.Scale(zero=False), title = 'Date'),
    y = alt.Y('mean(Price)', scale = alt.Scale(domain = x_scale), title = 'Price'),
    tooltip = ['date_string','mean(Price)'],).interactive().properties(width = 500)

    col1, col2 = st.columns(2)

    with col1:
        st.header("Price over Time")
        st.altair_chart(price_chart, use_container_width=True)
    with col2:
        st.header("Volume over Time")
        st.altair_chart(volume_chart, use_container_width=True)
    
    #AgGrid Chart
    st.subheader("Sales History")
    AgGrid(final_df.sort_values(by = ['Year','Month','Day','Time'],
     ascending = False),
     fit_columns_on_grid_load = True, theme = 'dark')
    
    #Download CSV
    final_df = final_df.to_csv(index = False).encode('utf-8')
    st.download_button(label = "Export to CSV", data = final_df, 
        file_name ="seatgeek_sales.csv", mime = 'text/csv')
    
    #SeatGeek API for Current Stats
    api_url_full = "https://api.seatgeek.com/2/events/{}?client_id=ODA3MjA1NXwxNjU2NzA1Njk2LjYyNTE0Mzg&client_secret=e81628dfe5fa78b2541818724a291649cb0454a30ea813b8d3d5f1dbdd3c1215"
    api_url = api_url_full.format(sg_id)
    api_payload={}
    api_headers = {
    'Cookie': '_pxhd=L8w7yqOP6Cx42r4k1-HX8OCd0j0eYOus48gXvrqwdXDfXcS6bNi/nZ0Nfg-FkRaGje5iOiYTdo1Oql9/HE1H2Q==:OsAKtGsLntFg0Z3hsIj26yisUL/rm/ajy0xx7amwXDqOpQ5MTU6HbSupHSdh2ouDwxMu4PI-OB4MZCLbiDYqL-k9WjRIJ99mTHZXX2NOqps=',
    }

    api_response = requests.request("GET", api_url, headers=api_headers, data=api_payload)
    api_data = api_response.json()
    api_data_2 = api_data['stats']

    test1 = api_data_2.get('listing_count')

    current_listings = str(list(api_data_2.values())[0]) 
    average_price = str(list(api_data_2.values())[1])
    lowest_price = str(list(api_data_2.values())[3])
    highest_price = str(list(api_data_2.values())[4])
    median_price = str(list(api_data_2.values())[7])

    st.header("Current Values")
    st.subheader("Number of Listings:" + " " + current_listings)
    st.subheader("Get-In Price:" + " " +  "$" + lowest_price)
    st.subheader("Average Price:" + " " + "$" +average_price)
    st.subheader("Median Price:" + " " + "$" + median_price)
    st.subheader("Highest Price:" + " " + "$" +  highest_price)
    
