import Link from "next/link";
import { getAllPosts } from "../lib/posts";

export default function Home({ posts }) {
  return (
    <div>
      <h1>Global Health Blog</h1>
      {posts.map((post) => (
        <div key={post.slug}>
          <Link href={`/blog/${post.slug}`}>
            <h2>{post.title}</h2>
          </Link>
        </div>
      ))}
    </div>
  );
}

export async function getStaticProps() {
  const posts = getAllPosts();
  return {
    props: { posts },
  };
}
