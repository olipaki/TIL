// components/Layout.jsx

const Layout = ({ children }) => {
  return (
    <div style={{ border: "1px solid #ccc", padding: "20px" }}>
      {/* 공통 헤더 영역 */}
      <header style={{ backgroundColor: "#f0f0f0", padding: "10px" }}>
        <h2>=== 헤더 ===</h2>
      </header>

      {/* 부모가 감싸서 보낸 내용이 이 자리에 쏙 들어옵니다! */}
      <main style={{ margin: "20px 0" }}>{children}</main>

      {/* 공통 푸터 영역 */}
      <footer style={{ backgroundColor: "#f0f0f0", padding: "10px" }}>
        <p>=== 푸터 ===</p>
      </footer>
    </div>
  );
};

export default Layout;
