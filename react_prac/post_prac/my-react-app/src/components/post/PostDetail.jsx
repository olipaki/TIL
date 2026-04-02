import { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import api from '../../api';
import useAuthStore from '../../store/useAuthStore';

const PostDetail = () => {
  const { id } = useParams();
  const [post, setPost] = useState(null);
  const navigate = useNavigate();
  const user = useAuthStore((state) => state.user);

  const handleDelete = async () => {
    if (!window.confirm("정말로 삭제하시겠습니까?")) return;
    try {
      await api.delete(`/posts/${id}`);
      alert("삭제되었습니다.");
      navigate('/board/posts');
    } catch (error) {
      console.log(error);
      alert("삭제 권한이 없습니다.");
    }
  };

  useEffect(() => {
    const fetchPost = async () => {
      try {
        const response = await api.get(`/posts/${id}`);
        setPost(response.data);
      } catch (error) {
        console.log(error)
        alert("글을 불러올 수 없습니다.");
        navigate('/board/posts');
      }
    };
    fetchPost();
  }, [id]);

  if (!post) return <div className="p-10 text-center">로딩 중... ⏳</div>;

  const isAuthor = user && post.author.id === user.id;

  return (
    <div className="max-w-3xl mx-auto p-8 mt-10 bg-white dark:bg-slate-900 rounded-2xl shadow-sm">
      <button onClick={() => navigate(-1)} className="mb-6 text-blue-600 font-medium">
        ← 목록으로 돌아가기
      </button>
      
      <h1 className="text-3xl font-extrabold text-slate-900 dark:text-white mb-4">
        {post.title}
      </h1>
      
      <div className="flex items-center gap-3 text-slate-500 mb-8 border-b pb-4">
        <span className="font-bold text-slate-800 dark:text-slate-200">{post.author?.email}</span>
        <span>•</span>
        <span>{new Date(post.created_at).toLocaleDateString()}</span>
      </div>

      <div className="prose dark:prose-invert max-w-none text-slate-700 dark:text-slate-300 leading-relaxed">
        {post.content}
      </div>

    {isAuthor && (
        <button 
        onClick={handleDelete}
        className="px-4 py-2 bg-red-500 text-white rounded-lg hover:bg-red-600 transition-all"
        >
        삭제
        </button>
    )}
    </div>
  );
};

export default PostDetail;
