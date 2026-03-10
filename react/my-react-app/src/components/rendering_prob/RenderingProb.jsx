import React from "react";
import WeatherStatus from "./WeatherStatus";
import NoticeBoard from "./NoticeBoard";
import StudentList from "./StudentList";
import TodoList from "./TodoList";
import StateBase from "../state_prac/StateBase";
const RenderingProb = () => {
  return (
    <div className="flex flex-col">
      <div>RenderingProb</div>
      <WeatherStatus />
      <WeatherStatus isRaining={true} temperature={10} />
      <hr />
      <NoticeBoard />
      <NoticeBoard
        hasNewMessage={false}
        isMember={false}
        errorMessage="에러임"
      />
      <hr />
      <StudentList />
      <hr />
      <TodoList />
      <hr />
      <StateBase />
    </div>
  );
};

export default RenderingProb;
