import React from "react";
import Card from "./Card";

const ChildrenBase = () => {
  return (
    <>
      <div>ChildrenBase</div>
      <Card />
      <Card>내용물을 채워넣는겁니다.</Card>
      <Card title="하하">
        <h1>안녕하세요</h1>
        <div>jsx같은 것도 전달할 수 있습니다.</div>
      </Card>
    </>
  );
};

export default ChildrenBase;
