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
    '__RequestVerificationToken': 'mHUM0lpc8_oauGe35xbLc2_4PdfCWmKwJQwi1jGB13PV3HypsONLWhRukfUkAL9yxtA_qcVuz2u1mB7MLY2dxnGg21lnUgwvdu7BHUn304k1',
    '.AspNet.ApplicationCookie': '3MO7DeOGIl9v2El3Cf-GlvuVz-bKutXBONqGhNocbghFYRxnu7Gclh9xDbGRUMPPPhPJ0DP_Rvjt7lwozv5tHoUKQyyvyMqM9jQJ_gD7R_RlQTpOGWG58LvFIFK1AIoodfBmvb01185Hwye8fUS21HsBrSEZ1IBCCp8Dv9GElmIlv0HgtXvekiOq7azwECva6mgHk-JgRDn0kcyOPdyyqH5mN3qHpHeyHhqha-Dw2j8sOat35LYC097luUtYJt_DFNjPP4DQaig3dzuHoavOXKUkeRmIcnHjCeaeag_Z_JNXhKH5ZgOBo1lqZ3xpt9KW0yzz2Yua2wnu91onIzHQTJcIkLjqZn3EnVbKqDIDAeF0Gx4TkVAZGvkR9CoB0Bo6yi_5wgGSJ7yKT17l_7p59ewPXXmEG4j_RiRDRuGMYP1Rxso1dZx4uMHyNGKq7XzJjgMYU7JP_9bC1BmoLM8-ut8mxd6GvtgruFk9iYOlmiMPs12QRSZtu2180_d9V4-e_zdzJW7o0wuGTPujs2lgghzYUgCsk-rkIcNOUQHlYh5wejDWPfA-eZ_xd5UxQ35paCQyXf5q7kX7MS23TG1H0cd66iZC1U_77ciMIgMQtEuEoULObdifECxWPnMyFSZf0ADeTzwOLBHXTzk6vENsdeK-ouXpGSp5rMfljuBU5BDjPLRL2li4-EnYch6KGzNlVRJTK463FSZb0uA4Sa1lKzj1dIhH3dSBrX-0NI4p3UW_ep9fIxsrxDph888-UZwOKgb7QIzNlmUbRc1BXmGMo_uxUbxPKe5yU-GYWP9REh5z7pEAfs5SSSdjYuHJuYKDahfzZRwTc9quf22E9nv6XSP7t5jJxGlPfQjwSUNFYKQS6osjCD3mKVY-30jiSYDdN1skFDhJnOvn35MzGiVfu7LAA0i-r0NrgliV1wAfKIO8fRbqCiK96ZO9LLyboOf1NSgqmdXSlXcJatp8dgJOCPhvhil3tL4Mv8a8Hvivq2ddRzYjkYe_9TOuowAs6K2L52rUIQEwrv65TDInWWG0L_fO5ixKAW6gEUCZvFEbQkxV3S0g3bx94kaW_BzUAvylypiVrKuJ6MGmWINFBq69u5sWfZD0LeYdNxWkGlpmcLI',
}

headers = {
    'authority': 'portal.stagefront.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'cookie': '__RequestVerificationToken=mHUM0lpc8_oauGe35xbLc2_4PdfCWmKwJQwi1jGB13PV3HypsONLWhRukfUkAL9yxtA_qcVuz2u1mB7MLY2dxnGg21lnUgwvdu7BHUn304k1; .AspNet.ApplicationCookie=3MO7DeOGIl9v2El3Cf-GlvuVz-bKutXBONqGhNocbghFYRxnu7Gclh9xDbGRUMPPPhPJ0DP_Rvjt7lwozv5tHoUKQyyvyMqM9jQJ_gD7R_RlQTpOGWG58LvFIFK1AIoodfBmvb01185Hwye8fUS21HsBrSEZ1IBCCp8Dv9GElmIlv0HgtXvekiOq7azwECva6mgHk-JgRDn0kcyOPdyyqH5mN3qHpHeyHhqha-Dw2j8sOat35LYC097luUtYJt_DFNjPP4DQaig3dzuHoavOXKUkeRmIcnHjCeaeag_Z_JNXhKH5ZgOBo1lqZ3xpt9KW0yzz2Yua2wnu91onIzHQTJcIkLjqZn3EnVbKqDIDAeF0Gx4TkVAZGvkR9CoB0Bo6yi_5wgGSJ7yKT17l_7p59ewPXXmEG4j_RiRDRuGMYP1Rxso1dZx4uMHyNGKq7XzJjgMYU7JP_9bC1BmoLM8-ut8mxd6GvtgruFk9iYOlmiMPs12QRSZtu2180_d9V4-e_zdzJW7o0wuGTPujs2lgghzYUgCsk-rkIcNOUQHlYh5wejDWPfA-eZ_xd5UxQ35paCQyXf5q7kX7MS23TG1H0cd66iZC1U_77ciMIgMQtEuEoULObdifECxWPnMyFSZf0ADeTzwOLBHXTzk6vENsdeK-ouXpGSp5rMfljuBU5BDjPLRL2li4-EnYch6KGzNlVRJTK463FSZb0uA4Sa1lKzj1dIhH3dSBrX-0NI4p3UW_ep9fIxsrxDph888-UZwOKgb7QIzNlmUbRc1BXmGMo_uxUbxPKe5yU-GYWP9REh5z7pEAfs5SSSdjYuHJuYKDahfzZRwTc9quf22E9nv6XSP7t5jJxGlPfQjwSUNFYKQS6osjCD3mKVY-30jiSYDdN1skFDhJnOvn35MzGiVfu7LAA0i-r0NrgliV1wAfKIO8fRbqCiK96ZO9LLyboOf1NSgqmdXSlXcJatp8dgJOCPhvhil3tL4Mv8a8Hvivq2ddRzYjkYe_9TOuowAs6K2L52rUIQEwrv65TDInWWG0L_fO5ixKAW6gEUCZvFEbQkxV3S0g3bx94kaW_BzUAvylypiVrKuJ6MGmWINFBq69u5sWfZD0LeYdNxWkGlpmcLI',
    'portal-version': '4.22',
    'referer': 'https://portal.stagefront.com/Pricing',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
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
    
