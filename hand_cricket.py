import streamlit, random
if not streamlit.session_state.get('score'):
    streamlit.session_state.score = 0
streamlit.title('HandCricket Game')
cols = streamlit.columns([1, 1])
with cols[1]:
    b = streamlit.button('Play Now', use_container_width=True, type='primary')
    with streamlit.container(border=True):
        streamlit.write('System 🎾')
        c = random.randrange(1, 7)
        streamlit.header(c)
with cols[0]:
    a = streamlit.text_input('Enter Number', label_visibility='collapsed', placeholder='Enter Number Between 1 and 6')
    if a and (int(a) < 1 or int(a) > 6):
         streamlit.toast('Enter a number bte 1 and 6')
         a = 0
    with streamlit.container(border=True):
        streamlit.write('User 🏏')
        if b:
            streamlit.header(a)
            if int(a) != c:
                streamlit.session_state.score += int(a)
            else:
                 streamlit.toast(f"You are Out, score: {streamlit.session_state.score}")
        else:
             streamlit.header(0)

with streamlit.container(border=True):
        streamlit.header(streamlit.session_state.score)