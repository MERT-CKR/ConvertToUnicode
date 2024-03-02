def main():
    print('bu kodun amacı yazıyı türkçe karakterlerden arındırmaktır.\nkodu çalıştırıp metinleri türkçeye özgü harflerden arındırabilirsiniz.\nörn: Türkçe -> Turkce')
    a =""" """
    a = input("\nmetni giriniz: ")


    tr =['ç','ş','ı','ğ','ö','ü','Ç','Ş','İ','Ğ','Ö','Ü']
    withoutTr=['c','s','i','g','o','u','C','S','I','G','O','U']

    for i in range(12):
        a=a.replace(tr[i],withoutTr[i])
    print("\n")
    print(a)
    print("\n")



while True:
    main()
    keepContinue = input("programı yeniden başlatmak için 1 e basın:\n")
    if keepContinue != "1":
        break