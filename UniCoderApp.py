print('bu kodun amacı yazıyı türkçe karakterlerden arındırmaktır.\nkodu çalıştırıp metinleri türkçeye özgü harflerden arındırabilirsiniz.\nörn: Türkçe -> Turkce')
a = (
 """
"""   
"""
bu kodun amacı yazıyı türkce karakterlerden arındırmaktır.
kodu çalıştırıp metinleri karşılaştırabilirsiniz
"""
)
a = input("metni giriniz: ")

a = a.replace('ç','c').replace('ş','s').replace('ı','i').replace('ğ','g').replace('ö','o').replace('ü','u').replace('Ç','C').replace('Ş','S').replace('İ','I').replace('Ğ','G').replace('Ö','O').replace('Ü','U')
print(str(a))


while True:
    pass

