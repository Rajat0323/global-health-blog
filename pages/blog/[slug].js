import Head from 'next/head'
import Header from '../../components/Header'
import { getAllPostSlugs, getPostData } from '../../lib/posts'

/**
 * ✅ REQUIRED for dynamic routes
 */
export async function getStaticPaths() {
  const paths = getAllPostSlugs()

  return {
    paths,
    fallback: false,
  }
}

/**
 * ✅ Fetch single post
 */
export async function getStaticProps({ params }) {
  const postData = await getPostData(params.slug)

  return {
    props: {
      postData,
    },
  }
}

export default function Post({ postData }) {
  // ✅ Locale fixed (SSR + Client same)
  const formattedDate = new Date(postData.date).toLocaleDateString('en-GB', {
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

      {/* ✅ HEADER NOW VISIBLE ON BLOG PAGE */}
      <Header />

      <main
        style={{
          maxWidth: '820px',
          margin: '40px auto',
          padding: '20px',
          fontFamily: 'Georgia, serif',
        }}
      >
        <h1
          style={{
            color: '#0a4fa3',
            fontSize: '38px',
            lineHeight: '1.3',
          }}
        >
          {postData.title}
        </h1>

        <p
          style={{
            color: '#777',
            fontSize: '14px',
            marginTop: '8px',
          }}
        >
          Published on {formattedDate}
        </p>

        <article
          style={{
            marginTop: '40px',
            lineHeight: '1.9',
            fontSize: '18px',
            color: '#333',
          }}
          dangerouslySetInnerHTML={{
            __html: postData.contentHtml,
          }}
        />
      </main>
    </>
  )
}
