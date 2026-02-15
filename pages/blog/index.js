import { getAllPosts } from "../../lib/posts";
import Layout from "../../components/Layout";
import ArticleCard from "../../components/ArticleCard";

export async function getStaticProps() {
  const posts = getAllPosts();
  return { props: { posts } };
}

export default function Blog({ posts }) {
  return (
    <Layout title="Health Blog">
      <h1>Latest Health Articles</h1>

      <div className="grid">
        {posts.map((post) => (
          <ArticleCard key={post.slug} post={post} />
        ))}
      </div>
    </Layout>
  );
}
