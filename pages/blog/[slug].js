import Head from 'next/head'
import { getAllPostSlugs, getPostData } from '../../lib/posts'

export async function getStaticPaths() {
  const paths = getAllPostSlugs()

  return {
    paths,
    fallback: false,
  }
}

export async function getStaticProps({ params }) {
  const postData = await getPostData(params.slug)

  return {
    props: {
      postData,
    },
  }
}

export default function Post({ postData }) {
  const formattedDate = new Date(postData.date).toLocaleDateString('en-IN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  })

  return (
    <>
      <Head>
        <title>{postData.title}</title>
        <meta name="description" content={postData.description} />
      </Head>

      <main
        style={{
          maxWidth: '820px',
          margin: '60px auto',
          padding: '20px',
          fontFamily: 'Georgia, serif',
        }}
      >
        <h1 style={{ color: '#0a4fa3', fontSize: '38px', lineHeight: '1.3' }}>
          {postData.title}
        </h1>

        <p style={{ color: '#777', fontSize: '14px', marginTop: '10px' }}>
          Published on {formattedDate}
        </p>

        <article
          style={{
            marginTop: '40px',
            lineHeight: '1.9',
            fontSize: '18px',
            color: '#333',
          }}
          dangerouslySetInnerHTML={{ __html: postData.contentHtml }}
        />
      </main>
    </>
  )
}
