import Link from "next/link";

export default function ArticleCard({ post }) {
  return (
    <div className="card">
      <h3>
        <Link href={`/blog/${post.slug}`}>
          {post.title}
        </Link>
      </h3>

      <p className="date">
        {post.date ? new Date(post.date).toDateString() : ""}
      </p>
    </div>
  );
}
