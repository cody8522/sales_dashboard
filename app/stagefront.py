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
    '_lr_tabs_-4olzxu%2Fconsignment-portal-beta': '{%22sessionID%22:0%2C%22recordingID%22:%225-baed781a-dd40-4f79-82ed-4075200e3379%22%2C%22lastActivity%22:1666705167301}',
    '_lr_hb_-4olzxu%2Fconsignment-portal-beta': '{%22heartbeat%22:1666705167302}',
    '_lr_uf_-4olzxu': '20af60f8-6e7f-41b5-9775-274930a7a2ca',
    '.AspNet.ApplicationCookie': 'wyJOiDMmTOxP2dEIK272UQe6XMUo4abpjptQ_Yj3WxKn2EutsW0bgDHk1mznleXzHIMS7qwIvuC3VaS5JXQP8IadIPPXTS_JO2MHxk1Q-T5mylOm_ReZAqCyhzcE4fXi7icV-Dh_D_UcPK1YsV_od8ofWKtcHLoQKr_A8Okz5maJVn6Vz361Flua01g_q1KKEjMv_bbHXdBeDY_ADIdRwQNSyBMt8MUwjdnTL9JdPM5s6HaUPnU4GhJNfiQTuC5He1MGWHZCarbHHmoeoMTnB5ZvpjY5VuEvrW4AY-I2lqkUhQylp4Z1FcQZ4s9jKYn_5ndFRL_NJKcmnh-kKXfm789q1EecjZdzViNKYttH6Oh3ECb02Ol-ArXfLwET4pw_JM52d9ExkeIfVOYAA1TAVjuH_PPXEW_73csGIGqS5pNzJ4cbutRwbsoIGCxwJcvQDxlOYjb3J69hsCzrbj-_VC--2vRaUc5Qv2XuHyhlRHUQWF3Z5oRGcEBwFUnT5nh7ELVU9L4ivttkd4XtVEyjd7VJW00sa7ZGuIvBsimQjhYTmESz88IOOU0rZjJLy-HuWD8lLTFyxU04Yd1eOEE2FnCTOzNJm4JmhsUXbX7uG0js9yh0bOr0f6-G4KEr-AT2BOGjJ3l3n3pDOTRCaVxPnH5UPMHsUWJt0g1cRCczhHmJqOmtAhVF5pPAo6UfX6y1-fgAeBKKjyP6SSwX19C_IYoMLPCfIERhryo7vJ3PRXCr5NLsx6HyI6sGY3D9NApkl6PgbVzCBxiyP7wtTW9z8EG_OJXsBwfE-sWp1m55efy2jrvap7GoOe_5iG-rmZrxgDyUDlSnCcnom57o_XR7WMRImOfVWw4zNQFRYMEIQWi7CpnOqESR1CuJD3X4ti-3F4_DvFsdDwKpLjhL0NVeZZ56UgFrgaWnsc19YYurN4PBQa3shhJ01Cptl7bbvHmahxshUOm3k-MXXdLCn7-v6ipKHLEEazI2klNTdz_xLuQ1NBdEVs4EAIsXqOY6-cHWTb-lpp7kwyzimpFH4XqyPLd_BEKy1aZk5JL5ppWfo2jm_O9LTX2e8kYZaSI1prky5QdRWtU_NA-SbmBYHbfKLopUFBXfcr6zIe-zixYHVrQ',
}

headers = {
    'authority': 'portal.stagefront.com',
    'accept': 'text/plain, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': '__RequestVerificationToken=mHUM0lpc8_oauGe35xbLc2_4PdfCWmKwJQwi1jGB13PV3HypsONLWhRukfUkAL9yxtA_qcVuz2u1mB7MLY2dxnGg21lnUgwvdu7BHUn304k1; _lr_tabs_-4olzxu%2Fconsignment-portal-beta={%22sessionID%22:0%2C%22recordingID%22:%225-baed781a-dd40-4f79-82ed-4075200e3379%22%2C%22lastActivity%22:1666705167301}; _lr_hb_-4olzxu%2Fconsignment-portal-beta={%22heartbeat%22:1666705167302}; _lr_uf_-4olzxu=20af60f8-6e7f-41b5-9775-274930a7a2ca; .AspNet.ApplicationCookie=wyJOiDMmTOxP2dEIK272UQe6XMUo4abpjptQ_Yj3WxKn2EutsW0bgDHk1mznleXzHIMS7qwIvuC3VaS5JXQP8IadIPPXTS_JO2MHxk1Q-T5mylOm_ReZAqCyhzcE4fXi7icV-Dh_D_UcPK1YsV_od8ofWKtcHLoQKr_A8Okz5maJVn6Vz361Flua01g_q1KKEjMv_bbHXdBeDY_ADIdRwQNSyBMt8MUwjdnTL9JdPM5s6HaUPnU4GhJNfiQTuC5He1MGWHZCarbHHmoeoMTnB5ZvpjY5VuEvrW4AY-I2lqkUhQylp4Z1FcQZ4s9jKYn_5ndFRL_NJKcmnh-kKXfm789q1EecjZdzViNKYttH6Oh3ECb02Ol-ArXfLwET4pw_JM52d9ExkeIfVOYAA1TAVjuH_PPXEW_73csGIGqS5pNzJ4cbutRwbsoIGCxwJcvQDxlOYjb3J69hsCzrbj-_VC--2vRaUc5Qv2XuHyhlRHUQWF3Z5oRGcEBwFUnT5nh7ELVU9L4ivttkd4XtVEyjd7VJW00sa7ZGuIvBsimQjhYTmESz88IOOU0rZjJLy-HuWD8lLTFyxU04Yd1eOEE2FnCTOzNJm4JmhsUXbX7uG0js9yh0bOr0f6-G4KEr-AT2BOGjJ3l3n3pDOTRCaVxPnH5UPMHsUWJt0g1cRCczhHmJqOmtAhVF5pPAo6UfX6y1-fgAeBKKjyP6SSwX19C_IYoMLPCfIERhryo7vJ3PRXCr5NLsx6HyI6sGY3D9NApkl6PgbVzCBxiyP7wtTW9z8EG_OJXsBwfE-sWp1m55efy2jrvap7GoOe_5iG-rmZrxgDyUDlSnCcnom57o_XR7WMRImOfVWw4zNQFRYMEIQWi7CpnOqESR1CuJD3X4ti-3F4_DvFsdDwKpLjhL0NVeZZ56UgFrgaWnsc19YYurN4PBQa3shhJ01Cptl7bbvHmahxshUOm3k-MXXdLCn7-v6ipKHLEEazI2klNTdz_xLuQ1NBdEVs4EAIsXqOY6-cHWTb-lpp7kwyzimpFH4XqyPLd_BEKy1aZk5JL5ppWfo2jm_O9LTX2e8kYZaSI1prky5QdRWtU_NA-SbmBYHbfKLopUFBXfcr6zIe-zixYHVrQ',
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
    
