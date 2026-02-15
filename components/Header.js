import Link from "next/link";

export default function Header() {
  return (
    <header className="header">
      <div className="header-inner">
        <h1 className="logo">
          <Link href="/">Symptoms Insight</Link>
        </h1>

        <nav className="nav">
          <Link href="/">Home</Link>
          <Link href="/blog">Blog</Link>
        </nav>
      </div>
    </header>
  );
}
