# used_cars_price
Предсказание цены подержанных авто
Датасет содержит информацию о характеристиках и ценах подержанных автомобилей в некоторой стране.

Целевая переменная (таргет) – selling_price: цена продажи, числовая

Признаки
- name (string): модель автомобиля
- year (numeric, int): год выпуска с завода-изготовителя
- km_driven (numeric, int): пробег на дату продажи
- fuel (categorical: Diesel или Petrol, или CNG, или LPG, или electric): тип топлива
- seller_type (categorical: Individual или Dealer, или Trustmark Dealer): продавец
- transmission (categorical: Manual или Automatic): тип трансмиссии
- owner (categorical: First Owner или Second Owner, или Third Owner, или Fourth & Above Owner): какой по счёту хозяин?
- mileage (string, по смыслу числовой): пробег, требует предобработки
- engine (string, по смыслу числовой): рабочий объем двигателя, требует предобработки
- max_power (string, по смыслу числовой): пиковая мощность двигателя, требует предобработки
- torque (string, по смыслу числовой, а то и 2): крутящий момент, требует предобработки
- seats (numeric, float; по смыслу categorical, int)

