import axios from "axios";

const getPosts = async () => {
  try {
    // 1. 주문 넣기 (GET 요청)
    const response = await axios.get("https://jsonplaceholder.typicode.com/posts");
    
    // 2. 결과 출력하기 (response.data에 실제 데이터가 들어있음!)
    console.log("--- 게시글 목록 ---");
    console.log(response.data.slice(0, 5)); // 너무 많으니 5개만 출력해보기
  } catch (error) {
    console.error("데이터 가져오기 실패:", error.message);
  }
};

getPosts();