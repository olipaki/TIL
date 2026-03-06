import React from "react";
import Article from "./Article";
import TagsComponent from "./TagsComponent";
import Todos from "./Todos";
import Hello from "./Hello";

const JsxBase = () => {
  return (
    <>
      <h1>JsxBase</h1>
      <Article />
      <hr />
      <TagsComponent />
      <hr />
      <Todos />
      <hr />
      <Hello />
    </>
  );
};

export default JsxBase;
