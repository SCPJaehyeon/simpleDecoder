import sys; #���ڸ� �޾ƿɴϴ�.
utf = ['cp949','euc-kr', 'utf-8', 'utf-16-le', 'utf-32-le']; #���ڵ� ���� ����Ʈ ����
filename = sys.argv[1]; #ù��°���� ��ǲ�����̸�
outfilename = sys.argv[2]; #�ι�°���� �ƿ�ǲ�����̸�

def inputfile(filename):
    f = open(filename, 'rb'); #������ ����Ʈ ������ ����
    fw = open(outfilename,'w'); #������ ����ϱ� ���� ����
    lines = f.readlines(); #�� ������ ����
    i = 0;
    for line in lines:
        try:
            s = line[:-1].decode(utf[0]); #���κ��� ����ó�� ���� ���� ����Ʈ�� ���� ���ڵ��� �����Ѵ�.
            print(s, end='\n');
            fw.write(s); #���ڵ��� �����ʹ� �ƿ�ǲ���Ϸ� ����.
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
    
    f.close(); #����� �Լ� �ݱ�
    fw.close();
if(len(sys.argv) > 2): #���� ������ 2�� ������ �Լ�����
    inputfile(filename);