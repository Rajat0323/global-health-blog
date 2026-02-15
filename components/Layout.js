import Head from "next/head";
import Header from "./Header";

export default function Layout({ children, title }) {
  const siteTitle = "Symptoms Insight";

  return (
    <>
      <Head>
        <title>{title ? `${title} | ${siteTitle}` : siteTitle}</title>
        <meta
          name="description"
          content="Evidence-based health symptoms, early warning signs, causes, diagnosis guidance, and prevention tips."
        />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </Head>

      <Header />

      <main className="container">
        {children}
      </main>

      <footer className="footer">
        <p>
          © {new Date().getFullYear()} <strong>Symptoms Insight</strong>.  
          Medical information for educational purposes only.
        </p>
      </footer>
    </>
  );
}
