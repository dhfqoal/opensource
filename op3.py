i, k, heartNum  =0,0,0

numstr, ch, heartstr = "","",""

 

 

if __name__=="__main__" :

        numstr = input("숫자를 여러 개 입력하세요 : ")

        print("")

        i=0

        ch = numstr[i]

        while True :

            heartNum = int(ch)

 

 

            heartstr = ""

            for k in range(0, heartNum) :

                heartstr += "\u2665"

                k += 1

 

 

 

            print(heartstr)

 

            i +=1

            if(i > len(numstr) -1) :

                break

 

 

            ch = numstr[i]

 
