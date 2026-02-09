### [Category 관리]
1. [POST] /categories: 카테고리 생성 (name 입력)
- 어떤 정보를 받을것이냐 - name
    CategoryCreate 데이터 모델이 필요하다.
- 어떤 응답을 할것이냐.
- category에 대한 create orm이 필요하다.
- category는 사실 unique한게 맞아보여요.
- {id : 1, name : 전자제품}, {id : 2, name : 전자제품}
    같이 있으면 안된다.

2. [GET] /categories: 모든 카테고리 목록 조회

3. [GET] /categories/{category_id}/products: 특정 카테고리에 속한 상품들만 모아보기
    prodct를 만들고 나서 진행을 해야함.

### [Product 관리]
1. [POST] /products: 상품 생성 (name, price, category 입력)
- name, price, category를 입력받습니다 - ProductCreate 데이터 모델이 필요
- response - category 포함해서.
