# TIL_Python
    
    
#### enumerate(a)      
    - 반복문 사용 시 몇 번째 반복문인지 확인이 필요할때 사용
    - 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환
  ex)
  <pre><code>
  >>> t = [1, 5, 7, 33, 39, 52]
  >>> for p in enumerate(t):
  ...     print(p)
   </pre></code>
(0, 1)
(1, 5)
(2, 7)
(3, 33)
(4, 39)
(5, 52)
        

#### i.isdecimal()      
    i가 10진수 숫자이면 참 아니면 거짓

ex)
  <pre><code>
  >>> t = [1, '3', 7, 33, 39, 52]
  >>> for i in t:
  ...     if i.isdecimal():
                print(i,end=' ')
   </pre></code>

#### from itertools import combinations          # 중복허용(X), 순서의미(O) 인 조합을 import
       
       사용법
  <pre></code>
  >>>  nums = [1,2,3,4]
  >>>  cmb = list(combinations(nums,3))        # nums배열을 3개씩 조합 후 list로 변경
  >>> 
  </pre></code>
   >>> [1,2,3], [1,2,4] , [2,3,4] 
