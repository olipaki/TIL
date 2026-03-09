// WeatherStatus.jsx
const WeatherStatus = ({ isRaining, temperature }) => {
    return (
    <div style={{ border : "1px solid blue", margin: "10px" , padding: "10p"}}>
        <h3>오늘의 날씨</h3>
        {/* 1.비 여부 체크 */}
        
    </div>
}
const WeatherStatus = ({ isRaining, temperature }) => {
  return (
    <div style={{ border: "1px solid blue", margin: "10px", padding: "10px" }}>
      <h3>오늘의 날씨</h3>
      {/* 1. 비 여부 체크 */}
      <p>{isRaining ? "☔ 우산을 챙기세요!" : "☀️ 날씨가 좋습니다!"}</p>

      {/* 2. 온도 체크 */}
      <p>{temperature >= 30 ? "🔥 더운 날씨입니다" : "☁️ 적당한 날씨입니다"}</p>
    </div>
  );
};

export default WeatherStatus;
