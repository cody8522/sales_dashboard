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
    '__RequestVerificationToken': 'jEDZ-vfi88LjdKCQ0DGccgKumK0txu0nUAtuBxPHJEAv7cyOuC9GKANsu8WzEhEOUYBldr2MiZoDeRa9IY0lzMCQZvWx_h98wtfDrQs5RgM1',
    '_lr_tabs_-4olzxu%2Fconsignment-portal-beta': '{%22sessionID%22:0%2C%22recordingID%22:%225-00cb1387-fac7-45ce-99a2-43a39c62e695%22%2C%22lastActivity%22:1671053698829}',
    '_lr_hb_-4olzxu%2Fconsignment-portal-beta': '{%22heartbeat%22:1671053698829}',
    '_lr_uf_-4olzxu': '3acf9c56-6542-4489-8edd-751fc85e7dcc',
    '.AspNet.ApplicationCookie': '8N2Z0QA4ZuLysHiYEtsZswqSJuP9uN_DtMEpMMVgKOy9-9T1o1p0KM9HXG_pO1V9qAsrDseSr6Q34TFvJRnl3yMcpXu2_FCtSrt-eSZVbGff1QkWECbkpwf316YnKuF1wMXb3j6bCeXW34zohcN-7PfeNIvtObNWpmOwcIrAZLt5T9TjelOELYCWuzPUmLwuypZaRdZoY0yFeeNTUo5LTnZS97UmJP5vvQRIPpWHbsWHMdTIWQLwfs7skVaG-kSPwAedSjfPQJ9kuZORAbjYkWnDU0Oyj25RPF8YccixrrwJl0-p6CafKenGH0jwaIQ7C5wQMxgkN4XKMkMr-y8yz52RMhTkrpGEWp_h5JRaEv655ogObwrTv562WjTMnwIPJSAUyG3V8qpJts-so1Y0YRS6_b4lEIR1uzFNoG2mcExobAWCksLB5fCKC1pZmy8ag6M4qQ6fizbyJDUYdAdBr-RM9LtdHlpBAAhGIuPhryAhPBpYiRewFZVZl7V9mJyiXkmaIMu9dsi_K6wTtbwGZavdAi-8VK0eRRefVlbaEsjSKG1B8a8TACyFDxBiVqCIFvDxoRMUDn9sIZg1o3rQpF2AgA23GDKqijcivr5dKSOqBa6jgcM8FnO-xeaCZmZme3mKyJ6tP0uDHffv6Ia-tx9l8RFXIx_I73hlOFLtmgY-QFTBSWqN6o3b3eNEqTXskkUoulkfd7HC8Hovlf3uc9Ex1ZD2S3Cf77MgadmzxOeYebfLsNh5atgcN3AdG2utfh0ykNjB-yN0sAukZHXzutAwtm2HBTDi5m08uU10jXJD0Tyvyh01bAAFZBt4OdvtfDAmbFR9D5_5ko-pjASKWXvo0eKZemNW1UHlbbdK0LZ06l7cM6Lc9Rnw-jAvZA8m0ACFulnZXVfbA4qSgWeSwKkb7l1bKRvXydLQ6UmWo1PMS7joc4i2OIEOoKZlPGIpLCjrp-dto8K3Rzj5UC2hQ4PnnA89DTnUuXH9HcaleOqP81EjJnu9IzgQwK6k0w3xfPlILmkW60PkXg0Y66JonyRB76884Cx5QRgLTcmx_vMdHQYQBqxd9Z-bI4pmReJuy6CzvBHTHa89DJtLob57vXfXTqxHZtAy4KGhuJyTYFA',
}

headers = {
    'authority': 'portal.stagefront.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': '__RequestVerificationToken=jEDZ-vfi88LjdKCQ0DGccgKumK0txu0nUAtuBxPHJEAv7cyOuC9GKANsu8WzEhEOUYBldr2MiZoDeRa9IY0lzMCQZvWx_h98wtfDrQs5RgM1; _lr_tabs_-4olzxu%2Fconsignment-portal-beta={%22sessionID%22:0%2C%22recordingID%22:%225-00cb1387-fac7-45ce-99a2-43a39c62e695%22%2C%22lastActivity%22:1671053698829}; _lr_hb_-4olzxu%2Fconsignment-portal-beta={%22heartbeat%22:1671053698829}; _lr_uf_-4olzxu=3acf9c56-6542-4489-8edd-751fc85e7dcc; .AspNet.ApplicationCookie=8N2Z0QA4ZuLysHiYEtsZswqSJuP9uN_DtMEpMMVgKOy9-9T1o1p0KM9HXG_pO1V9qAsrDseSr6Q34TFvJRnl3yMcpXu2_FCtSrt-eSZVbGff1QkWECbkpwf316YnKuF1wMXb3j6bCeXW34zohcN-7PfeNIvtObNWpmOwcIrAZLt5T9TjelOELYCWuzPUmLwuypZaRdZoY0yFeeNTUo5LTnZS97UmJP5vvQRIPpWHbsWHMdTIWQLwfs7skVaG-kSPwAedSjfPQJ9kuZORAbjYkWnDU0Oyj25RPF8YccixrrwJl0-p6CafKenGH0jwaIQ7C5wQMxgkN4XKMkMr-y8yz52RMhTkrpGEWp_h5JRaEv655ogObwrTv562WjTMnwIPJSAUyG3V8qpJts-so1Y0YRS6_b4lEIR1uzFNoG2mcExobAWCksLB5fCKC1pZmy8ag6M4qQ6fizbyJDUYdAdBr-RM9LtdHlpBAAhGIuPhryAhPBpYiRewFZVZl7V9mJyiXkmaIMu9dsi_K6wTtbwGZavdAi-8VK0eRRefVlbaEsjSKG1B8a8TACyFDxBiVqCIFvDxoRMUDn9sIZg1o3rQpF2AgA23GDKqijcivr5dKSOqBa6jgcM8FnO-xeaCZmZme3mKyJ6tP0uDHffv6Ia-tx9l8RFXIx_I73hlOFLtmgY-QFTBSWqN6o3b3eNEqTXskkUoulkfd7HC8Hovlf3uc9Ex1ZD2S3Cf77MgadmzxOeYebfLsNh5atgcN3AdG2utfh0ykNjB-yN0sAukZHXzutAwtm2HBTDi5m08uU10jXJD0Tyvyh01bAAFZBt4OdvtfDAmbFR9D5_5ko-pjASKWXvo0eKZemNW1UHlbbdK0LZ06l7cM6Lc9Rnw-jAvZA8m0ACFulnZXVfbA4qSgWeSwKkb7l1bKRvXydLQ6UmWo1PMS7joc4i2OIEOoKZlPGIpLCjrp-dto8K3Rzj5UC2hQ4PnnA89DTnUuXH9HcaleOqP81EjJnu9IzgQwK6k0w3xfPlILmkW60PkXg0Y66JonyRB76884Cx5QRgLTcmx_vMdHQYQBqxd9Z-bI4pmReJuy6CzvBHTHa89DJtLob57vXfXTqxHZtAy4KGhuJyTYFA',
    'referer': 'https://portal.stagefront.com/front-end/dashboard/index.html',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
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
    
    if len(sales) == 0:
        st.write("There have been no sales for this event")

    if len(sales) != 0:

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
    
