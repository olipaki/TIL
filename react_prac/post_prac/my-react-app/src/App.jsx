import './App.css'

import { RouterProvider } from "react-router-dom";
import router from "./pages/routers";
import { useEffect } from 'react';
import useAuthStore from './store/useAuthStore';
function App() {

  const checkAuth = useAuthStore((state) => state.checkAuth);

    useEffect(() => {
      checkAuth();
    }, []);

    return (
      <div>
        <RouterProvider router={router} />
      </div>
    )
}

export default App
