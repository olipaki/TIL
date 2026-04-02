import { Outlet, NavLink } from "react-router-dom";
import "./Layout.css";
import Header from "../components/auth/Header";
// import { useThemeStore } from "../store/useThemeStore";

const Layout = () => {
  return (
    <div
      className="rounded-3xl px-6 py-3 mb-2"
      style={{ backgroundColor: "#dff4ff" }}
    >
      <Header />

      <main className="min-h-100 m-2 p-8 bg-white dark:bg-slate-400 border border-gray-100 dark:border-slate-700 shadow-inner rounded-[2.5rem] dark:text-gray-200">
        <Outlet />
      </main>
      <footer className="mt-8 py-4 flex justify-center">
        <div
          className="bg-white dark:bg-slate-700 border border-gray-100 dark:border-slate-600 rounded-2xl px-5 py-3 flex flex-col gap-1.5"
          style={{ minWidth: "220px" }}
        >
          <p className="text-[10px] uppercase tracking-widest text-gray-400 font-medium">
            Contact
          </p>
          <div className="border-t border-gray-100 dark:border-slate-600 pt-1.5 flex flex-col gap-1">
            <div className="flex items-center gap-2">
              <span className="text-[11px] text-gray-400 w-10">E-mail</span>
              <span className="text-[11px] text-gray-700 dark:text-gray-200">
                shue03@naver.com
              </span>
            </div>
            <div className="flex items-center gap-2">
              <span className="text-[11px] text-gray-400 w-10">Phone</span>
              <span className="text-[11px] text-gray-700 dark:text-gray-200">
                02-1234-0000
              </span>
            </div>
          </div>
          <div className="border-t border-gray-100 dark:border-slate-600 pt-1.5">
            <p className="text-[10px] text-gray-400 text-center">
              © 2026 MyShop Corp.
            </p>
          </div>
        </div>
      </footer>

      {/* <footer className="mt-12 p-8 bg-gray-50 dark:bg-slate-600 rounded-4xl text-center border border-gray-100 dark:border-slate-700">
        <div className="space-y-1">
          <p className="text-xs uppercase tracking-widest text-gray-400 font-semibold">Customer Support</p>
          <p className="text-2xl font-black text-gray-500">1234-0000</p>
        </div>
        <div className="mt-6 pt-6 border-t border-gray-200/50 text-xs text-gray-400">
          <p>© 2026 MyShop Corp. All rights reserved.</p>
        </div>
      </footer> */}
    </div>
  );
};

export default Layout;
