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
    '_lr_tabs_-4olzxu%2Fconsignment-portal-beta': '{%22sessionID%22:0%2C%22recordingID%22:%225-3836d54b-171d-4763-90d1-81c7047f9292%22%2C%22lastActivity%22:1659962979785}',
    '_lr_hb_-4olzxu%2Fconsignment-portal-beta': '{%22heartbeat%22:1659962979786}',
    '_lr_uf_-4olzxu': 'd1628cfb-394a-44dd-8cb7-5c814eb9c41a',
    '.AspNet.ApplicationCookie': 'ZeqarSk1D84WMffgHgrWQ9GCj_TnGUJFI5m4wAOC6PhTzPGFdjlFDp2zXEkJoHdKgoNUe4nVPPbNs-ulhmn6xXeaufYKH_HtWeGqK7Apkd91BA80cV2BWLlPmFWYI2fDr4trMj-Fyl7H86dEbqvVPBw7ZJAQkZcEYjBgAHWpk1egrwqLO0ywFz52qYj1I_z_nrqA_7V31d-uN37GNICb1j2J8sawNJjx4ip3meqoz0JuW_1lzF9K7og2rjix1sG4pkNyUbut-oa7y0XRhRgB2EzZ5LlrJgK7p2V35PRNeQiq53AVDUU9Sat4qzfIGsJkgzffkyL04dFuxFCJefddfFiRLl4d7-0THmh88D7qoV0WpfJhcTH06fo43UUSpv1e1mm8T5NUlMoe-yclMYwpY1La4r7m78o3G7Rjv0pPrKT3aodrF_z6t9yngbcSYVQ1wn3Eukkbf2RlRED4eUmJUlo_BecAwtipVCOjWkzfGG_5IFV_A5spIgZ9bO6XV0KhdGGm2nSc3qJnXqdjx40DuasAv-XDYkP_GkZECRqIIsFLM21YDHq46MfDoNYBhf_v1giZ0CvkA18dgzRkYU_MM58R8XVu5yEACj9D1TNdHxXREQBoNc2MT9sTfVXU1BjInnxobZRtk2mXnwEOgW47wNeq--R8Bq8g7ldX_45s15YGZrxkkmorv4n3gUf81b29QbFnVpgatPNAtDCE5_NdQL0Lzg8ZKNLaHV9Srtk6I3ELUI_PEDpRcIF9eeWNHRNrTb3u2YW40F3UKsSHd6vdDY_hTxpigvkuL8TldqF940qe-37yAQudBJoLFd6tp2ApIrqWAbbOgK03ymw7zc8Jx0GZ7PGpgXklQKBLvtNKoFiEP-i0mB5NRuKkUa85-_qHm-7rcvuKy1MwaA61tjw2bW7P9meopurLVvoPgeoLr2YaYoSFwi8TMYdtlvIUy7xDcJb0CGmoK6Nl_b-b8S5LtlnvbLx1eqDfgzIQaXEgFMNVF2EJrOCWWhdSoIeGQgKx5Bwkp328F4y8jTi34-vtl3_v3d9d0DlxEmr_xwVyzbFN81FbzNtLFKtG1NeOWk_k1k0zYUF5eXQJ1IfnSGV51JtSDpJOa-q-Pe9mtawkd-A',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=utf-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'ApplicationGatewayAffinityCORS=05334906ea8a507815b43ce479c48243; ApplicationGatewayAffinity=05334906ea8a507815b43ce479c48243; __RequestVerificationToken=-892vBYHl2nOoS62lPjmegch3hmoFOdAebyexqspAoUeDST7p-8AJCwede5v0A8ZX3QySLh3MkObxfDu02NhTErtayWmtj_ArMvZg-ctN-o1; _lr_tabs_-4olzxu%2Fconsignment-portal-beta={%22sessionID%22:0%2C%22recordingID%22:%225-cb1c932c-0501-40e6-9543-466b55706e4f%22%2C%22lastActivity%22:1658369465520}; _lr_hb_-4olzxu%2Fconsignment-portal-beta={%22heartbeat%22:1658369465520}; _lr_uf_-4olzxu=43e73b70-8782-49ce-a03c-f9c2f6cafe86; .AspNet.ApplicationCookie=_t5JQsleoStO6NPkFrQTVAGFJ0qgy_ocnGLJhL-Nplos7gWjERPQgLFVfMCNP5gGmqNDVjlvZIEZEc3xxedUscLOM2mP1hDnFeK_mBRgik7_Xms754wXn0xReW2aWDTZyBCFTn-_kM2rsxmvOlcPaMHk4PVkAm-gdnXkOylO2bTqHgieYen60nbcftdEGhkCFPf26yS2-mVrcrrx0Un6h0YglorwnCqX2EybDeoeRExzaYk08yb_HGDuzRszg7oVD1A27NBmi2K2jTiITOub4923aExw7OKiEGkZntxralaX_wS8RS8ECjEMvuOKBNmU_H4XN7hgkLGuKXb9wmfLJirHdVrICRPlfhw_fuj82WzVwbt3Ef9XmZMem59vkZDUJuZkwEO6xgnE1s5cZwb7ww9mCgEkGfsJaWNGV4GByoKs_2ZfTXpcNeNseBpiQIhMtzy07eF5W8IY2FJuZ4B3yKUC9hKIGJhPIjaI78KJvYYk5f8Fh5zwrNBiuMs2liNX0e_2g__oahCX7To11LIKoXdcDnRiM-SXxeucxForx-WdxBwo-XVrtczCRnLLUhgOBsRKqMtUHhZa9uNcYOY-jNxv7-4WyZ2K9Dpe9DHCtrKBWvAuzvt3e-FDUtYncCU0pRayx8g2z5inMPFwjiNgG5HNKXZ0qMnt98zFSe7fAZIqy7k1FcrhmVY8pFfZKD_J2chXT4E8hDwMzJK5TUkyHfWR6nqfluFQeMO0phCISd-Om9hC_GxQbj1JA5oP3S4BtrYTuJ9esGyqytrWpAnO-Ak1EkdfpUeBsltObTvHUpeYPkrG0L2_wdGSv5oytipSoV-WKWCmeJw0RP5T3-OGCJ0LhOcKrAvFrrshbYcF3Sf1fi1qYrO128qHqk8TQHhiTFrc0HpKlnghPmDSoSANCq6gbousCg3mFUuB_V7D6VmZXFWVURyQl-4zkeMyIG9__b0l8RtkYJVF-_rgsb4mKGJCAYcFwXzFfD7gVtTEldEorGi3-DV-SQDq4d_6c0I3oLvYVgpsSHhWLg4Z5oc1Z054dQzktFUiR-z1GsE_FqQ-b-e0VSiyh0NYlZXDRdiBgWL9XITdIBS97DSG1vDLhI7FXQc4K2saptkhWnFIzgI',
    'Referer': 'https://portal.stagefront.com/Pricing',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
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
    
