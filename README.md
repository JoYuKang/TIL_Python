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
