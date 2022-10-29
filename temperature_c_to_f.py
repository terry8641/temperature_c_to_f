#攝氏('C)轉換成華氏('F)程式
#讓使用者輸入攝氏溫度
#然後印出華氏溫度

tempC = input('請輸入攝氏溫度: ')
tempC = float(tempC)
tempF = 9/5 * tempC + 32
print('華氏溫度為: ', tempF)