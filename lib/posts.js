import fs from 'fs'
import path from 'path'
import matter from 'gray-matter'
import { remark } from 'remark'
import html from 'remark-html'

const postsDirectory = path.join(process.cwd(), 'posts')

/**
 * ✅ Used by getStaticPaths in [slug].js
 */
export function getAllPostSlugs() {
  const years = fs.readdirSync(postsDirectory)
  const paths = []

  years.forEach((year) => {
    const yearPath = path.join(postsDirectory, year)
    if (!fs.statSync(yearPath).isDirectory()) return

    const files = fs.readdirSync(yearPath)
    files.forEach((file) => {
      if (file.endsWith('.md')) {
        paths.push({
          params: {
            slug: file.replace(/\.md$/, ''),
          },
        })
      }
    })
  })

  return paths
}

/**
 * ✅ Used by getStaticProps in [slug].js
 * Converts Markdown → HTML
 */
export async function getPostData(slug) {
  const years = fs.readdirSync(postsDirectory)

  for (const year of years) {
    const yearPath = path.join(postsDirectory, year)
    if (!fs.statSync(yearPath).isDirectory()) continue

    const fullPath = path.join(yearPath, `${slug}.md`)
    if (!fs.existsSync(fullPath)) continue

    const fileContents = fs.readFileSync(fullPath, 'utf8')
    const matterResult = matter(fileContents)

    // 🔥 Markdown → HTML
    const processedContent = await remark()
      .use(html)
      .process(matterResult.content)

    return {
      slug,
      year,
      contentHtml: processedContent.toString(), // IMPORTANT
      ...matterResult.data,
    }
  }

  return null
}
export function getSortedPostsData() {
  const years = fs.readdirSync(postsDirectory)
  let allPosts = []

  years.forEach((year) => {
    const yearPath = path.join(postsDirectory, year)
    if (!fs.statSync(yearPath).isDirectory()) return

    const files = fs.readdirSync(yearPath)

    files.forEach((file) => {
      if (!file.endsWith('.md')) return

      const fullPath = path.join(yearPath, file)
      const fileContents = fs.readFileSync(fullPath, 'utf8')
      const matterResult = matter(fileContents)

      allPosts.push({
        slug: file.replace(/\.md$/, ''),
        year,
        ...matterResult.data,
      })
    })
  })

  // newest first
  return allPosts.sort(
    (a, b) => new Date(b.date) - new Date(a.date)
  )
}
