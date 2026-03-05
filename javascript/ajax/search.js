// search.js
const searchForm = document.querySelector("#search-form");
const searchInput = document.querySelector("#search-input");

// 검색 함수 정의
async function searchMovies(event) {
  // form의 기본 동작(페이지 새로고침) 방지
  event.preventDefault();

  // 입력값 가져오기 (앞뒤 공백 제거)
  const keyword = searchInput.value.trim();

  // 빈 검색어 체크
  if (keyword === "") {
    alert("검색어를 입력해주세요!");
    return;
  }

  try {
    // API 요청 설정 
    const config = {
      params: {
        language: "ko-KR",
        query: keyword,
      },
      headers: {
        Authorization: `Bearer ${API_KEY}`,
      },
    };

    // TMDB 검색 API 요청
    const response = await axios.get(`${BASE_URL}/search/movie`, config);

    const movies = response.data.results;

    // 기존 내용 비우기
    movieList.innerHTML = "";

    // 검색 결과가 없는 경우
    if (movies.length === 0) {
      movieList.innerHTML = "<p>검색 결과가 없습니다.</p>";
      return;
    }

    // 영화 카드 생성 및 화면에 추가
    for (let movie of movies) {
      const card = document.createElement("div");
      card.className = "movie-card";

      const img = document.createElement("img");
      img.src = `${IMAGE_URL}${movie.poster_path}`;
      img.alt = movie.title;

      const title = document.createElement("h3");
      title.textContent = movie.title;

      const rating = document.createElement("p");
      rating.textContent = `평점: ${movie.vote_average}`;

      card.appendChild(img);
      card.appendChild(title);
      card.appendChild(rating);
      movieList.appendChild(card);
    }
  } catch (error) {
    // 에러 발생 시 사용자에게 메시지 표시
    movieList.innerHTML = "<p>검색 중 오류가 발생했습니다.</p>";
    console.log("에러 발생:", error.message);
  }
}

// form에 submit 이벤트 등록 (버튼 클릭 + Enter 키 모두 동작)
searchForm.addEventListener("submit", searchMovies);
