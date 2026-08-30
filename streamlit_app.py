from header import *

st.header("Capital Guesser")

if "points" in st.session_state:
    st.write("You currenty have ", st.session_state.points, " points")
else:
    st.write("You currenty have ", 0, " points")

if "points" not in st.session_state:
    st.session_state.points = 0
if st.button("New Game"):
    st.session_state.points = 0
if "result" not in st.session_state:
    reset_result()
if st.button("Reload Image"):
    reset_result()

print(st.session_state.result)
st.image("./geo_images/geo_image.png")

with st.form(key = "guess_form"):
    guess_capital = st.selectbox("Capital", options_capitals)
    guess_country = st.selectbox("Country", options_countries)
    if st.form_submit_button(label="Submit"):
        if guess_country == st.session_state.country:
            st.session_state.points += 0.5
        if guess_capital == st.session_state.capital:
            st.session_state.points += 0.5
        st.session_state.result = get_satelite_image()
        st.session_state.capital = st.session_state.result["Capital"]
        st.session_state.country = st.session_state.result["Country"]
        st.rerun()

if st.button("Help"):
    st.toast("Click 'New Game' to reset the points." + "\n" + "Click 'Reload Image' to get a new image. Points won't be affected." + "\n" + "Chose a capital and a country from the list. 'Click submit'. +0.5 points for correct capital/country.")

