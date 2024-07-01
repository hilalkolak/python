import yfinance as yf
import matplotlib.pyplot as plt

# Apple (AAPL) hisse senedi verilerini çekme
apple_data = yf.download('AAPL', start='2020-01-01', end='2022-01-01')

# Veriyi görselleştirme
plt.figure(figsize=(10, 6))
plt.plot(apple_data['Close'], label='Close Price')
plt.title('Apple (AAPL) Hisse Senedi Kapanış Fiyatları')
plt.xlabel('')
plt.ylabel('Fiyat (USD)')
plt.legend()
plt.grid(True)
plt.show()
