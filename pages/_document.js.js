import { Html, Head, Main, NextScript } from 'next/document'

export default function Document() {
  return (
    <Html lang="en">
      <Head>
        <link rel="icon" href="/favicon.ico" />
        <link rel="apple-touch-icon" href="/icon-512.png" />
        <meta name="theme-color" content="#0a4fa3" />
      </Head>
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}
