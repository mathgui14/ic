class SignalFilter:
    def __init__(self):
        self.last_values = []
        self.constante_E = 3.398338

    def filter_signal(self, pure_value):
        self.last_values.append(pure_value)
        if len(self.last_values) > 6:
            self.last_values.pop(0)

        E_media = sum(self.last_values) / 6
        V_seis = self.calculate_variation()

        # Cálculo do valor filtrado F
        F = (E_media * pure_value * V_seis) / 6490

        print(f"Resultado filtrado (F): {F:.2f}")

    def calculate_variation(self):
        if len(self.last_values) < 2:
            return 0

        last_value, prev_value = self.last_values[-1], self.last_values[-2]
        return last_value - prev_value

# Exemplo de uso
signal_filter = SignalFilter()

# Valores puros (exemplo)
valores_puros = [400, 400, 410, 420, 415, 405]

for valor_puro in valores_puros:
    signal_filter.filter_signal(valor_puro)
