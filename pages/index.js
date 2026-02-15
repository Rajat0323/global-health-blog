import Link from 'next/link'
import { getSortedPostsData } from '../lib/posts'
import Header from '../components/Header'

export async function getStaticProps() {
  const allPostsData = getSortedPostsData()

  return {
    props: {
      allPostsData,
    },
  }
}

export default function Home({ allPostsData }) {
  return (
    <>
      <Header />

      <main
        style={{
          maxWidth: '1100px',
          margin: '60px auto',
          padding: '20px',
        }}
      >
        <h1 style={{ color: '#0a4fa3', fontSize: '36px' }}>
          Symptoms Insight
        </h1>

        <p style={{ color: '#555', marginBottom: '40px' }}>
          Trusted health information written for awareness, early detection,
          and better understanding of symptoms.
        </p>

        <div
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
            gap: '24px',
          }}
        >
          {allPostsData.map((post) => (
            <Link
              key={post.slug}
              href={`/blog/${post.slug}`}
              style={{ textDecoration: 'none' }}
            >
              <div
                style={{
                  border: '1px solid #e6eef8',
                  borderRadius: '14px',
                  padding: '22px',
                  background: '#fff',
                  boxShadow: '0 6px 16px rgba(0,0,0,0.06)',
                }}
              >
                <h3 style={{ color: '#0a4fa3' }}>
                  {post.title}
                </h3>

                <p style={{ color: '#777', fontSize: '14px' }}>
                  {new Date(post.date).toLocaleDateString('en-GB')}
                </p>

                <p style={{ color: '#444', marginTop: '10px' }}>
                  {post.description}
                </p>
              </div>
            </Link>
          ))}
        </div>
      </main>
    </>
  )
}
