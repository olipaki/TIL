import { useEffect, useState } from 'react';

import { Link, useNavigate } from 'react-router-dom';
import api from '../../api';
import useAuthStore from '../../store/useAuthStore';


const PostList = () => {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  const user = useAuthStore((state) => state.user);

  const handleWriteClick = (e) => {
    if (!user) {
      e.preventDefault();
      alert("로그인 하세요라");
      navigate("/auth/login");
    }
};

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const response = await api.get("/posts");
        setPosts(response.data);
      } catch (error) {
        console.error("게시글 로딩 실패:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchPosts();
  }, []);

  if (loading) return <div className="p-10 text-center text-slate-500">로딩 중...</div>;

  return (
    <div className="max-w-4xl mx-auto p-6">
      {/* 헤더 영역 */}
      <div className="flex justify-between items-end mb-8 border-b pb-6">
        <div>
          <h1 className="text-3xl font-black text-slate-900">글 목록</h1>
          <p className="text-slate-500 mt-1 text-sm">다양한 소식을 확인해보세요.</p>
        </div>
        <Link 
          to="/board/posts/new" 
          className="px-5 py-2.5 bg-blue-600 hover:bg-blue-700 text-white text-sm font-bold rounded-2xl shadow-lg shadow-blue-100 transition-all active:scale-95"
          onClick={handleWriteClick}
        >
          글쓰기
        </Link>
      </div>

      {/* 게시글 목록 */}
      <div className="grid gap-4">
        {posts.length > 0 ? (
          posts.map((post) => (
            <div 
              key={post.id} 
              className="group p-6 bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 rounded-3xl shadow-sm hover:shadow-md hover:border-blue-200 transition-all cursor-pointer"
            >
              <div className="flex justify-between items-start mb-2">
                <Link to={`/board/posts/${post.id}`} className="group">
                  <h2 className="text-xl font-bold text-slate-800 dark:text-slate-100 group-hover:text-blue-600 transition-colors">
                    {post.title}
                  </h2>
                </Link>
                <span className="text-xs text-slate-400 font-medium">
                  {new Date(post.created_at).toLocaleDateString()}
                </span>
              </div>
              
              <p className="text-slate-600 dark:text-slate-400 line-clamp-2 text-sm mb-4 leading-relaxed">
                {post.content}
              </p>

              <div className="flex items-center gap-2 border-t pt-4 border-slate-50 dark:border-slate-800">
                <div className="w-6 h-6 bg-blue-100 dark:bg-blue-900/30 rounded-full flex items-center justify-center text-[10px] text-blue-600 font-bold">
                  {post.author.email[0].toUpperCase()}
                </div>
                <span className="text-xs font-semibold text-slate-500 dark:text-slate-400">
                  {post.author.email}
                </span>
              </div>
            </div>
          ))
        ) : (
          <div className="text-center py-20 text-slate-400">등록된 게시글이 없습니다.</div>
        )}
      </div>
    </div>
  );
};

export default PostList;
