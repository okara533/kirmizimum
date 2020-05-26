# kirmizimum
Kripto paralarda kapanı verilerinin tersi yönde mi yoksa aynı yönde mi daha çok hareket ettiğini gösteren basit bir algoritma.

Kripto Paralarda Kapanış Mumu ile Getiri Arasındaki İlişki
Kripto paralarda, özellikle alt koinlerde, yükseliş sonrası trene atlamak çok yapılan bir strateji. Bunun nedeni, market verilerine baktığımızda bir kaç altkoinin çok fazla değerlendiğini görmemiz ve yükselişe geçen bir altkoinin daha çok yükseleceğini düşünmemiz. Aslında bu yaklaşım yanlış değil. Bu stratejiyi momentum takibi sınıfına dahil edebiliriz. Ancak momentum için sadece kapanış mumuna bakmak yeterli olmaz. Hacim ve volatilitenin takibi çok önemli. Bu verileri barındıran indikatörleri kullanmanızı, eğer momentum trade yapmak istiyor iseniz, tavsiye ederim.
Bu yazıda basit bir stratejiyi deneyeceğim. Bir ikilinin(Örn:ETHBTC,BTCUSDT) negatif(kırmızı mum) günlük kapanışını, pozitif(yeşil mum) günlük kapanışı sonrası getirilerini kıyaslıyacağım. 
Strateji1: İkili dün negatif kapandı ise al, gün sonunda pozisyonu kapat veya ikili dün pozitif kapandı ise açığa sat gün sonunda pozisyonu kapat.(Trade komisyonu binde 1 olarak hesaplandı, spread veya faiz maliyeti dahil edilmedi)
Strateji2:İkili dün pozitif kapandı ise al, gün sonunda pozisyonu kapat veya ikili dün negatif kapandı ise açığa sat gün sonunda pozisyonu kapat.(Trade komisyonu binde 1 olarak hesaplandı, spread veya faiz maliyeti dahil edilmedi)
HODL: İlk açılış günü ile al elinde tut.
En az100 gün üzeri kapanış verisi olan 604 ikilinin 1 Ocak 2019'dan 24 Mayıs 2020 arasındaki verileri ile toplamda 136,863 kez trade ederek testi yaptım.

Not: pairlist.csv ile datalar uyumsuz. githuba bütün dataları ekleyemediğim için try except ile bu ilgili sorunu çözdüm. isteyen dataları bulup algoritmayı ona göre çalıştırabilir.

![Image description](https://cdn-images-1.medium.com/max/1100/1*ozybFIrLBxw5jtQLFU_nrg.png)

Bu grafik 604 ikili için 510 gün sonunda pozitif getiri sayısı ile negatif getiri sayılarını kendi içinde kıyaslamasını gösteriyor. Başarı oranına baktığımızda sadece bu stratejinin kullanılmasının yetmeyeceği gözüküyor. Ancak Strateji 1'in hem HODL hem de Strateji 2'den PnL başarısı olarak daha başarılı olduğunu görüyoruz. Örnek olarak Strateji 1 604 ikilide uyguladığınızda 189 pozitif,415'i negatif getiri ile kapatmış. Peki toplamda endeks ne kadar getiri elde etti?
