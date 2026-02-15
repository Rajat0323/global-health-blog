export default function Footer() {
  return (
    <footer style={{ borderTop: '1px solid #ddd', marginTop: '40px', padding: '20px 0' }}>
      <p>© {new Date().getFullYear()} SymptomsInsight.com</p>
      <small>Medical content for educational purposes only.</small>
    </footer>
  )
}
