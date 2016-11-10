# ������� �������������� ��� ��������� ��������������� �����������
# �' ����
# ������ ������������
# worked with Python 2.7.10
# @ Tasos Chatzipapadopoulos

'''

�������� 5� ��������� ����������
������������� 7 / ������ 89
�� ���������� ��� ��� ������� ��� ����� ���� Python � ����� �������� ������� �����
True/False �������. ������, �� ������ ��� True ����� ��� �� �� ������ ��� False.
�� ������� ���������, �� Python, � ������ ��������� ��� �������� ����� ���
������, �� ��������� �� True ���� ��� �� False ����������, ��� ��������� �������
������������. ��� ����������� �� ������ ����� �������� ���� �� ���������������
�� ���� if. �������� ��� �� ����� �������� ��� ������ ���� ��� ���� True.          

'''

# �������� �������
aList = [True, False, True, False, True, False, True, False,
         True, False, True, False, True, False, True, False, True, False,
         True, False, True, False, True, False, True, False, True, False]

# ������� ��� ������� ����� �� ��������� ��������������
def orderBoolean(aList):
    n = len(aList)
    mid = n // 2
    for i in range(1, mid, 2) :
        aList[i], aList[n-i-1] = aList[n-i-1], aList[i]
    return aList

# ����� ����������
x = orderBoolean(aList)
print x
