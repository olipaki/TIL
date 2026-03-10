import { useState } from "react";

const CharCounter = () => {
  const [text, setText] = useState("");

  return (
    <div style={{ padding: "20px", border: "1px solid #ddd" }}>
      <input
        type="text"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="내용을 입력하세요"
      />
      <p>현재 글자 수: **{text.length}**자</p>
    </div>
  );
};

export default CharCounter;
