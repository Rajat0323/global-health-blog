import Link from 'next/link'
import Image from 'next/image'

export default function Header() {
  return (
    <header
      style={{
        borderBottom: '1px solid #e6eef8',
        padding: '14px 0',
        marginBottom: '40px',
        background: '#ffffff',
      }}
    >
      <div
        style={{
          maxWidth: '1100px',
          margin: '0 auto',
          padding: '0 20px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
        }}
      >
        {/* 🔹 Left: Logo + Site Name */}
        <Link
          href="/"
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: '12px',
            textDecoration: 'none',
          }}
        >
          <Image
            src="/logo.png"
            alt="Symptoms Insight Logo"
            width={36}
            height={36}
            priority
          />

          <span
            style={{
              fontSize: '20px',
              fontWeight: '600',
              color: '#0a4fa3',
              letterSpacing: '0.3px',
            }}
          >
            Symptoms Insight
          </span>
        </Link>

        {/* 🔹 Right: Home Button */}
        <Link
          href="/"
          style={{
            padding: '8px 18px',
            borderRadius: '999px',
            background: '#0a4fa3',
            color: '#ffffff',
            textDecoration: 'none',
            fontSize: '14px',
            fontWeight: '500',
          }}
        >
          Home
        </Link>
      </div>
    </header>
  )
}
