import { useEffect, useState } from "react";

// One template literal on purpose: minifiers do not reassemble split parts,
// and the deploy gate greps the bundle for the whole baked string.
const frontendLine = `frontend: hello world oxzoo-react-django_${import.meta.env.GREETING_TAG}`;

export default function App() {
  const [backendLine, setBackendLine] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    let alive = true;
    fetch("/api/greeting")
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.text();
      })
      .then((body) => {
        if (alive) setBackendLine(`backend: ${body}`);
      })
      .catch((err) => {
        if (alive) setError(`backend error: ${err.message}`);
      });
    return () => {
      alive = false;
    };
  }, []);

  return (
    <main>
      <h1>oxzoo-react-django</h1>
      <p className="line">{frontendLine}</p>
      <p className="line">{error ?? backendLine ?? "loading..."}</p>
    </main>
  );
}
