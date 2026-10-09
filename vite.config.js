import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

// root is client/; the build lands in ../dist, which ox serves from [static] dir.
export default defineConfig({
  root: "client",
  plugins: [react()],
  build: {
    outDir: "../dist",
    emptyOutDir: true,
  },
  // Expose GREETING_* (and VITE_*) vars to the SPA at build time.
  envPrefix: ["GREETING_", "VITE_"],
});
