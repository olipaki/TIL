import React from "react";

function MySite() {
  // 스타일 정의 (사진의 회색 레이아웃 재현)
  const styles = {
    container: {
      display: "flex",
      flexDirection: "column",
      gap: "10px",
      padding: "10px",
      backgroundColor: "#f0f0f0",
    },
    header: { backgroundColor: "#cccccc", padding: "20px", fontSize: "24px" },
    nav: { backgroundColor: "#e0e0e0", padding: "10px" },
    contentWrapper: { display: "flex", gap: "10px" }, // 메인과 사이드바 가로 배치
    main: {
      flex: 3,
      backgroundColor: "white",
      padding: "20px",
      minHeight: "300px",
    },
    sidebar: { flex: 1, backgroundColor: "#e0e0e0", padding: "20px" },
    section: {
      backgroundColor: "#f9f9f9",
      margin: "10px 0",
      padding: "40px",
      border: "1px solid #eee",
    },
    footer: { backgroundColor: "#cccccc", padding: "10px" },
  };

  return (
    <div style={styles.container}>
      <header style={styles.header}>Header</header>
      <nav style={styles.nav}>Navigation</nav>

      <div style={styles.contentWrapper}>
        <main style={styles.main}>
          <h2>Main Content</h2>
          <div style={styles.section}>About</div>
          <div style={styles.section}>Recent Posts</div>
        </main>
        <aside style={styles.sidebar}>Sidebar</aside>
      </div>

      <footer style={styles.footer}>Footer</footer>
    </div>
  );
}

export default MySite; // 다른 곳에서 쓸 수 있게 내보내기!
