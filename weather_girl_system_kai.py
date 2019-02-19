import tkinter as tk
import tkinter.ttk as ttk
from city import prefectures
from area_code_excel import data_dict
import urllib.request
from bs4 import BeautifulSoup

def callback(c):
    #選択した都道府県に対応する市町村を選択してcombo2に入れる
    selected = prefectures[combo1.get()]
    combo2["values"] = selected
    
def callback2():
    #選択した市町村のエリアコードを取得
    area_code = data_dict[combo2.get()]
    # アクセスするURL
    url = "https://weather.yahoo.co.jp/weather/jp/" + area_code + ".html"
    
    html = urllib.request.urlopen(url)

    soup = BeautifulSoup(html, "html.parser")
    #取得した情報たち
    date = soup.find("p",class_="date").text
    weather = soup.find("p",class_="pict").text
    high_temp = soup.find("li",class_="high").text
    low_temp = soup.find("li",class_="low").text
    rain = soup.find("tr", class_="time")
    rain2 = soup.find("tr", class_="precip")
            
    rain_time1 = rain("td")[0].text
    rain_time2 = rain("td")[1].text
    rain_time3 = rain("td")[2].text
    rain_time4 = rain("td")[3].text
    rain_probability1 = rain2("td")[0].text
    rain_probability2 = rain2("td")[1].text
    rain_probability3 = rain2("td")[2].text
    rain_probability4 = rain2("td")[3].text
    result = (date + "\n" + weather + "\n" + high_temp + " " + low_temp + "\n" + "降水確率" 
          + "\n" + str(rain_time1) + "時は" + " " + str(rain_probability1) + "\n" + str(rain_time2) 
          + "時は" + " " + str(rain_probability2) + "\n" + str(rain_time3) + "時は" + " " 
          + str(rain_probability3) + "\n" + str(rain_time4) + "時は" + " " + str(rain_probability4) + "\n")
    
    next_date = soup("p",class_="date")[1].text
    next_weather = soup("p",class_="pict")[1].text
    next_high_temp = soup("li",class_="high")[1].text
    next_low_temp = soup("li",class_="low")[1].text
    next_rain = soup("tr", class_="time")[1]
    next_rain2 = soup("tr", class_="precip")[1]

    next_rain_time1 = next_rain("td")[0].text
    #next_rain_time2 = next_rain("td")[1].text
    #next_rain_time3 = next_rain("td")[2].text
    #next_rain_time4 = next_rain("td")[3].text
    next_rain_probability1 = next_rain2("td")[0].text
    #next_rain_probability2 = next_rain2("td")[1].text
    #next_rain_probability3 = next_rain2("td")[2].text
    #next_rain_probability4 = next_rain2("td")[3].text
    result += ("\n" + next_date + "\n" + next_weather + "\n" + next_high_temp + " " 
          + next_low_temp + "\n" + "降水確率" + "\n" + str(next_rain_time1) + "時は" + " " 
          + str(next_rain_probability1) + "\n")

    """result += ("\n" + next_date + "\n" + next_weather + "\n" + next_high_temp + " " 
          + next_low_temp + "\n" + "降水確率" + "\n" + str(next_rain_time1) + "時は" + " " 
          + str(next_rain_probability1) + "\n" + str(next_rain_time2) + "時は" + " " 
          + str(next_rain_probability2) + "\n" + str(next_rain_time3) + "時は" + " "
          + str(next_rain_probability3) + "\n" + str(next_rain_time4) + "時は" + " "
          + str(next_rain_probability4) + "\n")"""
    
    #占いも同様に
    astros = ["https://fortune.yahoo.co.jp/12astro/aries", 
              "https://fortune.yahoo.co.jp/12astro/taurus",
              "https://fortune.yahoo.co.jp/12astro/gemini",
              "https://fortune.yahoo.co.jp/12astro/cancer",
              "https://fortune.yahoo.co.jp/12astro/leo",
              "https://fortune.yahoo.co.jp/12astro/virgo",
              "https://fortune.yahoo.co.jp/12astro/libra",
              "https://fortune.yahoo.co.jp/12astro/scorpio",
              "https://fortune.yahoo.co.jp/12astro/sagittarius",
              "https://fortune.yahoo.co.jp/12astro/capricorn",
              "https://fortune.yahoo.co.jp/12astro/aquarius",
              "https://fortune.yahoo.co.jp/12astro/pisces"]
    
    for astro in astros:
        html2 = urllib.request.urlopen(astro)
        soup2 = BeautifulSoup(html2, "html.parser")
        
        name = soup2("strong")[2].text
        point = soup2.find("div", id="jumpdtl")
        point1 = point("img")[1]
        point2 = point("img")[2]
        point3 = point("img")[3]
        point4 = point("img")[4]
        total_point = point1.get("alt")
        love_point = point2.get("alt")
        money_point = point3.get("alt")
        work_point = point4.get("alt")
        
        result += ("\n" + name + "\n" + "総合運: " + total_point + "\n" + "恋愛運: " 
              + love_point + "\n" + "金運: " + money_point + "\n" + "仕事運: " + work_point)
        
    text_w.configure(state=tk.NORMAL)
    text_w.insert(tk.END, result)
    text_w.configure(state=tk.DISABLED)
    text_w.see(tk.END)
        
        
root = tk.Tk()

root.title("お天気お姉さんシステム")

root.geometry("250x400")

#紹介文
frame0 = tk.Frame(master=root)

label1 = tk.Label(frame0, text="お天気お姉さんシステムへようこそ！", font=('メイリオ', '14'))
label1.pack(anchor="w")

label2 = tk.Label(frame0, text="どちらの天気が知りたいですか？", font=('メイリオ', '14'))
label2.pack(anchor="w")

label3 = tk.Label(frame0, text="(○○県○○市と選択してね！)", font=('メイリオ', '14'))
label3.pack(anchor="w")

#市のドロップダウンリスト 
frame1 = tk.Frame(master=root)

label4 = tk.Label(frame1, text="都道府県", font=("メイリオ", "14"))
label4.pack(side="left")

combo1 = ttk.Combobox(frame1, state='readonly')
key = prefectures.keys()
combo1["values"] =  list(key)
combo1.pack(side="left")
#bindで、都道府県を設定した時にcallback関数を呼び出す
combo1.bind("<<ComboboxSelected>>", callback)

#市町村のドロップダウンリスト 
frame2 = tk.Frame(master=root)

label4 = tk.Label(frame2, text=" 市町村  ", font=("メイリオ", "14"))
label4.pack(side="left")

combo2 = ttk.Combobox(frame2, state='readonly')
combo2.pack()

#検索ボタン
frame3 = tk.Frame(master=root)
#commandで、ボタンを押した時にcallback2関数を呼び出す
button = tk.Button(frame3, text="検 索", fg="green", width=5, command=callback2)
button.pack()

text_w = tk.Text(master=root,state=tk.DISABLED,font=("メイリオ","14"),bg="white")
text_w.place(relx=0.05,rely=0.5,relwidth=0.85,relheight=0.4)

sb_y=tk.Scrollbar(master=root,orient=tk.VERTICAL,command=text_w.yview)
sb_y.place(relx=0.90,rely=0.5,relwidth=0.05,relheight=0.4)
text_w.configure(yscrollcommand=sb_y.set)


#frameとrootの配置
frame0.pack()
frame1.pack()
frame2.pack()
frame3.pack()
root.mainloop()