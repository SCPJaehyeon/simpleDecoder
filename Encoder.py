import sys; #인자를 받아옵니다.
utf = ['cp949','euc-kr', 'utf-8', 'utf-16-le', 'utf-32-le']; #인코딩 형식 리스트 선언
filename = sys.argv[1]; #첫번째인자 인풋파일이름
outfilename = sys.argv[2]; #두번째인자 아웃풋파일이름

def inputfile(filename):
    f = open(filename, 'rb'); #파일을 바이트 단위로 읽음
    fw = open(outfilename,'w'); #파일을 출력하기 위해 선언
    lines = f.readlines(); #줄 단위로 읽음
    i = 0;
    for line in lines:
        try:
            s = line[:-1].decode(utf[0]); #라인별로 예외처리 통해 위에 리스트를 돌며 인코딩을 시작한다.
            print(s, end='\n');
            fw.write(s); #인코딩된 데이터는 아웃풋파일로 들어간다.
        except:
            try:
                s1 = line[:-1].decode(utf[1]);
                print(s1, end='\n');
                fw.write(s1);
            except:
                try:
                    s2 = line[:-1].decode(utf[2]);
                    print(s2, end='\n');
                    fw.write(s2);
                except:
                    try:
                        s3 = line[:-1].decode(utf[3]);
                        print(s3, end='\n');
                        fw.write(s3);
                    except:
                        try:
                            s4 = line[:-1].decode(utf[4]);
                            print(s4, end='\n');
                            fw.write(s4);
                        except:
                            continue;
    
    f.close(); #입출력 함수 닫기
    fw.close();
if(len(sys.argv) > 2): #인자 갯수가 2개 넘으면 함수실행
    inputfile(filename);