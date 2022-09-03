# 데이터 구조

### 목차

1. 순서가 있는 데이터 구조
   1. 문자열(String)
   2. 리스트(List)
   3. 튜플(Tuple)

2. 순서가 없는 데이터 구조
   1. 셋(Set)
   2. 딕셔너리(Dictionary)

3. 얕은 복사와 깊은 복사

---

- 순서가 있는 데이터 구조

  *데이터 구조 활용*

  1. 데이터 구조를 활용하기 위해서는 메서드(method)를 활용

  2. 메서드는 클래스 내부에 정의한 함수, 사실상 함수 동일

  3. 쉽게 설명하자면 객체의 기능 (추후 객체 지향 프로그래밍에서 학습)

     ​        데이터 구조.메서드() 형태로 활용

     ​        어렵게 느껴지면 주어.동사()

  데이터 구조 활용 예시

    List.append(10), String.split(),

  - 문자열(String)
    - s.find(x) : x의 첫 번째 위치를 반환. 없으면, -1을 반환
    - s.index(x) : x의 첫 번째 위치를 반환. 없으면, 오류 발생
    - s.isalpha() : 알파벳 문자 여부 *단순 알파벳이 아닌 유니코드 상 Letter (한국어도 포함)*
    - s.isupper() : 대문자 여부
    - s.islower() : 소문자 여부
    - s.istitle() : 타이틀 형식 여부
    - s.replace(old, new[,count]) : 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
    - s.strip([chars]) : 공백이나 특정 문자를 제거
    - s.split(sep=None, maxsplit=-1) : 공백이나 특정 문자를 기준으로 분리
    - 'separator'.join([iterable]) : 구분자로 iterable을 합침
    - s.capitalize() : 가장 첫 번째 글자를 대문자로 변경
    - s.title() : 문자열 내 띄어쓰기 기준으로 각 단어의 첫글자는 대문자로, 나머지는 소문자로 변환
    - s.upper() : 모두 대문자로 변경
    - s.lower() : 모두 소문자로 변경
    - s.swapcase() : 대<->소문자 서로 변경
  - 리스트(List)
    - L.append(x) : 리스트 마지막에 항목 x를 추가
    - L.insert(i, x) : 리스트 인덱스 i에 항목 x를 삽입
    - L.remove(x) : 리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거 항목이 존재하지 않을 경우, ValueError
    - L.pop() : 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거
    - L.pop(i) : 리스트의 인덱스 i에 있는 항목을 반환 후 제거
    - L.extend(m) : 순회형 m의 모든 항목들의 리스트 끝에 추가 (+=과 같은 기능)
    - L.index(x, start, end) : 리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환
    - L.sort() : 리스트를 정렬 (매개변수 이용 가능)
    - L.count(x) : 리스트에서 항목 x가 몇 개 존재하는지 갯수를 반환
    - enumerate(List) : 위치와 값을 동시에 저장
  - 튜플(Tuple)
    - 튜플은 변경할 수 없기 대문에 값에 영향을 미치지 않는 메서드만을 지원
    - 리스트 메서드 중 항목을 변경하는 메서드들을 제외하고 대부분 동일

- 순서가 없는 데이터 구조

  - 셋(Set)
    - s.copy() : 셋의 얕은 복사본을 반환
    - s.add(x) : 항목 x가 셋 s에 없다면 추가
    - s.pop() : 셋 s에서 랜덤하게 항목을 반환하고, 해당 항목을 제거 set이 비어 있을 경우, KeyError
    - s.remove(s) : 항목 x를 셋 s에서 삭제, 항목이 존재하지 않을 경우, KeyError
    - s.discard(t) : 셋 t에 있는 모든 항목 중 셋 s에 없는 항목을 추가
    - s.clear() : 모든 항목을 제거
    - s.isdisjoint(t) : 셋 s가 셋 t의 서로 같은 항목을 하나라도 갖고 있지 않은 경우, True 반환
    - s.issubset(t) : 셋 s가 셋 t의 하위 셋인 경우, True 반환
    - s.issuperset(t) : 셋 s가 셋 t의 상위 셋인 경우, True 반환
  - 딕셔너리(Dictionary)
    - d.clear() : 모든 항목을 제거
    - d.copy() : 딕셔너리 d의 얕은 복사본을 반환
    - d.keys() : 딕셔너리 d의 모든 키를 담은 뷰를 반환
    - d.values() : 딕셔너리 d의 모든 값을 담은 뷰를 반환
    - d.items() : 딕셔너리 d의 모든 키-값의 쌍을 담은 뷰를 반환
    - d.get(k) : 키 k의 값을 반환하는데, 키 k가 딕셔너리 d에 없을 경우 None을 반환
    - d.get(k, v) : 키 k의 값을 반환하는데, 키 k가 딕셔너리 d에 없을 경우 v을 반환
    - d.pop(k) : 키 k의 값을 반환하고 키 k인 항목을 딕셔너리 d에서 삭제하는데, 키 k가 딕셔너리 d에 없을 경우 KeyError를 발생
    - d.pop(k, v) : 키 k의 값을 반환하고 키 k인 항목을 딕셔너리 d에서 삭제하는데, 키 k가 딕셔너리 d에 없을 경우 v를 반환
    - d.update([other]) : 딕셔너리 d의 값을 매핑하여 업데이트

- 얕은 복사와 깊은 복사

  - 할당

    - 대입 연산자(=) : 리스트 복사 확인하기

  - 얕은 복사

    - Slice 연산자를 활용하여 같은 원소를 가진 리스트지만 연산된 결과를 복사 (주소가 다름)

      *ex) b = a[:]*

  - 깊은 복사

    - 리스트 복사 확인하기

      ![image-20220725210801380](Python 4.assets/image-20220725210801380.png)