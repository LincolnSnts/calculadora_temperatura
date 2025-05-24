import streamlit as st

def converter_C_F(graus):
    temp_final = (9/5) * graus + 32
    st.success(f'{graus} °C → {temp_final:.2f} °F')

def converter_C_K(graus):
    temp_final = graus + 273.15
    st.success(f'{graus} °C → {temp_final:.2f} °K')

def converter_F_C(graus):
    temp_final = (5/9) * (graus - 32)
    st.success(f'{graus} °F → {temp_final:.2f} °C')

def converter_F_K(graus):
    temp_final = (5/9) * (graus - 32) + 273.15
    st.success(f'{graus} °F → {temp_final:.2f} °K')
    
def converter_K_C(graus):
    temp_final = graus - 273.15
    st.success(f'{graus} °K → {temp_final:.2f} °C')

def converter_K_F(graus):
    temp_final = (9/5) * (graus - 273.15) + 32
    st.success(f'{graus} °K → {temp_final:.2f} °F')

#Início do Main

def main():
    st.title('CONVERSOR DE TEMPERATURAS')
    temperatura = st.number_input('Digite uma temperatura')
    tipo_origem = st.selectbox('Selecione a unidade de medida de origem', ['Celsius', 'Fahrenheit', 'Kelvin'])
    tipo_destino = st.selectbox('Selecione a unidade de medida de destino', ['Celsius', 'Fahrenheit', 'Kelvin'])

    if st.button('Calcular'):
        if tipo_origem == 'Celsius' and temperatura < -273.15:
            st.error('Temperaturas abaixo de -273.15°C não são aceitas!')

        elif tipo_origem == 'Celsius':
            if tipo_destino == 'Fahrenheit':
                converter_C_F(temperatura)
                
            elif tipo_destino == 'Kelvin':
                converter_C_K(temperatura)
            
            elif tipo_destino == 'Celsius':
                st.error('A temperatura já está em Celsius.')

        if tipo_origem == 'Fahrenheit' and temperatura < -459.67:
            st.error('Temperaturas abaixo de -459.67°F não são aceitas!')

        elif tipo_origem == 'Fahrenheit':
            if tipo_destino == 'Celsius':
                converter_F_C(temperatura)
        
            elif tipo_destino == 'Kelvin':
                converter_F_K(temperatura)

            elif tipo_destino == 'Fahrenheit':
                st.error('A temperatura já está em Fahrenheit.')

        if tipo_origem == 'Kelvin' and temperatura < 0:
            st.error('Temperatura em Kelvin não pode ser negativa!')
        
        elif tipo_origem == 'Kelvin':
            if tipo_destino == 'Celsius':
                converter_K_C(temperatura)
        
            elif tipo_destino == 'Fahrenheit':
                converter_K_F(temperatura)

            elif tipo_destino == 'Kelvin':
                st.error('A temperatura já está em Kelvin.')

main()