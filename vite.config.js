import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

// root is client/; the build lands in ../dist, which ox's [frontend].dist serves.
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
