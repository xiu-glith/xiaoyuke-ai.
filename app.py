import streamlit as st
import random

st.title("🎮 小妤专属猜数字游戏")

# 用session_state保存游戏状态，刷新页面不重置
if "answer" not in st.session_state:
    st.session_state.answer = random.randint(1,10)
if "counts" not in st.session_state:
    st.session_state.counts = 3

st.info(f"系统生成了1-10之间的数字，你还有 {st.session_state.counts} 次机会")
guess = st.number_input("请输入你猜的数字", min_value=1, max_value=10, step=1)

if st.button("确认猜测"):
    st.session_state.counts -=1
    if guess == st.session_state.answer:
        st.success("🎉 猜对了但是没有奖励。。。")
        st.success("✨ 有点实力，小妤好厉害")
        st.balloons()
        st.session_state.counts = 0
    else:
        st.error("❌ 猜错了，有惩罚，惩罚小妤吃零食吧")
        if guess < st.session_state.answer:
            st.warning("提示：你猜的数字小了")
        else:
            st.warning("提示：你猜的数字大了")
    if st.session_state.counts ==0 and guess != st.session_state.answer:
        st.error(f"💔 3次机会用完啦，正确答案是 {st.session_state.answer}")

if st.button("重新开始游戏"):
    st.session_state.answer = random.randint(1,10)
    st.session_state.counts =3
    st.experimental_rerun()
