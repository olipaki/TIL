import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../../api';

const PostWrite = () => {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');

  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await api.post('/posts', { 
        title, 
        content 
      });

      if (response.status === 201) {
        alert('글이 성공적으로 등록되었습니다!');
        navigate('/board/posts');
      }
    } catch (error) {
      console.error('글 작성 에러:', error);
      alert(error.response?.data?.detail || '작성 중 오류가 발생했습니다.');
    }
  };

  return (
    <div className="max-w-2xl mx-auto p-8 bg-white rounded-xl shadow-md mt-10">
      <h2 className="text-2xl font-bold text-gray-800 mb-6">게시글 작성</h2>
      <form onSubmit={handleSubmit} className="flex flex-col gap-4">
        <input
          type="text"
          placeholder="제목을 입력하세요"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          className="w-full px-4 py-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none transition-all"
          required
        />
        <textarea
          placeholder="내용을 입력하세요"
          value={content}
          onChange={(e) => setContent(e.target.value)}
          rows="12"
          className="w-full px-4 py-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none resize-none transition-all"
          required
        />
        <div className="flex justify-end gap-3 mt-2">
          <button
            type="button"
            onClick={() => navigate(-1)}
            className="px-6 py-2.5 text-gray-500 font-medium hover:bg-gray-100 rounded-lg transition-colors"
          >
            취소
          </button>
          <button
            type="submit"
            className="px-6 py-2.5 bg-blue-600 text-white font-bold rounded-lg hover:bg-blue-700 shadow-lg shadow-blue-200 active:scale-95 transition-all"
          >
            등록하기
          </button>
        </div>
      </form>
    </div>
  );
};

export default PostWrite;
