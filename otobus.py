class Otobus:
    def __init__(self,marka,sofor,maxkoltuk,kalkis,varıs,toplamyolcu):
        self.__marka=marka
        self.__sofor=sofor
        self.__maxkoltuk=50
        self.__kalkis=kalkis
        self.__varıs=varıs
        self.__toplamyolcu=40
        print( "{}markalı {} isimli şöförün {} koltuk sayısına sahip otobüsü {} sehrinden kalkıp {} şehrine gidecektir ve toplam yolcu kapasitesi: {} ".format(self.__marka, self.__sofor, self.__maxkoltuk, self.__kalkis, self.__varıs, self.__toplamyolcu))
    def set_marka(self,yeni_marka):
        self.__marka=yeni_marka
    def get_marka(self):
        return "Otobüsün markası=",self.__marka
    def set_sofor(self,yeni_sofor):
        self.__sofor=yeni_sofor
    def get_sofor(self,sofor):
        return "Yeni şöför ad soyad=",self.__sofor
    def set_maxkoltuk(self,koltuk):
        self.__maxkoltuk=koltuk
    def get_maxkoltuk(self):
        return "Koltuk sayısı=",self.__maxkoltuk
    def set_kalkıs(self,kalkıs_n):
        self.__kalkis=kalkıs_n
    def get_kalkıs(self):
        return "Kalkıs Noktası=",self.__kalkis
    def set_varıs(self,varıs_n):
        self.__varıs=varıs_n
    def get_varıs(self):
        return "Varıs Noktası=",self.__varıs
    def yolculuk_et(self):
        a=0
        kakis=input("Kalkış noktanızı giriniz:")
        varıs=input("varıs noktasını giriniz:")
        yolcu=int(input("yolcu sayısını giriniz: "))
        if(0<yolcu<self.__maxkoltuk):
            a=1
            self.__toplamyolcu+=yolcu
        else:
            print("geçerli bir yolcu sayısı giriniz: ")


o1=Otobus("MERSSEDES","AYHAN AKMAN",50,"ANKARA","İSTANBUL",45)
o1.yolculuk_et()


