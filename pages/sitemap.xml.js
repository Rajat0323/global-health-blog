import fs from 'fs'
import path from 'path'

const SITE_URL = 'https://symptomsinsight.com' // change if needed

export async function getServerSideProps({ res }) {
  const postsDirectory = path.join(process.cwd(), 'posts')
  const years = fs.readdirSync(postsDirectory)

  let urls = []

  years.forEach((year) => {
    const yearPath = path.join(postsDirectory, year)
    if (!fs.statSync(yearPath).isDirectory()) return

    const files = fs.readdirSync(yearPath)
    files.forEach((file) => {
      if (file.endsWith('.md')) {
        const slug = file.replace(/\.md$/, '')
        urls.push(`${SITE_URL}/blog/${slug}`)
      }
    })
  })

  const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>${SITE_URL}</loc>
  </url>
  ${urls
    .map(
      (url) => `
  <url>
    <loc>${url}</loc>
  </url>`
    )
    .join('')}
</urlset>`

  res.setHeader('Content-Type', 'text/xml')
  res.write(sitemap)
  res.end()

  return {
    props: {},
  }
}

// ⚠️ REQUIRED dummy export (VERY IMPORTANT)
export default function Sitemap() {
  return null
}
