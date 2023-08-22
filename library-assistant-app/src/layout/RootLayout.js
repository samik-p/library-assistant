import { NavLink, Outlet } from "react-router-dom"

export default function RootLayout() {
    return (
      <div>
        <div className="root-layout">
          <nav>
            <NavLink to="/"></NavLink>
            <NavLink to="/staff"></NavLink>
          </nav>
        </div>
        <main>
          <Outlet />
        </main>
      </div>

    )
  }