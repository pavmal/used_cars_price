import streamlit as st
import pandas as pd
import pickle
from PIL import Image

import model


with open('./data/model_avto.pickle', 'rb') as f:
    model_cars = pickle.load(f)


def fun_prediction(df):
    price = model_cars.predict(df)[0]
    return round(price)


def get_main_page():
    show_main_page()
    process_side_bar_inputs()


def show_main_page():
    image = Image.open('./data/car.jpg')

    st.set_page_config(
        layout="wide",
        initial_sidebar_state="auto",
        page_title="Демо модели оценки подержанного автомобиля",
        page_icon=image,
    )

    st.write(
        """
        ## Сколько стоит подержанный авто?
        """
    )

    st.image(image)


def write_user_data(df):
    st.write("## Ваши значения данных")
    st.write(df)


def write_prediction(prediction):
    st.write("## Предсказание стоимости автомобиля")
    st.info(f"{prediction:,.2f}")


def process_side_bar_inputs():
    st.sidebar.header('Параметры для изменения')
    user_inputs = sidebar_input_features()
    write_user_data(user_inputs)
    user_inputs = model.scalar_data(user_inputs, scalar_num)
    prediction = fun_prediction(user_inputs)
    write_prediction(prediction)


def sidebar_input_features():
    year = st.sidebar.slider("Год выпуска", min_value=1980, max_value=2020, value=2000, step=1)
    km_driven = st.sidebar.slider("Пробег (км.)", min_value=1, max_value=1000000, value=300000, step=50)
    transmission = st.sidebar.selectbox("Коробка передач", ("Механика", "Автомат"))
    owner = st.sidebar.selectbox("Владелец по счёту", ("Первый", "Второй", "Третий", "Четвертый и более", "Test Drive"))
    max_power = st.sidebar.slider("Мощность движка (тыс оборотов/мин)", min_value=30, max_value=400, value=90, step=10)
    seats = st.sidebar.slider("Количество мест в авто", min_value=1, max_value=14, value=5, step=1)

    convertor = {
        "Механика": 1,
        "Автомат": 0,
        "Первый": 1,
        "Второй": 2,
        "Третий": 3,
        "Четвертый и более": 4,
        "Test Drive": 0,
    }

    data = {
        "year": year,
        "km_driven": km_driven,
        "transmission": convertor[transmission],
        "owner": convertor[owner],
        "max_power": max_power,
        "seats": seats,
    }

    df = pd.DataFrame(data, index=[0])

    return df


if __name__ == "__main__":
    scalar_num = model.get_ready_forecast()
    get_main_page()
