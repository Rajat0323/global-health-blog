import { getSortedPostsData } from '../lib/posts'
import Link from 'next/link'

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
    <main style={{ padding: '40px', maxWidth: '1100px', margin: 'auto' }}>
      <h1 style={{ fontSize: '36px', color: '#0a4fa3' }}>
        Symptoms Insight
      </h1>

      <p style={{ color: '#555', marginBottom: '30px' }}>
        Trusted health information written for awareness, early detection,
        and better understanding of symptoms.
      </p>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(280px,1fr))', gap: '20px' }}>
        {allPostsData.map((post) => (
          <Link key={post.slug} href={`/blog/${post.slug}`}>
            <div style={{
              border: '1px solid #e6eef8',
              borderRadius: '12px',
              padding: '20px',
              cursor: 'pointer',
              background: '#fff',
              boxShadow: '0 6px 16px rgba(0,0,0,0.06)'
            }}>
              <h3 style={{ color: '#0a4fa3' }}>{post.title}</h3>
              <small style={{ color: '#777' }}>{post.date}</small>
              <p style={{ marginTop: '10px', color: '#444' }}>
                {post.description}
              </p>
            </div>
          </Link>
        ))}
      </div>
    </main>
  )
}
