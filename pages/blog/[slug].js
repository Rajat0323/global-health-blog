import { getAllPosts, getPostData } from "../../lib/posts";

export default function Post({ postData }) {
  return (
    <div>
      <h1>{postData.title}</h1>
      <div dangerouslySetInnerHTML={{ __html: postData.contentHtml }} />
    </div>
  );
}

export async function getStaticPaths() {
  const posts = getAllPosts();
  const paths = posts.map((post) => ({
    params: { slug: post.slug },
  }));

  return { paths, fallback: false };
}

export async function getStaticProps({ params }) {
  const postData = await getPostData(params.slug);
  return { props: { postData } };
}
