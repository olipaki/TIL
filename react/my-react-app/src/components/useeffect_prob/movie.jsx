import { useState, useEffect } from "react";
import axios from "axios";

const MovieList = () => {
  // [1] 영화 데이터를 담을 바구니(State)를 준비합니다.
  const [movies, setMovies] = useState([]);

  // [2] 컴포넌트가 나타나자마자 실행할 미션(useEffect)을 정의합니다.
  useEffect(() => {
    const fetchMovies = async () => {
      // TMDB API 주소 (실제 사용 시 자신의 API KEY를 넣어야 합니다)
      const API_KEY =
        "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlYWI4Yzk4OTNlNzI1YjJlMTY3MTg3Y2VmNjZiYWUzZCIsIm5iZiI6MTYyNzYwODIyMC4xMzUsInN1YiI6IjYxMDM1NDljNGU1MmVkMDA3NTg3ZDhjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.7oh38inWROms2MMFyhEFbbTs8qt3a1tOu_9m-56aQn8";
      const url = `https://api.themoviedb.org/3/movie/now_playing?api_key=${API_KEY}&language=ko-KR`;

      const response = await axios.get(url);

      // [3] 가져온 데이터 중 영화 목록(results)을 바구니에 쏙 넣습니다.
      setMovies(response.data.results);
    };

    fetchMovies();
  }, []); // 빈 배열: 처음 나타날 때 딱 1번만 실행!

  // [4] 바구니에 담긴 영화들을 하나씩 꺼내서 화면에 그립니다.
  return (
    <div>
      <h2>현재 상영 영화 목록</h2>
      <div style={{ display: "flex", flexWrap: "wrap", gap: "20px" }}>
        {movies.map((movie) => (
          <div key={movie.id} style={{ width: "200px" }}>
            <img
              src={`https://image.tmdb.org/t/p/w500${movie.poster_path}`}
              alt={movie.title}
              style={{ width: "100%", borderRadius: "10px" }}
            />
            <h4>{movie.title}</h4>
          </div>
        ))}
      </div>
    </div>
  );
};
