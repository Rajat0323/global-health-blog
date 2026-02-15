import fs from 'fs'
import path from 'path'

const SITE_URL = 'https://symptomsinsight.com'

export async function getServerSideProps({ res }) {
  const postsDirectory = path.join(process.cwd(), 'posts')
  const years = fs.readdirSync(postsDirectory)

  const urls = []

  years.forEach((year) => {
    const yearPath = path.join(postsDirectory, year)
    if (!fs.statSync(yearPath).isDirectory()) return

    const files = fs.readdirSync(yearPath)
    files.forEach((file) => {
      if (file.endsWith('.md')) {
        const slug = file.replace(/\.md$/, '')
        urls.push(`
  <url>
    <loc>${SITE_URL}/blog/${slug}</loc>
    <lastmod>${new Date().toISOString()}</lastmod>
  </url>`)
      }
    })
  })

  const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>${SITE_URL}/</loc>
  </url>
  ${urls.join('')}
</urlset>`

  res.setHeader('Content-Type', 'text/xml')
  res.write(sitemap)
  res.end()

  return { props: {} }
}

/**
 * ✅ Required dummy export for Next.js
 */
export default function Sitemap() {
  return null
}
