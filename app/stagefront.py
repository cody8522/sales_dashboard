import requests
import urllib3
import pandas as pd
import warnings
import streamlit as st
import altair as alt

urllib3.disable_warnings()
warnings.filterwarnings('ignore')

cookies = {
    'ApplicationGatewayAffinityCORS': '05334906ea8a507815b43ce479c48243',
    'ApplicationGatewayAffinity': '05334906ea8a507815b43ce479c48243',
    '_lr_uf_-4olzxu': 'eca17b6d-f932-4c70-8256-44d114ac0de0',
    '__RequestVerificationToken': 'BldPUZFzYrJGOvaG9URKWiLxLAmJojDlziuhe8VrZhS3w-3_SFaqQOL1wZzeKQK48H43hHrRlHZQkRZ4fVzdI9OwavO9F3Qatlagc7_fsHY1',
    '.AspNet.ApplicationCookie': 'kvCjuJDWrw7FvKF2_ZFEFgMx4nlS2aXDBUWJ6jPylopgHRVylRLHMUlcL0iMP7JaEGan9jQHmntZFpB2OW9MHBhHSfyeijY5xOp24Fk2rvi9UQWErd2jVvdvCRiLhjbEJWKlikwJ9Tha31Wr5TdST7ZbMp_lb9VySXDTwXHt_7agWJq7JsUYp7EjBoMl4FkBNbDW10HyiTPFPK554vrOMbSQNXgiovFy8Zdc5OdGDKSsI3g8vCm65z56TBDraGQI-K7k_EhWTjq9p-RwWbo2KD7HvoJUm-KKk0drJtdxvdQmbcWSDOnQica4iqRf9V8rTeqSXdvQ62__Q2FNypyL0cv_zKnefh4E6gUlKKYkhdUby5n7HN2u8MLgXVGBpvLvXl2KdpOJue17-R_xqbLIT6Wx48pca4n2t8OBjrjkXzXLmJULL1yD2-3S2ZecnvnKCqmDdJzeILF9lngcBQRg6h6MG4iMyxNEv7n3DJhTES9ghWbPlAMTZZjafIzdustA8qsFet3PMVT3X_ZH3mQJr4v8v3kiqlints6GZ8oe7_SPyo6Z4CkQDoWKvq-j0VT-VAz0r1FIpMhHfrIo8HACM98vECTA6Igf9o2WlCiMvD_X4ClimUJoxai6SXm1W5FS6_Zby49ebF8DvpiGb21CU19j3If1Rj0-vRBmG_QvPh16THFBMAMrwBzou051Zk38bg0EF33-X2VTj_nBntHoY5aAxqT54OZfeS7uqk0zJ0ptX39r2synUfwm4o2Yn86ZIxnWRmthJA1_XjnH2sIIFzvEYdLPNtB0OlLv0ng3sdnVoCLjd0q0cVS_003ns3dlmkdKHIKMg_xGqc0V6uTjo2Qhv2Hg1fi10XPQXQwbvk0MwKrgKgvm1mLtcemwNZQQLL1mzCihCjkRdKJXY64Z2khCuTRcrqNtTKZs9VwurLVmzpEZK5jngHcn1WCX_ouHXiSX5i9KFRDCuNilgJBfQOyFfT-ygVE7fG-PpfKcryU6iFLUAFfHBCDOiGxM-5B-MyFToGibingTrh8nRd80vtofcV30VDzWb5rDSGuFLExAIatZABJBgmgAHXfyyQgyQG1F_s8ltHo-A5se98VYS1vCUfbLt8JGLQuMsvuwW3g',
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
    sg_id = st.text_input(label= 'SeatGeek ID')
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
    print(df)
    df2 = df[2].str.split("T", 1, expand = True)
    print(df2)

    sales_df2['Year'] = df[0]
    sales_df2['Month'] = df[1]
    sales_df2['Day'] = df2[0]
    sales_df2['Time'] = df2[1]
    sales_df2.drop(columns = ["putc"], inplace = True)

    print(sales_df2)

    df_rename = sales_df2.rename(columns = {'bp':'Price', 'q' : 'Qty', 's' : 'Sec', 'r' : 'Row'})
    print(df_rename)

    final_df = df_rename[['Year', 'Month', 'Day', 'Time', 'Price', 'Qty', 'Sec', 'Row']]
    final_df = final_df.sort_values(by=['Year', 'Month','Day', 'Time'])
    print(final_df)

    final_df['date_string'] = final_df['Year'].astype(str) + "-" + final_df['Month'].astype(str)+ "-" +  final_df['Day'].astype(str)

    ##volume chart
    v_scale = [0, max(final_df['Qty']) + 5]
    volume_chart = alt.Chart(final_df).mark_bar().encode(
    x = alt.X('date_string', title = 'Date'),
    y =alt.Y('Qty', scale =alt.Scale(domain = v_scale)),
        tooltip = ['date_string', 'Qty'],).interactive().properties(width = 500)


    ##price chart
    x_scale = [min(final_df['Price']) - 20, max(final_df['Price']) + 20]
    price_chart = alt.Chart(final_df).mark_line().encode(
    x = alt.X('date_string', scale=alt.Scale(zero=False), title = 'Date'),
    y = alt.Y('mean(Price)', scale = alt.Scale(domain = x_scale), title = 'Price'),
    tooltip = ['date_string','mean(Price)'],).interactive().properties(width = 500)

    col1, col2 = st.columns(2)

    with col1:
        st.header("Price over Time")
        st.altair_chart(price_chart, use_container_width=True)
    with col2:
        st.header("Volume over Time")
        st.altair_chart(volume_chart, use_container_width=True)

    st.dataframe(final_df)

    final_df = final_df.to_csv(index = False).encode('utf-8')
    st.download_button(label = "Export to CSV", data = final_df, 
        file_name ="seatgeek_sales.csv", mime = 'text/csv')
