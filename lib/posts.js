import fs from 'fs'
import path from 'path'
import matter from 'gray-matter'

const postsDirectory = path.join(process.cwd(), 'posts')

/* 🔹 HOME + LISTING */
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
      const { data } = matter(fileContents)

      allPosts.push({
        slug: file.replace(/\.md$/, ''),
        year,
        ...data,
      })
    })
  })

  return allPosts.sort((a, b) => new Date(b.date) - new Date(a.date))
}

/* 🔹 FOR [slug].js */
export function getPostData(slug) {
  const years = fs.readdirSync(postsDirectory)

  for (const year of years) {
    const yearPath = path.join(postsDirectory, year)
    if (!fs.statSync(yearPath).isDirectory()) continue

    const fullPath = path.join(yearPath, `${slug}.md`)
    if (!fs.existsSync(fullPath)) continue

    const fileContents = fs.readFileSync(fullPath, 'utf8')
    const matterResult = matter(fileContents)

    return {
      slug,
      year,
      content: matterResult.content,
      ...matterResult.data,
    }
  }

  return null
}

/* 🔹 STATIC PATHS */
export function getAllPostSlugs() {
  const years = fs.readdirSync(postsDirectory)
  let paths = []

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
